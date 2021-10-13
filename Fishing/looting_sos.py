# Treasure Map Puller by MatsaMilla
# SHOULD pull gold first and palce in beetle
# keeps recalls, gate & lvl 8 summoning scrolls no matter what
# you will have to re-assign bags every time you close Razor... fault of the program.
# Cursed Items will be sent to the trash bag

dragTime = 1300
msgColor = 68
self = Mobiles.FindBySerial(Player.Serial)

# *** Replace with beetle serial if you have one *** 
beetle = 0x0086B3F8

# *** False if you don not have beetle *** 
beetleBag = True

# True if you want to keep scrolls
sortScrolls = True

#check for wep bag
if Misc.CheckSharedValue('wepBag'):
    wepBag = Misc.ReadSharedValue('wepBag')
    if Items.FindBySerial(wepBag):
        Misc.NoOperation()
    else:
        wepBag = Target.PromptTarget('Select Bag for Weapons')
        Misc.SetSharedValue('wepBag', wepBag)
else:
    wepBag = Target.PromptTarget('Select Bag for Weapons')
    Misc.SetSharedValue('wepBag', wepBag)
#check for armor bag    
if Misc.CheckSharedValue('armorBag'):
    armorBag = Misc.ReadSharedValue('armorBag')
    if Items.FindBySerial(armorBag):
        Misc.NoOperation()
    else:
        armorBag = Target.PromptTarget('Select Bag for Armor')
        Misc.SetSharedValue('armorBag', armorBag)
else:
    armorBag = Target.PromptTarget('Select Bag for Armor')
    Misc.SetSharedValue('armorBag', armorBag)
    
#check for jewlery bag    
if Misc.CheckSharedValue('jewleryBag'):
    jewleryBag = Misc.ReadSharedValue('jewleryBag')
    if Items.FindBySerial(jewleryBag):
        Misc.NoOperation()
    else:
        jewleryBag = Target.PromptTarget('Select Bag for Jewelery')
        Misc.SetSharedValue('jewleryBag', jewleryBag)
else:
    jewleryBag = Target.PromptTarget('Select Bag for Jewelery')
Misc.SetSharedValue('jewleryBag', jewleryBag)
    
#check for trash bag    
if Misc.CheckSharedValue('trashbag'):
    trashbag = Misc.ReadSharedValue('trashbag')
    if Items.FindBySerial(trashbag):
        Misc.NoOperation()
    else:
        trashbag = Target.PromptTarget('Select Bag for trash')
        Misc.SetSharedValue('trashbag', trashbag)
else:
    trashbag = Target.PromptTarget('Select Bag for trash')
    Misc.SetSharedValue('trashbag', trashbag)

#check for treasure bag
if Misc.CheckSharedValue('treasurebag'):
    treasurebag = Misc.ReadSharedValue('treasurebag')
    if Items.FindBySerial(treasurebag):
        Misc.NoOperation()
    else:
        treasurebag = Target.PromptTarget('Select Bag for treasure')
        Misc.SetSharedValue('treasurebag', treasurebag)
else:
    treasurebag = Target.PromptTarget('Select Bag for treasure')
    Misc.SetSharedValue('treasurebag', treasurebag)
    
#check for reg bag
if Misc.CheckSharedValue('regBag'):
    regBag = Misc.ReadSharedValue('regBag')
    if Items.FindBySerial(regBag):
        Misc.NoOperation()
    else:
        regBag = Target.PromptTarget('Select Bag for Regs')
        Misc.SetSharedValue('regBag', regBag)
else:
    regBag = Target.PromptTarget('Select Bag for Regs')
    Misc.SetSharedValue('regBag', regBag)

#check for gem bag    
if Misc.CheckSharedValue('gemBag'):
    gemBag = Misc.ReadSharedValue('gemBag')
    if Items.FindBySerial(gemBag):
        Misc.NoOperation()
    else:
        gemBag = Target.PromptTarget('Select Bag for Gems')
        Misc.SetSharedValue('gemBag', gemBag)
else:
    gemBag = Target.PromptTarget('Select Bag for Gems')
    Misc.SetSharedValue('gemBag', gemBag)

