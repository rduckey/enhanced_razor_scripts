#Do NOT run this while wearing good armor, it will drain durability at higher skill levels

from System.Collections.Generic import List
from System import Byte
import sys

summon_list = [0x0080]
summon = Mobiles.Filter()
summon.Enabled = True
summon.RangeMax = 2
summon.IsGhost = False
summon.Bodies = List[int] (summon_list)
delay = 1800

def meditation_check():
    Player.UseSkill('Meditation')
    while Player.Mana != Player.ManaMax:
        if Journal.GetLineText('You cannot focus your concentration'):
            Misc.Pause(10000)
            Player.UseSkill('Meditation')
           
def dispel():
    while Player.Followers > 0:
        summonmob = Mobiles.ApplyFilter(summon)
    for v in summonmob:
        v = Mobiles.Select(summonmob, 'Nearest')
        Mobiles.SingleClick(v)
        Misc.WaitForContext(v.Serial, 10000)
        Misc.ContextReply(v.Serial, 138)
        Misc.Pause(1000)
           
while Player.GetRealSkillValue('Spell Weaving') < Player.GetSkillCap('Spell Weaving'):
    if Player.GetRealSkillValue('Spell Weaving') < 20:
        while Player.Mana > 24:
            Spells.CastSpellweaving('Arcane Circle')
            Misc.Pause(delay)
        else:
            meditation_check()
    elif Player.GetRealSkillValue('Spell Weaving') < 33:
        while Player.Mana > 32:
            Spells.CastSpellweaving('Immolating Weapon')
            Misc.Pause(delay)
        else:
            meditation_check()
    elif Player.GetRealSkillValue('Spell Weaving') < 44:
        while Player.Mana > 34:
            Spells.CastSpellweaving('Reaper Form')
            Misc.Pause(delay)
        else:
            meditation_check()
    elif Player.GetRealSkillValue('Spell Weaving') < 60:
        while Player.Mana > 24:
            Spells.CastSpellweaving('Summon Fey')
            Misc.Pause(2000)
            dispel()
        else:
            meditation_check()
    elif Player.GetRealSkillValue('Spell Weaving') < 74:
        while Player.Mana > 24:
            Spells.CastSpellweaving('Essence Of Wind')
            Misc.Pause(delay)
        else:
            meditation_check()
    elif Player.GetRealSkillValue('Spell Weaving') < 90:
        while Player.Mana > 50:
            Spells.CastSpellweaving('Wildfire')
            Target.WaitForTarget(2000, True)
            Target.Self()
            Misc.Pause(800)
        else:
            meditation_check()
    else:
        if Player.Hits > Player.HitsMax * .3:
            if Player.Mana > 50:
                Spells.CastSpellweaving('Word Of Death')
                Target.WaitForTarget(10000, True)
                Target.Self()
                Misc.Pause(2000)
            else:
                meditation_check()
        else:
            while Player.Hits != Player.HitsMax:
                Spells.CastMagery('Greater Heal')
                Target.WaitForTarget(10000, True)
                Target.Self()
                Misc.Pause(1500)
