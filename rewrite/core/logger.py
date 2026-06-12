# Copyright (c) 2026 Jeahnoh
# This software is licensed under the PolyForm Noncommercial License 1.0.0.
# You may not use this file except in compliance with the License.
# See LICENSE.md in the repository root for full terms.
#
# -----------------------------------------------------------------------------
# PRIOR ART / ORIGINAL AUTHORSHIP:
# Fork of the NEEDLESS IMMERSIVE COMMAND ENGINE (N.I.C.E.)
# Originally developed and copyrighted by Jeahnoh prior to this project.
#
# Note: This version has been stripped of the main command engine and 
# modified to utilize the logging framework exclusively. Future 
# contributions to this specific file by other developers do not 
# constitute co-ownership of the original N.I.C.E. architecture.
# -----------------------------------------------------------------------------

# Standard Library Imports
import sys
import atexit
from datetime import datetime
from enum import Enum

#================================================================
# CONFIGURATION
#================================================================
VERSION = 'v0.0.3-etl'
LAST_UPDATE = '2026-06-09'
ENGINE = "Watabou"
LOG_FILE = "nice_session.log"

SILENT_MODE = False  # Set to True to suppress console output and log only to file
DEBUG_MODE = False  # Set to True to enable verbose logging and diagnostics

class LogLevel(Enum):
    INFO = "INFO"
    WARN = "WARN"
    ERROR = "ERROR"
    DEBUG = "DEBUG"

def set_silent_mode(is_silent: bool):
    """Toggles the global silent state for terminal output."""
    global SILENT_MODE
    SILENT_MODE = bool(is_silent)
    
def set_debug_mode(is_debug: bool):
    """Toggles the global debug state and announces the change if active."""
    global DEBUG_MODE
    DEBUG_MODE = is_debug
    if DEBUG_MODE:
        logEMS("Debug mode ENABLED. Extended tracing active.", LogLevel.DEBUG)

def logEMS(message: str, level: LogLevel = LogLevel.INFO, echo: bool = True) -> str:
    """
    Writes a timestamped message to the log file and optionally prints it to the console.
    """
    if level == LogLevel.DEBUG and not DEBUG_MODE:
        return "" 

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    formatted_msg = f"{timestamp} [{level.value}] {message}"
    
    # Write directly to disk
    try:
        with open(LOG_FILE, "a", encoding="utf-8") as f:
            f.write(formatted_msg + "\n")
    except IOError as e:
        # Fallback if file locks up
        print(f"[LOGGING ERROR] Failed writing to file: {e}", file=sys.stderr)

    # Basic Console Echo
    if echo and not SILENT_MODE:
        stream = sys.stderr if level in (LogLevel.ERROR, LogLevel.WARN) else sys.stdout
        print(formatted_msg, file=stream)
    
    return formatted_msg

def logAppHeader(engine_name: str = "NICE ETL Pipeline") -> None:
    """Writes a simple session start boundary to the log."""

    width = 64
    border = "=" * width
    
    top_left = f"{ENGINE} Engine {VERSION}"
    top_right = f"{LAST_UPDATE}"
    line_1 = f"{top_left}{top_right:>{width - len(top_left)}}"
    line_2 = "Developed by Jeahnoh"
    headerMsg = f"{border}\n{line_1}\n{line_2}\n{border}"
    try:
        with open(LOG_FILE, "a", encoding="utf-8") as f:
            f.write(f"\n{headerMsg}\n")
    except IOError:
        pass
    
    if not SILENT_MODE:
        print(headerMsg)

def logAppFooter() -> None:
    """Writes a simple session end boundary to the log."""
    width = 64
    border = "=" * width

    footerMsg = f"{border}\n{f'{ENGINE} Engine Shutdown Sequence Complete'.center(width)}\n{border}\n"
    try:
        with open(LOG_FILE, "a", encoding="utf-8") as f:
            f.write(f"{footerMsg}\n")
    except IOError:
        pass

    if not SILENT_MODE:
        print(footerMsg)


#================================================================
# INITIALIZER
#================================================================
def initialize_logger(engine_name: str = "NICE ETL Pipeline", silent: bool = False) -> None:
    """Registers the exit hook and prints the header."""
    set_silent_mode(silent)
    # Guarantees the footer prints when sys.exit() is called or script finishes naturally
    atexit.register(logAppFooter)
    logAppHeader(engine_name)