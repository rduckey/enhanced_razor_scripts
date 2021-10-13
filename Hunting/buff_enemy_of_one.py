while Player.IsGhost == False:
    if Player.BuffsExist('Enemy Of One') is False:
        Spells.CastChivalry('Enemy Of One')
        Misc.Pause(1000) 