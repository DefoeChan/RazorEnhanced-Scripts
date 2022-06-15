Journal.Clear()
pack = Items.FindBySerial(Target.PromptTarget())
bagok = Items.FindBySerial(Target.PromptTarget())
for itemcontenuti in pack.Contains:
    Player.UseSkill("Item ID")
    Target.WaitForTarget(5000)
    Target.TargetExecute(itemcontenuti.Serial)
    Misc.Pause(1500)
    if Journal.Search("Vanquishing") == 1:
        Misc.SendMessage("--> OK");
        Items.Move(itemcontenuti , bagok, 0)
        Misc.Pause(1000)
    else:
        Misc.SendMessage("--> No");
    Journal.Clear()
Misc.SendMessage("DONE");