while Player.IsGhost is False:
    if Player.Hits == Player.HitsMax:
        if Items.BackpackCount(0x4078, -1) < 1:
            Misc.Pause(3000)
            if Items.BackpackCount(0x4078, -1) < 1:
                Spells.CastMysticism('Healing Stone')
                Misc.Pause(5000)
    else:
        if Player.Hits < Player.HitsMax * .4:
            Items.UseItemByID(0x4078)