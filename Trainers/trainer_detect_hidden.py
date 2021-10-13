#lock down trapped box in house and move away from it as difficulty decreases

#set to serial of trapped box
trapped_box = 0x4180D791

while Player.GetSkillCap("Detect Hidden") > Player.GetRealSkillValue("Detect Hidden"):
    Player.UseSkill("Detect Hidden")
    Target.WaitForTarget(10000, True)
    Target.TargetExecute(trapped_box)
    Misc.Pause(11000)