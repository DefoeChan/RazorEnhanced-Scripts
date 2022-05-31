def HomeBank():
    global status
    if Player.DistanceTo(Items.FindBySerial(0x41BDCCC7)) <= 2:
        Organizer.RunOnce('gold', Player.Backpack.Serial, 0x41BDCCC7, 500)
        Misc.Pause(500)
        Organizer.RunOnce('reagents', Player.Backpack.Serial, 0x40A7B9F2, 500)
        Misc.Pause(500)
        Organizer.RunOnce('loot', Player.Backpack.Serial, 0x433CECD9, 500)
        Misc.Pause(500)
        if Player.GetRealSkillValue('Magery') >= 30:
            Restock.RunOnce('reagents', 0x40A7B9F2, Player.Backpack.Serial, 500)
            Misc.Pause(500)
        if Player.GetRealSkillValue('Archery') >= 30:
            Restock.RunOnce('arrows', 0x40A7B9F2, Player.Backpack.Serial, 500)
            Misc.Pause(500)
        if Player.GetRealSkillValue('Healing') >= 30 or Player.GetRealSkillValue('Veterinary') >= 30:
            Restock.RunOnce('bandages', 0x40A7B9F2, Player.Backpack.Serial, 500)
            Misc.Pause(500)
    while Player.Hits < Player.HitsMax or Player.Mana < Player.ManaMax or Player.Stam < Player.StamMax: Misc.Pause(1000)
    status = 'Ready'
    
HomeBank()