#check for scroll bag
if sortScrolls:
    if Misc.CheckSharedValue('scrollBag'):
        scrollBag = Misc.ReadSharedValue('scrollBag')
        if Items.FindBySerial(scrollBag):
            Misc.NoOperation()
        else:
            scrollBag = Target.PromptTarget('Select Bag for Scrolls')
            Misc.SetSharedValue('scrollBag', scrollBag)
    else:
        scrollBag = Target.PromptTarget('Select Bag for Scrolls')
        Misc.SetSharedValue('scrollBag', scrollBag)
chest = Target.PromptTarget('Select Treasure Chest') 
 
#loot includes gate, recall & lvl 8 summoning scrolls
loot = []

gold = [0xeed]
gems = [0xf16,0xf15,0xf19,0xf25,0xf21,0xf10,0xf26,0xf2d,0xf13,0x0F0F,0x0F11,0x0F18,0x3197,0x3196]
wands = [0xdf5,0xdf3,0xdf4,0xdf2]
boneArmor= [0x1450,0x1f0b,0x1452,0x144f,0x1451,0x144e]
regs= [0xf7a,0xf7b,0xf86,0xf84,0xf85,0xf88,0xf8d,0xf8c,0x0F8F,0x0F7D,0x0F8E,0x0F78,0x0F8A]

jewlery= [0x1F09,0x108A,0x1F06,0x1086]

weps = [0xf62,0x1403,0xe87,0x1405,0x1401,0xf52,0x13b0,0xdf0,0x1439,0x1407,0xe89,0x143d,0x13b4,0xe81,0x13f8,
0xf5c,0x143b,0x13b9,0xf61,0x1441,0x13b6,0xec4,0x13f6,0xf5e,0x13ff,0xec3,0xf43,0xf45,0xf4d,0xf4b,0x143e,
0x13fb,0x1443,0xf47,0xf49,0xe85,0xe86,0x13fd,0xf50,0x26C9,0x26BB,0x0EC2,0x26CC,0x13B5,0x13B3,0x0FB5,
0x26C8,0x0F51,0x26CB,0x143A,0x13F5,0x13E3,0x26BD,0x0F44,0x26BF,0x26C5,0x26CD,0x26C7,0x1400,0x1402,0x0F4F,
0x0E8A,0x13FA,0x13F7,0x0F5F,0x26BE,0x13AF,0x26C3,0x26BA,0x0EC5,0x0F63,0x13BA,0x0F4A,0x1404,0x13F4,0x13F9,
0x26C0,0x13FC,0x13B1,0x1440,0x0F5D,0x1438,0x1406,0x26C1,0x0DF1,0x26C2,0x1442,0x0F4C,0x0F48,0x13FE,0x143C,
0x143F,0x26C4,0x26CA,0x26C6,0x0E88,0x0F46,0x0F60,0x26BC,0x0F4E]

armor = [0x1b72,0x1b73,0x1b7b,0x1b74,0x1b79,0x1b7a,0x1b76,0x1408,0x1410,0x1411,0x1412,0x1413,0x1414,0x1415,
0x140a,0x140c,0x140e,0x13bb,0x13be,0x13bf,0x13ee,0x13eb,0x13ec,0x13f0,0x13da,0x13db,0x13d5,0x13d6,0x13dc,
0x13c6,0x13cd,0x13cc,0x13c7,0x1db9,0x1c04,0x1c0c,0x1c02,0x1c00,0x1c08,0x1c06,0x13EF,0x13D4,
0x1453,0x1C01,0x13ED,0x141A,0x1455,0x13C4,0x13D3,0x1418,0x1717,0x13F1,0x1544,0x171B,0x13C5,0x1DBA,0x1457,
0x13DD,0x1BC5,0x153F,0x141C,0x1B75,0x171C,0x154B,0x1419,0x1416,0x1417,0x1714,0x1713,0x1BC3,0x1549,0x1718,
0x171A,0x13F2,0x1F0C,0x13E2,0x13D2,0x13E1,0x13C3,0x1716,0x13CE,0x1B77,0x1B78,0x1456,0x1C05,0x1BC4,0x1454,
0x1C03,0x140B,0x1547,0x13C0,0x1545,0x1C07,0x1409,0x140F,0x1543,0x140D,0x1C09,0x1C0D,0x141B]

