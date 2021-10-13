#Purified Phylactories
for i in Player.Backpack.Contains:
    if i is i.ItemID == 0x4686 and i.Hue == 0x0000:
        Items.UseItem(i)
        Target.WaitForTarget(10000)
        Misc.Pause(1000)
        Misc.SendMessage('Done!')
    elif i is i.ItemID == 0x4686 and i.Hue == 0x0000:
        Misc.SendMessage('Done!')