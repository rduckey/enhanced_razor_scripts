#for training pets in the Magic Resist skill
#make sure 
gainer = Target.PromptTarget('Target the pet to train Maic Resist')
casting_delay = 1000
while Player.IsGhost is False:
    Spells.CastMagery('Weaken')
    Target.WaitForTarget(10000, True)
    Target.TargetExecute(gainer)
    Misc.Pause(casting_delay)
    Spells.CastMagery('Clumsy')
    Target.WaitForTarget(10000, True)
    Target.TargetExecute(gainer)
    Misc.Pause(casting_delay)
    Spells.CastMagery('Feeblemind')
    Target.WaitForTarget(10000, True)
    Target.TargetExecute(gainer)
    Misc.Pause(casting_delay)