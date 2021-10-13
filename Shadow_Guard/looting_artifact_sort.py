loot_bag= Target.PromptTarget('Target loot bag')
loot_bag_serial= Items.FindBySerial(loot_bag)
dump_bag= Target.PromptTarget('Target artifact bag')
dump_bag_serial= Items.FindBySerial(dump_bag)
drag_timer= 1100

Items.UseItem(loot_bag)
Misc.Pause(drag_timer)
for e in loot_bag_serial.Contains:
    if 'Legendary Artifact' in Items.GetPropStringList(e):
        Items.Move(e, dump_bag_serial, 0)
        Misc.Pause(drag_timer)
Misc.SendMessage('Sort Complete')