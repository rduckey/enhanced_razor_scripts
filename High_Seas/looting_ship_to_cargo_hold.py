#For moving High Seas loot from backpack to cargo hold
#Must have 2 containers in cargo hold for:
#Cannon Supplies and Maritime Trade Cargo

#set cargo_hold to serial of your ships cargo hold
cargo_hold = 0x42F5DB23
dragTime = 1100
msgColor = 68

#check for Maritime Trade Cargo bag
if Misc.CheckSharedValue('cargobag'):
    cargobag = Misc.ReadSharedValue('cargobag')
    if Items.FindBySerial(cargobag):
        Misc.NoOperation()
    else:
        cargobag = Target.PromptTarget('Select Bag for Maritime Trade Cargo')
        Misc.SetSharedValue('cargobag', cargobag)
else:
    cargobag = Target.PromptTarget('Select Bag for Maritime Trade Cargo')
    Misc.SetSharedValue('cargobag', cargobag)
#check for cannon supplies bag    
if Misc.CheckSharedValue('cannonbag'):
    cannonbag = Misc.ReadSharedValue('cannonbag')
    if Items.FindBySerial(cannonbag):
        Misc.NoOperation()
    else:
        cannonbag = Target.PromptTarget('Select Bag for cannon supplies')
        Misc.SetSharedValue('cannonbag', cannonbag)
else:
    cannonbag = Target.PromptTarget('Select Bag for cannon supplies')
    Misc.SetSharedValue('cannonbag', cannonbag)
   
   
metal = [0x1BF2, 0x19B8]
leather = [0x1081, 0x0DF9]
tailoring = [0x0DF8]    
wood = [0x1BD7, 0x1BE0]
food = [0x1039]
cannonparts = [0x4224, 0xA2BE, 0x1420, 0xA2BF, 0x14F2] 
    
Items.UseItem(cargo_hold)
Misc.Pause(dragTime)
for e in Player.Backpack.Contains:
    if e.ItemID in metal:
        Items.Move(e, cargo_hold, 0)
        Misc.Pause(dragTime)
    elif e.ItemID in leather:
        Items.Move(e, cargo_hold, 0)
        Misc.Pause(dragTime)
    elif e.ItemID in wood:
        Items.Move(e, cargo_hold, 0)
        Misc.Pause(dragTime)
    elif e.ItemID in tailoring:
        Items.Move(e, cargo_hold, 0)
        Misc.Pause(dragTime)
    elif e.ItemID in food:
        Items.Move(e, cargo_hold, 0)
        Misc.Pause(dragTime)
    elif e.ItemID in cannonparts:
        Items.Move(e, cannonbag, 0)
        Misc.Pause(dragTime)
    elif e.ItemID == 0xA2C4:
        Items.Move(e, cargobag, 0)
        Misc.Pause(dragTime)