
import time

import sys

import math

#
#from System import Environment
#from System import EnvironmentVariableTarget
#home = Environment.GetEnvironmentVariable('USERPROFILE', EnvironmentVariableTarget.Process);
#path = home+'\\Desktop\\Razor/Scripts'
#Misc.SendMessage(path)
#sys.path.append(path)
#


import common
common.Player = Player
common.Items = Items
common.Mobiles = Mobiles
common.Misc = Misc
common.Journal = Journal
common.Statics = Statics
common.Gumps = Gumps
common.Spells = Spells
common.BandageHeal = BandageHeal
from common import MakeTinkerKits



tinker_kitsID = 0x1EB8
fletching_kitsID =  0x1022  
woodID = 0x1BD7
woodStorage = 0x44046D13
shaftID = 0x1BD4
metalID = 0x1BF2
BankRune = 0x42626C3C
LastLocRune = 0x4261E60B
StartX = 4432
EndX = 4546
StartY = 1378
EndY = 1471



from System.Collections.Generic import List
from System import Byte, Int32
#
#
Packhorse = None  # 0x00B0C1E5
findPack = Mobiles.Filter()
findPack.Enabled = True
findPack.RangeMax = 2
findPack.Bodies = List[int]((0x0123))
listPack = Mobiles.ApplyFilter(findPack)
if len(listPack) > 0:
    for i in listPack:
        Packhorse = listPack[0]
        Misc.SendMessage("Pack is 0x{:x}".format(Packhorse.Serial))
else:
    Misc.SendMessage("NO PACK HORSE")
    Packhorse = Mobiles.FindBySerial(0x00B0C1E5)
#


def MarkRune(rune):
    Journal.Clear()
    Spells.CastMagery("Mark")
    Target.WaitForTarget(4000)
    Target.TargetExecute(rune)
    Misc.Pause(1000)
    if Journal.Search("fizzles"):
        Misc.Pause(3000)
        MarkRune(rune)
#    


def RecallRune(rune):
    Journal.Clear()
    Spells.CastMagery("Recall")
    Target.WaitForTarget(4000)
    Target.TargetExecute(rune)
    Misc.Pause(1000)
    if Journal.Search("fizzles"):
        Misc.Pause(3000)
        RecallRune(rune)
#


def DepositItems():
    BankStorage = 0x4B23F910
    Mobiles.UseMobile(Packhorse)
    Misc.Pause(1000)
    Player.ChatSay(52, "bank")
    Misc.Pause(500)
    moveItemList = [0x1BD7, 0x3191, 0x3190, 0x2F5F,  0x318F]
    for item in Player.Backpack.Contains:
        if item.ItemID in moveItemList:
            Items.Move(item, BankStorage, 0)
            Misc.Pause(1000)
    while Mobiles.GetPropValue(Packhorse, "Weight") > 200: 
        Mobiles.UseMobile(Packhorse)
        Mobiles.WaitForProps(Packhorse, 5000)
        Misc.Pause(1000) 
        moveList = common.findRecursive(0x4BF00462, moveItemList)
        for item in moveList:
            Misc.SendMessage(str(item))
            Items.Move(item, BankStorage, 0)
            Misc.Pause(1000)               
 
Misc.ClearIgnore()
#for i in range(10):
#    Misc.SendMessage(str(i), i)
#    w_r = Player.GetItemOnLayer('RightHand')
#    #Misc.SendMessage("right={}".format(w_r))
#    w_l = Player.GetItemOnLayer('LeftHand')
#    #Misc.SendMessage("left={}".format(w_l))
#    if w_l != None: 
#       weapon = w_l
#    elif w_r != None:    
#       weapon = w_r
#    else:
#       weapon = None
#    props = weapon.Properties
#Journal.Clear()

def NearestCalc(itemList):
    if len(itemList) == 0:
        return None
    min_distance_item = None
    min_distance = 99999
    for i in itemList:
        dist = math.sqrt(((Player.Position.X - i.Position.X)**2) + ((Player.Position.Y - i.Position.Y)**2) )
        if dist < min_distance:
            min_distance = dist
            min_distance_item = i            
    Misc.SendMessage("dist: {} item: 0x{:x}".format(min_distance, min_distance_item.Serial), 5)
    return min_distance_item


def FindAxe():
    axe = Items.FindByID(0x0F43, 0, Player.Backpack.Serial)
    if None != axe:
        Items.UseItem(axe)
    else:
        if Items.BackpackCount(tinker_kitsID, 0) < 2:
            common.MakeTinkerKits()        
            Misc.Pause(1000)
            if Items.BackpackCount(tinker_kitsID, 0) < 2:
                Misc.SendMessage("Could not make tinker kits")
                return
        while Items.BackpackCount(0x0F43) < 4:        
            common.MakeHatchet()
            Misc.Pause(1000)
        axe = Items.FindByID(0x0F43, 0, Player.Backpack.Serial)        


def FindTrees():
    TreeStaticID = List[int]((0xc95, 0xc96, 0xc99, 0xc9b, 0xc9c, 0xc9D, 0xc8a, 0xca6, 0xca8, 
    0xcaa, 0xcab, 0xcc3, 0xcc4, 0xcc8, 0xcc9, 0xcca, 0xccb, 0xccc, 0xccd, 0xcd0, 0xcd1, 0xcd3, 0xcd6, 0xcd8, 
    0xcda, 0xcdd, 0xce0, 0xce3, 0xce6, 0xcf8, 0xcf8, 0xcfe, 0xd01, 0xd25, 0xd27, 0xd35, 0xd37, 0xd38, 
    0xd42, 0xd43, 0xd59, 0xd70, 0xd85, 0xd94, 0xd96, 0xd98, 0xd9a, 0xd9c, 0xd9e, 0xda0, 0xda2, 0xda04, 0xda8))
    findTrees = Items.Filter()
    findTrees.Enabled = True
    findTrees.OnGround = 1
    findTrees.Movable = False
    findTrees.RangeMin = -1
    findTrees.RangeMax = 16
    findTrees.Graphics = TreeStaticID
    findTrees.Hues = List[int]((  ))
    findTrees.CheckIgnoreObject = True
    listTrees = Items.ApplyFilter(findTrees)
    if len(listTrees) == 0:
        findTrees.RangeMax = 15
        listTrees = Items.ApplyFilter(findTrees)
    return listTrees
    

