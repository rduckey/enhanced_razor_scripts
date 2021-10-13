
#Corrupt Phylactories
for i in Player.Backpack.Contains:
    if i.ItemID == 0x4686 and i.Hue == 0x081B:
        Items.UseItem(i)
        Target.WaitForTarget(10000)
        Misc.Pause(1100)