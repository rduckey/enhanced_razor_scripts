for i in Player.Backpack.Contains:
    if i.ItemID == 0x26BD:
        Items.UseItemByID(0x13E3, 0x0966)
        Target.WaitForTarget(10000,True)
        Target.TargetExecute(i)
        Gumps.WaitForGump(999084, 1100)
        Gumps.SendAction(999084, 2)
        Misc.Pause(1100)
    elif i.ItemID == 0x0F4B:
        Items.UseItemByID(0x13E3, 0x0966)
        Target.WaitForTarget(10000,True)
        Target.TargetExecute(i)
        Gumps.WaitForGump(999084, 1100)
        Gumps.SendAction(999084, 2)
        Misc.Pause(1100)