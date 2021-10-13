while Player.IsGhost is False:
    if not Player.BuffsExist('Confidence') \
    and Player.Hits < (Player.HitsMax - 10):
        Spells.CastBushido('Confidence')
        Misc.Pause(4000)
        #    if Player.BuffsExist('Enemy Of One') is False \
        #    and Player.Mana > 19:
            #        Spells.CastChivalry('Enemy Of One')
            #        Misc.Pause(4000)
            #    if Player.Mana > 17 and Player.BuffsExist('Momentum Strike') is False:
            #        Spells.CastBushido('Momentum Strike')
            #        Misc.Pause(500)