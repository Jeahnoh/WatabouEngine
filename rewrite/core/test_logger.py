# Copyright (c) 2026 Jeahnoh
# This software is licensed under the PolyForm Noncommercial License 1.0.0.
# You may not use this file except in compliance with the License.
# See LICENSE.md in the repository root for full terms.

from core.logger import initialize_logger, logEMS, LogLevel

def run_logger_test():
    # 1. Initialize the system (This triggers the Header)
    initialize_logger("Logger Diagnostic Test")
    
    # 2. Standard Information
    logEMS("Core modules loaded. Commencing test sequence.", LogLevel.INFO)
    
    # 3. Debugging/Tracing (Great for watching your hex extraction loop)
    dummy_pointer = "0x4071"
    logEMS(f"Parsed Little Endian pointer: {dummy_pointer}", LogLevel.DEBUG)
    
    # 4. Warnings (Non-fatal errors, like a missing translation table)
    logEMS("Translation table 'wario_slack.json' missing. Skipping block.", LogLevel.WARN)
    
    # 5. Errors (Testing exception catching)
    try:
        # Forcing a math crash to simulate a bad hex conversion
        bad_math = 1 / 0
    except ZeroDivisionError as e:
        logEMS(f"Extraction halted on Bank 2F: {e}", LogLevel.ERROR)
        
    # 6. Silent Logging (Writes to file, but keeps the terminal clean)
    logEMS("SILENT LOG: This should only appear in nice_session.log.", LogLevel.INFO, echo=False)
    
    logEMS("Diagnostic complete. Exiting script.", LogLevel.INFO)

if __name__ == "__main__":
    run_logger_test()
    # The script ends here. The logAppFooter() should fire automatically right after!