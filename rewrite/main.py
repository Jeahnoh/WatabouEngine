import os
import json

from core.logger import initialize_logger, logEMS, LogLevel
from core.verifier import scan_rom_directory

# This will eventually be loaded from a config.json file!
APP_CONFIG = {
    "rom_directory": "../roms/",
    "approved_library": {
        "1CA6579359F21D8E27B446F865BF6B83": "Dragon Warrior Monsters - US",
        # You can add DWM2 hashes here later, and the engine will automatically support them!
        "ANOTHER_HASH_STRING_HERE": "Dragon Warrior Monsters (US - Revision A)"
    }
}

def run_pipeline():
    initialize_logger("Watabou Extraction Core")
    
    # Run the Discovery Scanner
    discovered_roms = scan_rom_directory(
        APP_CONFIG["rom_directory"], 
        APP_CONFIG["approved_library"]
    )
    
    if not discovered_roms:
        # The scanner already logged the ERROR, we just safely abort the pipeline.
        return
        
    # If we found multiple ROMs, we can iterate through them, 
    # or just grab the first one to start the extraction loop.
    target_rom = discovered_roms[0]
    logEMS(f"Commencing extraction pipeline for: {target_rom['title']}", LogLevel.INFO)
    
    # Phase 2 (Database Schema) would begin here...

if __name__ == "__main__":
    run_pipeline()