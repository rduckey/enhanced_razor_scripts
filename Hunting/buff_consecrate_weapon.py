while Player.IsGhost == False:
    if Player.BuffsExist('Consecrate Weapon') is False:
        Spells.CastChivalry('Consecrate Weapon')
        Misc.Pause(1000)