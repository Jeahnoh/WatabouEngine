[⬅️ Back to Master ROM Map](../DWM_Master_ROM_Map.md)
        
# Bank `0x7B`: Garbage Data (Wario Land II)
## Overview
**Local Hex Range:** `0x4000` - `0x7FFF`  
**Global Hex Range:** `0x1EC000` - `0x1EFFFF`  
**Bank Type:** N/A  
**Category:** Unused / Garbage Data  
**Summary:** Leftover data from *Wario Land II*. Entire bank matches Bank `0x7B` from WL2. Interestingly, also matches the first 0x36 bytes of Bank `0x3B` from WL2.

---

## Memory Map (Granular)
*Breakdown of the specific blocks within this bank.*

| Offset (Local) | Offset (Global) | Length | Description |
| :------------- | :-------------- | :----- | :---------- |
| `0x4000` | `0x1EC000` | `0x1212` | Wario Land II sprite data. Non-standard `2bpp` format. |
| `0x5212` | `0x1ED212` | `0x2DEE` | `0x00` padding (Safe Free Space) |

---

### Raw Data
```hex
Hex View  00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F  ascii
 
001ED210  FF 22 00 00 00 00 00 00  00 00 00 00 00 00 00 00  ."..............
001ED220  00 00 00 00 00 00 00 00  00 00 00 00 00 00 00 00  ................
001ED230  00 00 00 00 00 00 00 00  00 00 00 00 00 00 00 00  ................
... 
001EFFF0  00 00 00 00 00 00 00 00  00 00 00 00 00 00 00 00  ................
```
[⬅️ Back to Master ROM Map](../DWM_Master_ROM_Map.md)
---
© 2026 Jeahnoh. Licensed under CC BY-NC 4.0. Attribution Required.
See LICENSE.md in the repository root for full non-commercial terms.