scrolls = [0x1f2d,0x1f2e,0x1f2f,0x1f30,0x1f31,0x1f32,0x1f33,0x1f34,0x1f35,0x1f36,0x1f37,0x1f38,0x1f39,
0x1f3a,0x1f3b,0x1f3c,0x1f3d,0x1f3e,0x1f3f,0x1f40,0x1f41,0x1f42,0x1f43,0x1f44,0x1f45,0x1f46,0x1f47,0x1f48,
0x1f49,0x1f4a,0x1f4b,0x1f4d,0x1f4e,0x1f4f,0x1f50,0x1f51,0x1f52,0x1f53,0x1f54,0x1f55,0x1f56,0x1f57,0x1f58,
0x1f59,0x1f5a,0x1f5b,0x1f5c,0x1f5d,0x1f5e,0x1f5f,0x1f60,0x1f61,0x1f62,0x1f63,0x1f64,0x1f65,0x1f66,0x1f67,
0x1f68,0x1f69,0x1f6a,0x1f6b,0x1f6c,0x226E,0x226A,0x226D,0x2269,0x2270,0x2266,0x226A,0x2260,0x1f4c,0x1f60,
0x1f66,0x1f68,0x1f69,0x1f6a,0x1f6b,0x1f6c]

trash= [0x4CDA,0x4CD8,0x142A,0x4CD9,0x2D61,0x142B,0x0D1D, 0x2003]

treasure = [0x0DCA, 0xA3E9, 0xA421, 0x13B2, 0x13CB, 0x1F01, 0x1C0A, 0xA414, 0x3D8F, 0x3D8E, 0x0D1E]

mapChest = Items.FindBySerial(chest)
Items.UseItem(mapChest)
Misc.Pause(dragTime)
#Items.WaitForContents(mapChest, 50)
Misc.Pause(dragTime)

#moves gold to beetle
if beetleBag:
    for s in mapChest.Contains:
        if s.ItemID in gold:
            if Player.Mount:
                Mobiles.UseMobile(Player.Serial)
                Misc.Pause(dragTime)
            Items.Move(s, beetle, 0)
            Misc.Pause(dragTime)
            if not Player.Mount:
                Mobiles.UseMobile(beetle)
                Misc.Pause(dragTime)

for e in mapChest.Contains :
    if e.ItemID in gold:
        Items.Move(e, Player.Backpack.Serial, 0)
        Misc.Pause(dragTime)
    elif e.ItemID in gems:
        Items.Move(e, gemBag, 0)
        Misc.Pause(dragTime)
                

while len(mapChest.Contains) > 0:
    for i in mapChest.Contains :
        props = Items.GetPropStringList(i) 
        prop_string = str(props) 
        if 'cursed' in prop_string:
            Items.Move(i, trashbag, 0)
        elif i.ItemID in boneArmor:
            Items.Move(i, armorBag, 0)
            Misc.Pause(dragTime)
        elif i.ItemID in regs:
            Items.Move(i, regBag, 0)
            Misc.Pause(dragTime)
        elif i.ItemID in weps:
            Items.Move(i, wepBag, 0)
            Misc.Pause(dragTime)
        elif i.ItemID in armor:
            Items.Move(i, armorBag, 0)
            Misc.Pause(dragTime)
        elif i.ItemID in wands:
            Items.Move(i, trashbag, 0)
            Misc.Pause(dragTime)
        elif i.ItemID in jewlery:
            Items.Move(i, jewleryBag, 0)
            Misc.Pause(dragTime)
        elif i.ItemID in trash:
            Items.Move(i, trashbag, 0)
            Misc.Pause(dragTime)
        elif i.ItemID in treasure:
            Items.Move(i, treasurebag, 0)
            Misc.Pause(dragTime)
        elif sortScrolls:
            if i.ItemID in scrolls:
                Items.Move(i, scrollBag, 0)
                Misc.Pause(dragTime)

           
Player.HeadMessage(msgColor, 'All Done')