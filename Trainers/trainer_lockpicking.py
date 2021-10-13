stage_two_boxes = Target.PromptTarget('Target container with boxes to pick')
stage_two_boxes_serial = Items.FindBySerial(stage_two_boxes)
key = 0x176B
lockpicks = Target.PromptTarget('Target your lockpicks')
Items.UseItem(stage_two_boxes_serial)
delay = 1000
Misc.Pause(delay)
def lock_boxes():
    for i in stage_two_boxes_serial.Contains:
        if i.ItemID == 0x0E7D:
            for k in stage_two_boxes_serial.Contains:
               if k.ItemID == key:
                  Items.UseItem(k) 
                  Target.WaitForTarget(10000)
                  Target.TargetExecute(i)
                  Misc.Pause(delay)
                  
def pick_locks():
    for i in stage_two_boxes_serial.Contains:
        if i.ItemID == 0x0E7D:
            Journal.Clear()
            Items.UseItem(lockpicks)
            Target.WaitForTarget(10000)
            Target.TargetExecute(i)
            Misc.Pause(1000)
            while Journal.Search('You are unable to pick the lock'):
                Journal.Clear()
                Items.UseItem(lockpicks)
                Target.WaitForTarget(10000)
                Target.TargetExecute(i)
                Misc.Pause(1000)
while Player.GetRealSkillValue('Lockpicking') < 95:
    lock_boxes()
    pick_locks()            