while Player.GetRealSkillValue('Animal Taming') < Player.GetSkillCap('Animal Taming'):
    if Player.Mana >= 24:
        Spells.CastMastery('Combat Training')
        Target.WaitForTarget(10000,False)
        Target.Last()
        Misc.Pause(1000)
    else:
        while Player.Mana != Player.ManaMax:
            Player.UseSkill('Meditation')
            if Player.Mana != Player.ManaMax:
                Misc.Pause(11000)
            else:
                break