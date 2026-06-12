# Copyright (c) 2026 Jeahnoh
# This software is licensed under the PolyForm Noncommercial License 1.0.0.
# You may not use this file except in compliance with the License.
# See LICENSE.md in the repository root for full terms.

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
    # TODO: Initialize SQLite database connection, create db if it doesn't exist
    # TODO: Create tables for monsters, items, text entries, palettes, etc. with appropriate schemas per game
    # we should probably have a "games" table that just lists the games we have data for, and then each data table can have a game_id foreign key to link it back to the games table. That way we can easily query all monsters for a specific game, or all items, etc. without having to worry about separate databases or complex naming conventions. We just need to make sure our queries filter by game_id correctly when we pull data for the engine generation phase. Or we can do separate tables with game-specific prefixes, but I think having a single table with a game_id column is cleaner and more scalable in the long run. It also allows us to easily add support for new games without having to modify our database schema or create new tables. We just insert new rows with the appropriate game_id and we're good to go. Then when we query for data during engine generation, we just filter by game_id to get the correct data for the target game. This way we can keep all our data in one place and maintain a consistent structure across different games. Yeah but we need to be able to map monsters across games as they are actually the same monster, but might have different base stats or dif

if __name__ == "__main__":
    # Check if --silent was passed as a command-line argument
    is_silent = "--silent" in sys.argv
    run_pipeline(silent=is_silent)
