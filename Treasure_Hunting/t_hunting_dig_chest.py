#must be run from the top left of the maps Coords

delay = 1200
map = Target.PromptTarget('Please target the map that you are using') 

Journal.Clear()

def journal_check():
    Misc.Pause(delay)
    if Journal.Search('You dig and dig but fail to find any treasure.'):
        Journal.Clear()
    else:
        exit()


def east_move():
    player_position = Player.Position
    move = PathFinding.Route()
    move.MaxRetry = 20
    move.StopIfStuck = True
    move.X = player_position.X + 3
    move.Y = player_position.Y
    PathFinding.Go(move)
    
def south_move():
    player_position = Player.Position
    move = PathFinding.Route()
    move.MaxRetry = 20
    move.StopIfStuck = True
    move.X = player_position.X
    move.Y = player_position.Y + 3
    PathFinding.Go(move)
    
def west_move():
    player_position = Player.Position
    move = PathFinding.Route()
    move.MaxRetry = 20
    move.StopIfStuck = True
    move.X = player_position.X - 3
    move.Y = player_position.Y
    PathFinding.Go(move)    

def digging():
    Items.UseItemByID(0x0F39)
    Target.WaitForTarget(10000, True)
    Target.TargetExecute(map)
    Target.WaitForTarget(10000, True)
    Target.TargetExecute(Player.Position.X, Player.Position.Y, Player.Position.Z)

digging()
journal_check()
for x in range(0, 5):
    east_move()
    digging()
    journal_check()
south_move()
digging()
journal_check()
for x in range(0, 5):
    west_move()
    digging()
    journal_check()
south_move()
digging()
journal_check()
for x in range(0, 5):
    east_move()
    digging()
    journal_check()
south_move()
digging()
journal_check()
for x in range(0, 5):
    west_move()
    digging()
    journal_check()