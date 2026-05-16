import os
import json
import sqlite3

DEBUG = True

def load_character_map(tbl_path):
    char_map = {}
    if not os.path.exists(tbl_path):
        return char_map
    with open(tbl_path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip('\n')
            if '=' not in line:
                continue
            parts = line.split('=', 1)
            if len(parts) == 2:
                hex_str, char_str = parts
                char_map[int(hex_str, 16)] = char_str
    
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

    # Load layout definitions from config map
    monster_start = int(rom_map["offsets"]["monster_table_start"], 16)
    record_size = int(rom_map["offsets"]["monster_record_bytes"], 16)
    monster_count = rom_map["offsets"]["monster_count"]
    monster_names_start = int(rom_map["offsets"]["monster_names_start"], 16)
    skill_names_start = int(rom_map["offsets"]["skill_names_start"], 16)
    skill_count = rom_map["offsets"]["skill_count"]

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

    # Enforce database integrity rules
    cursor.execute("PRAGMA foreign_keys = ON;")

    # Master Lookup Table for Monster Families
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS families (
            family_id INTEGER PRIMARY KEY,
            family_name TEXT NOT NULL
        );
    """)

    # Master Lookup Table for Globally Available Skills
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS skills (
            skill_id INTEGER PRIMARY KEY,
            skill_name TEXT NOT NULL
        );
    """)

    # Normalized Monster Profile Table
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
            FOREIGN KEY (family_id) REFERENCES families(family_id),
            FOREIGN KEY (skill_1_id) REFERENCES skills(skill_id),
            FOREIGN KEY (skill_2_id) REFERENCES skills(skill_id),
            FOREIGN KEY (skill_3_id) REFERENCES skills(skill_id)
        );
    """)

    try:
        if DEBUG:
            print("[+] Seeding relational family classifications...")
        for f_id, f_name in config_families.items():
            cursor.execute("INSERT INTO families (family_id, family_name) VALUES (?, ?);", (int(f_id), f_name))

        with open(rom_path, "rb") as rom:
            char_map = load_character_map("extractor/dwm_english.tbl")
            
            # Extract actual names up to our known text limit
            if DEBUG:
                print(f"[+] Extracting {skill_count} global skill strings from cartridge context...")
            extracted_skills = extract_variable_names(rom, skill_names_start, skill_count, char_map)
            
            # Populate the entire 256 byte spectrum (0x00 to 0xFF) to clear foreign key constraints safely
            if DEBUG:
                print("[+] Seeding complete 1-byte matrix lookup tables for core skills layer...")
            for s_id in range(256):
                if s_id < len(extracted_skills):
                    # 0x00 to 0xDD: Actual strings from ROM (Blaze...Ahhh)
                    s_name = extracted_skills[s_id]
                elif s_id == 255:
                    # 0xFF: The universal "No skill equipped" marker
                    s_name = "Empty"
                else:
                    # 0xDE to 0xFE: Padding out unused dictionary space
                    s_name = f"Unused_0x{s_id:02X}"
                
                cursor.execute("INSERT INTO skills (skill_id, skill_name) VALUES (?, ?);", (s_id, s_name))
            
            # Extract and inject all core monster records
            if DEBUG:
                print("[+] Pre-loading variable-length monster name strings...")
            monster_names = extract_variable_names(rom, monster_names_start, monster_count, char_map)

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
        print(f"[SUCCESS] Relational database compilation complete. Linked structural records successfully.")

    except Exception as e:
        print(f"[-] Pipeline Failure: {e}")
    finally:
        conn.close()

if __name__ == "__main__":
    build_database()