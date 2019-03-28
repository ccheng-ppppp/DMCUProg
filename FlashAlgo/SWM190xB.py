"""
 Flash OS Routines (Automagically Generated)
 Copyright (c) 2017-2017 ARM Limited
"""

flash_algo = {
    'load_address' : 0x20000000,
    'instructions' : [
        0xE00ABE00, 0x062D780D, 0x24084068, 0xD3000040, 0x1E644058, 0x1C49D1FA, 0x2A001E52, 0x4770D1F2,
        0xD1382A01, 0x200349A2, 0x20006048, 0x280A1C40, 0xF3BFD3FC, 0x489F8F5F, 0x0C096841, 0x60410409,
        0x4A9D6841, 0x60414311, 0x220F6801, 0x43910212, 0x68016001, 0x43112220, 0x6A016001, 0x40114A97,
        0x6A016201, 0x43114A96, 0x49966201, 0x60882000, 0x1E414A95, 0x21016011, 0x60880789, 0x499360C8,
        0x620A2255, 0x624A4A92, 0x4A926248, 0x6288628A, 0x49916208, 0x20006108, 0xB5F04770, 0xD0162801,
        0xD0142802, 0xD1122803, 0x69534A8B, 0x48802101, 0xD00E2B02, 0x60022202, 0x68024888, 0xD5FC0752,
        0x430A6802, 0x20006002, 0x280A1C40, 0x2000D3FC, 0x2303BDF0, 0x20006003, 0x280A1C40, 0x6910D3FC,
        0x48740B04, 0x07D26882, 0x4E7DD1FC, 0x20006031, 0x2500497B, 0x23413140, 0x061B4F7A, 0x600DE00C,
        0x618D604F, 0x608A0302, 0x61CA18D2, 0x600A4A76, 0x03D2680A, 0x1C40D4FC, 0xD3F042A0, 0xE7D66035,
        0x0501B510, 0x2001D001, 0x4962BD10, 0x07D2688A, 0x6188D1FC, 0x09006808, 0x60080100, 0x4A6B6808,
        0x60084310, 0x62482020, 0x22016948, 0x61484310, 0x07C06948, 0x6808D1FC, 0x03122201, 0x60084390,
        0x230268C8, 0x68CB4018, 0x40232404, 0xD0054318, 0x220668C8, 0x60C84310, 0xBD102001, 0x69014856,
        0x61011889, 0xBD102000, 0x0583B570, 0x2001D001, 0x1CC9BD70, 0x00890889, 0xD1062800, 0x62134B54,
        0x691C4B4D, 0x6A946254, 0x4B42615C, 0x07E4689C, 0x681CD1FC, 0x016D2581, 0x601C432C, 0x06242441,
        0xCA20E004, 0x60351906, 0x1F091D00, 0xD1F82900, 0x07C06898, 0x6818D1FC, 0x03092101, 0x60184388,
        0x210268D8, 0x68D94008, 0x40112204, 0xD0054308, 0x210668D8, 0x60D84308, 0xBD702001, 0xBD702000,
        0x2000B510, 0x688A492B, 0xD1FC07D2, 0x618A0302, 0x0912680A, 0x600A0112, 0x4B34680A, 0x600A431A,
        0x624A2220, 0x2301694A, 0x614A431A, 0x07D2694A, 0x680AD1FC, 0x031B2301, 0x600A439A, 0x230268CA,
        0x68CB401A, 0x40232404, 0xD005431A, 0x220668C8, 0x60C84310, 0xBD102001, 0x281E1C40, 0x2001D3D3,
        0x03C0491D, 0x20006108, 0x2001BD10, 0xB5304770, 0xD0010583, 0xBD302001, 0x08891CC9, 0x28000089,
        0x4B1BD104, 0x4B146213, 0x6253691B, 0x689C4B09, 0xD1FC07E4, 0x061B2341, 0x18C5E007, 0x682D6814,
        0xD1E842AC, 0x1D121D00, 0x29001F09, 0xBD30D1F5, 0x40000500, 0x4004A000, 0x0000FFFF, 0x00FF00FF,
        0x03000200, 0x400A0800, 0xE000E180, 0x40000700, 0xFDFFFFFF, 0x007FFFFF, 0x40000080, 0x40005800,
        0x40000800, 0x00000909, 0x000103FF, 0x00001027, 0x0B11FFAC, 0x00000000
    ],

    'pc_Init'            : 0x20000021,
    'pc_UnInit'          : 0x2000009B,
    'pc_EraseSector'     : 0x20000121,
    'pc_ProgramPage'     : 0x20000189,
    'pc_Verify'          : 0x2000026F,
    'pc_EraseChip'       : 0x20000201,
    'pc_BlankCheck'      : 0x2000026B,
    'pc_Read'            : 0x12000001F,
    
    'static_base'        : 0x20000400,
    'begin_data'         : 0x20000800,
    'begin_stack'        : 0x20001000,

    'analyzer_supported' : False,

    # Relative region addresses and sizes
    'ro_start'           : 0x00000000,
    'ro_size'            : 0x000002D4,
    'rw_start'           : 0x000002D4,
    'rw_size'            : 0x00000004,
    'zi_start'           : 0x000002D8,
    'zi_size'            : 0x00000000,

    # Flash information
    'flash_start'        : 0x00000000,
    'flash_size'         : 0x0001E000,
    'flash_page_size'    : 0x00000400,
}