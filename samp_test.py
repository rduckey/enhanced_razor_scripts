import time
from System.Collections.Generic import List
from System import Byte

#MoblleID of priority enemies
bosses =['Neira', 'Neira the necromancer']
#Neira
bossesID = [0x0191]
revenantID = 0x0190
delay = 1000


fil = Mobiles.Filter()
fil.Enabled = True
fil.RangeMax = 2
fil.Notorieties = List[Byte](bytes([3,4,5,6]))
enemies = Mobiles.ApplyFilter(fil)

def onslaught():
    fil = Mobiles.Filter()
    fil.Enabled = True
    fil.RangeMax = 1
    fil.Notorieties = List[Byte](bytes([3,4,5,6]))
    enemies = Mobiles.ApplyFilter(fil)
    
    boss = []
    for enemy in enemies:
        if enemy.Body in bossesID:
            boss.append(enemy)
    if len(boss) > 0 and 'double axe' in str(weapon):
        if Timer.Check('mastery') == False:
            Spells.CastMastery('Onslaught')
            Timer.Create('mastery',10000)
        
        
def attack():
    fil = Mobiles.Filter()
    fil.Enabled = True
    fil.RangeMax = 1
    fil.Notorieties = List[Byte](bytes([3,4,5,6]))
    enemies = Mobiles.ApplyFilter(fil)
    
    ems = Mobiles.Filter()
    ems.Enabled = True
    ems.RangeMax = 1
    ems.Notorieties = List[Byte](bytes([3,4,5,6]))
    enemies = Mobiles.ApplyFilter(ems)

    boss = []
    eNumber = 0
    Mobiles.Select(enemies,'Nearest')
    for enemy in enemies:
        eNumber += 1
        if enemy.Name in bosses:
            boss.append(enemy)
    if eNumber == 1:
        if not Player.HasSpecial:
            Player.WeaponPrimarySA()
    elif eNumber == 2\
    or eNumber > 2 and 'bladed staff' in str(weapon):
        if not Player.SpellIsEnabled('Momentum Strike'):
            Spells.CastBushido('Momentum Strike')
    elif eNumber > 2 and 'double axe' in str(weapon):
        if not Player.HasSpecial:
            Player.WeaponSecondarySA()     
    for enemy in enemies:
        if len(boss) > 0:
            Player.Attack(boss[0])
        else:
            Player.Attack(enemy)
        Misc.Pause(400) 
        

def vampire():
    if Player.BuffsExist('Vampiric Embrace') == False:
        Dress.ChangeList('lrc')
        Dress.DressFStart()
        while Dress.DressStatus() == True:
            Misc.Pause(100)
        while Player.BuffsExist('Vampiric Embrace') == False:
            Spells.CastNecro('Vampiric Embrace')
            Misc.Pause(2000)
        Dress.ChangeList('samp_suit')
        Dress.DressFStart()
        while Dress.DressStatus() == True:
            Misc.Pause(100)
            
def counter_heal():
    healhits = Player.HitsMax *.8
    evadehits = Player.HitsMax *.6
    
    if Player.Hits < (healhits) and not Player.BuffsExist('Confidence'):
        if Timer.Check('Confidence') == False:
            Spells.CastBushido("Confidence")
            Timer.Create('Confidence',4000)
            Misc.Pause (500)
    elif Player.Hits < (evadehits) and not Player.BuffsExist('Evasion'):
        if Timer.Check('Evasion') == False:
            Spells.CastBushido("Evasion")
            Timer.Create('Evasion',24000)
            Misc.Pause (500)
    elif Player.BuffsExist('Counter Attack') == False:
        Spells.CastBushido('Counter Attack')
        Misc.Pause(500)

def remove_curse():
    if Player.BuffsExist('Clumsy')\
    or Player.BuffsExist('Feeblemind')\
    or Player.BuffsExist('Weaken'):
        if Player.Hits == Player.HitsMax:
            if Timer.Check('Remove Curse') == False:
                Spells.CastChivalry('Remove Curse')
                Target.WaitForTarget(2000, True)
                Target.Self()
                Timer.Create('Remove Curse',30000)

        
        
while Player.IsGhost == False:
    vampire() 
    counter_heal()
    weapon = Player.GetItemOnLayer('LeftHand')
    onslaught()
    attack()
    #remove_curse()
    boss = []
