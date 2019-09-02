#Made to be used with 100%LRC suit
#Must have spellbook with at least Weaken, Clumsy, and Feeblemind
casting_delay= 1500
while Player.GetRealSkillValue('Magic Resist') < Player.GetSkillCap('Magic Resist'):
    Spells.CastMagery('Weaken')
    Target.WaitForTarget(10000, True)
    Target.Self()
    Misc.Pause(casting_delay)
    Spells.CastMagery('Clumsy')
    Target.WaitForTarget(10000, True)
    Target.Self()
    Misc.Pause(casting_delay)
    Spells.CastMagery('Feeblemind')
    Target.WaitForTarget(10000, True)
    Target.Self()
    Misc.Pause(casting_delay)