eightByEightX = Player.Position.X / 8
eightByEightY = Player.Position.Y / 8
ScanRadius = 8
for ebe_x in range(eightByEightX, eightByEightX+14, 2):
    for ebe_y in range(eightByEightY, eightByEightY-12, -1):
        Misc.SendMessage("X: {} Y: {} Z: {}".format(ebe_x*8, ebe_y*8, 0))
        route = PathFinding.Route()
        route.X = ebe_x*8
        route.Y = ebe_y*8
        route.StopIfStuck = True
        route.MaxRetry = 5
        found = PathFinding.Go(route)
        if found == False:
            Misc.SendMessage("CANT GET THERE 1")
            continue
            #Player.PathFindTo(ebe_x*8, ebe_y*16, 0)
        #sys.exit(0)
        trees = FindTrees()
        while trees != None and len(trees) > 0:
            trees = FindTrees()
            #Misc.SendMessage(str(len(trees)), 5)
            #tree = Items.Select(trees, "Nearest")
            tree = NearestCalc(trees)
            while (None != tree):
                weight = Mobiles.GetPropValue(Packhorse, "Weight") 
                if weight > 1400:
                    MarkRune(LastLocRune)
                    Misc.Pause(4000)
                    RecallRune(BankRune)
                    save_position = Player.Position
                    #Player.PathFindTo(2873, 3482, 0)
                    DepositItems()
                    RecallRune(LastLocRune)
                    Misc.Pause(15000)
                    axe = FindAxe()
                    Items.UseItem(axe)
                    #Player.PathFindTo(save_position.X+1, save_position.Y+1, save_position.Z)
                #Misc.SendMessage("tree at ( {}, {}, {}".format(tree.Position.X, tree.Position.Y, tree.Position.Z), 5)    
                route2 = PathFinding.Route()
                route2.X = tree.Position.X
                route2.Y = tree.Position.Y-1
                route2.StopIfStuck = True
                route2.MaxRetry = 5
                found = PathFinding.Go(route2)
                if found == False:
                    Misc.SendMessage("CANT GET THERE 2")
                    trees.Remove(tree)
                    tree = Items.Select(trees, "Nearest")
                    continue
                #Player.PathFindTo(tree.Position.X, tree.Position.Y, tree.Position.Z)
                # Move to Packhorse
                woodID = 0x1BD7
                wood = Items.FindByID(woodID, -1, Player.Backpack.Serial) 
                prev_wood = 0   
                while wood != None:
                    Misc.SendMessage("{} 0x{:x} - 0x{:x}".format(wood.Name, prev_wood, wood.Serial), 5)
                    prev_wood = wood.Serial
                    Items.Move(wood.Serial, Packhorse, 0)
                    Misc.Pause(2000)
                    test = Items.FindBySerial(wood.Serial)
                    if test != None:
                        Misc.SendMessage("UNABLE TO MOVE WOOD", 6)
                        #break
                    wood = Items.FindByID(woodID, -1, Player.Backpack.Serial)    
                wait_secs = 0
                if not Player.InRangeItem(tree, 1):
                    Misc.Pause(1000)
                    wait_secs = wait_secs + 1
                    if wait_secs > 20:
                        Misc.SendMessage("SKIPPING Tree Location ( {}, {}, {})".format(tree.Position.X, tree.Position.Y, tree.Position.Z), 5)
                        continue
                wood_to_chop = True
                Journal.Clear()
                failed_chop_time = time.time() + 6
                while wood_to_chop:
                    axe = Player.GetItemOnLayer('LeftHand')
                    if None == axe:
                        axe = FindAxe()
                        Items.UseItem(axe)
                    Items.UseItem(axe)
                    Target.WaitForTarget(5000, False)
                    #Misc.SendMessage("0x{:x}".format(tree.Serial), 5)
                    Target.TargetExecute(tree.Serial)
                    Misc.Pause(3000)
                    check_tree = Items.FindBySerial(tree.Serial)
                    if check_tree == None:
                        Misc.SendMessage("Stopping due to None")
                        wood_to_chop = False
                    if Journal.Search("You put") or Journal.Search("You put"):
                        failed_chop_time = time.time() + 6
                    if Journal.Search("no more wood"):
                        Misc.SendMessage("Stopping due to Journal")
                        wood_to_chop = False
                    if Player.Weight > Player.MaxWeight * .95:
                        Misc.SendMessage("Stopping due to Player Weight")
                        wood_to_chop = False
                    if Journal.Search("Can't get there"):
                        Misc.SendMessage("Stopping due to Unreachable")
                        Misc.IgnoreObject(tree)
                        wood_to_chop = False    
                    if Journal.Search("far away"):
                        Misc.SendMessage("Stopping due to Unreachable")
                        Misc.IgnoreObject(tree)
                        wood_to_chop = False
                    if failed_chop_time <= time.time():
                        Misc.SendMessage("Stopping due to Time-out")
                        Misc.IgnoreObject(tree)
                        wood_to_chop = False
                trees.Remove(tree)
                tree = Items.Select(trees, "Nearest")