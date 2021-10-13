trash = Target.PromptTarget("Target the trash can you would like to use")

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

def too_many_items()
    count = 0
    for i in Player.Backpack.Contains:
        count = count + 1
        if count = 125:
            for i in Player.Backpack.Contains:
                if i.ItemID = [0x0F9E, 0x0FBC]
        

while Player.GetRealSkillValue('Tinkering') < 45:
    craft_tools()
    Items.UseItemByID(0x1EB9)
    Gumps.WaitForGump(460, 10000)
    Gumps.SendAction(460,  9003)
    Gumps.WaitForGump(460, 10000)
    Gumps.SendAction(460, 8)
    