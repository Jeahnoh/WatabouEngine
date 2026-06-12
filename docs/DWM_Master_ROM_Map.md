# DWM: Master ROM Map
## General Notes
- All *actual* ROM Banks are prefixed with the hex Bank ID in the first byte, ie, `Bank 2F`'s first byte is `0x2F` at `0xBC000`. The usage of this byte is currently unknown to be except as a visual marker for developers, however, it is possible it is used as a stored ID for when the bank is loaded to RAM, and is used for jumps in relative position to navigate across multiple banks. Any *other* ROM Banks that don't follow this pattern is already empty, or contains known byte for byte matches to Wario Land II, which does not follow that patterning. And `Bank 00` also doesn't intially follow this pattern, however, there is a `0x00` at `0x100`, which other games start their header data.

### Bank Templates
| Bank | Start    | End      | Size  | Category      | Description / Contents                  | Status       | Notes Link |
| :--- | :------- | :------- | :---- | :------------ | :-------------------------------------- | :----------- | :--------- |
| `00` | `0x0000` | `0x3FFF` | 16KB  | Core Engine   | RST vectors, Cart Header, 1BPP UI Math  | Mapped       | [Bank 00](./DWM_ROM_Maps/000_Bank_00.md) |
| `08` | `0x20000` | `0x23FFF` | 16KB  | UI       | Super Gameboy Borders         | Researching  | [Bank 08](./DWM_ROM_Maps/008_Bank_08.md) |
| `2F` | `0x4000` | `0x7FFF` | 16KB  | UI/Text Assets| Text Arrows, Cursors, Static UI Icons   | Extracting   | [Bank 2F](./DWM_ROM_Maps/047_Bank_2F.md) |
| `4F` | `0x4000` | `0x7FFF` | 16KB  | Font          | Core 2BPP Font Graphics                 | Mapped       | [Bank 4F](./DWM_ROM_Maps/079_Bank_4F.md) |
| `??` | `????`   | `????`   | ???   | Sprites       | Overworld Sprites (Terry, NPCs)         | Researching  | [Overworld Sprites](./DWM_ROM_Maps/Overworld_Sprites.md) |
---
### xxx Banks
| Bank | Start    | End      | Size  | Category      | Description / Contents                  | Status       | Notes Link |
| :--- | :------- | :------- | :---- | :------------ | :-------------------------------------- | :----------- | :--------- |
| `00` | `0x100` | `0x3FFF` | 15.75KB | Core Engine | | Unmapped | [Bank 00](./DWM_ROM_Maps/000_Bank_00.md) |
| `01` | `0x4000` | `0x7FFF` | 16KB  | Unknown | | Unmapped | [Bank 01](./DWM_ROM_Maps/001_Bank_01.md) |
| `02` | `0x8000` | `0xBFFF` | 16KB  | Unknown | | Unmapped | [Bank 02](./DWM_ROM_Maps/002_Bank_02.md) |
| `03` | `0xC000` | `0xFFFF` | 16KB  | Unknown | | Unmapped | [Bank 03](./DWM_ROM_Maps/003_Bank_03.md) |
| `04` | `0x10000` | `0x13FFF` | 16KB  | Unknown | | Unmapped | [Bank 04](./DWM_ROM_Maps/004_Bank_04.md) |
| `05` | `0x14000` | `0x17FFF` | 16KB  | Unknown | | Unmapped | [Bank 05](./DWM_ROM_Maps/005_Bank_05.md) |
| `06` | `0x18000` | `0x1BFFF` | 16KB  | Unknown | Skill data | Unmapped | [Bank 06](./DWM_ROM_Maps/006_Bank_06.md) |
| `07` | `0x1C000` | `0x1FFFF` | 16KB  | Unknown | | Unmapped | [Bank 07](./DWM_ROM_Maps/007_Bank_07.md) |
| `08` | `0x20000` | `0x23FFF` | 16KB  | Unknown | Super Gameboy Borders | Unmapped | [Bank 08](./DWM_ROM_Maps/008_Bank_08.md) |
| `09` | `0x24000` | `0x27FFF` | 16KB  | Unknown | | Unmapped | [Bank 09](./DWM_ROM_Maps/009_Bank_09.md) |
| `0A` | `0x28000` | `0x2BFFF` | 16KB  | Unknown | | Unmapped | [Bank 0A](./DWM_ROM_Maps/010_Bank_0A.md) |
| `0B` | `0x2C000` | `0x2FFFF` | 16KB  | Unknown | | Unmapped | [Bank 0B](./DWM_ROM_Maps/011_Bank_0B.md) |
| `0C` | `0x30000` | `0x33FFF` | 16KB  | Unknown | | Unmapped | [Bank 0C](./DWM_ROM_Maps/012_Bank_0C.md) |
| `0D` | `0x34000` | `0x37FFF` | 16KB  | Unknown | | Unmapped | [Bank 0D](./DWM_ROM_Maps/013_Bank_0D.md) |
| `0E` | `0x38000` | `0x3BFFF` | 16KB  | Unknown | | Unmapped | [Bank 0E](./DWM_ROM_Maps/014_Bank_0E.md) |
| `0F` | `0x3C000` | `0x3FFFF` | 16KB  | Unknown | | Unmapped | [Bank 0F](./DWM_ROM_Maps/015_Bank_0F.md) |
| `10` | `0x40000` | `0x43FFF` | 16KB  | Unknown | | Unmapped | [Bank 10](./DWM_ROM_Maps/016_Bank_10.md) |
| `11` | `0x44000` | `0x47FFF` | 16KB  | Unknown | | Unmapped | [Bank 11](./DWM_ROM_Maps/017_Bank_11.md) |
| `12` | `0x48000` | `0x4BFFF` | 16KB  | Unknown | | Unmapped | [Bank 12](./DWM_ROM_Maps/018_Bank_12.md) |
| `13` | `0x4C000` | `0x4FFFF` | 16KB  | Unknown | | Unmapped | [Bank 13](./DWM_ROM_Maps/019_Bank_13.md) |
| `14` | `0x50000` | `0x53FFF` | 16KB  | Unknown | | Unmapped | [Bank 14](./DWM_ROM_Maps/020_Bank_14.md) |
| `15` | `0x54000` | `0x57FFF` | 16KB  | Unknown | | Unmapped | [Bank 15](./DWM_ROM_Maps/021_Bank_15.md) |
| `16` | `0x58000` | `0x5BFFF` | 16KB  | Unknown | | Unmapped | [Bank 16](./DWM_ROM_Maps/022_Bank_16.md) |
| `17` | `0x5C000` | `0x5FFFF` | 16KB  | Unknown | | Unmapped | [Bank 17](./DWM_ROM_Maps/023_Bank_17.md) |
| `18` | `0x60000` | `0x63FFF` | 16KB  | Unknown | | Unmapped | [Bank 18](./DWM_ROM_Maps/024_Bank_18.md) |
| `19` | `0x64000` | `0x67FFF` | 16KB  | Unknown | | Unmapped | [Bank 19](./DWM_ROM_Maps/025_Bank_19.md) |
| `1A` | `0x68000` | `0x6BFFF` | 16KB  | Unknown | | Unmapped | [Bank 1A](./DWM_ROM_Maps/026_Bank_1A.md) |
| `1B` | `0x6C000` | `0x6FFFF` | 16KB  | Unknown | | Unmapped | [Bank 1B](./DWM_ROM_Maps/027_Bank_1B.md) |
| `1C` | `0x70000` | `0x73FFF` | 16KB  | Unknown | | Unmapped | [Bank 1C](./DWM_ROM_Maps/028_Bank_1C.md) |
| `1D` | `0x74000` | `0x77FFF` | 16KB  | Unknown | | Unmapped | [Bank 1D](./DWM_ROM_Maps/029_Bank_1D.md) |
| `1E` | `0x78000` | `0x7BFFF` | 16KB  | Unknown | | Unmapped | [Bank 1E](./DWM_ROM_Maps/030_Bank_1E.md) |
| `1F` | `0x7C000` | `0x7FFFF` | 16KB  | Unknown | | Unmapped | [Bank 1F](./DWM_ROM_Maps/031_Bank_1F.md) |
| `20` | `0x80000` | `0x83FFF` | 16KB  | Unknown | | Unmapped | [Bank 20](./DWM_ROM_Maps/032_Bank_20.md) |
| `21` | `0x84000` | `0x87FFF` | 16KB  | Unknown | | Unmapped | [Bank 21](./DWM_ROM_Maps/033_Bank_21.md) |
| `22` | `0x88000` | `0x8BFFF` | 16KB  | Unknown | | Unmapped | [Bank 22](./DWM_ROM_Maps/034_Bank_22.md) |
| `23` | `0x8C000` | `0x8FFFF` | 16KB  | Tiles | Graphic Bank | Unmapped | [Bank 23](./DWM_ROM_Maps/035_Bank_23.md) |
| `24` | `0x90000` | `0x93FFF` | 16KB  | Tiles | Graphic Bank | Unmapped | [Bank 24](./DWM_ROM_Maps/036_Bank_24.md) |
| `25` | `0x94000` | `0x97FFF` | 16KB  | Tiles | Graphic Bank | Unmapped | [Bank 25](./DWM_ROM_Maps/037_Bank_25.md) |
| `26` | `0x98000` | `0x9BFFF` | 16KB  | Unknown | | Unmapped | [Bank 26](./DWM_ROM_Maps/038_Bank_26.md) |
| `27` | `0x9C000` | `0x9FFFF` | 16KB  | Unknown | | Unmapped | [Bank 27](./DWM_ROM_Maps/039_Bank_27.md) |
| `28` | `0xA0000` | `0xA3FFF` | 16KB  | Unknown | | Unmapped | [Bank 28](./DWM_ROM_Maps/040_Bank_28.md) |
| `29` | `0xA4000` | `0xA7FFF` | 16KB  | Unknown | | Unmapped | [Bank 29](./DWM_ROM_Maps/041_Bank_29.md) |
| `2A` | `0xA8000` | `0xABFFF` | 16KB  | Unknown | | Unmapped | [Bank 2A](./DWM_ROM_Maps/042_Bank_2A.md) |
| `2B` | `0xAC000` | `0xAFFFF` | 16KB  | Unknown | | Unmapped | [Bank 2B](./DWM_ROM_Maps/043_Bank_2B.md) |
| `2C` | `0xB0000` | `0xB3FFF` | 16KB  | Unknown | | Unmapped | [Bank 2C](./DWM_ROM_Maps/044_Bank_2C.md) |
| `2D` | `0xB4000` | `0xB7FFF` | 16KB  | Unknown | | Unmapped | [Bank 2D](./DWM_ROM_Maps/045_Bank_2D.md) |
| `2E` | `0xB8000` | `0xBBFFF` | 16KB  | Unknown | | Unmapped | [Bank 2E](./DWM_ROM_Maps/046_Bank_2E.md) |
| `2F` | `0xBC000` | `0xBFFFF` | 16KB  | Sprites | Sprite Bank | Active Mapping | [Bank 2F](./DWM_ROM_Maps/047_Bank_2F.md) | MY FAVORITE BANK
| `30` | `0xC0000` | `0xC3FFF` | 16KB  | Unknown | | Unmapped | [Bank 30](./DWM_ROM_Maps/048_Bank_30.md) |
| `31` | `0xC4000` | `0xC7FFF` | 16KB  | Unknown | | Unmapped | [Bank 31](./DWM_ROM_Maps/049_Bank_31.md) |
| `32` | `0xC8000` | `0xCBFFF` | 16KB  | Unknown | | Unmapped | [Bank 32](./DWM_ROM_Maps/050_Bank_32.md) |
| `33` | `0xCC000` | `0xCFFFF` | 16KB  | Unknown | | Unmapped | [Bank 33](./DWM_ROM_Maps/051_Bank_33.md) |
| `34` | `0xD0000` | `0xD3FFF` | 16KB  | Unknown | | Unmapped | [Bank 34](./DWM_ROM_Maps/052_Bank_34.md) |
| `35` | `0xD4000` | `0xD7FFF` | 16KB  | Unknown | | Unmapped | [Bank 35](./DWM_ROM_Maps/053_Bank_35.md) |
| `36` | `0xD8000` | `0xDBFFF` | 16KB  | Unknown | | Unmapped | [Bank 36](./DWM_ROM_Maps/054_Bank_36.md) |
| `37` | `0xDC000` | `0xDFFFF` | 16KB  | Unknown | | Unmapped | [Bank 37](./DWM_ROM_Maps/055_Bank_37.md) |
| `38` | `0xE0000` | `0xE3FFF` | 16KB  | Unknown | | Unmapped | [Bank 38](./DWM_ROM_Maps/056_Bank_38.md) |
| `39` | `0xE4000` | `0xE7FFF` | 16KB  | Unknown | | Unmapped | [Bank 39](./DWM_ROM_Maps/057_Bank_39.md) |
| `3A` | `0xE8000` | `0xEBFFF` | 16KB  | Unknown | | Unmapped | [Bank 3A](./DWM_ROM_Maps/058_Bank_3A.md) |
| `3B` | `0xEC000` | `0xEFFFF` | 16KB  | Unknown | | Unmapped | [Bank 3B](./DWM_ROM_Maps/059_Bank_3B.md) |
| `3C` | `0xF0000` | `0xF3FFF` | 16KB  | Unknown | | Unmapped | [Bank 3C](./DWM_ROM_Maps/060_Bank_3C.md) |
| `3D` | `0xF4000` | `0xF7FFF` | 16KB  | Unknown | | Unmapped | [Bank 3D](./DWM_ROM_Maps/061_Bank_3D.md) |
| `3E` | `0xF8000` | `0xFBFFF` | 16KB  | Unknown | | Unmapped | [Bank 3E](./DWM_ROM_Maps/062_Bank_3E.md) |
| `3F` | `0xFC000` | `0xFFFFF` | 16KB  | Unknown | | Unmapped | [Bank 3F](./DWM_ROM_Maps/063_Bank_3F.md) |
| `40` | `0x100000` | `0x103FFF` | 16KB  | Unknown | | Unmapped | [Bank 40](./DWM_ROM_Maps/064_Bank_40.md) |
| `41` | `0x104000` | `0x107FFF` | 16KB  | Unknown | | Unmapped | [Bank 41](./DWM_ROM_Maps/065_Bank_41.md) |
| `42` | `0x108000` | `0x10BFFF` | 16KB  | Unknown | | Unmapped | [Bank 42](./DWM_ROM_Maps/066_Bank_42.md) |
| `43` | `0x10C000` | `0x10FFFF` | 16KB  | Unknown | | Unmapped | [Bank 43](./DWM_ROM_Maps/067_Bank_43.md) |
| `44` | `0x110000` | `0x113FFF` | 16KB  | Unknown | | Unmapped | [Bank 44](./DWM_ROM_Maps/068_Bank_44.md) |
| `45` | `0x114000` | `0x117FFF` | 16KB  | Unknown | | Unmapped | [Bank 45](./DWM_ROM_Maps/069_Bank_45.md) |
| `46` | `0x118000` | `0x11BFFF` | 16KB  | Unknown | | Unmapped | [Bank 46](./DWM_ROM_Maps/070_Bank_46.md) |
| `47` | `0x11C000` | `0x11FFFF` | 16KB  | Unknown | | Unmapped | [Bank 47](./DWM_ROM_Maps/071_Bank_47.md) |
| `48` | `0x120000` | `0x123FFF` | 16KB  | Unknown | | Unmapped | [Bank 48](./DWM_ROM_Maps/072_Bank_48.md) |
| `49` | `0x124000` | `0x127FFF` | 16KB  | Unknown | | Unmapped | [Bank 49](./DWM_ROM_Maps/073_Bank_49.md) |
| `4A` | `0x128000` | `0x12BFFF` | 16KB  | Unknown | | Unmapped | [Bank 4A](./DWM_ROM_Maps/074_Bank_4A.md) |
| `4B` | `0x12C000` | `0x12FFFF` | 16KB  | Unknown | | Unmapped | [Bank 4B](./DWM_ROM_Maps/075_Bank_4B.md) |
| `4C` | `0x130000` | `0x133FFF` | 16KB  | Unknown | | Unmapped | [Bank 4C](./DWM_ROM_Maps/076_Bank_4C.md) |
| `4D` | `0x134000` | `0x137FFF` | 16KB  | Unknown | | Unmapped | [Bank 4D](./DWM_ROM_Maps/077_Bank_4D.md) |
| `4E` | `0x138000` | `0x13BFFF` | 16KB  | Unknown | | Unmapped | [Bank 4E](./DWM_ROM_Maps/078_Bank_4E.md) |
| `4F` | `0x13C000` | `0x13FFFF` | 16KB  | Unknown | | Unmapped | [Bank 4F](./DWM_ROM_Maps/079_Bank_4F.md) |
| `50` | `0x140000` | `0x143FFF` | 16KB  | Unknown | | Unmapped | [Bank 50](./DWM_ROM_Maps/080_Bank_50.md) |
| `51` | `0x144000` | `0x147FFF` | 16KB  | Unknown | | Unmapped | [Bank 51](./DWM_ROM_Maps/081_Bank_51.md) |
| `52` | `0x148000` | `0x14BFFF` | 16KB  | Unknown | | Unmapped | [Bank 52](./DWM_ROM_Maps/082_Bank_52.md) |
| `53` | `0x14C000` | `0x14FFFF` | 16KB  | Unknown | | Unmapped | [Bank 53](./DWM_ROM_Maps/083_Bank_53.md) |
| `54` | `0x150000` | `0x153FFF` | 16KB  | Unknown | | Unmapped | [Bank 54](./DWM_ROM_Maps/084_Bank_54.md) |
| `55` | `0x154000` | `0x157FFF` | 16KB  | Unknown | | Unmapped | [Bank 55](./DWM_ROM_Maps/085_Bank_55.md) |
| `56` | `0x158000` | `0x15BFFF` | 16KB  | Unknown | | Unmapped | [Bank 56](./DWM_ROM_Maps/086_Bank_56.md) |
| `57` | `0x15C000` | `0x15FFFF` | 16KB  | Unknown | | Unmapped | [Bank 57](./DWM_ROM_Maps/087_Bank_57.md) |
| `58` | `0x160000` | `0x163FFF` | 16KB  | Unknown | | Unmapped | [Bank 58](./DWM_ROM_Maps/088_Bank_58.md) |
| `59` | `0x164000` | `0x167FFF` | 16KB  | Unknown | | Unmapped | [Bank 59](./DWM_ROM_Maps/089_Bank_59.md) |
| `5A` | `0x168000` | `0x16BFFF` | 16KB  | Unknown | | Unmapped | [Bank 5A](./DWM_ROM_Maps/090_Bank_5A.md) |
| `5B` | `0x16C000` | `0x16FFFF` | 16KB  | Unknown | | Unmapped | [Bank 5B](./DWM_ROM_Maps/091_Bank_5B.md) |
| `5C` | `0x170000` | `0x173FFF` | 16KB  | Unknown | | Unmapped | [Bank 5C](./DWM_ROM_Maps/092_Bank_5C.md) |
| `5D` | `0x174000` | `0x177FFF` | 16KB  | Unknown | | Unmapped | [Bank 5D](./DWM_ROM_Maps/093_Bank_5D.md) |
| `5E` | `0x178000` | `0x17BFFF` | 16KB  | Unknown | | Unmapped | [Bank 5E](./DWM_ROM_Maps/094_Bank_5E.md) |
| `5F` | `0x17C000` | `0x17FFFF` | 16KB  | Unknown | | Unmapped | [Bank 5F](./DWM_ROM_Maps/095_Bank_5F.md) |

