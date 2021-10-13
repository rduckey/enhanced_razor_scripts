corpse= Target.PromptTarget('Target the corpse')
corpse_serial= Items.FindBySerial(corpse)
drag_time= 1000

for loot in corpse_serial.Contains:
    if 'Legendary Artifact' in Items.GetPropStringList(loot):
        Items.Move(loot, Player.Backpack.Serial, 0)
        Misc.Pause(drag_time)