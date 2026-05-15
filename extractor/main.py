import os
import json

# Standardized Game Boy header offsets
HEADER_TITLE_OFFSET = 0x0134
HEADER_TITLE_LENGTH = 15

def verify_and_parse_rom():
    # --- Step 0: Load and Verify the ROM Map Configuration ---
    json_path = "extractor/rom_map.json"
    
    if not os.path.exists(json_path):
        print(f"[-] Error: Missing configuration file at '{json_path}'")
        return

    with open(json_path, "r") as f:
        rom_map = json.load(f)

    # Convert the hex strings dynamically to Python integers
    monster_start = int(rom_map["offsets"]["monster_table_start"], 16)
    record_size = int(rom_map["offsets"]["monster_record_bytes"], 16)
    monster_count = rom_map["offsets"]["monster_count"]

    # Sanity print check
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
    print(f"[+] Found potential ROM: {rom_path}")

    try:
        # --- Step 2: Read Binary & Check Header ---
        with open(rom_path, "rb") as rom:
            rom.seek(HEADER_TITLE_OFFSET)
            title_bytes = rom.read(HEADER_TITLE_LENGTH)
            game_title = title_bytes.decode("ascii", errors="ignore").strip()
            
            print(f"[+] Internal Game Title: '{game_title}'")
            
            is_valid_rom = False
            if game_title == "DRAGON WMONAWQE":
                print("[======= VERIFICATION SUCCESS =======]")
                print(" Watabou Engine confirms this is a valid")
                print(" Dragon Warrior Monsters (US/EU) GBC ROM.")
                print("[====================================]")
                is_valid_rom = True
            elif game_title == "DQ/MONSTERS":
                print("[======= VERIFICATION SUCCESS =======]")
                print(" Watabou Engine confirms this is a valid")
                print(" Terry no WonderLand (JP) GBC ROM.       ")
                print("[!] Warning: Phase 1 offsets are mapped for US.")
                print("[====================================]")
                is_valid_rom = True
            else:
                print("[-] Verification Failed: Unknown ROM Header.")

            # --- Step 3: Raw Data Print Test ---
            if is_valid_rom:
                print("\n==================================================")
                print("[+] DATA INSPECTOR: Parsing True Monster Attributes")
                print("==================================================")
                
                rom.seek(monster_start)
                
                # Let's read the data for the first 3 monsters to inspect structural values
                sample_size = record_size * 3
                raw_bytes = rom.read(sample_size)
                
                family_names = {
                    0: "Slime", 1: "Dragon", 2: "Beast", 3: "Flying",
                    4: "Plant", 5: "Bug",    6: "Devil", 7: "Zombie",
                    8: "Material", 9: "Boss"
                }

                for i in range(3):
                    start_idx = i * record_size
                    end_idx = start_idx + record_size
                    monster_chunk = raw_bytes[start_idx:end_idx]
                    
                    # Parse properties straight from the documentation offset array mapping
                    family_id = monster_chunk[0]
                    level_cap = monster_chunk[1]
                    exp_index = monster_chunk[2]
                    gender_ratio = monster_chunk[3]
                    
                    # Skills occupy offsets 0x06, 0x07, 0x08
                    skill_1 = monster_chunk[6]
                    skill_2 = monster_chunk[7]
                    skill_3 = monster_chunk[8]
                    
                    family_string = family_names.get(family_id, f"Unknown ({family_id})")
                    
                    print(f"Monster #{i+1:03d} Properties:")
                    print(f"  ├─ Calculated Family : {family_string}")
                    print(f"  ├─ Base Level Cap    : {level_cap}")
                    print(f"  ├─ Exp Table Index   : {exp_index}")
                    print(f"  ├─ Gender Ratio Code : 0x{gender_ratio:02X}")
                    print(f"  ├─ Base Skill Bytes  : [0x{skill_1:02X}, 0x{skill_2:02X}, 0x{skill_3:02X}]")
                    print(f"  └─ Full Raw Row Link : {' '.join(f'{b:02X}' for b in monster_chunk[:16])}...\n")
                    
                print("==================================================")

    except Exception as e:
        print(f"[-] An error occurred: {e}")

if __name__ == "__main__":
    verify_and_parse_rom()