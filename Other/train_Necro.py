# Train Necro
def trainNecro():
    
    while Player.GetSkillValue('Necromancy') < 100.0:
        
        necro = Player.GetSkillValue('Necromancy')
        if necro <= 70.0:
            Spells.CastNecro("Horrific Beast")
        elif necro > 70.0 and necro <= 90.0:
            Spells.CastNecro("Wither")
        elif necro > 90.0 and necro <= 100.0:
            Spells.CastNecro("Lich Form")
        
        Misc.Pause(3500)
        
        if Player.Mana < 30:
            Player.UseSkill("Meditation")
            Misc.Pause(20000)
            
trainNecro()