
#change delay between casting spells based on personal Faster Cast Recovery
recovery = 5000

def meditation_check():
    Misc.Pause(1000)
    Player.UseSkill('Meditation')
    Misc.Pause(1000)
    if Player.Mana != Player.ManaMax:
        while Player.Mana != Player.ManaMax:
            if Player.BuffsExist('Meditation') is False:
                Misc.Pause(6000)
                Player.UseSkill('Meditation')

           

while Player.GetRealSkillValue('Magery') < Player.GetSkillCap('Magery'):
    if Player.GetRealSkillValue('Magery') < 45:
        while Player.Mana >= 9:
            Spells.CastMagery('Bless')
            Target.WaitForTarget(10000, True)
            Target.Self()
            Misc.Pause(recovery)
        else:
            meditation_check()
    elif Player.GetRealSkillValue('Magery') < 55:
        while Player.Mana >= 11:
            Spells.CastMagery('Curse')
            Target.WaitForTarget(10000, True)
            Target.Self()
            Misc.Pause(recovery)
        else:
            meditation_check()
    elif Player.GetRealSkillValue('Magery') < 65:
        while Player.Mana >= 14:
            Spells.CastMagery('Magic Reflection')
            Target.WaitForTarget(10000, True)
            Target.Self()
            Misc.Pause(recovery)
        else:
            meditation_check()
    elif Player.GetRealSkillValue('Magery') < 75:
        while Player.Mana >= 20:
            Spells.CastMagery('Invisibility')
            Target.WaitForTarget(10000, True)
            Target.Self()
            Misc.Pause(recovery)
        else:
            meditation_check()
    elif Player.GetRealSkillValue('Magery') < 90:
        while Player.Mana >= 40:
            Spells.CastMagery('Mana Vampire')
            Target.WaitForTarget(10000, True)
            Target.Self()
            Misc.Pause(recovery)
        else:
            meditation_check()
    else:
        while Player.Mana >= 50:
            Spells.CastMagery('Earthquake')
            Misc.Pause(recovery)
        else:
            meditation_check()