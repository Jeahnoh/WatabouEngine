# Watabou Engine (DWM: HD Classic)

**Watabou Engine** is an open-source, clean-room engine recreation for the classic Game Boy Color monster-taming RPG, *Dragon Warrior Monsters* (1998). It serves as Phase 1 of a potential larger **Project Ruida** framework.

Built natively in C# using the **MonoGame** framework, this project aims to faithfully reconstruct the original turn-based combat, breeding mechanics, and exploration logic within a highly performant, modern environment, completely bypassing original hardware limitations.

## 🗺️ Project Roadmap: Mechanics vs. Aesthetics

To manage the massive scope of this reconstruction, the engine intentionally decouples gameplay logic from visual presentation. This allows players to mix and match their preferred mechanical ruleset with their favorite visual theme.

### Gameplay Logic Modes
* **HD Classic (Current Focus):** A bare-bones, 1:1 behavioral reconstruction of the original DWM1 mechanics, adhering strictly to the 1998 balance and breeding rules. It features engine-level upgrades like continuous camera scrolling, widescreen, and dynamic "Fog of War".
* **DX HD (Planned Expansion):** A modernized content expansion that merges the classic GBC titles. This mode backports *DWM2* features into the DWM1 world, specifically introducing the **Water family**, expanded **breeding recipes**, and an updated item roster.
* **HD Modern (Theoretical Branch):** A complete mechanical overhaul that transforms the core gameplay loop. This branch will replace the classic 1998 breeding logic with modern *Dragon Quest Monsters* skill inheritance/synthesis, while introducing brand-new mechanics to the retro world, such as an **Equipment System** and an **Alchemy Pot System(inspired by DQVIII/XI)** for crafting items/equipment.

### Global Visual Theming
Regardless of the chosen gameplay mode, the engine's modular data structure is designed to support toggleable visual resource packages. Planned aesthetic themes include:
* **Authentic GBC:** The extracted 1998 2bpp pixel art.
* **Retro Throwbacks:** Ripped or recreated assets mimicking the 8-bit NES (*Dragon Warrior 1*) or 16-bit SNES eras.
* **Modern HD:** High-resolution pixel art inspired by modern releases (e.g., *Dragon Quest XI S*).
*(Note: All themes rely on the same "Bring Your Own Asset" extraction pipeline to maintain legal compliance).*

## 🏗️ Architecture

The project is split into two distinct pipelines:

* `/extractor` **(Python):** A data pipeline tool designed to read an authentic `DWM.gbc` ROM. It parses hex offsets to extract the monster database, text files, and 2bpp sprite sheets, outputting them into standardized JSON and PNG formats.
* `/engine` **(C# / MonoGame):** The native game client. It ingests the extracted JSON data and loads the graphics dynamically into its rendering pipeline, building the playable world directly from the raw data.

## 🤝 Acknowledgements

* Massive thanks to the developers behind **Link's Awakening DX HD (LADXHD)** and the wider reverse-engineering source-port community. Their work proved what is possible for Game Boy classics and served as the primary inspiration for this engine recreation.
* Special thanks to the historical DWM disassembly community (including the foundational work by Mallos31 and others) for meticulously documenting the hardware logic and ROM maps that make data extraction possible. 

## ⚖️ Legal Disclaimer

This project is a custom-written engine and **does not distribute any copyrighted material**. 
To play or compile this project, the end-user must supply their own legally dumped copy of the original game. All extracted audio, graphics, and text data are placed in a `.gitignore` restricted `local_resources/` folder that is never uploaded or shared. 

*Dragon Warrior Monsters, Dragon Quest, and all related properties are trademarks of Square Enix Co., Ltd. This is an unofficial, non-profit community project.*

