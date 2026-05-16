import os
import json

DEBUG = True

# Standardized Game Boy header offsets
HEADER_TITLE_OFFSET = 0x0134
HEADER_TITLE_LENGTH = 15

def load_character_map(tbl_path):
    """Dynamically loads a .tbl file into a hex-to-string Python dictionary."""
    char_map = {}
    if not os.path.exists(tbl_path):
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

def verify_and_parse_rom():
    """Validates the target GBC file signature and provides a hex data inspector loop."""
    # --- Step 0: Load and Verify the ROM Map Configuration ---
    json_path = "extractor/rom_map.json"
    if not os.path.exists(json_path):
        print(f"[-] Configuration error: '{json_path}' missing.")
        return

    with open(json_path, "r") as f:
        rom_map = json.load(f)
        
    monster_start = int(rom_map["offsets"]["monster_table_start"], 16)
    record_size = int(rom_map["offsets"]["monster_record_bytes"], 16)
    monster_count = rom_map["offsets"]["monster_count"]
    names_start = int(rom_map["offsets"]["monster_names_start"], 16)
    
    # TODO: Locate in ROM actual text entries for family names
    config_families = rom_map["families"]

    if DEBUG:
        print("\n==================================================")
        print("[+] SANITY CHECK: rom_map.json loaded successfully!")
        print(f"[+] Monster Table Start (Hex String): {rom_map['offsets']['monster_table_start']}")
        print(f"[+] Monster Table Start (Converted Int): {monster_start}")
        print(f"[+] Record Size: {record_size} bytes | Expected Total Monsters: {monster_count}")
        print("==================================================\n")

    # --- Step 1: Look for the ROM File ---
    rom_dir = "./roms"
    rom_files = [f for f in os.listdir(rom_dir) if f != "PLACE_ROMS_HERE.txt" and not f.startswith('.')]
    
    if not rom_files:
        print("[-] Error: No ROM file found in the 'roms/' directory.")
        return

    rom_path = os.path.join(rom_dir, rom_files[0])

    # --- Step 2: Read Binary & Check Header ---
    with open(rom_path, "rb") as rom:
        rom.seek(HEADER_TITLE_OFFSET)
        title_bytes = rom.read(HEADER_TITLE_LENGTH)
        title = title_bytes.decode("ascii", errors="ignore").strip()
        
        if DEBUG:
            print(f"[+] Internal Game Title: '{title}'")
        
        if title == "DRAGON WMONAWQE":
            print("[SUCCESS] Dragon Warrior Monsters (US/EU) GBC ROM Verified.")
        elif title == "DQ/MONSTERS":
            print("[SUCCESS] Terry no WonderLand (JP) GBC ROM Verified.")
            print("[!] Warning: Phase 1 offsets are currently mapped for US layout rules.")
        else:
            print(f"[-] Verification Failed: Unknown ROM Header Title '{title}'.")
            return

        # --- Step 3: Raw Data Print Test (Diagnostic Mode Only) ---
        if DEBUG:
            print("\n==================================================")
            print("[+] DATA INSPECTOR: Parsing True Monster Attributes")
            print("==================================================")
            
            tbl_path = "extractor/dwm_english.tbl"
            char_map = load_character_map(tbl_path)
            monster_names = extract_variable_names(rom, names_start, monster_count, char_map)

            TEST_SAMPLE = 10
            rom.seek(monster_start)
            sample_size = record_size * TEST_SAMPLE
            raw_bytes = rom.read(sample_size)
            
            for i in range(TEST_SAMPLE):
                start_idx = i * record_size
                end_idx = start_idx + record_size
                monster_chunk = raw_bytes[start_idx:end_idx]
                
                family_id = monster_chunk[0]
                level_cap = monster_chunk[1]
                exp_index = monster_chunk[2]
                gender_ratio = monster_chunk[3]
                skill_1 = monster_chunk[6]
                skill_2 = monster_chunk[7]
                skill_3 = monster_chunk[8]
                
                family_string = config_families.get(str(family_id), f"Unknown ({family_id})")                    
                true_name = monster_names[i]
                
                print(f"Monster #{i+1:03d} Properties:")
                print(f"  ├─ True Name         : {true_name}")
                print(f"  ├─ Calculated Family : {family_string}")
                print(f"  ├─ Base Level Cap    : {level_cap}")
                print(f"  ├─ Exp Table Index   : {exp_index}")
                print(f"  ├─ Gender Ratio Code : 0x{gender_ratio:02X}")
                print(f"  ├─ Base Skill Bytes  : [0x{skill_1:02X}, 0x{skill_2:02X}, 0x{skill_3:02X}]")
                print(f"  └─ Full Raw Row Link : {' '.join(f'{b:02X}' for b in monster_chunk[:16])}...\n")
            print("==================================================")

if __name__ == "__main__":
    verify_and_parse_rom()