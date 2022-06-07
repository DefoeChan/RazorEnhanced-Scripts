import sys

delay = 500
if Player.InRangeItem(0x405D612C, 3): # Parliament
    chestgold = 0x405D612C
    chestreagents = 0x40262E27
    chestarmor = 0x41F0264E
    chestloot = 0x4020356F
else: # Highgate Cemetery
    chestgold = 0x41BDCCC7
    chestreagents = 0x40A7B9F2
    chestarmor = 0x471B1D1F
    chestloot = 0x433CECD9

def HouseBank():
    global status
    global chestgold
    global chestreagents
    global chestarmor
    global chestloot
    if Player.InRangeItem(chestgold, 3):
        Organizer.RunOnce('gold', Player.Backpack.Serial, chestgold, delay)
        Misc.Pause(delay)
        Organizer.RunOnce('reagents', Player.Backpack.Serial, chestreagents, delay)
        Misc.Pause(delay)
        Organizer.RunOnce('loot', Player.Backpack.Serial, chestloot, delay)
        Misc.Pause(delay)
        Organizer.RunOnce('unidentified', Player.Backpack.Serial, chestloot, delay)
        Misc.Pause(delay)
        if Player.GetRealSkillValue('Magery') >= 30:
            Restock.RunOnce('reagents', chestreagents, Player.Backpack.Serial, delay)
            Misc.Pause(delay)
        if Player.GetRealSkillValue('Archery') >= 30:
            Restock.RunOnce('arrows', chestreagents, Player.Backpack.Serial, delay)
            Misc.Pause(delay)
        if Player.GetRealSkillValue('Healing') >= 30 or Player.GetRealSkillValue('Veterinary') >= 30:
            Restock.RunOnce('bandages', chestreagents, Player.Backpack.Serial, delay)
            Misc.Pause(delay)
#    while Player.Hits < Player.HitsMax or Player.Mana < Player.ManaMax or Player.Stam < Player.StamMax: Misc.Pause(1000)
    status = 'Ready'
    sys.exit()
    
    
HouseBank()