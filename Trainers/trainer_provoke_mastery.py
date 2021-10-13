#Currently uses lap harp, tamborine [tassel], drums, and lute
insturments = [0x0EB3, 0x0E9E, 0x0E9C, 0x0EB2, 0x0E9D]

while Player.GetSkillValue("Provocation") < Player.GetSkillCap("Provocation"):
    Spells.CastMastery("Invigorate")
    Misc.Pause(1000)
    if Journal.Search('play'):
        Target.WaitForTarget(10000, True)
        for i in Player.Backpack.Contains:
            if i.ItemID in insturments:
                Target.TargetExecute(i)
                Misc.Pause(1200)
                Items.UseItem(i)
    Journal.Clear()

    