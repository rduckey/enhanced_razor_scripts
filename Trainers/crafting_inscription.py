def meditation_check():
    while Player.Mana != Player.ManaMax:
        if Player.BuffsExist('Meditation') == False:
            Player.UseSkill('Meditation')
            Misc.Pause(7000)
            
while Player.GetRealSkillValue('Inscribe') < Player.GetSkillCap('Inscribe'):               
    Items.UseItemByID(0x0FBF)
    Journal.Clear()             
        while Player.Mana > 50:
            if not Journal.Search('You have worn out your tool!'):
                Gumps.WaitForGump(1113623231,2000)
                #Summon Air Elemental
                #Gumps.SendAction(460, 60)
                #Resurrection
                Gumps.SendAction(460,59)
                Gumps.WaitForGump(1113623231,3000)
            else:
                Items.UseItemByID(0x0FBF)
                Journal.Clear()
        if Player.Mana < 50:
            meditation_check()