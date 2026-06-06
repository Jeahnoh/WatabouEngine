[⬅️ Back to Master ROM Map](../DWM_Master_ROM_Map.md)
        
# Bank 7D: Empty / Garbage Data
## Overview
**Local Hex Range:** `0x4000` - `0x7FFF`  
**Global Hex Range:** `0x1F4000` - `0x1F7FFF`  
**Bank Type:** N/A  
**Category:** Empty / Garbage  
**Summary:** Leftover data from Wario Land II. Entire bank matches Bank `0x7D` from WL2.

---

## Memory Map (Granular)
*Break down the specific blocks within this bank.*

| Offset (Local) | Offset (Global) | Length | Description |
| :------------- | :-------------- | :----- | :---------- |
| `0x4000` | `0x1F4000` | `0x26AD` | Wario Land II sprite data. Non-standard `2bpp` format. |
| `0x66AD` | `0x1f66AD` | `0x1953` | 0x00's |

---

### Raw Data
```hex
Hex View  00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F  ascii

001F66A0  01 47 1C 3C 21 DB 36 D6  E6 02 C2 37 32 00 00 00  .G.<!.6....72...
001F66B0  00 00 00 00 00 00 00 00  00 00 00 00 00 00 00 00  ................
001F66C0  00 00 00 00 00 00 00 00  00 00 00 00 00 00 00 00  ................
... 
001F7FF0  00 00 00 00 00 00 00 00  00 00 00 00 00 00 00 00  ................
```
[⬅️ Back to Master ROM Map](../DWM_Master_ROM_Map.md)