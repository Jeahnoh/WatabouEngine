import os
import json
from core.logger import logEMS, LogLevel

CONFIG_FILE = "config.json"

DEFAULT_CONFIG = {
    "rom_directory": "../roms/",
    "debug_mode": False
    # Future user settings (like UI preferences or export paths) go here
}

def load_or_create_config() -> dict:
    """Loads config.json, generates it if missing, and patches missing keys."""
    
    # 1. Generate if missing
    if not os.path.exists(CONFIG_FILE):
        logEMS("No config.json found. Generating default configuration...", LogLevel.INFO)
        try:
            with open(CONFIG_FILE, 'w', encoding='utf-8') as f:
                json.dump(DEFAULT_CONFIG, f, indent=4)
            return DEFAULT_CONFIG
        except IOError as e:
            logEMS(f"Failed to create config.json: {e}", LogLevel.ERROR)
            return DEFAULT_CONFIG # Fallback to in-memory so the engine doesn't crash

    # 2. Load existing
    try:
        with open(CONFIG_FILE, 'r', encoding='utf-8') as f:
            user_config = json.load(f)
    except json.JSONDecodeError:
        logEMS("CRITICAL: config.json is corrupted! Falling back to defaults.", LogLevel.ERROR)
        return DEFAULT_CONFIG

    # 3. Patch missing keys (Invisible self-healing)
    patched = False
    for key, value in DEFAULT_CONFIG.items():
        if key not in user_config:
            user_config[key] = value
            patched = True
            
    if patched:
        logEMS("Missing keys detected in config.json. Applying defaults.", LogLevel.WARN)
        try:
            with open(CONFIG_FILE, 'w', encoding='utf-8') as f:
                json.dump(user_config, f, indent=4)
        except IOError:
            pass

    return user_config