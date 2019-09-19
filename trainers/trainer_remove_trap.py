#*******IMPORTANT**********
#Must Have enough magery to cast Greater Heal
#This script will only work if the player has enough tinkering skill to trap a box 
#currently tinkering skill must be raised manually
#Remove Trap     Tinkering
#   30-50           50
#   50-80           80
#   80-100          100

trapped_box = Target.PromptTarget('Target the trapped box')
key = Target.PromptTarget('Target Key for Trapped Box')

#Craft Tinkering Tools
def craft_tools():
    tool_count = 0
    for i in Player.Backpack.Contains:
        if i.ItemID is 0x1EB9:
            tool_count = tool_count + 1
        if tool_count is 1:
            while tool_count < 3:
                Items.UseItemByID(0x1EB9)
                Gumps.WaitForGump(460, 10000)
                Gumps.SendAction(460,  9003)
                Gumps.WaitForGump(460, 10000)
                Gumps.SendAction(460, 11)
                tool_count = tool_count + 1

def trap_box():
    Items.UseItemByID(0x1EB9)
    Gumps.WaitForGump(460, 10000)
    Gumps.SendAction(460,  9008)
    Gumps.WaitForGump(460, 10000)
    Gumps.SendAction(460, 400)
    Target.WaitForTarget(10000)
    Target.TargetExecute(trapped_box)
    Gumps.WaitForGump(460, 10000)
    if Gumps.LastGumpTextExist('You can only trap an unlocked object.'):
        Items.UseItem(key)
        Target.WaitForTarget(10000)
        Target.TargetExecute(trapped_box)
        Gumps.WaitForGump(460, 10000)
        Gumps.SendAction(460, 400)
        Target.WaitForTarget(10000)
        Target.TargetExecute(trapped_box)
        Gumps.WaitForGump(460, 10000)
    while Gumps.LastGumpTextExist('You failed to create the item, and some of your materials are lost.'):
        Gumps.SendAction(460, 400)
        Target.WaitForTarget(10000)
        Target.TargetExecute(trapped_box)
        Gumps.WaitForGump(460, 10000)
    Items.UseItem(key)
    Target.WaitForTarget(460, 10000)
    Target.TargetExecute(trapped_box)
    
def remove_trap():
    Journal.Clear( )
    Player.UseSkill('Remove Trap')
    if Journal.Search("That doesn't appear to be trapped"):
        trap_box()
    Target.WaitForTarget(10000)
    Target.TargetExecute(trapped_box)
    Misc.Pause(1000)
    while Journal.Search("You breathe a sigh of relief as you fail to disarm the trap but don't set it off")\
    or Journal.Search('A dart imbeds itself in your flesh'):
        if Player.Hits < Player.HitsMax:
            Spells.CastMagery('Greater Heal')
            Target.WaitForTarget(10000)
            Target.Self( )
        Misc.Pause(10000)
        Journal.Clear( )
        Player.UseSkill('Remove Trap')
        Target.WaitForTarget(10000)
        Target.TargetExecute(trapped_box)
        Misc.Pause(1000)


while Player.GetRealSkillValue('Remove Trap') <= Player.GetRealSkillValue('Tinkering')\
and Player.IsGhost is False:        
    craft_tools()
    trap_box()
    remove_trap()
    Misc.Pause(10000)
    
    
