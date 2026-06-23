[⬅️ Back to Master ROM Map](../DWM_Master_ROM_Map.md)
        
# Bank `0x1B`: Dialogue Tables `0x00` - `0x02`
## Overview
**Local Hex Range:** `0x4000` - `0x7FFF`  
**Global Hex Range:** `0x6C000` - `0x6FFFF`  
**Bank Type:** Swappable  
**Category:** Text   
**Summary:** This bank includes the first three Text Data Tables in the game, and three standard Assembly subroutines to call text box functions.

---

<a id="top"></a>
## Master Memory Map (General Overview)
*Breakdown of the specific block sectors within this bank.*

| Offset (Local) | Offset (Global) | Length | Description |
| :------------- | :-------------- | :----- | :---------- |
| `0x4000` | `0x6C000` | `0x126` | [Bank Meta Table](#meta) |
| `0x4126` | `0x6C126` | `0x1E8` | [Text Table](#data-1) `0x00` - Tree Spirit Lore |
| `0x430E` | `0x6C30E` | `0x1829` | [Text Table](#data-2) `0x01` - General Dialogue (Class D / Early Game) |
| `0x5B37` | `0x6DB37` | `0x1A46` | [Text Table](#data-3) `0x02` - General Dialogue (Class A / Library Info) |
| `0x757D` | `0x6F57D` | `0xA83` | `0x00` padding (Safe Free Space) |

---

<a id="meta"></a>
## Bank Meta Table
*Breakdown of the blocks within this bank's Meta Table.*

| Offset (Local) | Offset (Global) | Length | Description |
| :------------- | :-------------- | :----- | :---------- |
| `0x4000` | `0x6C000` | `0x1` | Bank ID Header (`0x1B`) |
| `0x4001` | `0x6C001` | `0x6` | Jump Table (3 Assembly Subroutines) |
| `0x4007` | `0x6C007` | `0x6` | Master Pointer Table (3 Data Tables) |
| `0x400D` | `0x6C00D` | `0xC` | [Data Pointer Table](#data-1) (6 Dialogue Pointers) |
| `0x4019` | `0x6C019` | `0x88` | [Data Pointer Table](#data-2) (68 Dialogue Pointers) |
| `0x40A1` | `0x6C0A1` | `0x70` | [Data Pointer Table](#data-3) (55 Dialogue Pointers) |
| `0x4111` | `0x6C111` | `0x1D` | [Assembly Subroutine 1](#subroutine-1) |
| `0x4118` | `0x6C118` | `0x1D` | [Assembly Subroutine 2](#subroutine-2) |
| `0x411F` | `0x6C11F` | `0x1D` | [Assembly Subroutine 3](#subroutine-3) |

---

### Raw Meta Table Map
*Visual breakdown of the engine's memory routing. Refer to the Master ROM Map for structural notation key.*

```hex
Hex View  00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
 
0006C000  [1B]|11 41 18 41 1F 41|(0D  40 19 40 A1 40){26 41 7B  
0006C010  41 AD 41 DF 41 48 42 82  42}{0E 43 44 43 A2 43 17  
0006C020  44 4A 44 86 44 A7 44 E7  44 55 45 C3 45 16 46 65  
0006C030  46 CF 46 54 47 99 47 2E  48 5B 48 7C 48 62 49 7D  
0006C040  49 99 49 AF 49 27 4A 41  4A D5 4A 78 4B B2 4B 40  
0006C050  4C 88 4C B5 4C 34 4D 95  4D 33 4E 68 4E 77 4E A4  
0006C060  4E B1 4E DE 4E 33 4F 6B  4F D9 4F F4 4F 27 50 91  
0006C070  50 DB 50 92 51 AD 51 6E  52 0D 53 C2 53 33 54 93  
0006C080  54 A7 55 E0 55 0F 56 DF  56 24 57 6C 57 D1 57 3C  
0006C090  58 3F 59 97 59 FB 59 1E  5A 37 5A C0 5A DB 5A F9  
0006C0A0  5A}{37 5B 78 5B ED 5B 2B  5C 44 5C 5F 5C 9A 5C FC  
0006C0B0  5C 1D 5D 4C 5D B6 5D D7  5D F9 5D 32 5E 46 5E AB  
0006C0C0  5E 47 5F 3C 60 DE 60 33  61 EE 61 0E 62 25 62 02  
0006C0D0  63 F1 63 6D 64 E6 64 30  65 20 66 81 66 AA 66 E9  
0006C0E0  66 2C 67 0F 68 9C 68 D2  68 62 69 F5 69 5A 6A C5  
0006C0F0  6A 6C 6B 01 6C 78 6C 91  6C 41 6D F4 6D A6 6E 55  
0006C100  6F 05 70 B2 70 5D 71 0E  72 BC 72 6C 73 1B 74 CC  
0006C110  74}<11 07 40 CD B6 05 C9><11 07 40 CD F6 05 C9><CD
0006C120  11 41 CD 09 06 C9>                               
```

[⬆️ Back to Top](#top)

---

## Subroutines
These three local assembly routines act as standard wrappers. They feed the data pointers from this bank into the game's core execution library in Bank 0 to parse and display the dialogue on the screen.

<a id="subroutine-1"></a>
### Subroutine 1 (`0x4111`) - The Memory State Setter
*This simple wrapper routine passes the Master Pointer Table to the engine's core library in Bank 0 (`0x05B6`). The Bank 0 routine then sets up the active Work RAM (WRAM) variables needed to prepare the engine to parse text.*

```assembly
11 07 40    LD DE, $4007      ; Loads Master Pointer Table to DE
CD B6 05    CALL   $05B6      ; Calls Bank 0 Memory Prep Routine
C9          RET               ; Return
```

[⬆️ Back to Top](#top)

<a id="subroutine-2"></a>
### Subroutine 2 (`0x4118`) - The Text String Copier
*This simple wrapper routine passes the Master Pointer Table to the engine's core library in Bank 0 (`0x05F6`), which triggers a loop that copies the text bytes into Work RAM (WRAM) until it hits the `[End]` (`0xF0`) control code.* 

```assembly
11 07 40    LD DE, $4007      ; Loads Master Pointer Table to DE
CD F6 05    CALL   $05F6      ; Calls Bank 0 String Copy Loop
C9          RET               ; Return
```
[⬆️ Back to Top](#top)

<a id="subroutine-3"></a>
### Subroutine 3 (`0x411F`) - The Execution & Wait Wrapper
*This simple wrapper routine first calls Subroutine 1 to prep the memory, then calls a Bank 0 system function (`0x0609`) which flags the UI to draw the text box and loops until the player presses the 'A' button to clear it.*

```assembly
CD 11 41    CALL $4111        ; Calls Subroutine 1 (Memory Prep)
CD 09 06    CALL $0609        ; Calls Bank 0 Wait/Draw Loop
C9          RET               ; Return
```
[⬆️ Back to Top](#top)

---

<a id="data-1"></a>
## Dialogue Sector: Text Table `0x00` - Tree Spirit Lore
*Breakdown of the 6 dialogue sequences defined by the Data Pointer Table.*

| Index | Pointer (LE) | Start (Local) | Length | String Key | Category | Audio / Flags | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `00` | `26 41` | `0x4126` | `0x55` | `VOICE_00` | UNCHECKED | `Voice(High)` | GreatLog's Spirit is called Warubou. |
| `01` | `7B 41` | `0x417B` | `0x32` | `VOICE_01` | UNCHECKED | `Voice(High)` | Warubou is a weird name. |
| `02` | `AD 41` | `0x41AD` | `0x32` | `VOICE_02` | UNCHECKED | `Voice(High)` | I wonder if that lady is ok? |
| `03` | `DF 41` | `0x41DF` | `0x69` | `VOICE_03` | UNCHECKED | `Voice(High)` | I heard Warubou and Watabou hate each other! |
| `04` | `48 42` | `0x4248` | `0x3A` | `VOICE_04` | UNCHECKED | `Voice(High)` | I'll never forget Warubou's name. |
| `05` | `82 42` | `0x4282` | `0x8C` | `VOICE_05` | UNCHECKED | `Voice(Low)` | About GreatTree's growth. |

[⬆️ Back to Top](#top)

---

<a id="data-2"></a>
## Dialogue Sector: Text Table `0x01` - General Dialogue (Class D / Early Game)
*Breakdown of the 68 dialogue sequences defined by the Data Pointer Table.*

| Index | Pointer (LE) | Start (Local) | Length | String Key | Category | Audio / Flags | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `00` | `0E 43` | `0x430E` | `0x36` | `VOICE_06` | Bazaar | `Voice(Low)` | No beggars! |
| `01` | `44 43` | `0x4344` | `0x5E` | `VOICE_07` | Bazaar | `Voice(Low)` | If he doesn't want to sell, why is he even here? |
| `02` | `A2 43` | `0x43A2` | `0x7A` | `VOICE_08` | UNCHECKED | `Voice(High)` | There's a monster in front of you, you'll trigger a fight. |
| `03` | `17 44` | `0x4417` | `0x33` | `VOICE_09` | UNCHECKED | `Voice(Low)` | Peace and Bravery Gates are open. |
| `04` | `4A 44` | `0x444A` | `0x3C` | `VOICE_0A` | UNCHECKED | `Voice(Low)` | No one's here. I want some entertainment. |
| `05` | `86 44` | `0x4486` | `0x21` | `VOICE_0B` | UNCHECKED | None | K-thump! Something hit you. |
| `06` | `A7 44` | `0x44A7` | `0x40` | `VOICE_0C` | UNCHECKED | `Voice(Low)` | There's an Egg Evaluator somewhere. |
| `07` | `E7 44` | `0x44E7` | `0x6E` | `MONSTER_0D` | UNCHECKED | `Voice(Low)` | BadMeat is only good for Undead Monsters. | I'm fairly certain it's Hork, but need to check.
| `08` | `55 45` | `0x4555` | `0x6E` | `MONSTER_0E` | UNCHECKED | `Voice(Low)` | Monsters disobey when wild, but are more likely listen to a Command that matches their Personality. |
| `09` | `C3 45` | `0x45C3` | `0x53` | `VOICE_0F` | UNCHECKED | `Voice(Low)` | You can jump off some places. |
| `0A` | `16 46` | `0x4616` | `0x4F` | `VOICE_10` | UNCHECKED | `Voice(Low)` | Monster Stables are down there. |
| `0B` | `65 46` | `0x4665` | `0x6A` | `VOICE_11` | UNCHECKED | `Voice(Low)` | I catch a lot of junk. |
| `0C` | `CF 46` | `0x46CF` | `0x85` | `VOICE_12` | UNCHECKED | `Voice(High)` | You're at the Farm, Stables are downstairs. |
| `0D` | `54 47` | `0x4754` | `0x45` | `VOICE_13` | UNCHECKED | `Voice(High)` | There are hidden Traveler's Gates throughout GreatTree. |
| `0E` | `99 47` | `0x4799` | `0x95` | `VOICE_14` | UNCHECKED | `Voice(High)` | MetalCut is good for fighting MetalSlimes. Anteaters can learn it. |
| `0F` | `2E 48` | `0x482E` | `0x2D` | `VOICE_15` | UNCHECKED | `Voice(High)` | I'm sleepy, let's go to bed. |
| `10` | `5B 48` | `0x485B` | `0x21` | `VOICE_16` | UNCHECKED | `Voice(High)` | BigEye learns IceBolt. |
| `11` | `7C 48` | `0x487C` | `0xE6` | `VOICE_17` | UNCHECKED | `Voice(Low)` | Larger + numbers will grow stronger. |
| `12` | `62 49` | `0x4962` | `0x1B` | `WATABOU_18` | UNCHECKED | `Voice(High)` | Watabou eating. |
| `13` | `7D 49` | `0x497D` | `0x1C` | `WATABOU_19` | UNCHECKED | `Voice(High)` | Watabou still eating. |
| `14` | `99 49` | `0x4999` | `0x16` | `WATABOU_1A` | UNCHECKED | `Voice(High)` | Want some? |
| `15` | `AF 49` | `0x49AF` | `0x78` | `WATABOU_1B` | UNCHECKED | None | You eat a monster treat. |
| `16` | `27 4A` | `0x4A27` | `0x1A` | `WATABOU_1C` | UNCHECKED | `Voice(High)` | You gotta win! |
| `17` | `41 4A` | `0x4A41` | `0x94` | `VOICE_1D` | UNCHECKED | `Voice(High)` | Beasts and Dragons are weak to my SleepAir. |
| `18` | `D5 4A` | `0x4AD5` | `0xA3` | `VOICE_1E` | UNCHECKED | `Voice(Low)` | Zzz... We're all asleep here... |
| `19` | `78 4B` | `0x4B78` | `0x3A` | `VOICE_1F` | UNCHECKED | None | There's delicious meat. |
| `1A` | `B2 4B` | `0x4BB2` | `0x8E` | `KING_20` | UNCHECKED | `Voice(Low)` | You beat MadKnight! |
| `1B` | `40 4C` | `0x4C40` | `0x48` | `VOICE_21` | UNCHECKED | That special [e9 60] | Dresser has SleepAir in it. |
| `1C` | `88 4C` | `0x4C88` | `0x2D` | `VOICE_22` | UNCHECKED | `Voice(Low)` | You beat D Class. |
| `1D` | `B5 4C` | `0x4CB5` | `0x7F` | `VOICE_23` | UNCHECKED | `Voice(Low)` | Congrats on D Class. Go see the King. |
| `1E` | `34 4D` | `0x4D34` | `0x61` | `VOICE_24` | UNCHECKED | `Voice(High)` | Mick is in the Queen's room. | Sidenote: why do you have to go to the Arena to get to the Queen's chambers? Let's rework the layout. Make it a shortcut, but have her chambers actually in the castle.
| `1F` | `95 4D` | `0x4D95` | `0x9E` | `VOICE_25` | UNCHECKED | `Voice(Low)` | Wanna breed a monster with my IceMan? |
| `20` | `33 4E` | `0x4E33` | `0x35` | `GWAELIN_00` | UNCHECKED | `Voice(High)` | You came here to save me? | Just need to verify the order
| `21` | `68 4E` | `0x4E68` | `0xF` | `GWAELIN_01` | UNCHECKED | `Voice(High)` | I see... |
| `22` | `77 4E` | `0x4E77` | `0x2D` | `GWAELIN_02` | UNCHECKED | `Voice(High)` |I want to go back to the castle...  |
| `23` | `A4 4E` | `0x4EA4` | `0xD` | `GWAELIN_03` | UNCHECKED | `Voice(High)` | \*sigh\* |
| `24` | `B1 4E` | `0x4EB1` | `0x2D` | `GWAELIN_04` | UNCHECKED | `Voice(High)` | Please carry me back. |
| `25` | `DE 4E` | `0x4EDE` | `0x55` | `GWAELIN_05` | UNCHECKED | `Voice(High)` | I want  to go back to the castle...  |
| `26` | `33 4F` | `0x4F33` | `0x38` | `VOICE_2C` | UNCHECKED | None | Tried to prick up the princess.|
| `27` | `6B 4F` | `0x4F6B` | `0x6E` | `GWAELIN_06` | UNCHECKED | `Voice(High)` | You're still young. |
| `28` | `D9 4F` | `0x4FD9` | `0x1B` | `GWAELIN_07` | UNCHECKED | `Voice(High)` | Please leave. |
| `29` | `F4 4F` | `0x4FF4` | `0x33` | `GWAELIN_08` | UNCHECKED | `Voice(High)` | I'll wait for a stronger hero. |
| `2A` | `27 50` | `0x5027` | `0x6A` | `VOICE_30` | UNCHECKED | `Voice(Low)` | Why don't you breed with my IceMan. My LavaMan is strong. | daheck?
| `2B` | `91 50` | `0x5091` | `0x4A` | `VOICE_31` | UNCHECKED | `Voice(Low)` | Nice meeting you! |
| `2C` | `DB 50` | `0x50DB` | `0xB7` | `VOICE_32` | UNCHECKED | `Voice(Low)` | Monsters can learn 3 skills, but won't learn them if their MP and level are too low. |
| `2D` | `92 51` | `0x5192` | `0x1B` | `VOICE_33` | UNCHECKED | `Voice(Low)` | Eyeder pun. |
| `2E` | `AD 51` | `0x51AD` | `0xC1` | `VOICE_34` | UNCHECKED | `Voice(Low)` | Mick wants his LizardMan to breed with something specific. |
| `2F` | `6E 52` | `0x526E` | `0x9F` | `VOICE_35` | UNCHECKED | `Voice(Low)` | Save before you leave. |
| `30` | `0D 53` | `0x530D` | `0xB5` | `VOICE_36` | UNCHECKED | `Voice(High)` | It's easier to change monsters personalities at lower levels. |
| `31` | `C2 53` | `0x53C2` | `0x71` | `VOICE_37` | UNCHECKED | `Voice(Low)` | The other guy is my rival. His monster knows a thunder skill. | This is a hint for the Well Doctor's Gate.
| `32` | `33 54` | `0x5433` | `0x60` | `VOICE_38` | UNCHECKED | `Voice(Low)` | My BoneSlave is strong against his monsters. |
| `33` | `93 54` | `0x5493` | `0x114` | `VOICE_39` | UNCHECKED | `Voice(Low)` | Recommended items to bring into Gates. |
| `34` | `A7 55` | `0x55A7` | `0x39` | `VOICE_3A` | UNCHECKED | `Voice(Low)` | How long do I need to do this? |
| `35` | `E0 55` | `0x55E0` | `0x2F` | `VOICE_3B` | UNCHECKED | `Voice(Low)` | Wanna know about D class roster? |
| `36` | `0F 56` | `0x560F` | `0xD0` | `VOICE_3C` | UNCHECKED | `Voice(Low)` | Info on Mick's monsters. |
| `37` | `DF 56` | `0x56DF` | `0x45` | `BEBE_MASTER_00` | UNCHECKED | `Voice(Low)` | Bebe, these are Hashis. |
| `38` | `24 57` | `0x5724` | `0x48` | `VOICE_3E` | UNCHECKED | `Voice(Low)` | Why can't you say chopsticks? |
| `39` | `6C 57` | `0x576C` | `0x65` | `VOICE_3F` | UNCHECKED | `Voice(Low)` | I wonder how the Master Monster Tamer does it? |
| `3A` | `D1 57` | `0x57D1` | `0x6B` | `VOICE_40` | UNCHECKED | `Voice(High)` | That guy paces. |
| `3B` | `3C 58` | `0x583C` | `0x103` | `VOICE_41` | UNCHECKED | `Voice(Low)` | Can you bring a Thunder skill Monster? |
| `3C` | `3F 59` | `0x593F` | `0x58` | `VOICE_42` | UNCHECKED | `Voice(Low)` | If you find one, bring it to me. |
| `3D` | `97 59` | `0x5997` | `0x64` | `VOICE_43` | UNCHECKED | `Voice(Low)` | You don't have one? |
| `3E` | `FB 59` | `0x59FB` | `0x23` | `VOICE_44` | UNCHECKED | `Voice(Low)` | Oh you brought one! |
| `3F` | `1E 5A` | `0x5A1E` | `0x19` | `VOICE_45` | UNCHECKED | `Voice(Low)` | Can I have your Monster? |
| `40` | `37 5A` | `0x5A37` | `0x89` | `VOICE_47` | UNCHECKED | `Voice(Low)` | Now to do the experiment. |
| `41` | `C0 5A` | `0x5AC0` | `0x1B` | `VOICE_48` | UNCHECKED | `Voice(Low)` | Oh well... |
| `42` | `DB 5A` | `0x5ADB` | `0x1E` | `VOICE_49` | UNCHECKED | `Voice(Low)` | Now can I have your monster? |
| `43` | `F9 5A` | `0x5AF9` | `0x3E` | `VOICE_4A` | UNCHECKED | `Voice(Low)` | Did you bring a monster with Thunder? |

[⬆️ Back to Top](#top)

---

<a id="data-3"></a>
## Dialogue Sector - Table `0x02` General Dialogue (Class A / Library Info)
*Breakdown of the 55 dialogue sequences defined by the Dialogue Pointer Table.*

| Index | Pointer (LE) | Start (Local) | Length | String Key | Category | Audio / Flags | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `00` | `37 5B` | `0x5B37` | `0x41` | `VOICE_4B` | UNCHECKED | `Voice(Low)` | Sometimes I want to go behind the Gate of Labyrinth. |
| `01` | `78 5B` | `0x5B78` | `0x75` | `VOICE_4C` | UNCHECKED | `Voice(High)` | The Dragon talks in his sleep. |
| `02` | `ED 5B` | `0x5BED` | `0x3E` | `VOICE_4D` | UNCHECKED | `Voice(High)` | There's lots of me at Judgement. |
| `03` | `2B 5C` | `0x5C2B` | `0x19` | `WARUBOU_00` | UNCHECKED | `Voice(Low)` | Warubou eating. |
| `04` | `44 5C` | `0x5C44` | `0x1B` | `WARUBOU_01` | UNCHECKED | `Voice(Low)` | Warubou still eating. |
| `05` | `5F 5C` | `0x5C5F` | `0x3B` | `WARUBOU_02` | UNCHECKED | `Voice(Low)` | Do you want to eat this? |
| `06` | `9A 5C` | `0x5C9A` | `0x62` | `VOICE_51` | UNCHECKED | None | You get BadMeat. | Has some weird characters. Possibly unused?
| `07` | `FC 5C` | `0x5CFC` | `0x21` | `WARUBOU_03` | UNCHECKED | `Voice(Low)` | Serves you right! |
| `08` | `1D 5D` | `0x5D1D` | `0x2F` | `WARUBOU_04` | UNCHECKED | `Voice(Low)` | What you don't want this? |
| `09` | `4C 5D` | `0x5D4C` | `0x6A` | `VOICE_54` | UNCHECKED | None | You get BadMeat. |
| `0A` | `B6 5D` | `0x5DB6` | `0x21` | `WARUBOU_05` | UNCHECKED | `Voice(Low)` | Serves you right! |
| `0B` | `D7 5D` | `0x5DD7` | `0x22` | `VOICE_56` | UNCHECKED | `Voice(High)` | WhipBird can use Call. |
| `0C` | `F9 5D` | `0x5DF9` | `0x39` | `VOICE_57` | UNCHECKED | None | Nasty looking treat. | `EE` in here too...
| `0D` | `32 5E` | `0x5E32` | `0x14` | `VOICE_58` | UNCHECKED | None | Got a WarpWing. |
| `0E` | `46 5E` | `0x5E46` | `0x65` | `VOICE_59` | UNCHECKED | None | Found a WarpWing. But inventory full.|
| `0F` | `AB 5E` | `0x5EAB` | `0x9C` | `VOICE_5A` | UNCHECKED | `Voice(Low)` | You beat A Class. Labyrinth and Judgement Gates are open now. |
| `10` | `47 5F` | `0x5F47` | `0xF2` | `VOICE_5B` | UNCHECKED | `Voice(Low)` | A Class, skip 2 classes message. |
| `11` | `3C 60` | `0x603C` | `0xA2` | `VOICE_5C` | UNCHECKED | `Voice(Low)` | A Class, 4 gates opened. |
| `12` | `DE 60` | `0x60DE` | `0x55` | `VOICE_5D` | UNCHECKED | `Voice(High)` | Last match A class info. |
| `13` | `33 61` | `0x6133` | `0xBB` | `VOICE_5E` | UNCHECKED | `Voice(Low)` | Sometimes Same monsters bred make a new monster. |
| `14` | `EE 61` | `0x61EE` | `0x20` | `VOICE_5F` | UNCHECKED | `Voice(Low)` | Vivify. |
| `15` | `0E 62` | `0x620E` | `0x17` | `VOICE_60` | UNCHECKED | `Voice(Low)` | MadRaven pun. |
| `16` | `25 62` | `0x6225` | `0xDD` | `VOICE_61` | UNCHECKED | `Voice(Low)` | Books exist for personality changing hint. |
| `17` | `02 63` | `0x6302` | `0xEF` | `VOICE_62` | UNCHECKED | `Voice(High)` | Skills that certain monsters learn. |
| `18` | `F1 63` | `0x63F1` | `0x7C` | `VOICE_63` | UNCHECKED | `Voice(Low)` | My rival wants a monster with MultiCut. | Must be a hint for what to breed with his mon.
| `19` | `6D 64` | `0x646D` | `0x79` | `VOICE_64` | UNCHECKED | `Voice()` | A SkyDragon knows how to beat my rival's monster. |
| `1A` | `E6 64` | `0x64E6` | `0x4A` | `VOICE_65` | UNCHECKED | `Voice(Low)` | Wanna know about A Class? |
| `1B` | `30 65` | `0x6530` | `0xF0` | `VOICE_66` | UNCHECKED | `Voice(Low)` | Info on A Class champ. |
| `1C` | `20 66` | `0x6620` | `0x61` | `VOICE_67` | UNCHECKED | `Voice(High)` | Wow, a KingSlime! | Queen request?
| `1D` | `81 66` | `0x6681` | `0x29` | `VOICE_68` | UNCHECKED | `Voice(High)` | Use this INTseed wisely. | Badumtss.
| `1E` | `AA 66` | `0x66AA` | `0x3F` | `BEBE_MASTER_01` | UNCHECKED | `Voice(Low)` | Bebe, these are Medama-yaki. |
| `1F` | `E9 66` | `0x66E9` | `0x43` | `VOICE_6A` | UNCHECKED | `Voice(Low)` | Just say fried egg! |
| `20` | `2C 67` | `0x672C` | `0xE3` | `VOICE_6B` | UNCHECKED | `Voice(Low)` | Breeding info on + numbers. |
| `21` | `0F 68` | `0x680F` | `0x8D` | `VOICE_6C` | UNCHECKED | `Voice(High)` | Splash splash! Breeding gives different results. |
| `22` | `9C 68` | `0x689C` | `0x36` | `VOICE_6D` | UNCHECKED | `Voice(High)` | Breeding monsters is fun. |
| `23` | `D2 68` | `0x68D2` | `0x90` | `VOICE_6E` | UNCHECKED | `Voice(Low)` | DrakSlime vs DragonKid breeding. |
| `24` | `62 69` | `0x6962` | `0x93` | `VOICE_6F` | UNCHECKED | `Voice(Low)` | Are you using the Library? |
| `25` | `F5 69` | `0x69F5` | `0x65` | `VOICE_70` | UNCHECKED | `Voice(High)` | This guy stinks! |
| `26` | `5A 6A` | `0x6A5A` | `0x6B` | `KING_00` | UNCHECKED | `Voice(Low)` | You beat Gigantes! | 
| `27` | `C5 6A` | `0x6AC5` | `0xA7` | `VOICE_72` | UNCHECKED | None | 'Journal of My Baby' Part 2. |
| `28` | `6C 6B` | `0x6B6C` | `0x95` | `VOICE_73` | UNCHECKED | None | 'Journal of My Baby' Part 3. |
| `29` | `01 6C` | `0x6C01` | `0x77` | `VOICE_74` | UNCHECKED | `Voice(High)` | You've collected 100+ monsters. |
| `2A` | `78 6C` | `0x6C78` | `0x19` | `VOICE_75` | UNCHECKED | `Voice(High)` | This room is yours. |
| `2B` | `91 6C` | `0x6C91` | `0xB0` | `VOICE_76` | UNCHECKED | None | Book hint on MadDragon breeding. |
| `2C` | `41 6D` | `0x6D41` | `0xB3` | `VOICE_77` | UNCHECKED | None | Book hint on Spikerous breeding. |
| `2D` | `F4 6D` | `0x6DF4` | `0xB2` | `VOICE_78` | UNCHECKED | None | Book hint on IronTurt breeding. |
| `2E` | `A6 6E` | `0x6EA6` | `0xAF` | `VOICE_79` | UNCHECKED | None | Book hint on SuperTen breeding. |
| `2F` | `55 6F` | `0x6F55` | `0xB0` | `VOICE_7A` | UNCHECKED | None | Book hint on BullBird breeding. |
| `30` | `05 70` | `0x7005` | `0xAD` | `VOICE_7B` | UNCHECKED | None | Book hint on MadGoose breeding. |
| `31` | `B2 70` | `0x70B2` | `0xAB` | `VOICE_7C` | UNCHECKED | None | Book hint on TreeBoy breeding. |
| `32` | `5D 71` | `0x715D` | `0xB1` | `VOICE_7D` | UNCHECKED | None | Book hint on Oniono breeding. |
| `33` | `0E 72` | `0x720E` | `0xAE` | `VOICE_7E` | UNCHECKED | None | Book hint on GiantMoth breeding. |
| `34` | `BC 72` | `0x72BC` | `0xB0` | `VOICE_7F` | UNCHECKED | None | Book hint on ArmyCrab breeding. |
| `35` | `6C 73` | `0x736C` | `0xAF` | `VOICE_80` | UNCHECKED | None | Book hint on Ogre breeding. |
| `36` | `1B 74` | `0x741B` | `0xB1` | `VOICE_81` | UNCHECKED | None | Book hint on GoatHorn breeding. |
| `37` | `CC 74` | `0x74CC` | `0xB1` | `VOICE_82` | UNCHECKED | None | Book hint on Mudron breeding. |


[⬆️ Back to Top](#top)

---

[⬅️ Back to Master ROM Map](../DWM_Master_ROM_Map.md)
---
© 2026 Jeahnoh. Licensed under CC BY-NC 4.0. Attribution Required.
See LICENSE.md in the repository root for full non-commercial terms.