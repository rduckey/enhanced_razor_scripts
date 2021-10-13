tree = Target.PromptTarget('Target the tree you wish to cut')
#set axe
axe = [0x0F49]
    
Journal.Clear( )
Items.UseItemByID(axe)
Target.TargetExecute(tree)
#while notJournal.Search('You hack at the tree for a while, but fail to produce any useable wood.')\
#or Journal.Search('You chop some ordinary logsand put them into your backpack')
while not Journal.Search("There's not enough wood here to harvest"):
    Journal.Clear( )
    Items.UseItemByID(axe)
    Target.TargetExecute(tree)
    Misc.Pause(500)