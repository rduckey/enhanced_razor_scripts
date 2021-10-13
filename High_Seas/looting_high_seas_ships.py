dragTime = 1100
msgColor = 68
self = Mobiles.FindBySerial(Player.Serial)

metal = [0x1BF2, 0x19B8]
leather = [0x1081]
tailoring = [0x0DF8, 0x0DF9]    
wood = [0x1BD7, 0x1BE0]
food = [0x1039]
cannonparts = [0x4224, 0xA2BE, 0x1420, 0xA2BF, 0x14F2]
hides = 0x1078

chest = Target.PromptTarget('Where be the booty?')
booty = Items.FindBySerial(chest)

Items.UseItem(booty)
Misc.Pause(dragTime)
#Items.WaitForContents(booty, 50)
Misc.Pause(dragTime)

def checkWeight():
    if Player.Weight >= Player.MaxWeight:
        Player.ChatSay(msgColor, 'I am Overweight, stopping')
        Stop 

def cut_hide():
    hides = 0x1078
    for i in Player.Backpack.Contains:
        if i.ItemID == hides:
          Items.UseItemByID(0x0F9E, -1)
          Target.WaitForTarget(10000)
          Target.TargetExecute(i.Serial)
          Misc.Pause(dragTime)
        
for e in booty.Contains:
    checkWeight()
    if e.ItemID in metal:
        Items.Move(e, Player.Backpack.Serial, 0)
        Misc.Pause(dragTime)
    elif e.ItemID in leather:
        Items.Move(e, Player.Backpack.Serial, 0)
        Misc.Pause(dragTime)
    elif e.ItemID in wood:
        Items.Move(e, Player.Backpack.Serial, 0)
        Misc.Pause(dragTime)
    elif e.ItemID == hides:
        Items.Move(e, Player.Backpack.Serial, 0)
        Misc.Pause(dragTime)
        cut_hide()
    #elif e.ItemID in tailoring:
        #Items.Move(e, Player.Backpack.Serial, 0)
        #Misc.Pause(dragTime)
    #elif e.ItemID in food:
        #Items.Move(e, Player.Backpack.Serial, 0)
        #Misc.Pause(dragTime)
    elif e.ItemID in cannonparts:
        Items.Move(e, Player.Backpack.Serial, 0)
        Misc.Pause(dragTime)
    elif e.ItemID == 0xA2C4:
        Items.Move(e, Player.Backpack.Serial, 0)
        Misc.Pause(dragTime)
        
Player.ChatSay(15, 'Store your bounty')
       