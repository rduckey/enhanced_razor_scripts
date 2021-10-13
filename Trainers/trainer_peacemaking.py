#Currently uses lap harp, tamborine [tassel], drums, and lute
insturments = [0x0EB3, 0x0E9E, 0x0E9C, 0x0EB2, 0x0E9D]

def make_music():
    for i in insturments:
        Items.UseItemByID(i)
        Misc.Pause(1100)
def peacemaking():
    
        for e in Player.Backpack.Contains:
            if e.ItemID in insturments:
                Items.UseItem(e)
                Player.UseSkill('Peacemaking')
                Target.WaitForTarget(10000)
                Target.Self()
                
def target_insturment():
    if Journal.Search('play the music on'):
        Target.WaitForTarget(10000, True)
        for i in Player.Backpack.Contains:
            if i.ItemID in insturments:
                Target.TargetExecute(i)
    Journal.Clear()
    
def mastery():

    Spells.CastMastery('Resilience')
    Misc.Pause(2000)
    target_insturment()
    
            
while Player.GetRealSkillValue('Musicianship') < 50:
    for i in insturments:
        Items.UseItemByID(i)
        Misc.Pause(1100)
while Player.GetRealSkillValue('Peacemaking') < Player.GetSkillCap('Peacemaking'):
    #peacemaking()
    mastery()

        
