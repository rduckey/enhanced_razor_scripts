#buy skill up  to 40 before using this script
#Change delay between casting spells based on personal Faster Cast Recovery
recovery = 1000

def meditation_check():
    Misc.Pause(1000)
    Player.UseSkill('Meditation')
    Misc.Pause(1000)
    if Player.Mana != Player.ManaMax:
        while Player.Mana != Player.ManaMax:
            if Player.BuffsExist('Meditation') is False:
                Player.UseSkill('Meditation')
                Misc.Pause(6000)
           

while Player.GetRealSkillValue('Mysticism') < Player.GetSkillCap('Mysticism'):
    if Player.GetRealSkillValue('Mysticism') < 63:
        while Player.Mana >= 11:
            Spells.CastMysticism('Stone Form')
            Misc.Pause(recovery)
        else:
            meditation_check()
    elif Player.GetRealSkillValue('Mysticism') < 80:
        while Player.Mana >= 20:
            Spells.CastMysticism('Cleansing Winds')
            Target.WaitForTarget(10000, True)
            Target.Self()
            Misc.Pause(recovery)
        else:
            meditation_check()
    elif Player.GetRealSkillValue('Mysticism') < 95:
        while Player.Mana >= 50:
            Spells.CastMysticism('Hail Storm')
            Target.WaitForTarget(10000, True)
            Target.Self()
            Misc.Pause(recovery)
        else:
            meditation_check()

    else:
        while Player.Mana >= 50:
            Spells.CastMysticism('Nether Cyclone')
            Target.WaitForTarget(10000, False)
            Target.TargetExecute(Player.Position.X, Player.Position.Y, Player.Position.Z)
            Misc.Pause(recovery)
        else:
            meditation_check()