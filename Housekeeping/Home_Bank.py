import sys

delay = 500
if Player.InRangeItem(0x405D612C, 3): # Parliament
    chestGold = 0x405D612C
    chestReagents = 0x40262E27
    chestArmor = 0x41F0264E
    chestLoot = 0x4360F2E5
else: # Highgate Cemetery
    chestGold = 0x41BDCCC7
    chestReagents = 0x40A7B9F2
    chestArmor = 0x471B1D1F
    chestLoot = 0x433CECD9

def HouseBank():
    global status
    global chestGold
    global chestReagents
    global chestArmor
    global chestLoot
    if Player.InRangeItem(chestGold, 3):
        Organizer.RunOnce('gold', Player.Backpack.Serial, chestGold, delay)
        Misc.Pause(delay)
        Organizer.RunOnce('reagents', Player.Backpack.Serial, chestReagents, delay)
        Misc.Pause(delay)
        Organizer.RunOnce('loot', Player.Backpack.Serial, chestLoot, delay)
        Misc.Pause(delay)
        Organizer.RunOnce('unidentified', Player.Backpack.Serial, chestLoot, delay)
        Misc.Pause(delay)
        if Player.GetRealSkillValue('Magery') >= 30:
            Restock.RunOnce('reagents', chestReagents, Player.Backpack.Serial, delay)
            Misc.Pause(delay)
        if Player.GetRealSkillValue('Archery') >= 30:
            Restock.RunOnce('arrows', chestReagents, Player.Backpack.Serial, delay)
            Misc.Pause(delay)
        if Player.GetRealSkillValue('Healing') >= 30 or Player.GetRealSkillValue('Veterinary') >= 30:
            Restock.RunOnce('bandages', chestReagents, Player.Backpack.Serial, delay)
            Misc.Pause(delay)
#    while Player.Hits < Player.HitsMax or Player.Mana < Player.ManaMax or Player.Stam < Player.StamMax: Misc.Pause(1000)
    status = 'Ready'
    sys.exit()
    
    
HouseBank()