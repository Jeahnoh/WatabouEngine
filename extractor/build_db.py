import os
import json
import sqlite3

DEBUG = True

def load_character_map(tbl_path):
    """Dynamically loads a .tbl file into a hex-to-string Python dictionary."""
    char_map = {}
    if not os.path.exists(tbl_path):
        if DEBUG:
            print(f"[-] Warning: '{tbl_path}' missing.")
        return char_map
    with open(tbl_path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip('\n')
            if '=' not in line:
                continue
            parts = line.split('=', 1)
            if len(parts) == 2:
                hex_str, char_str = parts
                try:
                    char_map[int(hex_str, 16)] = char_str
                except ValueError:
                    continue
    char_map[0x00] = ""
    char_map[0x50] = ""
    char_map[0xF0] = ""
    return char_map

def extract_variable_names(rom, start_offset, count, char_map):
    """Reads consecutive F0-terminated strings from the ROM."""
    rom.seek(start_offset)
    names = []
    for _ in range(count):
        decoded = []
        while True:
            b = rom.read(1)[0]
            if b == 0xF0:
                break
            decoded.append(char_map.get(b, '?'))
        names.append("".join(decoded))
    return names

def build_database():
    """Compiles raw cartridge binary structures into a relational SQLite asset."""
    json_path = "extractor/rom_map.json"
    with open(json_path, "r") as f:
        rom_map = json.load(f)

    monster_start = int(rom_map["offsets"]["monster_table_start"], 16)
    record_size = int(rom_map["offsets"]["monster_record_bytes"], 16)
    monster_count = rom_map["offsets"]["monster_count"]
    names_start = int(rom_map["offsets"]["monster_names_start"], 16)

    # TODO: Locate in ROM actual text entries for family names
    config_families = rom_map["families"]

    rom_dir = "./roms"
    rom_files = [f for f in os.listdir(rom_dir) if f != "PLACE_ROMS_HERE.txt" and not f.startswith('.')]
    if not rom_files:
        print("[-] Error: No ROM file found in the 'roms/' directory.")
        return

    rom_path = os.path.join(rom_dir, rom_files[0])
    db_path = "./engine/Assets/watabou_core.db"
    
    os.makedirs(os.path.dirname(db_path), exist_ok=True)

    if os.path.exists(db_path):
        if DEBUG:
            print(f"[+] Purging preexisting database asset -> {db_path}")
        os.remove(db_path)

    print(f"[+] Initializing database compilation pipeline -> {db_path}")
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Enable Foreign Key Constraints in SQLite
    cursor.execute("PRAGMA foreign_keys = ON;")

    # Table 1: Master Lookup Table for Monster Families
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS families (
            family_id INTEGER PRIMARY KEY,
            family_name TEXT NOT NULL
        );
    """)

    # Table 2: Normalized Monster Entities Table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS monsters (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            monster_index INTEGER NOT NULL,
            name TEXT NOT NULL,
            family_id INTEGER NOT NULL,
            level_cap INTEGER NOT NULL,
            exp_index INTEGER NOT NULL,
            gender_ratio INTEGER NOT NULL,
            skill_1_id INTEGER NOT NULL,
            skill_2_id INTEGER NOT NULL,
            skill_3_id INTEGER NOT NULL,
            raw_chunk BLOB NOT NULL,
            FOREIGN KEY (family_id) REFERENCES families(family_id)
        );
    """)

    try:
        if DEBUG:
            print("[+] Seeding relational family classifications...")
        for f_id, f_name in config_families.items():
            cursor.execute("INSERT INTO families (family_id, family_name) VALUES (?, ?);", (int(f_id), f_name))

        with open(rom_path, "rb") as rom:
            char_map = load_character_map("extractor/dwm_english.tbl")
            
            if DEBUG:
                print("[+] Pre-loading variable-length game text strings...")
            monster_names = extract_variable_names(rom, names_start, monster_count, char_map)

            if DEBUG:
                print(f"[+] Processing and injecting {monster_count} core entities into relational tables...")
            rom.seek(monster_start)
            
            for i in range(monster_count):
                monster_chunk = rom.read(record_size)
                
                family_id = monster_chunk[0]
                level_cap = monster_chunk[1]
                exp_index = monster_chunk[2]
                gender_ratio = monster_chunk[3]
                skill_1 = monster_chunk[6]
                skill_2 = monster_chunk[7]
                skill_3 = monster_chunk[8]
                true_name = monster_names[i]

                cursor.execute("""
                    INSERT INTO monsters (
                        monster_index, name, family_id, 
                        level_cap, exp_index, gender_ratio, 
                        skill_1_id, skill_2_id, skill_3_id, raw_chunk
                    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?);
                """, (
                    i, true_name, family_id,
                    level_cap, exp_index, gender_ratio,
                    skill_1, skill_2, skill_3, sqlite3.Binary(monster_chunk)
                ))

        conn.commit()
        print(f"[SUCCESS] Relational compilation complete. {monster_count} core records written.")

    except Exception as e:
        print(f"[-] Pipeline Failure: {e}")
    finally:
        conn.close()

if __name__ == "__main__":
    build_database()