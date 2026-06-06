import os

# Configuration
NUM_BANKS = 128  # 0x00 to 0x7F (Covers a standard 2MB GBC ROM)
OUTPUT_DIR = "." # Saves directly to the folder the script is run in

def generate_bank_files():
    for bank_num in range(NUM_BANKS):
        # Format bank number as 2-digit uppercase Hex (e.g., 00, 0A, 4F)
        bank_hex = f"{bank_num:02X}"
        # Decimal prefix for VS Code sorting (e.g., 000, 010, 127)
        dec_prefix = f"{bank_num:03d}"
        
        # Calculate Game Boy Memory Mapping Math
        global_start = f"{(bank_num * 0x4000):06X}"
        global_end = f"{((bank_num * 0x4000) + 0x3FFF):06X}"
        
        if bank_num == 0:
            local_start = "0000"
            local_end = "3FFF"
            bank_type = "ROM0 (Always Loaded)"
            example_local = "0150"
            example_global = "000150"
        else:
            local_start = "4000"
            local_end = "7FFF"
            bank_type = "Swappable"
            example_local = "4000"
            example_global = global_start

        # The Markdown Template
        # NOTE: The Overview lines end with exactly TWO SPACES to force a Markdown line break!
        template = f"""[⬅️ Back to Master ROM Map](../DWM_Master_ROM_Map.md)
        
# Bank {bank_hex}: [System/Asset Name]
## Overview
**Local Hex Range:** `0x{local_start}` - `0x{local_end}`  
**Global Hex Range:** `0x{global_start}` - `0x{global_end}`  
**Bank Type:** {bank_type}  
**Category:** [Graphics / Text / Code / Audio / Unknown]  
**Summary:** [A brief 1-2 sentence description of what this bank does.]

---

## Memory Map (Granular)
*Break down the specific blocks within this bank.*

| Offset (Local) | Offset (Global) | Length | Description |
| :------------- | :-------------- | :----- | :---------- |
| `0x{example_local}`         | `0x{example_global}`        | ???b    | [Example Entry - Replace or Delete] |

---

## Technical Notes & Observations

### [Sub-System Name]
* **Compression/Encoding:** [e.g., 1BPP -> 2BPP Expansion, custom 0x08, None]
* **Debugger Notes:** * [Add your BGB debugging observations here]

### Raw Data / Hex Snippets
```hex
[Paste raw hex dumps here for quick reference]

```

### Visual Reference

![[placeholder_image.png]]
*Caption: [Add details about the visualizer render]*

---

## ETL / Extraction Plan

* [ ] [Extraction step 1]
# Bank {bank_hex}: [System/Asset Name]
"""

        # Write the file with the new decimal prefix
        filename = os.path.join(OUTPUT_DIR, f"{dec_prefix}_Bank_{bank_hex}.md")
        with open(filename, "w", encoding="utf-8") as f:
            f.write(template)
            print(f"Successfully generated {NUM_BANKS} Bank Markdown files with mathematically mapped Hex ranges!")

if __name__ == "__main__":
    generate_bank_files()


