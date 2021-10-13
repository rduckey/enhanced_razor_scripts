pet = Target.PromptTarget('Please target the pet that you would like to use for traiing')
while Player.GetRealSkillValue('Animal Lore') < Player.GetSkillCap('Animal Lore'):
    Player.UseSkill('Animal Lore')
    Target.WaitForTarget(10000, True)
    Target.TargetExecute(pet)
    Misc.Pause(1000)
    

    Gumps.CloseGump(Gumps.CurrentGump())
        
         