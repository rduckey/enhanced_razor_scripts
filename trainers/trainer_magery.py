
#change delay between casting spells based on personal Faster Cast Recovery
recovery = 1300

def meditation_check():
    Player.UseSkill('Meditation')
    while Player.Mana != Player.ManaMax:
        if Journal.GetLineText('You cannot focus your concentration'):
            Misc.Pause(6000)
            Player.UseSkill('Meditation')
            Misc.Pause(6000)
           

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
