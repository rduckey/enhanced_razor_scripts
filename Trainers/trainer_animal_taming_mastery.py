
pet = Target.PromptTarget('Target the pet that you want to use for training')

def meditation_check():
    Misc.Pause(1000)
    Player.UseSkill('Meditation')
    Misc.Pause(1000)
    if Player.Mana != Player.ManaMax:
        while Player.Mana != Player.ManaMax:
            if Player.BuffsExist('Meditation') is False:
                Misc.Pause(6000)
                Player.UseSkill('Meditation')

while Player.GetRealSkillValue('Animal Taming') < Player.GetSkillCap('Animal Taming'):
    if Player.Mana >= 40:
        Spells.CastMastery('Combat Training')
        Target.WaitForTarget(11000,True)
        Target.TargetExecute(pet)
        Misc.Pause(2000)
    else:
           meditation_check()