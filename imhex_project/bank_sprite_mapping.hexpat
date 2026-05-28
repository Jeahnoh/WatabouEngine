#pragma endian little

// Game Boy Bank Structure (16KB)
struct RomBank {
    u8 data[0x4000]; 
};

struct DataBitstream<auto Size> {
    u8 pixels[Size] [[color("00FF00")]];
};

// Meta data of some kind. Struct used to mark compression flag sections
struct MetaBitstream<auto Size> {
    u8 flags[Size] [[color("FF0000")]];
};

struct UnknownBitstream<auto Size> {
    u8 stuffs[Size] [[color("FFFF00")]];
};

struct TextBitstream<auto Size> {
    u8 textBlock[Size] [[color("AAFF44")]];
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
// BANK 2F - Sprite Bank (I just chose this one at random to work on)
// =========================================================================

MetaBitstream<4>  terry_S1_meta @ 0x0BC070; //Unknown starting point
DataBitstream<16> terry_S1_ul   @ 0x0BC074;
DataBitstream<16> terry_S1_bl   @ 0x0BC084;
DataBitstream<16> terry_S1_br   @ 0x0BC094;

MetaBitstream<3>  terry_S2_meta  @ 0x0BC0A4; //0x01fef2
DataBitstream<10> terry_S2_ul    @ 0x0BC0A7; 
MetaBitstream<3>  terry_S2_meta2 @ 0x0BC0B1; //0x010e00
DataBitstream<12> terry_S2_bl    @ 0x0BC0B4; 
DataBitstream<16> terry_S2_br    @ 0x0BC0C0;

DataBitstream<16> terry_e1_ul @0x000bc0d0;
DataBitstream<16> terry_e1_ur @0x000BC0e0;
DataBitstream<16> terry_e1_bl @0x000bc0f0;
DataBitstream<4>  terry_e1_br_00 @0xBC100;
MetaBitstream<3>  terry_e1_meta  @0xbc104;
DataBitstream<4>  terry_e1_br_01 @0xBC107;
MetaBitstream<3>  terry_e1_meta2 @0xbc10b;

//Why not upper left? yes we have a match of terry_e1_ul, 
//but is terry_e1_meta2 covering terry_e1 and/or terry_e2?
DataBitstream<16> terry_e2_ur @0x000bc10e;
DataBitstream<8>  terry_e2_BL @0xBC123;
DataBitstream<8>  terry_e2_BR @0xbc130;

DataBitstream<16> terry_n1_ul @0xbc138;
DataBitstream<16> terry_n1_bl @0xbc148;
DataBitstream<8>  terry_n1_br @0xbc158;

//DataBitstream<8>  terry_n1_BR2 @0xbc15a;

DataBitstream<6>  terry_n2_ul @0xbc166;

DataBitstream<6>  terry_n2_bl @0xbc16f;
//3
//why the flip? is this a coincidence in metadata looking just like another line?
DataBitstream<2>  terry_n2_ur @0xbc178;

DataBitstream<8>  terry_n2_br @0xbc17d;


DataBitstream<16> drakslime_S1_UL @0xbc18e;
DataBitstream<16> drakslime_S1_BL @0xbc19e;
DataBitstream<16> drakslime_S1_BR @0xbc1ae;


//========================================================================
// BANK 4F - charmap images, no compression
//========================================================================
//
// TODO: clean up punctuation names
// TODO: strip images for font-set creation for WatabouEngine
//
//---------------------------
// Notes:
//---------------------------
// unknown section of 7 bytes, possibly instructions or a marker for the
// uncompressed charmap images.
//========================================================================

UnknownBitstream<16> unknown_section_bank_AF_00 @0x13c000;
DataBitstream<16> charmap_00_0 @0x13c010;
DataBitstream<16> charmap_01_1 @0x13c020;
DataBitstream<16> charmap_02_2 @0x13c030;
DataBitstream<16> charmap_03_3 @0x13c040;
DataBitstream<16> charmap_04_4 @0x13c050;
DataBitstream<16> charmap_05_5 @0x13c060;
DataBitstream<16> charmap_06_6 @0x13c070;
DataBitstream<16> charmap_07_7 @0x13c080;
DataBitstream<16> charmap_08_8 @0x13c090;
DataBitstream<16> charmap_09_9 @0x13c0a0;
DataBitstream<16> charmap_0A_0 @0x13c0b0;
DataBitstream<16> charmap_0B_1 @0x13c0c0;
DataBitstream<16> charmap_0C_2 @0x13c0d0;
DataBitstream<16> charmap_0D_3 @0x13c0e0;
DataBitstream<16> charmap_0E_blank @0x13c0f0;
DataBitstream<16> charmap_0F_blank @0x13c100;
DataBitstream<16> charmap_10_family_slime @0x13c110;
DataBitstream<16> charmap_11_family_dragon @0x13c120;
DataBitstream<16> charmap_12_family_beast @0x13c130;
DataBitstream<16> charmap_13_family_bird @0x13c140;
DataBitstream<16> charmap_14_family_plant @0x13c150;
DataBitstream<16> charmap_15_family_bug @0x13c160;
DataBitstream<16> charmap_16_family_demon @0x13c170;
DataBitstream<16> charmap_17_family_undead @0x13c180;
DataBitstream<16> charmap_18_family_material @0x13c190;
DataBitstream<16> charmap_19_family_boss @0x13c1a0;
DataBitstream<16> charmap_1A_blank @0x13c1b0;
DataBitstream<16> charmap_1B_blank @0x13c1c0;
DataBitstream<16> charmap_1C_blank @0x13c1d0;
DataBitstream<16> charmap_1D_blank @0x13c1e0;
DataBitstream<16> charmap_1E_blank @0x13c1f0;
DataBitstream<16> charmap_1F_blank @0x13c200;
DataBitstream<16> charmap_20_blank @0x13c210;
DataBitstream<16> charmap_21_blank @0x13c220;
DataBitstream<16> charmap_22_blank @0x13c230;
DataBitstream<16> charmap_23_blank @0x13c240;
DataBitstream<16> charmap_24_A @0x13c250;
DataBitstream<16> charmap_25_B @0x13c260;
DataBitstream<16> charmap_26_C @0x13c270;
DataBitstream<16> charmap_27_D @0x13c280;
DataBitstream<16> charmap_28_E @0x13c290;
DataBitstream<16> charmap_29_F @0x13c2a0;
DataBitstream<16> charmap_2A_G @0x13c2b0;
DataBitstream<16> charmap_2B_H @0x13c2c0;
DataBitstream<16> charmap_2C_I @0x13c2d0;
DataBitstream<16> charmap_2D_J @0x13c2e0;
DataBitstream<16> charmap_2E_K @0x13c2f0;
DataBitstream<16> charmap_2F_L @0x13c300;
DataBitstream<16> charmap_30_M @0x13c310;
DataBitstream<16> charmap_31_N @0x13c320;
DataBitstream<16> charmap_32_O @0x13c330;
DataBitstream<16> charmap_33_P @0x13c340;
DataBitstream<16> charmap_34_Q @0x13c350;
DataBitstream<16> charmap_35_R @0x13c360;
DataBitstream<16> charmap_36_S @0x13c370;
DataBitstream<16> charmap_37_T @0x13c380;
DataBitstream<16> charmap_38_U @0x13c390;
DataBitstream<16> charmap_39_V @0x13c3a0;
DataBitstream<16> charmap_3A_W @0x13c3b0;
DataBitstream<16> charmap_3B_X @0x13c3c0;
DataBitstream<16> charmap_3C_Y @0x13c3d0;
DataBitstream<16> charmap_3D_Z @0x13c3e0;
DataBitstream<16> charmap_3E_a @0x13c3f0;
DataBitstream<16> charmap_3F_b @0x13c400;
DataBitstream<16> charmap_40_c @0x13c410;
DataBitstream<16> charmap_41_d @0x13c420;
DataBitstream<16> charmap_42_e @0x13c430;
DataBitstream<16> charmap_43_f @0x13c440;
DataBitstream<16> charmap_44_g @0x13c450;
DataBitstream<16> charmap_45_h @0x13c460;
DataBitstream<16> charmap_46_i @0x13c470;
DataBitstream<16> charmap_47_j @0x13c480;
DataBitstream<16> charmap_48_k @0x13c490;
DataBitstream<16> charmap_49_l @0x13c4a0;
DataBitstream<16> charmap_4A_m @0x13c4b0;
DataBitstream<16> charmap_4B_n @0x13c4c0;
DataBitstream<16> charmap_4C_o @0x13c4d0;
DataBitstream<16> charmap_4D_p @0x13c4e0;
DataBitstream<16> charmap_4E_q @0x13c4f0;
DataBitstream<16> charmap_4F_r @0x13c500;
DataBitstream<16> charmap_50_s @0x13c510;
DataBitstream<16> charmap_51_t @0x13c520;
DataBitstream<16> charmap_52_u @0x13c530;
DataBitstream<16> charmap_53_v @0x13c540;
DataBitstream<16> charmap_54_w @0x13c550;
DataBitstream<16> charmap_55_x @0x13c560;
DataBitstream<16> charmap_56_y @0x13c570;
DataBitstream<16> charmap_57_z @0x13c580;
DataBitstream<16> charmap_58_blank @0x13c590;
DataBitstream<16> charmap_59_blank @0x13c5a0;
DataBitstream<16> charmap_5A_blank @0x13c5b0;
DataBitstream<16> charmap_5B_blank @0x13c5c0;
DataBitstream<16> charmap_5C_apostrophe @0x13c5d0;
DataBitstream<16> charmap_5D_forward @0x13c5e0;
DataBitstream<16> charmap_5E_comma @0x13c5f0;
DataBitstream<16> charmap_5F_period @0x13c600;
DataBitstream<16> charmap_60_semicolon @0x13c610;
DataBitstream<16> charmap_61_double_dot @0x13c620;
DataBitstream<16> charmap_62_blank @0x13c630;
DataBitstream<16> charmap_63_exclamation @0x13c640;
DataBitstream<16> charmap_64_question @0x13c650;
DataBitstream<16> charmap_65_quote @0x13c660;
DataBitstream<16> charmap_66_apost_l @0x13c670;
DataBitstream<16> charmap_67_apost_t @0x13c680;
DataBitstream<16> charmap_68_apost_s @0x13c690;
DataBitstream<16> charmap_69_apost_r @0x13c6a0;
DataBitstream<16> charmap_6A_apost_m @0x13c6b0;
DataBitstream<16> charmap_6B_apost_y @0x13c6c0;
DataBitstream<16> charmap_6C_apost_v @0x13c6d0;
DataBitstream<16> charmap_6D_apost_d @0x13c6e0;
DataBitstream<16> charmap_6E_apost_e @0x13c6f0;
DataBitstream<16> charmap_6F_apost_c @0x13c700;
DataBitstream<16> charmap_70_apost_n @0x13c710;
DataBitstream<16> charmap_71_apost_T @0x13c720;
DataBitstream<16> charmap_72_blank @0x13c730;
DataBitstream<16> charmap_73_blank @0x13c740;
DataBitstream<16> charmap_74_blank @0x13c750;
DataBitstream<16> charmap_75_blank @0x13c760;
DataBitstream<16> charmap_76_blank @0x13c770;
DataBitstream<16> charmap_77_blank @0x13c780;
DataBitstream<16> charmap_78_blank @0x13c790;
DataBitstream<16> charmap_79_blank @0x13c7a0;
DataBitstream<16> charmap_7A_blank @0x13c7b0;
DataBitstream<16> charmap_7B_blank @0x13c7c0;
DataBitstream<16> charmap_7C_blank @0x13c7d0;
DataBitstream<16> charmap_7D_blank @0x13c7e0;
DataBitstream<16> charmap_7E_blank @0x13c7f0;
DataBitstream<16> charmap_7F_blank @0x13c800;
DataBitstream<16> charmap_80_blank @0x13c810;
DataBitstream<16> charmap_81_blank @0x13c820;
DataBitstream<16> charmap_82_blank @0x13c830;
DataBitstream<16> charmap_83_blank @0x13c840;
DataBitstream<16> charmap_84_blank @0x13c850;
DataBitstream<16> charmap_85_blank @0x13c860;
DataBitstream<16> charmap_86_blank @0x13c870;
DataBitstream<16> charmap_87_apost_t @0x13c880;
DataBitstream<16> charmap_88_blank @0x13c890;
DataBitstream<16> charmap_89_blank @0x13c8a0;
DataBitstream<16> charmap_8A_blank @0x13c8b0;
DataBitstream<16> charmap_8B_blank @0x13c8c0;
DataBitstream<16> charmap_8C_blank @0x13c8d0;
DataBitstream<16> charmap_8D_blank @0x13c8e0;
DataBitstream<16> charmap_8E_blank @0x13c8f0;
DataBitstream<16> charmap_8F_open_circle @0x13c900;
DataBitstream<16> charmap_90_blank @0x13c910;
DataBitstream<16> charmap_91_blank @0x13c920;
DataBitstream<16> charmap_92_blank @0x13c930;
DataBitstream<16> charmap_93_blank @0x13c940;
DataBitstream<16> charmap_94_blank @0x13c950;
DataBitstream<16> charmap_95_blank @0x13c960;
DataBitstream<16> charmap_96_bracket_open @0x13c970;
DataBitstream<16> charmap_97_bracket_close @0x13c980;
DataBitstream<16> charmap_98_question @0x13c990;
DataBitstream<16> charmap_99_exclamation @0x13c9a0;
DataBitstream<16> charmap_9A_qoute_bottom @0x13c9b0;
DataBitstream<16> charmap_9B_middle_period @0x13c9c0;
DataBitstream<16> charmap_9C_dash @0x13c9d0;
DataBitstream<16> charmap_9D_tilde @0x13c9e0;
DataBitstream<16> charmap_9E_slash @0x13c9f0;
DataBitstream<16> charmap_9F_asterix @0x13ca00;
DataBitstream<16> charmap_A0_parens_open @0x13ca10;
DataBitstream<16> charmap_A1_parens_close @0x13ca20;
DataBitstream<16> charmap_A2_plus @0x13ca30;
DataBitstream<16> charmap_A3_colon @0x13ca40;
DataBitstream<16> charmap_A4_middle_three_dots @0x13ca50;
DataBitstream<16> charmap_A5_Lv @0x13ca60;
DataBitstream<16> charmap_A6_Ex @0x13ca70;
DataBitstream<16> charmap_A7_Male @0x13ca80;
DataBitstream<16> charmap_A8_Female @0x13ca90;
DataBitstream<16> charmap_A9_UP @0x13caa0;
DataBitstream<16> charmap_AA_kanji_0 @0x13cab0;
DataBitstream<16> charmap_AB_kanji_1 @0x13cac0;
DataBitstream<16> charmap_AC_star @0x13cad0;
DataBitstream<16> charmap_AD_DOWN @0x13cae0;
DataBitstream<16> charmap_AE_LEFT @0x13caf0;
DataBitstream<16> charmap_AF_RIGHT @0x13cb00;
DataBitstream<16> charmap_B0_NW @0x13cb10;
DataBitstream<16> charmap_B1_NE @0x13cb20;
DataBitstream<16> charmap_B2_SW @0x13cb30;
DataBitstream<16> charmap_B3_SE @0x13cb40;
DataBitstream<16> charmap_B4_zz @0x13cb50;
DataBitstream<16> charmap_B5_copywrite @0x13cb60;
DataBitstream<16> charmap_B6_ampersand @0x13cb70;
DataBitstream<16> charmap_B7_blank @0x13cb80;
DataBitstream<16> charmap_B8_blank @0x13cb90;
DataBitstream<16> charmap_B9_blank @0x13cba0;
DataBitstream<16> charmap_BA_blank @0x13cbb0;
DataBitstream<16> charmap_BB_blank @0x13cbc0;
DataBitstream<16> charmap_BC_blank @0x13cbd0;
DataBitstream<16> charmap_BD_blank @0x13cbe0;
DataBitstream<16> charmap_BE_blank @0x13cbf0;
DataBitstream<16> charmap_BF_blank @0x13cc00;
DataBitstream<16> charmap_C0_blank @0x13cc10;
DataBitstream<16> charmap_C1_blank @0x13cc20;
DataBitstream<16> charmap_C2_blank @0x13cc30;
DataBitstream<16> charmap_C3_blank @0x13cc40;
DataBitstream<16> charmap_C4_blank @0x13cc50;
DataBitstream<16> charmap_C5_blank @0x13cc60;
DataBitstream<16> charmap_C6_blank @0x13cc70;
DataBitstream<16> charmap_C7_blank @0x13cc80;
DataBitstream<16> charmap_C8_blank @0x13cc90;
DataBitstream<16> charmap_C9_blank @0x13cca0;
DataBitstream<16> charmap_CA_blank @0x13ccb0;
DataBitstream<16> charmap_CB_blank @0x13ccc0;
DataBitstream<16> charmap_CC_blank @0x13ccd0;
DataBitstream<16> charmap_CD_blank @0x13cce0;
DataBitstream<16> charmap_CE_blank @0x13ccf0;
DataBitstream<16> charmap_CF_blank @0x13cd00;
DataBitstream<16> charmap_D0_blank @0x13cd10;
DataBitstream<16> charmap_D1_blank @0x13cd20;
DataBitstream<16> charmap_D2_blank @0x13cd30;
DataBitstream<16> charmap_D3_TE @0x13cd40;
DataBitstream<16> charmap_D4_ER @0x13cd50;
DataBitstream<16> charmap_D5_RR @0x13cd60;
DataBitstream<16> charmap_D6_RY @0x13cd70;
DataBitstream<16> charmap_D7_blank @0x13cd80;
DataBitstream<16> charmap_D8_blank @0x13cd90;
DataBitstream<16> charmap_D9_blank @0x13cda0;
DataBitstream<16> charmap_DA_blank @0x13cdb0;
DataBitstream<16> charmap_DB_blank @0x13cdc0;
DataBitstream<16> charmap_DC_blank @0x13cdd0;
DataBitstream<16> charmap_DD_blank @0x13cde0;
DataBitstream<16> charmap_DE_blank @0x13cdf0;
DataBitstream<16> charmap_DF_blank @0x13ce00;
DataBitstream<16> charmap_E0_blank @0x13ce10;
DataBitstream<16> charmap_E1_blank @0x13ce20;
DataBitstream<16> charmap_E2_blank @0x13ce30;
DataBitstream<16> charmap_E3_blank @0x13ce40;
DataBitstream<16> charmap_E4_blank @0x13ce50;
DataBitstream<16> charmap_E5_blank @0x13ce60;
DataBitstream<16> charmap_E6_blank @0x13ce70;
DataBitstream<16> charmap_E7_blank @0x13ce80;
DataBitstream<16> charmap_E8_blank @0x13ce90;
DataBitstream<16> charmap_E9_blank @0x13cea0;
DataBitstream<16> charmap_EA_blank @0x13ceb0;
DataBitstream<16> charmap_EB_blank @0x13cec0;
DataBitstream<16> charmap_EC_blank @0x13ced0;
DataBitstream<16> charmap_ED_blank @0x13cee0;
DataBitstream<16> charmap_EE_blank @0x13cef0;
DataBitstream<16> charmap_EF_blank @0x13cf00;
DataBitstream<16> charmap_F0_blank @0x13cf10;
DataBitstream<16> charmap_F1_blank @0x13cf20;
DataBitstream<16> charmap_F2_blank @0x13cf30;
DataBitstream<16> charmap_F3_blank @0x13cf40;
DataBitstream<16> charmap_F4_blank @0x13cf50;
DataBitstream<16> charmap_F5_blank @0x13cf60;
DataBitstream<16> charmap_F6_blank @0x13cf70;
DataBitstream<16> charmap_F7_blank @0x13cf80;
DataBitstream<16> charmap_F8_blank @0x13cf90;
DataBitstream<16> charmap_F9_blank @0x13cfa0;
DataBitstream<16> charmap_FA_blank @0x13cfb0;
DataBitstream<16> charmap_FB_blank @0x13cfc0;
DataBitstream<16> charmap_FC_blank @0x13cfd0;
DataBitstream<16> charmap_FD_blank @0x13cfe0;
DataBitstream<16> charmap_FE_blank @0x13cff0;
DataBitstream<16> charmap_FF_blank @0x13d000;

//========================================================================
// All Text Banks
//========================================================================
//
// TODO: dump texts to plaintext output for further analysis
// TODO: parse to usable format for WatabouEngine (sqlite3 db)
//
//---------------------------
// Notes:
//---------------------------
// Text tables are prefixed with 0xCD0906C9, or with this string near the start
// Dialogue lines are normally prefixed with 0xEA or 0xEB, however that is not
// always the case. 0xFAF7 and then a \n indicate a window break.
// All strings terminate in 0xF0.
//========================================================================

//BANK 18
TextBitstream<0x18cd> text_dump_00 @ 0x61694; // 48 dialogue streams
//BANK 1A
TextBitstream<0x3056> text_dump_01 @ 0x68152; //153 dialogue streams
//BANK 1B
TextBitstream<0x3457> text_dump_02 @ 0x6C126; //130 dialogue streams
//BANK 1F
TextBitstream<0x38f7> text_dump_03 @ 0x7C106; //114 dialogue streams
//BANK 21
TextBitstream<0x3af3> text_dump_04 @ 0x84106; //116 dialogue streams
//BANK 22
TextBitstream<0x276f> text_dump_05 @ 0x8819e; //126 dialogue streams
//BANK 3F
TextBitstream<0x2e3c> text_dump_06 @ 0xFC56c; //104 dialogue streams
//BANK 41
TextBitstream<0x336d> text_dump_07 @0x104AA8; //Multiple Tables: Debug menu, basic menu dia and texts,
// gate names, rando name table, monster table, action table, item table?, 2 letter combos? items, 
// item descripts?, personalities, elvel up dia, book read dia, item/abi usage dia

//BANK 42
TextBitstream<0x3c82> text_dump_08 @0x108142; //113 dialogue streams
//BANK 43
TextBitstream<0x359b> text_dump_09 @0x10C193; //142 dialogue streams
//BANK 44
TextBitstream<0x3e12> text_dump_0A @0x110157; // 98 dialogue streams
//BANK 45
TextBitstream<0x3902> text_dump_0B @0x114158; //124 dialogue streams
//BANK 46
TextBitstream<0x3c60> text_dump_0C @0x118180; //144 dialogue streams
//BANK 47
TextBitstream<0x1ab2> text_dump_0D @0x11C0C1; // 56 dialogue streams
//BANK 48
TextBitstream<0x3486> text_dump_0E @0x12016b; //108 dialogue streams
//BANK 49
TextBitstream<0x3a76> text_dump_0F @0x12419c; //158 dialogue streams
//BANK 4A
TextBitstream<0x2992> text_dump_10 @0x128293; //205 dialogue streams
//BANK 4B
TextBitstream<0x239d> text_dump_11 @0x12C0D1; // 63 dialogue streams
//BANK 4C
TextBitstream<0x2650> text_dump_12 @0x130304; //Battle Dialogues, and Credits.
//BANK 4D
TextBitstream<0x334c> text_dump_13 @0x1343CE; //Library Breeding recipe text, and monster descriptions
//BANK 4E
TextBitstream<0x38c9> text_dump_14 @0x138143; // 88 dialogue streams
//BANK 4F
TextBitstream<0x1901> text_dump_15 @0x13d25b; // 87 dialogue streams
//BANK 55 has the CD0906C9 prefix. Unknown semi-gibberish
UnknownBitstream<0xb7> possible_text_dump_00 @0x15486D;
//BANK 56
//CD0906C9 prefix located @0x158912, unknown purpose of this section
UnknownBitstream<0x536> unknown_section_00 @0x158916;
TextBitstream<0x17ff> text_dump_16 @0x158E4C; //Debug menu stuff, then Skill descripts table.
//BANK 59
UnknownBitstream<0x39>  unknown_section_01 @0x1652F9;
TextBitstream<0x875>  text_dump_17 @0x165332; //Looks like unused debug dialogue explaining battle system
//BANK 5F no CD0906C9 prefix
UnknownBitstream<0x350>  unknown_section_02 @0x17E640; //possibly a charmap print test screen? grabbed extra before and after, will need to trim