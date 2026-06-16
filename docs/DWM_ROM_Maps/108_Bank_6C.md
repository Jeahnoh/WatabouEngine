[⬅️ Back to Master ROM Map](../DWM_Master_ROM_Map.md)
        
# Bank `0x6C`: Empty
## Overview
**Local Hex Range:** `0x4000` - `0x7FFF`  
**Global Hex Range:** `0x1B0000` - `0x1B3FFF`  
**Bank Type:** N/A  
**Category:** Free  
**Summary:** This bank contains no game data. It consists entirely of padding (`0x00`) and is safe to use for custom code injection or expanded assets.  

---

## Memory Map (Granular)
*Break down of the specific blocks within this bank.*

| Offset (Local) | Offset (Global) | Length | Description |
| :------------- | :-------------- | :----- | :---------- |
| `0x4000` | `0x1B0000` | 16KB | `0x00` padding (Safe Free Space) |

---

### Raw Data
```hex
Hex View  00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
 
001B0000  00 00 00 00 00 00 00 00  00 00 00 00 00 00 00 00  ................
001B0010  00 00 00 00 00 00 00 00  00 00 00 00 00 00 00 00  ................
001B0020  00 00 00 00 00 00 00 00  00 00 00 00 00 00 00 00  ................
... 
001B3FF0  00 00 00 00 00 00 00 00  00 00 00 00 00 00 00 00  ................
```
[⬅️ Back to Master ROM Map](../DWM_Master_ROM_Map.md)
---
© 2026 Jeahnoh. Licensed under CC BY-NC 4.0. Attribution Required.
See LICENSE.md in the repository root for full non-commercial terms.