#Currently uses lap harp, tamborine [tassel], drums, and lute
insturments = [0x0EB3, 0x0E9E, 0x0E9C, 0x0EB2, 0x0E9D]


def target_insturment():
    if Journal.Search('play'):
        Target.WaitForTarget(10000, True)
        for i in Player.Backpack.Contains:
            if i.ItemID in insturments:
                Target.TargetExecute(i)
                Misc.Pause(1200)
                Items.UseItem(i)
    Journal.Clear()

def mastery():
    Spells.CastMastery('Tribulation')
    Misc.Pause(1000)
    target_insturment()
    Target.WaitForTarget(3000, True)
    Target.Self()
    Misc.Pause(2000)
    Spells.CastMastery('Tribulation')
    Misc.Pause(2000)
    
def disco():
    Player.UseSkill('Discordance')
    target_insturment()
    Target.WaitForTarget(10000, False)
    Target.Self()
    Misc.Pause(7000)
    
while Player.GetSkillValue('Discordance') < Player.GetSkillCap('Discordance'):    
    #disco()
    mastery()