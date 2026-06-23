[⬅️ Back to Master ROM Map](../DWM_Master_ROM_Map.md)
        
# Bank `0x1F`: Dialogue Tables `0x03` - `0x05`
## Overview
**Local Hex Range:** `0x4000` - `0x7FFF`  
**Global Hex Range:** `0x07C000` - `0x07FFFF`  
**Bank Type:** Swappable  
**Category:** Text  
**Summary:** This bank includes three Text Data Tables, and three standard Assembly subroutines to call text box functions.

---

<a id="top"></a>
## Master Memory Map (General Overview)
*Breakdown of the specific block sectors within this bank.*

| Offset (Local) | Offset (Global) | Length | Description |
| :------------- | :-------------- | :----- | :---------- |
| `0x4000` | `0x7C000` | `0x106` | [Bank Meta Table](#meta) |
| `0x4106` | `0x7C106` | `0x1CB5` | [Text Table](#data-1) `0x03` -  General Dialogue (C Class / Mid-game) |
| `0x5DBB` | `0x7DDBB` | `0x13FE` | [Text Table](#data-2) `0x04` - Starry Night Tournament |
| `0x71B9` | `0x7F1B9` | `0x844` | [Text Table](#data-3) `0x05` - Ending |
| `0x79FD` | `0x7F9FD` | `0xC4` | *Wario Land II* data.[^1] | 
| `0x7AC1` | `0x7FAC1` | `0x53F` | `0x00` padding (Safe Free Space) |

[^1]: Exact match of bytes and location.

---

<a id="meta"></a>
## Bank Meta Table
*Breakdown of the blocks within this bank's Meta Table.*

| Offset (Local) | Offset (Global) | Length | Description |
| :------------- | :-------------- | :----- | :---------- |
| `0x4000` | `0x7C000` | `0x1` | Bank ID Header (`0x1F`) |
| `0x4001` | `0x7C001` | `0x6` | Jump Table (3 Assembly Subroutines) |
| `0x4007` | `0x7C007` | `0x6` | Master Pointer Table (3 Data Tables) |
| `0x400D` | `0x7C00D` | `0x80` | [Data Pointer Table](#data-1) (64 Dialogue Pointers) |
| `0x408D` | `0x7C08D` | `0x40` | [Data Pointer Table](#data-2) (32 Dialogue Pointers) |
| `0x40CD` | `0x7C0CD` | `0x24` | [Data Pointer Table](#data-3) (18 Dialogue Pointers) |
| `0x40F1` | `0x7C0F1` | `0x1D` | [Assembly Subroutine 1](#subroutine-1) |
| `0x40F8` | `0x7C0F8` | `0x1D` | [Assembly Subroutine 2](#subroutine-2) |
| `0x40FF` | `0x7C0FF` | `0x1D` | [Assembly Subroutine 3](#subroutine-3) |

---

### Raw Memory Map
*Visual breakdown of the engine's memory routing. Refer to the Master ROM Map for structural notation key.*

```hex
Hex View  00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
 
0007C000  [1F]|F1 40 F8 40 FF 40|(0D  40 8D 40 CD 40){06 41 2C
0007C010  41 5D 41 93 41 C8 41 2E  42 51 42 8C 42 EB 42 6B  
0007C020  43 8B 43 79 45 C5 45 28  46 6C 46 A0 46 D8 46 72  
0007C030  47 E7 47 BC 48 DC 48 3B  49 97 49 B6 49 E7 49 23  
0007C040  4A 66 4A 09 4B 35 4B 64  4B A0 4B D0 4B 3D 4C 91  
0007C050  4D 23 4E 1B 50 72 50 03  51 41 51 68 51 B6 51 17  
0007C060  52 93 52 C6 52 77 53 8B  53 D1 53 DB 54 1B 56 6E  
0007C070  56 AB 56 EA 56 FA 57 8F  58 5A 59 32 5A 79 5A 75  
0007C080  5B 8B 5B B0 5B 5F 5C E9  5C 5C 5D 87 5D}{BB 5D EC
0007C090  5D 62 5E 93 5E EE 5F CA  60 6D 63 16 64 20 64 A0  
0007C0A0  64 BF 64 E6 64 23 65 85  65 03 66 3B 66 C5 67 0C  
0007C0B0  69 5F 6A DF 6B 85 6C 97  6D 41 6E D6 6E 05 6F 1F  
0007C0C0  6F 33 6F 87 6F 9B 70 D3  70 12 71 9B 71}{B9 71 CB
0007C0D0  71 E1 71 37 72 80 72 2E  73 7D 73 DC 73 F4 73 0B  
0007C0E0  74 2B 74 72 74 81 74 AF  74 4A 75 D0 75 D7 77 F3  
0007C0F0  77}<11 07 40 CD B6 05 C9><11 07 40 CD F6 05 C9><CD
0007C100  F1 40 CD 09 06 C9>      
```

[⬆️ Back to Top](#top)

---

## Subroutines
These three local assembly routines act as standard wrappers. They feed the data pointers from this bank into the game's core execution library in Bank 0 to parse and display the dialogue on the screen.

<a id="subroutine-1"></a>
### Subroutine 1 (`0x40F1`) - The Memory State Setter
*This simple wrapper routine passes the Master Pointer Table to the engine's core library in Bank 0 (`0x05B6`). The Bank 0 routine then sets up the active Work RAM (WRAM) variables needed to prepare the engine to parse text.*

```assembly
11 07 40    LD DE, $4007      ; Loads Master Pointer Table to DE
CD B6 05    CALL   $05B6      ; Calls Bank 0 Memory Prep Routine
C9          RET               ; Return
```

[⬆️ Back to Top](#top)

<a id="subroutine-2"></a>
### Subroutine 2 (`0x40F8`) - The Text String Copier
*This simple wrapper routine passes the Master Pointer Table to the engine's core library in Bank 0 (`0x05F6`), which triggers a loop that copies the text bytes into Work RAM (WRAM) until it hits the `[End]` (`0xF0`) control code.* 

```assembly
11 07 40    LD DE, $4007      ; Loads Master Pointer Table to DE
CD F6 05    CALL   $05F6      ; Calls Bank 0 String Copy Loop
C9          RET               ; Return
```
[⬆️ Back to Top](#top)

<a id="subroutine-3"></a>
### Subroutine 3 (`0x40FF`) - The Execution & Wait Wrapper
*This simple wrapper routine first calls Subroutine 1 to prep the memory, then calls a Bank 0 system function (`0x0609`) which flags the UI to draw the text box and loops until the player presses the 'A' button to clear it.*

```assembly
CD F1 40    CALL $40F1        ; Calls Subroutine 1 (Memory Prep)
CD 09 06    CALL $0609        ; Calls Bank 0 Wait/Draw Loop
C9          RET               ; Return
```
[⬆️ Back to Top](#top)

---

<a id="data-1"></a>
## Dialogue Sector: Text Table `0x03` - General Dialogue (C Class / Mid-game)
*Breakdown of the 64 dialogue sequences defined by the Data Pointer Table.*

| Index | Pointer (LE) | Start (Local) | Length | String Key | Category | Audio / Flags | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `00` | `06 41` | `0x4106` | `0x26` | `VOICE_00` | UNCHECKED | `Voice(High)` | Who makes such a quake? |
| `01` | `2C 41` | `0x412C` | `0x31` | `VOICE_01` | UNCHECKED | `Voice(High)` | Hey watch where you're going! |
| `02` | `5D 41` | `0x415D` | `0x36` | `VOICE_02` | UNCHECKED | `Voice(Low)` | Thanks to the quake you can get here! |
| `03` | `93 41` | `0x4193` | `0x35` | `VOICE_03` | UNCHECKED | `Voice(High)` | There are now new shops! |
| `04` | `C8 41` | `0x41C8` | `0x66` | `VOICE_04` | UNCHECKED | `Voice(High)` | I love festivals! |
| `05` | `2E 42` | `0x422E` | `0x23` | `VOICE_05` | UNCHECKED | `Voice(High)` | Are you a monster master? |
| `06` | `51 42` | `0x4251` | `0x3B` | `VOICE_06` | UNCHECKED | `Voice(High)` | I wanna be a monster master too! |
| `07` | `8C 42` | `0x428C` | `0x5F` | `VOICE_07` | UNCHECKED | `Voice(High)` | Only those who can attract monsters can be masters. |
| `08` | `EB 42` | `0x42EB` | `0x80` | `VOICE_08` | UNCHECKED | `Voice(Low)` | The Bazaar is bigger! Do you wanna know what you can now get? |
| `09` | `6B 43` | `0x436B` | `0x20` | `VOICE_09` | UNCHECKED | `Voice(Low)` | You must be a veteran! |
| `0A` | `8B 43` | `0x438B` | `0x1EE` | `VOICE_0A` | UNCHECKED | `Voice(Low)` | About items you can buy. |
| `0B` | `79 45` | `0x4579` | `0x4C` | `VOICE_0B` | UNCHECKED | `Voice(Low)` | Wanna know what you can get? |
| `0C` | `C5 45` | `0x45C5` | `0x63` | `VOICE_0C` | UNCHECKED | `Voice(Low)` | That shopkeep is now separated! Ha! |
| `0D` | `28 46` | `0x4628` | `0x44` | `VOICE_0D` | UNCHECKED | `Voice(Low)` | There's nothing around here. |
| `0E` | `6C 46` | `0x466C` | `0x34` | `VOICE_0E` | UNCHECKED | `Voice(Low)` | It would be better if more shops were built... |
| `0F` | `A0 46` | `0x46A0` | `0x38` | `VOICE_0F` | UNCHECKED | `Voice(Low)` | Don't say that! |
| `10` | `D8 46` | `0x46D8` | `0x9A` | `VOICE_10` | UNCHECKED | `Voice(High)` | There are hidden gates around the kingdom. |
| `11` | `72 47` | `0x4772` | `0x75` | `VOICE_11` | UNCHECKED | `Voice(Low)` | Strength, Anger / Peace, Bravery Gates. |
| `12` | `E7 47` | `0x47E7` | `0xD5` | `VOICE_12` | UNCHECKED | `Voice(Low)` | Villager, Talisman / Beginning / Memories, Bewilder Gates. |
| `13` | `BC 48` | `0x48BC` | `0x20` | `VOICE_13` | UNCHECKED | None | Splash! Something hit the player! |
| `14` | `DC 48` | `0x48DC` | `0x5F` | `VOICE_14` | UNCHECKED | `Voice(Low)` | Where do monsters come from? |
| `15` | `3B 49` | `0x493B` | `0x5C` | `VOICE_15` | UNCHECKED | `Voice(Low)` | The cliffs are now connected! |
| `16` | `97 49` | `0x4997` | `0x1F` | `LIPSY_16` | UNCHECKED | `Voice(High)` | Oh Darling! |
| `17` | `B6 49` | `0x49B6` | `0x31` | `VOICE_17` | UNCHECKED | `Voice(Low)` | Go(at) down to the stables. |
| `18` | `E7 49` | `0x49E7` | `0x3C` | `VOICE_18` | UNCHECKED | `Voice(Low)` | Mostly garbage! |
| `19` | `23 4A` | `0x4A23` | `0x43` | `VOICE_19` | UNCHECKED | `Voice(Low)` | Do you want to know the max levels of your monsters? |
| `1A` | `66 4A` | `0x4A66` | `0xA3` | `VOICE_1A` | UNCHECKED | `Voice(High)` | I'm a +5 Monster! |
| `1B` | `09 4B` | `0x4B09` | `0x2C` | `VOICE_1B` | UNCHECKED | `Voice(Low)` | I'm from the Gate of Peace! |
| `1C` | `35 4B` | `0x4B35` | `0x2F` | `VOICE_1C` | UNCHECKED | `Voice(Low)` | Did you see the farm changes? |
| `1D` | `64 4B` | `0x4B64` | `0x3C` | `VOICE_1D` | UNCHECKED | `Voice(Low)` | Finally! MadKnight and Lipsy are together again! |
| `1E` | `A0 4B` | `0x4BA0` | `0x30` | `VOICE_1E` | UNCHECKED | `Voice(Low)` | Go quick! |
| `1F` | `D0 4B` | `0x4BD0` | `0x6D` | `VOICE_1F` | UNCHECKED | `Voice(Low)` | Goopi loves RoShamBo! |
| `20` | `3D 4C` | `0x4C3D` | `0x154` | `VOICE_20` | UNCHECKED | `Voice(Low)` | I was waiting for you! You have permission to compete in the C class. You need to win through S. |
| `21` | `91 4D` | `0x4D91` | `0x92` | `VOICE_21` | UNCHECKED | `Voice(Low)` | You won C Class! You get Joy and Wisdom gates! |
| `22` | `23 4E` | `0x4E23` | `0x1F8` | `VOICE_22` | UNCHECKED | `Voice(High)` | Lots of Arena Info. |
| `23` | `1B 50` | `0x501B` | `0x57` | `VOICE_23` | UNCHECKED | `Voice(High)` | The last match will be against Teto! |
| `24` | `72 50` | `0x5072` | `0x91` | `VOICE_24` | UNCHECKED | `Voice(Low)` | Hey Terry! I'm in C Class! |
| `25` | `03 51` | `0x5103` | `0x3E` | `VOICE_25` | UNCHECKED | `Voice(Low)` | The last fight will be great in C Class! |
| `26` | `41 51` | `0x5141` | `0x27` | `VOICE_26` | UNCHECKED | `Voice(Low)` | We'll have to fight again! |
| `27` | `68 51` | `0x5168` | `0x4E` | `VOICE_27` | UNCHECKED | `Voice(High)` | I wonder how my brothers are doing. |
| `28` | `B6 51` | `0x51B6` | `0x61` | `VOICE_28` | UNCHECKED | `Voice(Low)` | BeastTails do sstuff in battle too! |
| `29` | `17 52` | `0x5217` | `0x7C` | `VOICE_29` | UNCHECKED | `Voice(Low)` | I dreamt this statue could move! |
| `2A` | `93 52` | `0x5293` | `0x33` | `VOICE_2A` | UNCHECKED | `Voice(Low)` | The statue is moving! |
| `2B` | `C6 52` | `0x52C6` | `0xB1` | `VOICE_2B` | UNCHECKED | `Voice(Low)` | There are shops in the Gates. |
| `2C` | `77 53` | `0x5377` | `0x14` | `VOICE_2C` | UNCHECKED | `Voice(Low)` | Hi ho! |
| `2D` | `8B 53` | `0x538B` | `0x46` | `VOICE_2D` | UNCHECKED | `Voice(Low)` | Wanna know who's in C Class? |
| `2E` | `D1 53` | `0x53D1` | `0x10A` | `VOICE_2E` | UNCHECKED | `Voice(Low)` | Last one is Teto. |
| `2F` | `DB 54` | `0x54DB` | `0x140` | `VOICE_2F` | UNCHECKED | None | Book. About skill inheritance. |
| `30` | `1B 56` | `0x561B` | `0x53` | `VOICE_30` | UNCHECKED | `Voice(High)` | Wanna know how to change a monster's gender? |
| `31` | `6E 56` | `0x566E` | `0x3D` | `BEBE_MASTER_31` | UNCHECKED | `Voice(Low)` | This is Miso Shiru. |
| `32` | `AB 56` | `0x56AB` | `0x3F` | `VOICE_32` | UNCHECKED | `Voice(Low)` | JUST SAY SOUP! |
| `33` | `EA 56` | `0x56EA` | `0x110` | `VOICE_33` | UNCHECKED | `Voice(Low)` | Breeding tips. FangSlime / Unicorn. |
| `34` | `FA 57` | `0x57FA` | `0x95` | `VOICE_34` | UNCHECKED | None | Book. Egg Blessing. |
| `35` | `8F 58` | `0x588F` | `0xCB` | `VOICE_35` | UNCHECKED | None | Prof Monster's Diary. Terry's a good kid. |
| `36` | `5A 59` | `0x595A` | `0xD8` | `VOICE_36` | UNCHECKED | None | Terry beat D Class! |
| `37` | `32 5A` | `0x5A32` | `0x47` | `VOICE_37` | UNCHECKED | `Voice(Low)` | Isn't my daughter pretty? |
| `38` | `79 5A` | `0x5A79` | `0xFC` | `VOICE_38` | UNCHECKED | `Voice(Low)` | Don't use commands on monsters with Wild. |
| `39` | `75 5B` | `0x5B75` | `0x16` | `VOICE_39` | UNCHECKED | `Voice(Low)` | Leave me alone! |
| `3A` | `8B 5B` | `0x5B8B` | `0x24` | `VOICE_3A` | UNCHECKED | `Voice(High)` | Gramps is stubborn. |
| `3B` | `B0 5B` | `0x5BB0` | `0xB0` | `VOICE_3B` | UNCHECKED | None | Journal of My Baby, Part 1 |
| `3C` | `5F 5C` | `0x5C5F` | `0x8A` | `VOICE_3C` | UNCHECKED | None | Journal of My Baby, Part 2 |
| `3D` | `E9 5C` | `0x5CE9` | `0x73` | `VOICE_3D` | UNCHECKED | `Voice(High)` | Who are you? How did you get here? |
| `3E` | `5C 5D` | `0x5D5C` | `0x2B` | `VOICE_3E` | UNCHECKED | `Voice(High)` | Good excuse! |
| `3F` | `87 5D` | `0x5D87` | `0x34` | `VOICE_3F` | UNCHECKED | `Voice(High)` | Did you sneak in to steal things? |

[⬆️ Back to Top](#top)

---

<a id="data-2"></a>
## Dialogue Sector: Text Table `0x04` - Starry Night Tournament
*Breakdown of the 32 dialogue sequences defined by the Data Pointer Table.*

| Index | Pointer (LE) | Start (Local) | Length | String Key | Category | Audio / Flags | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `00` | `BB 5D` | `0x5DBB` | `0x31` | `VOICE_40` | Starry Night | `Voice(High)` | BigTrunk vs. GreatTree. |
| `01` | `EC 5D` | `0x5DEC` | `0x76` | `VOICE_41` | Starry Night | `Voice(High)` | GreatTree won! |
| `02` | `62 5E` | `0x5E62` | `0x31` | `VOICE_42` | Starry Night | `Voice(High)` | DeadTree vs. GreatTree. |
| `03` | `93 5E` | `0x5E93` | `0x15B` | `VOICE_43` | Starry Night | `Voice(High)` | The rep of GreetTree, you! |
| `04` | `EE 5F` | `0x5FEE` | `0xDC` | `VOICE_44` | Starry Night | `Voice(High)` | The rep of GreatLog, Milayou! |
| `05` | `CA 60` | `0x60CA` | `0x2A3` | `MILAYOU_45` | Starry Night | `Voice(High)` | Hello there! ~~General Kenobi~~ Terry! |
| `06` | `6D 63` | `0x636D` | `0xA9` | `MILAYOU_46` | Starry Night | `Voice(High)` | Challenging me again? |
| `07` | `16 64` | `0x6416` | `0xA` | `VOICE_47` | Starry Night | None | Empty. |
| `08` | `20 64` | `0x6420` | `0x80` | `MILAYOU_48` | Starry Night | `Voice(High)` | Let's fight! |
| `09` | `A0 64` | `0x64A0` | `01Fx` | `MILAYOU_49` | Starry Night | `Voice(High)` | You were strong! |
| `0A` | `BF 64` | `0x64BF` | `0x27` | `WARUBOU_xx` | Starry Night | `Voice(Low)` | You're useless now! |
| `0B` | `E6 64` | `0x64E6` | `0x3D` | `VOICE_4B` | Starry Night | `Voice(High)` | Congratulations! You're a star! |
| `0C` | `23 65` | `0x6523` | `0x62` | `MAY_00` | Starry Night | `Voice(High)` | That's my Terry! |
| `0D` | `85 65` | `0x6585` | `0x7E` | `MICK_4D` | Starry Night | `Voice(Low)` | I came back to congratulate you! |
| `0E` | `03 66` | `0x6603` | `0x38` | `MICK_4E` | Starry Night | `Voice(Low)` | Congratulations! |
| `0F` | `3B 66` | `0x663B` | `0x18A` | `KING_4F` | Starry Night | `Voice(Low)` | Congratulations! You won! |
| `10` | `C5 67` | `0x67C5` | `0x147` | `KING_50` | Starry Night | `Voice(Low)` | Why don't you stay and live here in GreatTree? |
| `11` | `0C 69` | `0x690C` | `0x153` | `KING_51` | Starry Night | `Voice(Low)` | Go to the Starry Shrine. |
| `12` | `5F 6A` | `0x6A5F` | `0x180` | `KING_52` | Starry Night | `Voice(Low)` | You'll stay? Go to the Starry Shrine. |
| `13` | `DF 6B` | `0x6BDF` | `0xA6` | `KING_53` | Starry Night | `Voice(Low)` | Go to the Starry Shrine. |
| `14` | `85 6C` | `0x6C85` | `0x112` | `QUEEN_54` | Starry Night | `Voice(High)` | My husband is so happy! |
| `15` | `97 6D` | `0x6D97` | `0xAA` | `QUEEN_55` | Starry Night | `Voice(High)` | Tonight is the Starry Night. Enjoy yourself! |
| `16` | `41 6E` | `0x6E41` | `0x95` | `VOICE_56` | Starry Night | `Voice(High)` | Congratulations! |
| `17` | `D6 6E` | `0x6ED6` | `0x2F` | `VOICE_57` | Starry Night | `Voice(High)` | I knew you'd win! |
| `18` | `05 6F` | `0x6F05` | `0x1A` | `VOICE_58` | Starry Night | `Voice(High)` | You did it! |
| `19` | `1F 6F` | `0x6F1F` | `0x14` | `VOICE_59` | Starry Night | `Voice(High)` | Congrats! |
| `1A` | `33 6F` | `0x6F33` | `0x54` | `VOICE_5A` | Starry Night | `Voice(High)` | You have become a true master! |
| `1B` | `87 6F` | `0x6F87` | `0x114` | `PROF_MONSTER_5B` | Starry Night | `Voice(Low)` | Follow me to the Shrine. |
| `1C` | `9B 70` | `0x709B` | `0x38` | `PROF_MONSTER_5C` | Starry Night | `Voice(Low)` | Let's go! |
| `1D` | `D3 70` | `0x70D3` | `0x3F` | `PROF_MONSTER_5D` | Starry Night | `Voice(Low)` | Let me know when you want to go! |
| `1E` | `12 71` | `0x7112` | `0x89` | `PROF_MONSTER_5E` | Starry Night | `Voice(Low)` | Want to go now? |
| `1F` | `9B 71` | `0x719B` | `0x1E` | `VOICE_5F` | Starry Night | `Voice(Low)` | I'll fish for stars! |


[⬆️ Back to Top](#top)

---

<a id="data-3"></a>
## Dialogue Sector: Text Table `0x05` - Ending
*Breakdown of the 18 dialogue sequences defined by the Data Pointer Table.*

| Index | Pointer (LE) | Start (Local) | Length | String Key | Category | Audio / Flags | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `00` | `B9 71` | `0x71B9` | `0x12` | `VOICE_60` | UNCHECKED | `Voice(Low)` | No running! |
| `01` | `CB 71` | `0x71CB` | `0x16` | `VOICE_61` | UNCHECKED | `Voice(High)` | Squawk! |
| `02` | `E1 71` | `0x71E1` | `0x56` | `VOICE_62` | Ending | None | Jar is filled with stars. |
| `03` | `37 72` | `0x7237` | `0x49` | `VOICE_63` | Ending | `Voice(High)` | Someday I will follow the player... |
| `04` | `80 72` | `0x7280` | `0xAE` | `PULIO_64` | Ending | `Voice(High)` | If you didn't help me, I wouldn't be here for the Starry Night. |
| `05` | `2E 73` | `0x732E` | `0x4F` | `VOICE_65` | Ending | `Voice(High)` | Yo, I heard you won! |
| `06` | `7D 73` | `0x737D` | `0x5F` | `VOICE_66` | Ending | `Voice(Low)` | You did it! The King is happy! | Minister?
| `07` | `DC 73` | `0x73DC` | `0x18` | `VOICE_67` | Ending | `Voice(Low)` | You won! |
| `08` | `F4 73` | `0x73F4` | `0x17` | `VOICE_68` | Ending | `Voice(High)` | You did great! |
| `09` | `0B 74` | `0x740B` | `0x20` | `VOICE_69` | Ending | `Voice(High)` | Do you want a reward? |
| `0A` | `2B 74` | `0x742B` | `0x47` | `VOICE_6A` | Ending | `Voice(High)` | Tickling. | Is this supposed to be a Puff-Puff instead?
| `0B` | `72 74` | `0x7472` | `0xF` | `VOICE_6B` | Ending | `Voice(High)` | Giggle. |
| `0C` | `81 74` | `0x7481` | `0x2E` | `VOICE_6C` | Ending | `Voice(High)` | I danced too much. |
| `0D` | `AF 74` | `0x74AF` | `0x9B` | `VOICE_6D` | Ending | `Voice(Low)` | I madea song for you and your sister. | Mick?
| `0E` | `4A 75` | `0x754A` | `0x86` | `VOICE_6E` | Ending | `Voice(Low)` | It is filled with the stars that fell to the ground. |
| `0F` | `D0 75` | `0x75D0` | `0x207` | `VOICE_6F` | Ending | `Voice(Low)` | Yes, this is the true reason for ~~Christmas~~ The Starry Night. |
| `10` | `D7 77` | `0x77D7` | `0x1C` | `VOICE_70` | Ending | `Voice(Low)` | Get back there. |
| `11` | `F3 77` | `0x77F3` | `0x20A` | `MILAYOU_??` | Ending | `Voice(High)` | It wasn't a dream?! |

[⬆️ Back to Top](#top)

---

[⬅️ Back to Master ROM Map](../DWM_Master_ROM_Map.md)
---
© 2026 Jeahnoh. Licensed under CC BY-NC 4.0. Attribution Required.
See LICENSE.md in the repository root for full non-commercial terms.