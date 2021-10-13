loot_bag = Target.PromptTarget('Target Bag With Loot')
loot_bag_serial = Items.FindBySerial(loot_bag)
dump_bag = Target.PromptTarget('Target Bag to Dump to')
dump_bag_serial = Items.FindBySerial(dump_bag)

Items.UseItem(loot_bag)
Misc.Pause(1500)
for i in loot_bag_serial.Contains:
    Items.Move(i, dump_bag_serial, 0)
    Misc.Pause(1200)