[⬅️ Back to Master ROM Map](../DWM_Master_ROM_Map.md)
        
# Bank 4C: [System/Asset Name]
## Overview
**Local Hex Range:** `0x4000` - `0x7FFF`  
**Global Hex Range:** `0x130000` - `0x133FFF`  
**Bank Type:** Swappable  
**Category:** [Graphics / Text / Code / Audio / Unknown]  
**Summary:** [A brief 1-2 sentence description of what this bank does.]

---

## Memory Map (Granular)
*Break down the specific blocks within this bank.*

| Offset (Local) | Offset (Global) | Length | Description |
| :------------- | :-------------- | :----- | :---------- |
| `0x4000`         | `0x130000`        | ???b    | [Example Entry - Replace or Delete] |

---

## Technical Notes & Observations

### [Sub-System Name]
* **Compression/Encoding:** [e.g., 1BPP -> 2BPP Expansion, custom 0x08, None]
* **Debugger Notes:** * [Add your BGB debugging observations here]

### Raw Data / Hex Snippets
```hex
Hex View  00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
 
00130000  [4C](D1 42 E3 42 EA 42 F1  42)(19 40 15 42 3B 42 49  L.B.B.B.B.@.B;BI
00130010  42 5B 42 63 42 99 42 CF  42){05 43 1F 43 40 43 66  B[BcB.B.B.C.C@Cf
00130020  43 87 43 AB 43 CF 43 F1  43 15 44 38 44 52 44 82  C.C.C.C.C.D8DRD.
00130030  44 AF 44 D1 44 F0 44 17  45 28 45 39 45 55 45 6A  D.D.D.D.E(E9EUEj
00130040  45 7D 45 97 45 A9 45 BE  45 D2 45 E6 45 11 46 3A  E}E.E.E.E.E.E.F:
00130050  46 66 46 92 46 BE 46 E9  46 11 47 47 47 7D 47 8A  FfF.F.F.F.GGG}G.
00130060  47 99 47 A8 47 B6 47 CF  47 DF 47 F3 47 08 48 1D  G.G.G.G.G.G.G.H.
00130070  48 2F 48 42 48 5F 48 87  48 A4 48 B5 48 D6 48 F1  H/HBH_H.H.H.H.H.
00130080  48 0D 49 26 49 5E 49 72  49 8D 49 B0 49 CE 49 E5  H.I&I^IrI.I.I.I.
00130090  49 00 4A 1A 4A 32 4A 50  4A 6A 4A A6 4A BB 4A D9  I.J.J2JPJjJ.J.J.
001300A0  4A EE 4A 03 4B 17 4B 2C  4B 3A 4B 4F 4B 6C 4B 84  J.J.K.K,K:KOKlK.
001300B0  4B 9F 4B B5 4B EB 4B 11  4C 35 4C 4C 4C 63 4C 87  K.K.K.K.L5LLLcL.
001300C0  4C AC 4C D0 4C F4 4C 23  4D 4E 4D 5D 4D 94 4D AB  L.L.L.L#MNM]M.M.
001300D0  4D C7 4D DB 4D E8 4D 01  4E 1A 4E 33 4E 65 4E 93  M.M.M.M.N.N3NeN.
001300E0  4E C8 4E F4 4E 20 4F 54  4F 76 4F 93 4F AB 4F D3  N.N.N OTOvO.O.O.
001300F0  4F F1 4F 1A 50 33 50 51  50 70 50 8C 50 AA 50 BC  O.O.P3PQPpP.P.P.
00130100  50 FE 50 2B 51 42 51 54  51 75 51 93 51 A5 51 B9  P.P+QBQTQuQ.Q.Q.
00130110  51 E2 51 12 52 3F 52 57  52 71 52 87 52 9F 52 B9  Q.Q.R?RWRqR.R.R.
00130120  52 D9 52 EB 52 0A 53 21  53 37 53 56 53 75 53 8F  R.R.R.S!S7SVSuS.
00130130  53 A9 53 C5 53 D9 53 EA  53 FB 53 19 54 39 54 5A  S.S.S.S.S.S.T9TZ
00130140  54 77 54 94 54 B4 54 CC  54 E6 54 03 55 29 55 54  TwT.T.T.T.T.U)UT
00130150  55 81 55 9C 55 B8 55 C8  55 E1 55 F4 55 11 56 2C  U.U.U.U.U.U.U.V,
00130160  56 3C 56 67 56 77 56 96  56 B8 56 CE 56 FE 56 14  V<VgVwV.V.V.V.V.
00130170  57 22 57 42 57 60 57 79  57 95 57 B9 57 DC 57 F6  W"WBW`WyW.W.W.W.
00130180  57 10 58 2D 58 3C 58 5A  58 71 58 87 58 A6 58 D6  W.X-X<XZXqX.X.X.
00130190  58 EC 58 04 59 1D 59 38  59 38 59 4A 59 63 59 7F  X.X.Y.Y8Y8YJYcY.
001301A0  59 9A 59 B7 59 D0 59 E6  59 FA 59 0D 5A 24 5A 38  Y.Y.Y.Y.Y.Y.Z$Z8
001301B0  5A 54 5A 6A 5A 7C 5A 8D  5A 9F 5A B9 5A C8 5A D7  ZTZjZ|Z.Z.Z.Z.Z.
001301C0  5A E6 5A F9 5A 0D 5B 25  5B 38 5B 48 5B 5E 5B 72  Z.Z.Z.[%[8[H[^[r
001301D0  5B 80 5B 97 5B AF 5B CE  5B EB 5B 04 5C 23 5C 7B  [.[.[.[.[.[.\#\{
001301E0  5C 8A 5C 9E 5C BB 5C CB  5C E8 5C F9 5C 0E 5D 2B  \.\.\.\.\.\.\.]+
001301F0  5D 47 5D 5A 5D 71 5D 8B  5D 9E 5D B6 5D D4 5D F4  ]G]Z]q].].].].].
00130200  5D 2C 5E 4D 5E 6A 5E 8D  5E B2 5E D7 5E FD 5E 12  ],^M^j^.^.^.^.^.
00130210  5F 41 5F 6C 5F}{6D 5F 86  5F A7 5F CA 5F 02 60 32  _A_l_m_._._._.`2
00130220  60 69 60 9E 60 F2 60 27  61 45 61 70 61 9A 61 C8  `i`.`.`'aEapa.a.
00130230  61 FB 61 43 62 70 62 AC  62 E3 62}{1F 63 45 63 45  a.aCbpb.b.b.cEcE
00130240  63 75 63 A3 63 B5 63 C9  63}{E5 63 E5 63 E5 63 E5  cuc.c.c.c.c.c.c.
00130250  63 E5 63 E5 63 E5 63 E5  63 E5 63}{E5 63 01 64 29  c.c.c.c.c.c.c.d)
00130260  64 47 64}{64 64 78 64 90  64 AC 64 BC 64 C8 64 D5  dGdddxd.d.d.d.d.
00130270  64 E8 64 03 65 1B 65 34  65 42 65 4D 65 5A 65 65  d.d.e.e4eBeMeZee
00130280  65 79 65 89 65 95 65 9E  65 B1 65 B1 65 BA 65 C7  eye.e.e.e.e.e.e.
00130290  65 DB 65 E6 65 FA 65 05  66}{06 66 14 66 2D 66 3F  e.e.e.e.f.f.f-f?
001302A0  66 52 66 54 66 75 66 9F  66 BA 66 CC 66 CE 66 E4  fRfTfuf.f.f.f.f.
001302B0  66 08 67 30 67 71 67 7C  67 BB 67 BD 67 CC 67 0D  f.g0gqg|g.g.g.g.
001302C0  68 5C 68 A7 68 B9 68 C9  68 E8 68 FA 68 10 69}{44  h\h.h.h.h.h.h.iD         {44 69} WL2 garbage
001302D0  69}<FA 23 C8 FE FF C8 11  09 40 CD B6 05 3E FF EA  i.#......@...>..
001302E0  23 C8 C9><11 09 40 CD F6  05 C9><CD D1 42 CD 09 06  #....@......B...
001302F0  C9><FA 6D DD C6 D7 EA 23  C8 AF EA 22 C8 CD D1 42  ..m....#..."...B
00130300  AF EA 6D DD C9>                                   ..m..
```



---

## ETL / Extraction Plan

* [ ] [Extraction step 1]
[⬅️ Back to Master ROM Map](../DWM_Master_ROM_Map.md)
---
© 2026 Jeahnoh. Licensed under CC BY-NC 4.0. Attribution Required.
See LICENSE.md in the repository root for full non-commercial terms.