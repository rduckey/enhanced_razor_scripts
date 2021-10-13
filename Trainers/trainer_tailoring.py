#requires enough tinkering skill to craft sewing kits
#In backpack to start must have tinker tools, scissors
#Resource container must include cloth and ingots
#Will store the bandages created from cutting up oil rags in the resource container
resource_container = Target.PromptTarget('Target the container with your resources') 
container_resources = Items.FindBySerial(resource_container)
Items.UseItem(container_resources)
sewing_kit_count = 0
tinker_tool_count = 0
cloth = 0
ingots = 0
craft_ids = [0x4060, 0x4064, 0x175D, 0x2797, 0x2798, 0x1F03, 0x2307, 0x1515, 0x2309, 0x152E]

def check_resources():
    global ingots, cloth
    ingots = Items.ContainerCount(container_resources, 0x1BF2, -1)
    cloth = Items.ContainerCount(container_resources, 0x1766, -1)
    for i in container_resources.Contains:
        if Items.BackpackCount(0x1BF2, -1) < 5:
            if i.ItemID == 0x1BF2:
                Items.Move(i, Player.Backpack, 20)
                Misc.Pause(1100)
    Misc.Pause(1200)
    for i in container_resources.Contains:
        if Items.BackpackCount(0x1766, -1) < 20:
            if i.ItemID == 0x1766:
                Items.Move(i, Player.Backpack, 500)
                Misc.Pause(1100)
    return ingots, cloth

def craft_tools():
    global sewing_kit_count, tinker_tool_count
    sewing_kit_count = Items.BackpackCount(0x0F9D, -1)
    tinker_tool_count = Items.BackpackCount(0x1EB9, -1)
#Craft Tinker Tools
    if tinker_tool_count == 1:
        while tinker_tool_count < 2:
            Items.UseItemByID(0x1EB9, -1)
            Gumps.WaitForGump(460, 3000)
            Gumps.SendAction(460, 11)
            Gumps.WaitForGump(460, 3000)
            tinker_tool_count = Items.BackpackCount(0x1EB9, -1)
            Misc.Pause(1100)
            check_resources()
            tinker_tool_count += 1
#Craft Sewing Kits
    if sewing_kit_count == 0:
        while sewing_kit_count < 5:
            Items.UseItemByID(0x1EB9, -1)
            Gumps.WaitForGump(460, 3000)
            Gumps.SendAction(460, 14)
            Gumps.WaitForGump(460, 3000)
            sewing_kit_count = Items.BackpackCount(0x0F9D, -1)
            Misc.Pause(1100)
            check_resources()
    return sewing_kit_count, tinker_tool_count
    
def recover_cloth():
    Misc.Pause(1000)
    for i in Player.Backpack.Contains:
        if i.ItemID in craft_ids:
           Items.UseItemByID(0x0F9E, -1)
           Target.WaitForTarget(3000)
           Target.TargetExecute(i)
           Misc.Pause(1100)

################################################################################
if Player.GetSkillValue('Tailoring') < 29:
    Misc.SendMessage('Go train skill up to 29')
    exit()

while Player.GetSkillValue('Tailoring') < Player.GetSkillCap('Tailoring'):
#Craft Short Pants
    while Player.GetSkillValue('Tailoring') <= 35:
        check_resources()
        craft_tools()
        Items.UseItemByID(0x0F9D)
        Journal.Clear()             
        if not Journal.Search('You have worn out your tool!'):
            Gumps.WaitForGump(460,2000)
            Gumps.SendAction(460,37)
            Gumps.WaitForGump(460,3000)
        else:
            Items.UseItemByID(0x0F9D)
            Journal.Clear()
        recover_cloth()
        
#Craft Fur Cape           
    while Player.GetSkillValue('Tailoring') <= 41.4:
        check_resources()
        craft_tools()
        Items.UseItemByID(0x0F9D)
        Journal.Clear()             
        if not Journal.Search('You have worn out your tool!'):
            Gumps.WaitForGump(460,2000)
            Gumps.SendAction(460,28)
            Gumps.WaitForGump(460,3000)
        else:
            Items.UseItemByID(0x0F9D)
            Journal.Clear()
        recover_cloth()
        
