import os
import hashlib
from core.logger import logEMS, LogLevel

def compute_md5(file_path: str) -> str:
    """Streams a file in 4K chunks to calculate MD5 without flooding RAM."""
    md5_hash = hashlib.md5()
    try:
        with open(file_path, "rb") as f:
            for byte_block in iter(lambda: f.read(4096), b""):
                md5_hash.update(byte_block)
        return md5_hash.hexdigest().upper()
    except IOError as e:
        logEMS(f"File lock error while reading '{file_path}': {e}", LogLevel.DEBUG)
        return ""

def scan_rom_directory(target_dir: str, approved_hashes: dict) -> list:
    """
    Scans a directory for approved ROMs based on MD5 checksums.
    Silently ignores unrelated games.
    
    Returns a list of dictionaries containing data for valid ROMs found.
    """
    if not os.path.isdir(target_dir):
        logEMS(f"Target ROM directory '{target_dir}' does not exist.", LogLevel.ERROR)
        return []

    logEMS(f"Scanning directory '{target_dir}' for approved engine ROMs...", LogLevel.INFO)
    valid_roms_found = []

    # Filter to only scan approved extensions to save processing time
    valid_extensions = (
        # Nintendo Handhelds
        '.gb', '.gbc', '.gba', 
        '.nds', '.3ds',
        
        # Nintendo Consoles
        '.nes', '.smc', '.sfc', 
        
        # Raw Memory Dumps / Dev Builds (We can add bypass hashes for these later if needed)
        '.bin'
    )

    for filename in os.listdir(target_dir):
        if not filename.lower().endswith(valid_extensions):
            continue

        file_path = os.path.join(target_dir, filename)
        file_hash = compute_md5(file_path)

        if file_hash in approved_hashes:
            # We found a match in our approved library
            game_title = approved_hashes[file_hash]
            logEMS(f"Approved ROM validated: '{filename}' ({game_title})", LogLevel.INFO)
            
            valid_roms_found.append({
                "path": file_path,
                "title": game_title,
                "hash": file_hash
            })
        else:
            # It's a Game Boy ROM, but not one we support. Log to debug, keep terminal clean.
            logEMS(f"Ignored unsupported ROM: '{filename}'", LogLevel.DEBUG, echo=False)

    # Final reporting logic based on your requirements
    if not valid_roms_found:
        logEMS("No approved ROMs found in the target directory. Extraction halted.", LogLevel.ERROR)
    else:
        logEMS(f"Scan complete. Mounted {len(valid_roms_found)} valid ROM(s) for extraction.", LogLevel.INFO)

    return valid_roms_found