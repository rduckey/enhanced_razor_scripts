#Must have a bag containing the bods that you would like to fill. 

bod_bag = Target.PromptTarget('Target your BOD bag')
#ingot_container = Target.PromptTarget('Target your ingot storage')
ingot_container_serial = 0x40A0C3C2
salvage_bag = 0x42CE1AD2

Items.UseItem(bod_bag)
Misc.Pause(1200)
Items.UseItem(ingot_container_serial)
Misc.Pause(1200)
Items.UseItem(salvage_bag)


smith_hammer = 0x13E3
tinker_tools = 0x1EB9
sewing_kit = 0x0F9D
ingots = ' ' 
exceptional = ' '
number_to_make = ' '
craft = ' ' 
smith_dict = {
            'ringmail gloves':1, 'ringmail leggings':2, 'ringmail sleeves':3,
            'ringmail tunic':4, 'chainmail coif':5, 'chainmail leggings':6, 'chainmail tunic':7,
            'platemail arms':8, 'platemail gloves':9, 'platemail gorget':10, 'platemail legs':11,
            'platemail tunic':12, 'female plate':13, 'bascinet':20, 'close helmet':21, 'helmet':22,
            'norse helm':23, 'plate helm':24, 'buckler':33, 'bronze shield':34, 'heater shield':35,
            'metal shield':36, 'metal kite shield': 37, 'tear kite shield':38, 'broadsword':42,
            'cutlass':44, 'dagger':45, 'katana':46, 'kryss':47, 'longsword':48, 'scimitar':49, 
            'viking sword':50, 'axe':59, 'battle axe':60, 'double axe':61, 'executioner\'s axe':62, 
            'large battle axe':63, 'two handed axe':64, 'bardiche':66, 'halberd':69, 'short spear':72,
            'spear':74, 'war fork':75, 'hammer pick':76, 'mace':77, 'maul':78, 'war mace':80, 
            'war hammer':81
        }

metals_dict = {
            0000:5000, 2419:5001, 2406:5002, 2413:5003, 2418:5004, 
            2213:5005, 2425:5006, 2207:5007, 2219:5008
        }

def material_type():
    global ingots 
    if i.ItemID == 0x2258: 
        Items.WaitForProps(i, 5000) 
        props = Items.GetPropStringList(i) 
        metal_prop = str(props[4]) 
        if 'valorite' in metal_prop: 
            ingots = 2219
        elif 'dull' in metal_prop: 
            ingots = 2419 
        elif 'shadow' in metal_prop: 
            ingots = 2406  
        elif 'copper' in metal_prop:  
            ingots = 2413  
        elif 'bronze' in metal_prop:  
            ingots = 2418  
        elif 'gold' in metal_prop:  
            ingots = 2213  
        elif 'agapite' in metal_prop:  
            ingots = 2425  
        elif 'verite'  in metal_prop:  
            ingots = 2207  
        elif 'iron' in metal_prop: 
            ingots = 0000  
        
        
def exceptional_check():   
    global exceptional 
    Items.WaitForProps(bod, 5000) 
    props = Items.GetPropStringList(bod) 
    Misc.SendMessage(str(props[5]))
    if str(props[5]) == "exceptional": 
        exceptional = True  
    else:  
        exceptional = False        

def quantity():  
    global number_to_make 
    Items.WaitForProps(bod, 5000) 
    props = Items.GetPropStringList(bod) 
    whole_prop = props[6] 
    whole_prop_split = whole_prop.split() 
    number_to_make = whole_prop_split[3] 
       
def item_to_craft(): 
    global craft  
    Items.WaitForProps(bod, 5000) 
    props = Items.GetPropStringList(bod) 
    craftable = str(props[7]) 
    craftable_split = craftable.split(": ") 
    craft = craftable_split[0]

def change_metal():
    Misc.Pause(1200)
    Items.UseItemByID(smith_hammer, 0000)
    Gumps.WaitForGump(460, 5000)
    while Gumps.HasGump() == False:
        Items.UseItemByID(smith_hammer, 0000)
        Gumps.WaitForGump(460, 5000)
    Gumps.SendAction(460, metals_dict.get(ingots))
        
def craft_items():
    crafted = 0
    Journal.Clear()
    restock()
    Misc.Pause(1200)
    Items.UseItemByID(smith_hammer, 0000)
    Gumps.WaitForGump(460, 5000)
    while Gumps.HasGump() == False:
        Items.UseItemByID(smith_hammer, 0000)
        Gumps.WaitForGump(460, 5000)
    while crafted < int(number_to_make):
        Gumps.SendAction(460, smith_dict.get(craft))
        Gumps.WaitForGump(460, 5000)
        Misc.Pause(500)
        if exceptional == True and Gumps.LastGumpTextExist('mark') == True:
            crafted += 1
        elif exceptional == False and Gumps.LastGumpTextExist('create') == True:
            crafted += 1
        if Journal.Search('You have worn out your tool!'):
            Misc.Pause(1000)
            Journal.Clear()
            Items.UseItemByID(smith_hammer, 0000)
            Gumps.WaitForGump(460, 5000)
        restock()
        Gumps.CloseGump(460)
        
def restock():
    Misc.Pause(500)
    if Items.ContainerCount(salvage_bag, 0x1BF2, -1) < 30:
        for i in Items.FindBySerial(ingot_container_serial).Contains:
            if i.Hue == ingots and i.ItemID == 0x1BF2:
                Items.Move(i, salvage_bag, 200)

def fill_bod():
    Misc.Pause(1200)
    Items.UseItem(bod)
    Gumps.WaitForGump(456, 10000)
    Gumps.SendAction(456, 11)
    Target.WaitForTarget(10000, False)
    Target.TargetExecute(salvage_bag)

def salvage():
    Misc.Pause(1100)
    Items.SingleClick(salvage_bag)
    Misc.WaitForContext(salvage_bag, 10000)
    Misc.ContextReply(salvage_bag, 910)
    
def return_ingots():
    Misc.Pause(1100)
    for i in Player.Backpack.Contains:
        if i.ItemID == 0x1BF2:
            Items.Move(i, ingot_container_serial, 0)
            Misc.Pause(1200)
    for i in Items.FindBySerial(salvage_bag).Contains:
        if i.ItemID == 0x1BF2:
            Items.Move(i, ingot_container_serial,  0)
            Misc.Pause(1200)


            
for i in Items.FindBySerial(bod_bag).Contains: 
    if i.ItemID == 0x2258:
        bod = i.Serial
        material_type()
        exceptional_check()
        quantity()
        item_to_craft()
        Misc.SendMessage(ingots)  
        Misc.SendMessage(exceptional)
        Misc.SendMessage(number_to_make) 
        Misc.SendMessage(craft)
        change_metal()
        craft_items()
        fill_bod()
        salvage()
        return_ingots()