#Runebooks MUST be dyed using the top option of the Blue Tab
#Must Create Buy Agent list and include Blank Scrolls
home_runebook_serial = 0x4100F093
scroll_bag = 0x422611DF
beetle = 0x0282C31D

blank_scrolls = 0x0EF3
BuyAgent.Enable()

def scroll_dump():
    if  Player.Weight > Player.MaxWeight - 200:
        home_runebook_properties = Items.GetPropStringList(home_runebook_serial)
        home_title = home_runebook_properties[5]
        home_title_list = home_title.split()
        home_rune = home_title_list[1]
        recall_response = 49 + int(home_rune)
        Items.UseItem(home_runebook_serial)
        Gumps.WaitForGump(89, 10000)
        Gumps.SendAction(89, recall_response)
        Misc.Pause(4000)
        for i in Player.Backpack.Contains:
            if i.ItemID == blank_scrolls:
                Items.Move(i, scroll_bag, 0)
                Misc.Pause(2000)
                
def overweight():
    if Player.Weight > Player.MaxWeight:
        for s in Player.Backpack.Contains:
            if s.ItemID == blankscrolls:
                if Player.Mount:
                    Mobiles.UseMobile(Player.Serial)
                    Misc.Pause(dragTime)
                Items.Move(s, beetle, 0)
                Misc.Pause(1200)
                if not Player.Mount:
                    Mobiles.UseMobile(beetle)
                    Misc.Pause(1200)
        home_runebook_properties = Items.GetPropStringList(home_runebook_serial)
        home_title = home_runebook_properties[5]
        home_title_list = home_title.split()
        home_rune = home_title_list[1]
        recall_response = 49 + int(home_rune)
        Items.UseItem(home_runebook_serial)
        Gumps.WaitForGump(89, 10000)
        Gumps.SendAction(89, recall_response)
        Misc.Pause(4000)                    
                    

while Player.IsGhost == False:
    for i in Player.Backpack.Contains:
        if i.ItemID == 0x22C5 and i.Hue == 2122:
            book = Items.GetPropStringList(i)
            book_title = book[5]
            title_list = book_title.split()
            runes = title_list[1]
            recalls = 1
            gump_action = 50
            while recalls < int(runes):
                Journal.Clear()
                Items.UseItem(i)
                Gumps.WaitForGump(89, 5000)
                while Gumps.HasGump() == False:
                    Items.UseItem(i)
                    Gumps.WaitForGump(89, 5000)
                Gumps.SendAction(89, gump_action)
                Misc.Pause(4000)
                while Journal.GetLineText('blocking') or Journal.GetLineText('teleport'):
                    recalls += 1
                    gump_action += 1
                    Journal.Clear()
                    Items.UseItem(i)
                    Gumps.WaitForGump(89, 5000)
                    while Gumps.HasGump() == False:
                        Items.UseItem(i)
                        Gumps.WaitForGump(89, 5000)
                    Gumps.SendAction(89, gump_action)
                    Misc.Pause(4000)
                Player.ChatSay(1, 'Vendor Buy')
                recalls += 1
                gump_action+= 1
                Misc.Pause(1000)
                scroll_dump()
                if Player.Weight > Player.MaxWeight:
                    Spells.CastMagery('Bless')
                    Target.WaitForTarget(10000, False)
                    Target.Self()
                    Misc.Pause(1000)
                    
    Misc.Pause(300000)