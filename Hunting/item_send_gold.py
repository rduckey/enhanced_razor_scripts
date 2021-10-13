bag_of_sending = 0x429E85B8

while Player.IsGhost == False:
    if Player.Weight >= Player.MaxWeight - 10:
        Scavenger.Stop()
        Misc.Pause(1200)
        Items.UseItem(bag_of_sending)
        Target.WaitForTarget(10000, True)
        for i in Player.Backpack.Contains:
            if i.ItemID == 0x0EED:
                Target.TargetExecute(i)
                Journal.Clear()
        Misc.Pause(1200)
        Scavenger.Start() 