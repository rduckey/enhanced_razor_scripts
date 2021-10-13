animal = Target.PromptTarget("Target the creature you would like to tame")

def taming():
    Player.UseSkill("Animal Taming")
    Target.WaitForTarget(10000, False)
    Target.TargetExecute(animal)
    Misc.Pause(6000)

Journal.Clear()
taming()
if Journal.GetLineText("You fail to tame the creature"):
    Journal.Clear()
    taming()
