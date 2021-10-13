arrows = Items.FindByID(0x0F3F,-1,Player.Backpack)
quiver = Items.FindByID(0x413DCF26)
while Player.IsGhost is False:
    if Items.GetPropValue(quiver,'Ammo') == 0:
        Items.Move(arrows,quiver,200)
        Misc.Pause(1000)
    else:
        Misc.NoOperation()