

def consecrate_weapon():
    if Player.BuffsExist('Consecrate Weapon') is False:
        Spells.CastChivalry('Consecrate Weapon')
        Misc.Pause(1000)
        #    if Player.BuffsExist('Weaken') or 
        #    Player.BuffsExist('Feeble Mind') or 
        #    Player.BuffsExist('Clumsy')
        #    Spells.CastChivalry('Remove Curse')
        
def eoo():
    if Player.BuffsExist('Enemy Of One') is False:
        Spells.CastChivalry('Enemy Of One')
        Misc.Pause(1000)
        
while Player.IsGhost is False:
    #concecrate_weapon()
    eoo()