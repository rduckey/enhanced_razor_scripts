from System.Collections.Generic import List
from System import Byte
    
Misc.SetSharedValue('run',False)


def attack():
    eNumber = 0
    fil = Mobiles.Filter()
    fil.Enabled = True
    fil.RangeMax = 1
    fil.Notorieties = List[Byte](bytes([3,4,5,6]))

    if Misc.ReadSharedValue('bush') == 'True':
        bush()
    if Misc.ReadSharedValue('eoo') == 'True':
        enemyOfOne()
    if Misc.ReadSharedValue('consec') == 'True':  
        consecrateWep()
    if Misc.ReadSharedValue('honor') == 'True':
        honorNearest()
    if Misc.ReadSharedValue('devFury') == 'True':
        divineFury()
    if Misc.ReadSharedValue('onslaught') == 'True':
        onslaughtMastery()
    if Misc.ReadSharedValue('cAttack') == 'True':
        counterAttack()
    if Misc.ReadSharedValue('ojPetal') == 'True':
        orangePetal()
    if Misc.ReadSharedValue('dAxe') == 'True':
        enemies = Mobiles.ApplyFilter(fil)
        Mobiles.Select(enemies,'Nearest')
        for enemy in enemies:
            eNumber += 1
        if eNumber == 1:
            eNumber = 0
            if not Player.HasSpecial:
                Player.WeaponPrimarySA()
            Player.Attack(enemy)
        if eNumber == 2:
            eNumber = 0
            if not Player.SpellIsEnabled('Momentum Strike'):
                Spells.CastBushido('Momentum Strike')
            Player.Attack(enemy) 
        if eNumber > 2 :
            eNumber = 0
            if not Player.HasSpecial:
                Player.WeaponSecondarySA()
            Player.Attack(enemy)
        Misc.Pause(250) 
    if Misc.ReadSharedValue('bStaff') == 'True':
        enemies = Mobiles.ApplyFilter(fil)
        Mobiles.Select(enemies,'Nearest')
        for enemy in enemies:
            eNumber += 1
        if eNumber == 1:
            eNumber = 0
            if not Player.HasSpecial:
                Player.WeaponPrimarySA()
            Player.Attack(enemy)
        if eNumber >= 2:
            eNumber = 0
            if not Player.SpellIsEnabled('Momentum Strike'):
                Spells.CastBushido('Momentum Strike')
            Player.Attack(enemy)    
    
      
def bush():
    healhits = 90
    evadehits = 120
    if Player.Hits < (healhits) and not Player.BuffsExist('Confidence'):
        Misc.Pause (400)
        Spells.CastBushido("Confidence")
        Misc.Pause (500)
        
    if Player.Hits < (evadehits) and not Player.BuffsExist('Evasion'):
        Misc.Pause (400)
        Spells.CastBushido("Evasion")
        Misc.Pause (500)
        
def enemyOfOne():
    if not Player.BuffsExist('Enemy Of One'):
        Spells.CastChivalry('Enemy Of One')
        Misc.Pause(500)
        
def consecrateWep():
    if not Player.BuffsExist('Consecrate Weapon'):
        Spells.CastChivalry('Consecrate Weapon')
        Misc.Pause(500)
        
def honorNearest():
    if not Player.BuffsExist('Honered'):
        honfil = Mobiles.Filter()
        honfil.Enabled = True
        honfil.RangeMax = 8
        honfil.Notorieties = List[Byte](bytes([3,4,5,6]))
        enemies = Mobiles.ApplyFilter(honfil)
        Misc.Pause(200)
        enemy = Mobiles.Select(enemies,'Nearest')
        Misc.Pause(400)
        Player.InvokeVirtue("Honor")
        Target.WaitForTarget(1000, False)
        Target.TargetExecute(enemy.Serial)
        
def divineFury():
    if Player.Stam < 120:   
        Spells.CastChivalry("Divine Fury")
        Misc.Pause(500)
        
def onslaughtMastery():
    if Timer.Check('mastery') == False:
        Spells.CastMastery('Onslaught')
        Timer.Create('mastery',10000)
    
def counterAttack():
    if not Player.BuffsExist('Counter Attack'):
        Spells.CastBushido('Counter Attack')
        Misc.Pause(500)
        
def orangePetal():
    ojpetals = Items.FindByID(0x1021,0x002B,Player.Backpack.Serial)
    if Player.BuffsExist('Poison'):
        if not Player.BuffsExist('Orange Petals'):
            Items.UseItem(ojpetals.Serial)
            Misc.Pause(200)
            
while True: 
    if Misc.ReadSharedValue('run') == 'True':
        attack()
    else:
        Misc.Pause(2000)
    