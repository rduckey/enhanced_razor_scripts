import time
target= Target.PromptTarget()
while Player.GetSkillValue("EvalInt") < 100:
    Player.UseSkill("Eval Int")
    Target.WaitForTarget(15000, True)
    Target.TargetExecute(target)
    time.sleep(1.5)
