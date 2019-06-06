#uses Combat Training to raise Animal Taming skill


while Player.GetRealSkillValue('Animal Taming') < Player.GetSkillCap('Animal Taming'):
    if Player.Mana >= 24:
        Spells.CastMastery('Combat Training')
        Target.WaitForTarget(10000,False)
        Target.Last()
        Misc.Pause(1000)
    else:
      Player.UseSkill('Meditation')
    while Player.Mana != Player.ManaMax:
        if Journal.GetLineText('You cannot focus your concentration'):
            Misc.Pause(10000)
            Player.UseSkill('Meditation')