---
### Empty/Garbage Banks
These Banks contain no useful data that is utilized in Dragon Warrior Monsters in any known capacity. Prime real estate for custom content to be added. There are other empty/garbage sectors in prior banks, however these banks should be safe to fully zero out.
| Bank | Start    | End      | Size  | Category      | Description / Contents                  | Status       | Notes Link |
| :--- | :------- | :------- | :---- | :------------ | :-------------------------------------- | :----------- | :--------- |
| `60` | `0x180000` | `0x183FFF` | 16KB  | Empty | Empty Bank | Mapped | [Bank 60](./DWM_ROM_Maps/096_Bank_60.md)    |
| `61` | `0x184000` | `0x187FFF` | 16KB  | Empty | Functionally Empty Bank. Garbage Wario Land II Data. | Mapped | [Bank 61](./DWM_ROM_Maps/097_Bank_61.md)    |
| `62` | `0x188000` | `0x18BFFF` | 16KB  | Empty | Functionally Empty Bank. Garbage Wario Land II Data. | Mapped | [Bank 62](./DWM_ROM_Maps/098_Bank_62.md)    |
| `63` | `0x18C000` | `0x18FFFF` | 16KB  | Empty | Functionally Empty Bank. Garbage Wario Land II Data. | Mapped | [Bank 63](./DWM_ROM_Maps/099_Bank_63.md)    |
| `64` | `0x190000` | `0x193FFF` | 16KB  | Empty | Empty Bank | Mapped | [Bank 64](./DWM_ROM_Maps/100_Bank_64.md)    |
| `65` | `0x194000` | `0x197FFF` | 16KB  | Empty | Functionally Empty Bank. Garbage Wario Land II Data. | Mapped | [Bank 65](./DWM_ROM_Maps/101_Bank_65.md)    |
| `66` | `0x198000` | `0x19BFFF` | 16KB  | Empty | Functionally Empty Bank. Garbage Wario Land II Data. | Mapped | [Bank 66](./DWM_ROM_Maps/102_Bank_66.md)    |
| `67` | `0x19C000` | `0x19FFFF` | 16KB  | Empty | Empty Bank | Mapped | [Bank 67](./DWM_ROM_Maps/103_Bank_67.md)    |
| `68` | `0x1A0000` | `0x1A3FFF` | 16KB  | Empty | Functionally Empty Bank. Garbage Wario Land II Data. | Mapped | [Bank 68](./DWM_ROM_Maps/104_Bank_68.md)    |
| `69` | `0x1A4000` | `0x1A7FFF` | 16KB  | Empty | Empty Bank | Mapped | [Bank 69](./DWM_ROM_Maps/105_Bank_69.md)    |
| `6A` | `0x1A8000` | `0x1ABFFF` | 16KB  | Empty | Empty Bank | Mapped | [Bank 6A](./DWM_ROM_Maps/106_Bank_6A.md)    |
| `6B` | `0x1AC000` | `0x1AFFFF` | 16KB  | Empty | Empty Bank | Mapped | [Bank 6B](./DWM_ROM_Maps/107_Bank_6B.md)    |
| `6C` | `0x1B0000` | `0x1B3FFF` | 16KB  | Empty | Empty Bank | Mapped | [Bank 6C](./DWM_ROM_Maps/108_Bank_6C.md)    |
| `6D` | `0x1B4000` | `0x1B7FFF` | 16KB  | Empty | Empty Bank | Mapped | [Bank 6D](./DWM_ROM_Maps/109_Bank_6D.md)    |
| `6E` | `0x1B8000` | `0x1BBFFF` | 16KB  | Empty | Empty Bank | Mapped | [Bank 6E](./DWM_ROM_Maps/110_Bank_6E.md)    |
| `6F` | `0x1BC000` | `0x1BFFFF` | 16KB  | Empty | Empty Bank | Mapped | [Bank 6F](./DWM_ROM_Maps/111_Bank_6F.md)    |
| `70` | `0x1C0000` | `0x1C3FFF` | 16KB  | Empty | Empty Bank | Mapped | [Bank 70](./DWM_ROM_Maps/112_Bank_70.md)    |
| `71` | `0x1C4000` | `0x1C7FFF` | 16KB  | Empty | Empty Bank | Mapped | [Bank 71](./DWM_ROM_Maps/113_Bank_71.md)    |
| `72` | `0x1C8000` | `0x1CBFFF` | 16KB  | Empty | Empty Bank | Mapped | [Bank 72](./DWM_ROM_Maps/114_Bank_72.md)    |
| `73` | `0x1CC000` | `0x1CFFFF` | 16KB  | Empty | Empty Bank | Mapped | [Bank 73](./DWM_ROM_Maps/115_Bank_73.md)    |
| `74` | `0x1D0000` | `0x1D3FFF` | 16KB  | Empty | Empty Bank | Mapped | [Bank 74](./DWM_ROM_Maps/116_Bank_74.md)    |
| `75` | `0x1D4000` | `0x1D7FFF` | 16KB  | Empty | Empty Bank | Mapped | [Bank 75](./DWM_ROM_Maps/117_Bank_75.md)    |
| `76` | `0x1D8000` | `0x1DBFFF` | 16KB  | Empty | Empty Bank | Mapped | [Bank 76](./DWM_ROM_Maps/118_Bank_76.md)    |
| `77` | `0x1DC000` | `0x1DFFFF` | 16KB  | Empty | Empty Bank | Mapped | [Bank 77](./DWM_ROM_Maps/119_Bank_77.md)    |
| `78` | `0x1E0000` | `0x1E3FFF` | 16KB  | Empty | Functionally Empty Bank. Garbage Wario Land II Data. | Mapped | [Bank 78](./DWM_ROM_Maps/120_Bank_78.md)    |
| `79` | `0x1E4000` | `0x1E7FFF` | 16KB  | Empty | Empty Bank | Mapped | [Bank 79](./DWM_ROM_Maps/121_Bank_79.md)    |
| `7A` | `0x1E8000` | `0x1EBFFF` | 16KB  | Empty | Empty Bank | Mapped | [Bank 7A](./DWM_ROM_Maps/122_Bank_7A.md)    |
| `7B` | `0x1EC000` | `0x1EFFFF` | 16KB  | Empty | Functionally Empty Bank. Garbage Wario Land II Data. | Mapped | [Bank 7B](./DWM_ROM_Maps/123_Bank_7B.md)    |
| `7C` | `0x1F0000` | `0x1F3FFF` | 16KB  | Empty | Empty Bank | Mapped | [Bank 7C](./DWM_ROM_Maps/124_Bank_7C.md)    |
| `7D` | `0x1F4000` | `0x1F7FFF` | 16KB  | Empty | Functionally Empty Bank. Garbage Wario Land II Data. | Mapped | [Bank 7D](./DWM_ROM_Maps/125_Bank_7D.md)    |
| `7E` | `0x1F8000` | `0x1FBFFF` | 16KB  | Empty | Empty Bank | Mapped | [Bank 7E](./DWM_ROM_Maps/126_Bank_7E.md)    |
| `7F` | `0x1FC000` | `0x1FFFFF` | 16KB  | Empty | Empty Bank | Mapped | [Bank 7F](./DWM_ROM_Maps/127_Bank_7F.md)    | 
---
© 2026 Jeahnoh. Licensed under CC BY-NC 4.0. Attribution Required.
See LICENSE.md in the repository root for full non-commercial terms.