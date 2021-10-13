pet = Target.PromptTarget('Target Pet')
pet_serial = Mobiles.FindBySerial(pet)

while Player.IsGhost is False:
    if pet_serial.Poisoned is True:
        Spells.CastMagery('Arch Cure')
        Target.WaitForTarget(10000, True)
        Target.TargetExecute(pet_serial)
        Misc.Pause(1200)
    elif pet_serial.Hits < .9 * pet_serial.HitsMax:
        Spells.CastMagery("Greater Heal")
        Target.WaitForTarget(10000, False)
        Target.TargetExecute(pet_serial)
        Misc.Pause(800)