def meditation_check():
    while Player.Mana != Player.ManaMax:
        if Player.BuffsExist('Meditation') == False:
            Player.UseSkill('Meditation')
            Misc.Pause(7000)

           

while Player.GetRealSkillValue('Magery') < Player.GetSkillCap('Magery'):
    if Player.GetRealSkillValue('Magery') < 45:
        spell_level = 3
        while Player.Mana >= 9:
            Spells.CastMagery('Bless')
            Target.WaitForTarget(10000, True)
            Target.Self( )
            Misc.Pause(1900)
        else:
            meditation_check()
    elif Player.GetRealSkillValue('Magery') < 55:
        spell_level = 4000
        while Player.Mana >= 11:
            Spells.CastMagery('Curse')
            Target.WaitForTarget(10000, True)
            Target.Self()
            Misc.Pause(1900)
        else:
            meditation_check()
    elif Player.GetRealSkillValue('Magery') < 65:
        spell_level = 5000
        while Player.Mana >= 14:
            Spells.CastMagery('Magic Reflection')
            Target.WaitForTarget(10000, True)
            Target.Self()
            Misc.Pause(1900)
        else:
            meditation_check()
    elif Player.GetRealSkillValue('Magery') < 75:
        spell_level = 6000
        while Player.Mana >= 20:
            Spells.CastMagery('Invisibility')
            Target.WaitForTarget(10000, True)
            Target.Self()
            Misc.Pause(recovery)
        else:
            meditation_check()
    elif Player.GetRealSkillValue('Magery') < 90:
        spell_level = 7000
        while Player.Mana >= 40:
            Spells.CastMagery('Mana Vampire')
            Target.WaitForTarget(10000, True)
            Target.Self()
            Misc.Pause(2000)
        else:
            meditation_check()
    else:
        spell_level = 8000
        while Player.Mana >= 50:
            Spells.CastMagery('Earthquake')
            Misc.Pause(4300)
        else:
            meditation_check()