# Use this to cast Mana Vampire on someone (or yourself) until you run out of regs.
# By MatsaMilla

#----------------------------------------------------

training = Target.PromptTarget("Target training dummy")
dummy = Mobiles.FindBySerial(training)

import sys

while True:
    dummy = Mobiles.FindBySerial(training)
    if Player.DistanceTo(dummy) < 12:
        Player.SetWarMode(False)
        if Player.GetRealSkillValue("Magery") < 70:
            Spells.CastMagery("Mana Drain")
        else:
            Spells.CastMagery("Mana Vampire")
        Target.WaitForTarget(1500, False)
        Target.TargetExecute(dummy)
        Player.SetWarMode(True)
        Player.SetWarMode(False)
        Misc.Pause(2500)
    
    Player.SetWarMode(False)
    
    if Player.Mana < 40:
        Player.UseSkill('Meditation')
        while Player.Mana < Player.ManaMax:
            
            if not Player.BuffsExist('Meditation') and Timer.Check('med') == False:
                Misc.Pause(2000)
                Player.UseSkill('Meditation')
                Timer.Create('med', 7000)
            Misc.Pause(100)
                
    if Items.BackpackCount( 0x0F8D, -1) < 1:
        sys.exit()
    if Journal.Search('Did it, got it') == 50:
        sys.exit()
            
