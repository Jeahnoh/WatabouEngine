[⬅️ Back to Master ROM Map](../DWM_Master_ROM_Map.md)
        
# Bank 2F: Sprite Bank 0
## Overview
**Local Hex Range:** `0x4000` - `0x7FFF`  
**Global Hex Range:** `0x0BC000` - `0x0BFFFF`  
**Bank Type:** Swappable  
**Category:** Graphics
**Summary:** [A brief 1-2 sentence description of what this bank does.]

---

## Memory Map (Granular)
*Break down the specific blocks within this bank.*
### Bank Header 
| Offset (Local) | Offset (Global) | Length | Description |
| :------------- | :-------------- | :----- | :---------- |
| `0x4000`       | `0xBC000`       | `0x1`  | Bank ID: `0x2F` |
| `0x4001`       | `0xBC001`       | `0x70` | Sprite Pointer Table. 56 Pointers. |

### Pointer Table
```hex
Hex View  00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
 
000BC000  2F [71 40] 8B 41 5B 42 44  43 FE 43 AD 44 92 45 70  
000BC010  46 2C 47 AE 47 14 48 C2  48 A3 49 85 4A 48 4B F5  
000BC020  4B D7 4C 8F 4D 7F 4E 10  4F 30 50 D4 50 8B 51 86  
000BC030  52 3D 53 F3 53 58 54 F4  54 DA 55 70 56 13 57 D7  
000BC040  57 3B 59 83 5A E8 5A 9F  5B E6 5C D1 5E FE 5F 7A  
000BC050  61 D0 62 85 64 B2 65 91  67 11 69 EF 6A 6D 6C 59  
000BC060  6D 47 6F F7 70 16 72 96  73 62 75 53 76 93 77 AA  
000BC070  79
```
***Note:** The first pointer `[71 40]` is Little Endian for address `0x4071`.*

### Overworld Sprite Table
*Note: Lengths denote contiguous blocks to the next pointer address, including the 3-byte header.*

| Offset (Local) | Offset (Global) | Length | Description |
| :------------- | :-------------- | :----- | :---------- |
| `0x4071`       | `0xBC071`       | `0x11A`| Terry's Overworld Sprites |
| `0x418B`       | `0xBC18B`       | `0xD0` | DrakSlime Overworld Sprite |
| `0x425B`       | `0xBC25B`       | `0xE9` | SpotSlime Overworld Sprite |
| `0x4344`       | `0xBC344`       | `0xBA` | WingSlime Overworld Sprite |
| `0x43FE`       | `0xBC3FE`       | `0xAF` | TreeSlime Overworld Sprite |
| `0x44AD`       | `0xBC4AD`       | `0xE5` | Snaily Overworld Sprite |
| `0x4592`       | `0xBC592`       | `0xDE` | SlimeNite Overworld Sprite |
| `0x4670`       | `0xBC670`       | `0xBC` | Babble Overworld Sprite |
| `0x472C`       | `0xBC72C`       | `0x82` | BoxSlime Overworld Sprite |
| `0x47AE`       | `0xBC7AE`       | `0x66` | Slime Overworld Sprite |
| `0x4814`       | `0xBC814`       | `0xAE` | Healer Overworld Sprite |
| `0x48C2`       | `0xBC8C2`       | `0xE1` | FangSlime Overworld Sprite |
| `0x49A3`       | `0xBC9A3`       | `0xE2` | RockSlime Overworld Sprite |
| `0x4A85`       | `0xBCA85`       | `0xC3` | SlimeBorg Overworld Sprite |
| `0x4B48`       | `0xBCB48`       | `0xAD` | Slabbit Overworld Sprite |
| `0x4BF5`       | `0xBCBF5`       | `0xE2` | SpotKing Overworld Sprite |
| `0x4CD7`       | `0xBCCD7`       | `0xB8` | KingSlime Overworld Sprite |

***Note:** Metaly, Metabble, MetalKing and GoldSlime's (the remaining Slimes) Overworld sprites are not included in this bank.*

### Battle Sprite Table
| Offset (Local) | Offset (Global) | Length | Description |
| :------------- | :-------------- | :----- | :---------- |
| `0x` | `0x` | `0x` | DrakSlime Battle Sprite |
| `0x` | `0x` | `0x` | SpotSlime Battle Sprite |
| `0x` | `0x` | `0x` | WingSlime Battle Sprite |
| `0x` | `0x` | `0x` | Battle Sprite |
---

## Technical Notes & Observations

### [Sub-System Name]
* **Compression/Encoding:** [e.g., 1BPP -> 2BPP Expansion, custom 0x08, None]
* **Debugger Notes:** * [Add your BGB debugging observations here]   
sprite breakdown w/ headers examples
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

[⬅️ Back to Master ROM Map](../DWM_Master_ROM_Map.md)

* I still need to decompress everything here to verify these are actually all THESE sprites