#################################################
#SETUP                                          #
#WARNING!!!! If you do  not set master_spellbook#
#to the serial of the spellbook containing all  #
#of your spells this script WILL trash it.      #
master_spellbook = 0x41761718                   #                        
trash = 0x433B5553                              #
#################################################
pen = 0x0FBF
blank_scrolls = 0x0EF3
slayers = ['elemental slayer', 'demon slayer', 'fey slayer', 'reptile slayer', 'dragon slayer', 'snake slayer',
'arachnid slayer', 'scorpion slayer', 'spider slayer', 'repond slayer', 'undead slayer', 'vermin slayer',
'air elemental slayer', 'terathan slayer', 'ophidian slayer', 'blood elemental slayer', 'fire elemental slayer',
'water elemental slayer', 'dinosaur slayer', 'eodon slayer', 'mymridex slayer']


supply_container = Target.PromptTarget('Target container with supplies.')
supply_container_serial = Items.FindBySerial(supply_container)
Items.UseItem(supply_container)
slayer_container = Target.PromptTarget('Target container to store slayer books.')
slayer_container_serial = Items.FindBySerial(slayer_container)
Items.UseItem(slayer_container)
three_prop_container = Target.PromptTarget('Target container to store 3 property books.')
three_prop_container_serial = Items.FindBySerial(three_prop_container)
Items.UseItem(three_prop_container)
Misc.Pause(1200)



def restock():
    if Items.BackpackCount(blank_scrolls, -1) < 10:
        for i in supply_container_serial.Contains:
            if i.ItemID == blank_scrolls:
                Items.Move(i, Player.Backpack.Serial, 200)
    if Journal.Search('You have worn out your tool!'):
        Journal.Clear()
        for i in supply_container_serial.Contains:
            if i.ItemID == pen:
                Items.Move(i, Player.Backpack.Serial, 0)
                Items.UseItemByID(pen)
            break    

def craft_spellbook():
    Journal.Clear()
    restock()
    Items.UseItemByID(pen)
    Gumps.WaitForGump(460, 3000)
    Gumps.SendAction(460, 202)
    Gumps.WaitForGump(460, 3000)
    restock()
    while Gumps.LastGumpTextExist('You failed to create the item, and some of your materials are lost.'):
        Gumps.WaitForGump(460, 3000)
        Gumps.SendAction(460, 202)
        Gumps.WaitForGump(460, 3000)
        restock()
        
def three_property_check():
    for i in Player.Backpack.Contains:
        if i.ItemID == 0x0EFA:
            if i.Serial != master_spellbook:
                Items.WaitForProps(i, 5000)
                props = Items.GetPropStringList(i)
                Misc.Pause(100)
                if len(props) == 8:
                    Items.Move(i, three_prop_container_serial, 0)
                    Misc.Pause(1200)    
        
def slayer_check():
    for i in Player.Backpack.Contains:
        if i.ItemID == 0x0EFA:
            if i.Serial != master_spellbook:
                Items.WaitForProps(i, 5000)
                props = Items.GetPropStringList(i)
                Misc.Pause(100)
                for prop in props:
                    Misc.SendMessage(str(prop))
                    if prop in slayers:
                        Items.Move(i, slayer_container_serial, 0)
                        Misc.Pause(1200)
                   
def sdi():
    value = ''
    for i in Player.Backpack.Contains:
        if 'spell damage increase' in i:
            print('found')
            for c in i:
                if c.isdigit():
                    print(c)
                    value += c
            return int(value)
                        
def trash_books():
    for i in Player.Backpack.Contains:
        if i.ItemID == 0x0EFA:
            if i.Serial != master_spellbook:
                Items.Move(i, trash, 0)
                Misc.Pause(1200)

while Items.ContainerCount(supply_container_serial, blank_scrolls, -1) > 0\
or Items.BackpackCount(blank_scrolls, -1) > 10:
    craft_spellbook()
    three_property_check()
    slayer_check()  
    trash_books()
