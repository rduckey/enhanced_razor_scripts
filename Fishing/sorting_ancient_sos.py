sos_bag = Target.PromptTarget('Target your SOS bag')
sos_bag_serial = Items.FindBySerial(sos_bag)

ancient_bag = Target.PromptTarget('Target the bag you want to place your Ancient SOS messages')
ancient_bag_serial = Items.FindBySerial(ancient_bag)

Items.UseItem(sos_bag_serial)
Misc.Pause(1100)
for i in sos_bag_serial.Contains:
    if i.ItemID == 0x14EE and i.Hue == 0x0481: #ID and Hue of Ancient SOS
        Items.Move(i, ancient_bag_serial, 0)
        Misc.Pause(1100)