Journal.Clear()
chestLoot = Items.FindBySerial(0x4360F2E5)
chestVanquishing = Items.FindBySerial(0x42A851FD)
chestRepond = Items.FindBySerial(0x42912AF1)
trashcan = Items.FindBySerial(0x413220D0)

for iteminchest in chestLoot.Contains:
    Player.UseSkill("Item ID")
    Target.WaitForTarget(5000)
    Target.TargetExecute(iteminchest.Serial)
    Misc.Pause(1500)
    if Journal.Search("Repond") == 1 or \
       Journal.Search("Silver") == 1:
        Misc.SendMessage("--> Slayer");
        Items.Move(iteminchest , chestRepond, 0)
        Misc.Pause(1000)
    elif 
        Journal.Search("Vanquishing") == 1:
        Misc.SendMessage("--> Vanquishing");
        Items.Move(iteminchest , chestVanquishing, 0)
        Misc.Pause(1000)
    elif Journal.Search("orcish pickaxe") == 1 or \
         Journal.Search("Orcish Pickaxe") == 1:
        Misc.SendMessage("Trash");
        Items.Move(iteminchest , trashcan, 0)
        Misc.Pause(1000)
    elif Journal.Search("Ruin") == 1 or \
         Journal.Search("Might") == 1 or \
         Journal.Search("Force") == 1 or \
         Journal.Search("Power") == 1 or \
         Journal.Search("Defense") == 1 or \
         Journal.Search("Guarding") == 1 or\
         Journal.Search("Hardening") == 1:
        Misc.SendMessage("--> Ruin / Might / Force");
        Items.Move(iteminchest , Player.Backpack, 0)
        Misc.Pause(1000)
    Journal.Clear()
    
Misc.SendMessage("DONE");