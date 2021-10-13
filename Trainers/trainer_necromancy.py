def meditation_check():
    Misc.Pause(1000)
    Player.UseSkill('Meditation')
    Misc.Pause(1000)
    if Player.Mana != Player.ManaMax:
        while Player.Mana != Player.ManaMax:
            if Player.BuffsExist('Meditation') is False:
                Misc.Pause(6000)
                Player.UseSkill('Meditation')

           
while Player.GetRealSkillValue('Necromancy') < Player.GetSkillCap('Necromancy'):
    if Player.GetRealSkillValue('Necromancy') < 50:
        spell_level = 3
        while Player.Mana >= 11:
            Spells.CastNecro('Corpse Skin')
            Target.WaitForTarget(10000, True)
            Target.Self( )
            Misc.Pause(1900)
        else:
            meditation_check()
    elif Player.GetRealSkillValue('Necromancy') < 70:
        spell_level = 4000
        while Player.Mana >= 11:
            Spells.CastNecro('Horrific Beast')
            Misc.Pause(1800)
        else:
            meditation_check()
    elif Player.GetRealSkillValue('Necromancy') < 90:
        spell_level = 5000
        while Player.Mana >= 23:
            Spells.CastNecro('Wither')
            Misc.Pause(1900)
        else:
            meditation_check()
    elif Player.GetRealSkillValue('Necromancy') < 100:
        spell_level = 6000
        while Player.Mana >= 23:
            Spells.CastNecro('Lich Form')
            Misc.Pause(4000)
            if Player.Hits < Player.HitsMax *.3:
                Spells.CastMagery('Greater Heal')
                Target.WaitForTarget(10000, True)
                Target.Self()
                Misc.Pause(3000)
        else:
            meditation_check()
    else:
        spell_level = 8000
        while Player.BuffsExist('Lich Form'):
            Spells.CastNecro('Lich Form')
            Misc.Pause(3000)
        while Player.Mana >= 23:
            Spells.CastNecro('Vampiric Embrace')
            Misc.Pause(4300)
        else:
            meditation_check()