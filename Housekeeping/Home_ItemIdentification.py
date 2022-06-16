Journal.Clear()
chestLoot = Items.FindBySerial(0x4360F2E5)
chestVanquishing = Items.FindBySerial(0x42A851FD)
chestVanquishing = Items.FindBySerial(0x42A851FD)
chestRepond = Items.FindBySerial(0x42912AF1)
trashcan = Items.FindBySerial(0x413220D0)

for iteminchest in chestLoot.Contains:
    Player.UseSkill("Item ID")
    Target.WaitForTarget(5000)
    Target.TargetExecute(iteminchest.Serial)
    Misc.Pause(1500)
    if Journal.Search("Repond") == 1:
        Misc.SendMessage("--> Slayer");
        Items.Move(iteminchest , chestRepond, 0)
    elif Journal.Search("Ogre Trashing") == 1:
        Misc.SendMessage("--> Slayer");
        Items.Move(iteminchest , chestRepond, 0)
    elif Journal.Search("Orc Slaying") == 1:
        Misc.SendMessage("--> Slayer");
        Items.Move(iteminchest , chestRepond, 0)
    elif Journal.Search("Troll Slaughter") == 1:
        Misc.SendMessage("--> Slayer");
        Items.Move(iteminchest , chestRepond, 0)
    elif Journal.Search("Silver") == 1:
        Misc.SendMessage("--> Slayer");
        Items.Move(iteminchest , chestRepond, 0)
    elif Journal.Search("Fey") == 1:
        Misc.SendMessage("--> Slayer");
        Items.Move(iteminchest , chestRepond, 0)
    elif Journal.Search("Elemental Ban") == 1:
        Misc.SendMessage("--> Slayer");
        Items.Move(iteminchest , chestRepond, 0)
    elif Journal.Search("Blood Drinking") == 1:
        Misc.SendMessage("--> Slayer");
        Items.Move(iteminchest , chestRepond, 0)
    elif Journal.Search("Earth Shatter") == 1:
        Misc.SendMessage("--> Slayer");
        Items.Move(iteminchest , chestRepond, 0)
    elif Journal.Search("Elemental Health") == 1:
        Misc.SendMessage("--> Slayer");
        Items.Move(iteminchest , chestRepond, 0)
    elif Journal.Search("Flame Dousing") == 1:
        Misc.SendMessage("--> Slayer");
        Items.Move(iteminchest , chestRepond, 0)
    elif Journal.Search("Summer Wind") == 1:
        Misc.SendMessage("--> Slayer");
        Items.Move(iteminchest , chestRepond, 0)
    elif Journal.Search("Vacuum") == 1:
        Misc.SendMessage("--> Slayer");
        Items.Move(iteminchest , chestRepond, 0)
    elif Journal.Search("Water Dissipation") == 1:
        Misc.SendMessage("--> Slayer");
        Items.Move(iteminchest , chestRepond, 0)
    elif Journal.Search("Exorcism") == 1:
        Misc.SendMessage("--> Slayer");
        Items.Move(iteminchest , chestRepond, 0)
    elif Journal.Search("Daemon Dismissal") == 1:
        Misc.SendMessage("--> Slayer");
        Items.Move(iteminchest , chestRepond, 0)
    elif Journal.Search("Gargoyles Foe") == 1:
        Misc.SendMessage("--> Slayer");
        Items.Move(iteminchest , chestRepond, 0)
    elif Journal.Search("Balron Damnation") == 1:
        Misc.SendMessage("--> Slayer");
        Items.Move(iteminchest , chestRepond, 0)
    elif Journal.Search("Arachnid Doom") == 1:
        Misc.SendMessage("--> Slayer");
        Items.Move(iteminchest , chestRepond, 0)
    elif Journal.Search("Scorpions Bane") == 1:
        Misc.SendMessage("--> Slayer");
        Items.Move(iteminchest , chestRepond, 0)
    elif Journal.Search("Spiders Death") == 1:
        Misc.SendMessage("--> Slayer");
        Items.Move(iteminchest , chestRepond, 0)
    elif Journal.Search("Terathan") == 1:
        Misc.SendMessage("--> Slayer");
        Items.Move(iteminchest , chestRepond, 0)
    elif Journal.Search("Reptilian Death") == 1:
        Misc.SendMessage("--> Slayer");
        Items.Move(iteminchest , chestRepond, 0)
    elif Journal.Search("Dragon Slaying") == 1:
        Misc.SendMessage("--> Slayer");
        Items.Move(iteminchest , chestRepond, 0)
    elif Journal.Search("Lizardman Slaughter") == 1:
        Misc.SendMessage("--> Slayer");
        Items.Move(iteminchest , chestRepond, 0)
    elif Journal.Search("Ophidian") == 1:
        Misc.SendMessage("--> Slayer");
        Items.Move(iteminchest , chestRepond, 0)
    elif Journal.Search("Snakes Bane") == 1:
        Misc.SendMessage("--> Slayer");
        Items.Move(iteminchest , chestRepond, 0)
    elif Journal.Search("Vanquishing") == 1:
        Misc.SendMessage("--> Vanquishing");
        Items.Move(iteminchest , chestVanquishing, 0)
    elif Journal.Search("Invulnerability") == 1:
        Misc.SendMessage("--> Invulnerability");
        Items.Move(iteminchest , chestInvulnerability, 0)
    elif Journal.Search("orcish pickaxe") == 1 or \
         Journal.Search("Orcish Pickaxe") == 1:
        Misc.SendMessage("Trash");
        Items.Move(iteminchest , trashcan, 0)
    elif Journal.Search("Ruin") == 1 or \
         Journal.Search("Might") == 1 or \
         Journal.Search("Force") == 1 or \
         Journal.Search("Power") == 1 or \
         Journal.Search("Defense") == 1 or \
         Journal.Search("Guarding") == 1 or\
         Journal.Search("Hardening") == 1:
         Misc.SendMessage("--> Sell");
        Items.Move(iteminchest , Player.Backpack, 0)
    Misc.Pause(1000)
    Journal.Clear()
    
Misc.SendMessage("DONE");