#Craft Cloaks           
    while Player.GetSkillValue('Tailoring') <= 50:
        check_resources()
        craft_tools()
        Items.UseItemByID(0x0F9D)
        Journal.Clear()             
        if not Journal.Search('You have worn out your tool!'):
            Gumps.WaitForGump(460,2000)
            Gumps.SendAction(460,25)
            Gumps.WaitForGump(460,3000)
        else:
            Items.UseItemByID(0x0F9D)
            Journal.Clear()
        recover_cloth()
#Craft Fur Boots           
    while Player.GetSkillValue('Tailoring') <= 54:
        check_resources()
        craft_tools()    
        Items.UseItemByID(0x0F9D)
        Journal.Clear()             
        if not Journal.Search('You have worn out your tool!'):
            Gumps.WaitForGump(460,2000)
            Gumps.SendAction(460,601)
            Gumps.WaitForGump(460,3000)
        else:
            Items.UseItemByID(0x0F9D)
            Journal.Clear()
        recover_cloth()
        
#Craft Robes           
    while Player.GetSkillValue('Tailoring') <= 65:
        check_resources()
        craft_tools()
        Items.UseItemByID(0x0F9D)
        Journal.Clear()             
        if not Journal.Search('You have worn out your tool!'):
            Gumps.WaitForGump(460,2000)
            Gumps.SendAction(460,26)
            Gumps.WaitForGump(460,3000)
        else:
            Items.UseItemByID(0x0F9D)
            Journal.Clear()
        recover_cloth()
        
#Craft Kasa           
    while Player.GetSkillValue('Tailoring') <= 72:
        check_resources()
        craft_tools()
        Items.UseItemByID(0x0F9D)
        Journal.Clear()             
        if not Journal.Search('You have worn out your tool!'):
            Gumps.WaitForGump(460,2000)
            Gumps.SendAction(460,17)
            Gumps.WaitForGump(460,3000)
        else:
            Items.UseItemByID(0x0F9D)
            Journal.Clear()
        recover_cloth()
        
#Craft Ninja Tabi           
    while Player.GetSkillValue('Tailoring') <= 78:
        check_resources()
        craft_tools()
        Items.UseItemByID(0x0F9D)
        Journal.Clear()             
        if not Journal.Search('You have worn out your tool!'):
            Gumps.WaitForGump(460,2000)
            Gumps.SendAction(460,602)
            Gumps.WaitForGump(460,3000)
        else:
            Items.UseItemByID(0x0F9D)
            Journal.Clear()
        recover_cloth()
        
#Craft Oil Cloth          
    while Player.GetSkillValue('Tailoring') <= 99:
        check_resources()
        craft_tools()
        Items.UseItemByID(0x0F9D)
        Journal.Clear()             
        if not Journal.Search('You have worn out your tool!'):
            Gumps.WaitForGump(460,2000)
            Gumps.SendAction(460,500)
            Gumps.WaitForGump(460,3000)
        else:
            Items.UseItemByID(0x0F9D)
            Journal.Clear()            
#Cut Oil Rags into bandages and store in resources container
        recover_cloth()
        for b in Player.Backpack.Contains:
            if b.ItemID == 0x0E21:
                Items.Move(b, resource_container, 0)
                    
#Craft Gargish Cloth Kilt         
    while Player.GetSkillValue('Tailoring') <= 117:
        check_resources()
        craft_tools()
        Items.UseItemByID(0x0F9D)
        Journal.Clear()             
        if not Journal.Search('You have worn out your tool!'):
            Gumps.WaitForGump(460,2000)
            Gumps.SendAction(460,207)
            Gumps.WaitForGump(460,3000)
        else:
            Items.UseItemByID(0x0F9D)
            Journal.Clear()
        recover_cloth()       
        
#Craft Gargish Cloth Arms         
    while Player.GetSkillValue('Tailoring') <= 117:
        check_resources()
        craft_tools()
        Items.UseItemByID(0x0F9D)
        Journal.Clear()             
        if not Journal.Search('You have worn out your tool!'):
            Gumps.WaitForGump(460,2000)
            Gumps.SendAction(460,200)
            Gumps.WaitForGump(460,3000)
        else:
            Items.UseItemByID(0x0F9D)
            Journal.Clear()
        recover_cloth()               