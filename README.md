# Watabou Engine (DWM: HD Classic)

**Watabou Engine** is an open-source, clean-room engine recreation for the classic Game Boy Color monster-taming RPG, *Dragon Warrior Monsters* (1998). It serves as Phase 1 of a potential larger **Project Ruida** framework.

**Project Scope Disclaimer:** The roadmap, features, and design philosophies outlined below represent the initial planned scope of this passion project. All plans are entirely subject to change, and no statements made here carry legal weight or guarantees of delivery.

At its bare bones, the primary goal is to rebuild the original game as a 1:1 PC port experience. Beyond that, the intention is to offer modern enhancements (inspired by LADXHD) and eventually a highly customizable "HD Modern" mode, pulling inspiration from modern franchise entries and niche mechanics across the *Dragon Quest* series.

**Developed and Maintained by:** [Jeahnoh](https://github.com/cdunlap-gravic)

## 🗺️ Project Roadmap: Mechanics vs. Aesthetics

To manage the massive scope of this reconstruction, the engine intentionally decouples gameplay logic from visual presentation. This allows players to mix and match their preferred mechanical ruleset with their favorite visual theme.

### Gameplay Logic Modes

* **Strict Vanilla:** A pure 1:1 replication of the original game. This disables all modern engine enhancements (like widescreen or smooth camera scrolling) to provide an experience functionally identical to playing the 1998 Game Boy Color release.
* **HD Classic (Current Focus):** A bare-bones behavioral reconstruction of the original DWM1 mechanics, adhering strictly to the 1998 balance and breeding rules, but allowing for engine-level visual upgrades like continuous camera scrolling, widescreen, and dynamic "Fog of War".
* **DX HD (Planned Expansion):** A modernized content expansion that merges the classic GBC titles. This mode backports *DWM2* features into the DWM1 world, specifically introducing the **Water family**, expanded **breeding recipes**, and an updated item roster.
* **HD Modern (Theoretical Branch):** A complete mechanical overhaul that transforms the core gameplay loop with deep customization options to tailor the experience. This branch plans to replace classic breeding with modern skill inheritance/synthesis, while introducing brand-new mechanics like an **Equipment System** and an **Alchemy Pot System** for crafting.

### Global Visual Theming

Regardless of the chosen gameplay mode, the engine's modular data structure is designed to support toggleable visual resource packages. Planned aesthetic themes include:

* **Authentic GBC:** The extracted 1998 2bpp pixel art.
* **Retro Throwbacks:** Ripped or recreated assets mimicking the 8-bit NES or 16-bit SNES eras.
* **Modern HD:** High-resolution pixel art inspired by modern releases.
*(Note: All themes rely on the same "Bring Your Own Asset" extraction pipeline to maintain legal compliance).*

## 🏗️ Architecture

The project is split into distinct pipelines *(Note: While C# and MonoGame are the current leading choices for the engine client, the final tech stack is still being evaluated)*:

* `/extractor` **(Python):** A data pipeline tool supported by a custom logging framework (forked from the N.I.C.E. engine) designed to read authentic ROMs. It parses hex offsets to extract the monster database, text files, and decompressing 2bpp sprite sheets, structuring them into a highly relational **SQLite Master Database**.
* `/docs` **(Markdown):** Comprehensive, handcrafted documentation detailing the reverse-engineered hex logic, data structures, and memory offsets used to build the extraction pipeline.
* `/save_manager` **(Utility):** A planned two-way save importer/exporter. This will allow players to import their original 1998 `.sav` files, and more importantly, **sanitize and export** modern engine progress back into a strict, vanilla-compliant `.sav` format so it can be flashed back onto authentic Game Boy hardware.
* `/engine` **(C# / MonoGame - Tentative):** The native game client. It ingests the SQLite database and loads the graphics dynamically into its rendering pipeline, building the playable world directly from the raw data.

## 🤝 Acknowledgements

* Massive thanks to the developers behind **Link's Awakening DX HD (LADXHD)** and the wider reverse-engineering source-port community. Their work proved what is possible for Game Boy classics and served as the primary inspiration for this engine recreation.
* Special thanks to the historical DWM disassembly community (including the foundational work by Mallos31 and others), alongside the incredible folks at **Dragon's Den** and the **Dragon Quest Translations** communities, for their years of dedication to documenting the hardware logic and preserving the deeper mechanics of the franchise. *(Note: This section will be updated as individual contributors and reverse-engineers verify how they wish to be credited).*

## ⚖️ License & Legal (By a Fan, For Fans)

This project is a clean-room reimplementation and operates under a strict non-commercial ethos. No one is permitted to profit from the distribution of this code or its documentation.

* **Engine & Source Code:** Licensed under the [PolyForm Noncommercial License 1.0.0](https://polyformproject.org/licenses/noncommercial/1.0.0). Modders are welcome (and may accept voluntary tips), but the engine and any forks cannot be sold or paywalled.
* **Documentation & Hex Maps:** Licensed under **CC BY-NC 4.0**. You must provide attribution. Commercial wikis (e.g., those utilizing GFDL) are legally prohibited from copying this formatting or research expression directly.
* **Media Exemption:** Content creators are explicitly encouraged to stream, review, and monetize gameplay videos of this engine without restriction.
* **Game Assets:** This project is an **empty engine**. It does not distribute original ROMs, modern game directories, extracted sprites, sound files, or any commercial game data. Users must legally source their own game files to utilize this engine.

**See the full `LICENSE.md` in the repository root for complete legal terms.**

## 🤖 AI Transparency & Studio Stance

I view AI as a standard utility in the modern development stack. I use Gemini as a workflow accelerator—primarily for rubber-duck debugging, quickly referencing syntax, and bouncing ideas around during planning.

However, it is just a tool. **Programmers are still 100% responsible for everything within their commits**, and we must continue to program responsibly. Every architectural decision, line of code, and data structure deployed in this project is strictly human-authored and meticulously hand-crafted by me.

**On Generative Media:** I strongly disavow the use of AI to replace the creative process. Using generative AI for final art, music, or media is lazy and actively takes jobs and opportunities away from human creators. While it may serve a minor purpose for private, early-stage conceptual visualizations before real development begins (e.g., taking five minutes to test a visual direction before committing to a style), it should never be used in any final product when a real person could have benefited from doing the work.

Art is art, and LLMs are not (yet) free-thinking or creative entities. AI is a fantastic programming utility, but at the end of the day, it remains exactly that: just a tool. 

Please, by all means, give work to human creatives. Do your research, and double check your work. Make your knowledge your own. LLMs can speed up the process but they are not infalible.