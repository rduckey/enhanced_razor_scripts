
bolts_to_cut = (Player.MaxWeight - Player.Weight) / 5 - 50

bolts = 0x0F95
cloth = 0x1766 
bandies =0x0E21
dragtime = 1100

bolt_container = Target.PromptTarget('Target container with Bolts of Cloth.')
bolt_container_serial = Items.FindBySerial(bolt_container)
total_bolts = Items.ContainerCount(bolt_container, bolts, -1)

Items.UseItem(bolt_container_serial)

bandies_container = Target.PromptTarget('Target container to store Bandages')
bandies_container_serial = Items.FindBySerial(bandies_container)

while total_bolts > 0:
    for i in bolt_container_serial.Contains:
        if i.ItemID == bolts:
            Items.Move(i, Player.Backpack.Serial, bolts_to_cut)
            Misc.Pause(dragtime)
    for i in Player.Backpack.Contains:
        if i.ItemID == bolts:
            Items.UseItemByID(0x0F9E, -1)
            Target.WaitForTarget(10000)
            Target.TargetExecute(i.Serial)
            Misc.Pause(dragtime)
    for c in Player.Backpack.Contains:
        if c.ItemID == cloth:
            Items.UseItemByID(0x0F9E, -1)
            Target.WaitForTarget(10000)
            Target.TargetExecute(c.Serial)
            Misc.Pause(dragtime)
    for b in Player.Backpack.Contains:
        if b.ItemID == cloth or b.ItemID == bandies:
            Items.Move(b, bandies_container_serial, 0)
            Misc.Pause(dragtime)
            total_bolts = Items.ContainerCount(bolt_container, bolts, -1)   