import os
import json
import sys

from core.logger import initialize_logger, set_debug_mode, logEMS, LogLevel
from core.config import load_or_create_config
from core.constants import APPROVED_ROM_LIBRARY
from core.verifier import scan_rom_directory

def run_pipeline(silent: bool = False):
    initialize_logger("Watabou Extraction Core", silent=silent)
    
    # 1. Boot up configurations
    app_config = load_or_create_config()
    target_dir = app_config.get("rom_directory", "./input_roms/")
    
    set_debug_mode(app_config.get("debug_mode", False))
    # 2. Run the Discovery Scanner
    discovered_roms = scan_rom_directory(target_dir, APPROVED_ROM_LIBRARY)
    
    if not discovered_roms:
        # Halt safely. The verifier already logged the failure.
        return
        
    target_rom = discovered_roms[0]
    logEMS(f"Commencing extraction pipeline for: {target_rom['title']}", LogLevel.INFO)
    
    # Phase 2: Database Initialization will go here

if __name__ == "__main__":
    # Check if --silent was passed as a command-line argument
    is_silent = "--silent" in sys.argv
    run_pipeline(silent=is_silent)
