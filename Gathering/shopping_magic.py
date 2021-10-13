beetle = 0x0282C31D
resources = [0x0F7A,0x0F86,0x0F88,0x0F8C,0x0F85,0x0F84,0x0F8D,0x0F7B,0x0EF3]


for s in Player.Backpack.Contains:
        if s.ItemID in resources:
           Items.Move(s, beetle, 0)
           Misc.Pause(1200)
            