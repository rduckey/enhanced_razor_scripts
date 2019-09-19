#Currently uses lap harp, tamborine [tassel], drums, and lute
insturments = [0x0EB3, 0x0E9E, 0x0E9C, 0x0EB2]
while Player.GetRealSkillValue('Musicianship') < 50:
    for i in insturments:
        Items.UseItemByID(i)
        Misc.Pause(1100)

while Player.GetRealSkillValue('Peacemaking') < Player.GetSkillCap('Peacemaking'):
    for e in Player.Backpack.Contains:
        if e.ItemID in insturments:
            Items.UseItem(e)
        Player.UseSkill('Peacemaking')
        Target.WaitForTarget(10000)
        Target.Self()
        Misc.Pause(9000)
   