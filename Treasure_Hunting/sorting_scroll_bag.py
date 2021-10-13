
dragTime = 1100


#Scroll storage bag assignment section

#check for first circle scrolls bag
if Misc.CheckSharedValue('firstbag'):
    firstbag = Misc.ReadSharedValue('firstbag')
    if Items.FindBySerial(firstbag):
        Misc.NoOperation()
    else:
        firstbag = Target.PromptTarget('Select Bag for 1st Circle Scrolls')
        Misc.SetSharedValue('firstbag', firstbag)
else:
    firstbag = Target.PromptTarget('Select Bag for 1st Circle Scrolls')
    Misc.SetSharedValue('firstbag', firstbag)

#check for second circle scrolls bag
if Misc.CheckSharedValue('secondbag'):
    secondbag = Misc.ReadSharedValue('secondbag')
    if Items.FindBySerial(secondbag):
        Misc.NoOperation()
    else:
        secondbag = Target.PromptTarget('Select Bag for 2nd Circle Scrolls')
        Misc.SetSharedValue('secondbag', secondbag)
else:
    secondbag = Target.PromptTarget('Select Bag for 2nd Circle Scrolls')
    Misc.SetSharedValue('secondbag', secondbag)
    
#check for third Circle Scrolls bag
if Misc.CheckSharedValue('thirdbag'):
    thirdbag = Misc.ReadSharedValue('thirdbag')
    if Items.FindBySerial(thirdbag):
        Misc.NoOperation()
    else:
        thirdbag = Target.PromptTarget('Select Bag for 3rd Cricle Scrolls')
        Misc.SetSharedValue('thirdbag', thirdbag)
else:
    thirdbag = Target.PromptTarget('Select Bag for 3rd Cricle Scrolls')
    Misc.SetSharedValue('thirdbag', thirdbag)
    
#check for forth Circle Scrolls bag
if Misc.CheckSharedValue('fourthbag'):
    fourthbag = Misc.ReadSharedValue('fourthbag')
    if Items.FindBySerial(fourthbag):
        Misc.NoOperation()
    else:
        fourthbag = Target.PromptTarget('Select Bag for 4th Circle Scrolls')
        Misc.SetSharedValue('fourthbag', foruthbag)
else:
    fourthbag = Target.PromptTarget('Select Bag for 4th Circle Scrolls')
    Misc.SetSharedValue('fourthbag', fourthbag)

#check for Fifth circle Scrolls bag
if Misc.CheckSharedValue('fifthbag'):
    fifthbag = Misc.ReadSharedValue('fifthbag')
    if Items.FindBySerial(fifthbag):
        Misc.NoOperation()
    else:
        fifthbag = Target.PromptTarget('Select Bag for 5th Circle Scrolls')
        Misc.SetSharedValue('fifthbag', fifthbag)
else:
    fifthbag = Target.PromptTarget('Select Bag for 5th Circle Scrolls')
    Misc.SetSharedValue('fifthbag', fifthbag)
    
    #check for sixth Circle Scrolls bag
if Misc.CheckSharedValue('sixthbag'):
    sixthbag = Misc.ReadSharedValue('sixthbag')
    if Items.FindBySerial(sixthbag):
        Misc.NoOperation()
    else:
        sixthbag = Target.PromptTarget('Select Bag for 6th Circle Scrolls')
        Misc.SetSharedValue('sixthbag', sixthbag)
else:
    sixthbag = Target.PromptTarget('Select Bag for 6th Circle Scrolls')
    Misc.SetSharedValue('sixthbag', sixthbag)
    
#check for Seventh Circle Scrolls bag
if Misc.CheckSharedValue('seventhbag'):
    seventhbag = Misc.ReadSharedValue('seventhbag')
    if Items.FindBySerial(seventhbag):
        Misc.NoOperation()
    else:
        seventhbag = Target.PromptTarget('Select Bag for 7th Circle Scrolls')
        Misc.SetSharedValue('seventhbag', seventhbag)
else:
    seventhbag = Target.PromptTarget('Select Bag for 7th Circle Scrolls')
    Misc.SetSharedValue('seventhbag', seventhbag)
    
    #check for Eighth Circle Scrolls bag
if Misc.CheckSharedValue('eighthbag'):
    eighthbag = Misc.ReadSharedValue('eighthbag')
    if Items.FindBySerial(eighthbag):
        Misc.NoOperation()
    else:
        eighthbag = Target.PromptTarget('Select Bag for 8th Circle Scrolls')
        Misc.SetSharedValue('eighthbag', eighthbag)
else:
    eighthbag = Target.PromptTarget('Select Bag for 8th Circle Sctolls')
    Misc.SetSharedValue('eighthbag', eighthbag)
    
#check for Necromancy Scrolls bag
if Misc.CheckSharedValue('necrobag'):
    necrobag = Misc.ReadSharedValue('necrobag')
    if Items.FindBySerial(necrobag):
        Misc.NoOperation()
    else:
        necrobag = Target.PromptTarget('Select Bag for Necromancy Scrolls')
        Misc.SetSharedValue('necrobag', necrobag)
else:
    necrobag = Target.PromptTarget('Select Bag for Necromancy Scrolls')
    Misc.SetSharedValue('necrobag', necrobag)

   
    
#Main Section

first_circle = []
second_circle = []
third_circle = []
fourth_circle = [0x1F45,0x1F47,0x1F48,0x1F4A,0x1F49,0x1F4B]
fifth_circle = [0x1F4F,0x1F53,0x1F51,0x1F4D,0x1F54,0x1F50,0x1F4E,0x1F4C,0x1F46]
sixth_circle = [0x1F55,0x1F57,0x1F59,0x1F5B,0x1F5A,0x1F52,0x1F56,0x1F58,0x1F5C]
seventh_circle = [0x1F61,0x1F5D,0x1F5F,0x1F64,0x1F62,0x1F60,0x1F5E,0x1F63]
eighth_circle = [0x1F63,0x2266,0x226A]
necro = [0x2270,0x226D,0x226E,0x2269]


scroll_bag = Target.PromptTarget('Select Scroll Bag')
scroll_bag_serial = Items.FindBySerial(scroll_bag)
Items.UseItem(scroll_bag_serial)
Misc.Pause(dragTime)


for i in scroll_bag_serial.Contains :
    if i.ItemID in first_circle:
        Items.Move(i, firstbag, 0)
        Misc.Pause(dragTime)
    elif i.ItemID in second_circle:
        Items.Move(i, secondbag, 0)
        Misc.Pause(dragTime)
    elif i.ItemID in third_circle:
        Items.Move(i, thirdbag, 0)
        Misc.Pause(dragTime)
    elif i.ItemID in fourth_circle:
        Items.Move(i, fourthbag, 0)
        Misc.Pause(dragTime)
    elif i.ItemID in fifth_circle:
        Items.Move(i, fifthbag, 0)
        Misc.Pause(dragTime)
    elif i.ItemID in sixth_circle:
        Items.Move(i, sixthbag, 0)
        Misc.Pause(dragTime)
    elif i.ItemID in seventh_circle:
        Items.Move(i, seventhbag, 0)
        Misc.Pause(dragTime)
    elif i.ItemID in eighth_circle:
        Items.Move(i, eighthbag, 0)
        Misc.Pause(dragTime)
    elif i.ItemID in necro:
        Items.Move(i, necrobag, 0)
        Misc.Pause(dragTime)

