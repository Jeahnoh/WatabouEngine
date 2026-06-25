#pragma endian little

// Game Boy Bank Structure (16KB)
struct RomBank {
    u8 data[0x4000]; 
};

struct BankHeader {
    u8 bankID;
}

struct JumpTable<u32 count> {
    u16 asmPointers[count];
};

struct MetaTable(u32 count) {
    u16 tablePointers[count];
};

struct PointerTable(u32 count) {
    u16 dataPointers[count];
};

// =========================================================================
// GLOBAL ROM BANKS
// =========================================================================
// Master Layout Container
struct RomMap {
    RomBank Bank_00 @ 0x000000;
    RomBank Bank_01 @ 0x004000;
    RomBank Bank_02 @ 0x008000;
    RomBank Bank_03 @ 0x00C000;
    RomBank Bank_04 @ 0x010000;
    RomBank Bank_05 @ 0x014000;
    RomBank Bank_06 @ 0x018000;
    RomBank Bank_07 @ 0x01C000;
    RomBank Bank_08 @ 0x020000;
    RomBank Bank_09 @ 0x024000;
    RomBank Bank_0A @ 0x028000;
    RomBank Bank_0B @ 0x02C000;
    RomBank Bank_0C @ 0x030000;
    RomBank Bank_0D @ 0x034000;
    RomBank Bank_0E @ 0x038000;
    RomBank Bank_0F @ 0x03C000;
    RomBank Bank_10 @ 0x040000;
    RomBank Bank_11 @ 0x044000;
    RomBank Bank_12 @ 0x048000;
    RomBank Bank_13 @ 0x04C000;
    RomBank Bank_14 @ 0x050000;
    RomBank Bank_15 @ 0x054000;
    RomBank Bank_16 @ 0x058000;
    RomBank Bank_17 @ 0x05C000;
    RomBank Bank_18 @ 0x060000;
    RomBank Bank_19 @ 0x064000;
    RomBank Bank_1A @ 0x068000;
    RomBank Bank_1B @ 0x06C000;
    RomBank Bank_1C @ 0x070000;
    RomBank Bank_1D @ 0x074000;
    RomBank Bank_1E @ 0x078000;
    RomBank Bank_1F @ 0x07C000;
    RomBank Bank_20 @ 0x080000;
    RomBank Bank_21 @ 0x084000;
    RomBank Bank_22 @ 0x088000;
    RomBank Bank_23 @ 0x08C000;
    RomBank Bank_24 @ 0x090000;
    RomBank Bank_25 @ 0x094000;
    RomBank Bank_26 @ 0x098000;
    RomBank Bank_27 @ 0x09C000;
    RomBank Bank_28 @ 0x0A0000;
    RomBank Bank_29 @ 0x0A4000;
    RomBank Bank_2A @ 0x0A8000;
    RomBank Bank_2B @ 0x0AC000;
    RomBank Bank_2C @ 0x0B0000;
    RomBank Bank_2D @ 0x0B4000;
    RomBank Bank_2E @ 0x0B8000;
    RomBank Bank_2F @ 0x0BC000;
    RomBank Bank_30 @ 0x0C0000;
    RomBank Bank_31 @ 0x0C4000;
    RomBank Bank_32 @ 0x0C8000;
    RomBank Bank_33 @ 0x0CC000;
    RomBank Bank_34 @ 0x0D0000;
    RomBank Bank_35 @ 0x0D4000;
    RomBank Bank_36 @ 0x0D8000;
    RomBank Bank_37 @ 0x0DC000;
    RomBank Bank_38 @ 0x0E0000;
    RomBank Bank_39 @ 0x0E4000;
    RomBank Bank_3A @ 0x0E8000;
    RomBank Bank_3B @ 0x0EC000;
    RomBank Bank_3C @ 0x0F0000;
    RomBank Bank_3D @ 0x0F4000;
    RomBank Bank_3E @ 0x0F8000;
    RomBank Bank_3F @ 0x0FC000;
    RomBank Bank_40 @ 0x100000;
    RomBank Bank_41 @ 0x104000;
    RomBank Bank_42 @ 0x108000;
    RomBank Bank_43 @ 0x10C000;
    RomBank Bank_44 @ 0x110000;
    RomBank Bank_45 @ 0x114000;
    RomBank Bank_46 @ 0x118000;
    RomBank Bank_47 @ 0x11C000;
    RomBank Bank_48 @ 0x120000;
    RomBank Bank_49 @ 0x124000;
    RomBank Bank_4A @ 0x128000;
    RomBank Bank_4B @ 0x12C000;
    RomBank Bank_4C @ 0x130000;
    RomBank Bank_4D @ 0x134000;
    RomBank Bank_4E @ 0x138000;
    RomBank Bank_4F @ 0x13C000;
    RomBank Bank_50 @ 0x140000;
    RomBank Bank_51 @ 0x144000;
    RomBank Bank_52 @ 0x148000;
    RomBank Bank_53 @ 0x14C000;
    RomBank Bank_54 @ 0x150000;
    RomBank Bank_55 @ 0x154000;
    RomBank Bank_56 @ 0x158000;
    RomBank Bank_57 @ 0x15C000;
    RomBank Bank_58 @ 0x160000;
    RomBank Bank_59 @ 0x164000;
    RomBank Bank_5A @ 0x168000;
    RomBank Bank_5B @ 0x16C000;
    RomBank Bank_5C @ 0x170000;
    RomBank Bank_5D @ 0x174000;
    RomBank Bank_5E @ 0x178000;
    RomBank Bank_5F @ 0x17C000;
    RomBank Bank_60 @ 0x180000;
    RomBank Bank_61 @ 0x184000;
    RomBank Bank_62 @ 0x188000;
    RomBank Bank_63 @ 0x18C000;
    RomBank Bank_64 @ 0x190000;
    RomBank Bank_65 @ 0x194000;
    RomBank Bank_66 @ 0x198000;
    RomBank Bank_67 @ 0x19C000;
    RomBank Bank_68 @ 0x1A0000;
    RomBank Bank_69 @ 0x1A4000;
    RomBank Bank_6A @ 0x1A8000;
    RomBank Bank_6B @ 0x1AC000;
    RomBank Bank_6C @ 0x1B0000;
    RomBank Bank_6D @ 0x1B4000;
    RomBank Bank_6E @ 0x1B8000;
    RomBank Bank_6F @ 0x1BC000;
    RomBank Bank_70 @ 0x1C0000;
    RomBank Bank_71 @ 0x1C4000;
    RomBank Bank_72 @ 0x1C8000;
    RomBank Bank_73 @ 0x1CC000;
    RomBank Bank_74 @ 0x1D0000;
    RomBank Bank_75 @ 0x1D4000;
    RomBank Bank_76 @ 0x1D8000;
    RomBank Bank_77 @ 0x1DC000;
    RomBank Bank_78 @ 0x1E0000;
    RomBank Bank_79 @ 0x1E4000;
    RomBank Bank_7A @ 0x1E8000;
    RomBank Bank_7B @ 0x1EC000;
    RomBank Bank_7C @ 0x1F0000;
    RomBank Bank_7D @ 0x1F4000;
    RomBank Bank_7E @ 0x1F8000;
    RomBank Bank_7F @ 0x1FC000;
};

RomMap Master_ROM_Map @ 0x000000;
// =========================================================================
// BANK 2F - 
// =========================================================================