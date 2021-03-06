from Scripts.Glossary.colors import colors

def SetSkills():
    Player.SetSkillStatus('*',1)
    Player.SetSkillStatus('Spirit Speak',0)
    Player.SetSkillStatus('Item ID',0)
    Player.SetSkillStatus('Snooping',0)
    Player.SetSkillStatus('Arms Lore',0)
    Player.SetSkillStatus('Detect Hidden',0)
    Player.SetSkillStatus('Eval Int',0)
    Player.SetSkillStatus('TasteID',0)
    

def TrainSpiritSpeak():
    '''
    Trains Spirit Speak to its skill cap
    '''

    if Player.GetSkillValue( 'Spirit Speak' ) == Player.GetSkillCap( 'Spirit Speak' ):
        Player.HeadMessage( colors[ 'green' ], 'Your Spirit Speak is already at its skill cap!' )
        return

    Misc.SendMessage( 'Beginning Spirit Speak training', colors[ 'cyan' ] )

    Player.UseSkill( 'Spirit Speak' )
    # Skill cooldown is 10,000 ms, but adding an extra 200 ms in case of latency issues
    Timer.Create( 'spiritSpeakTimer', spiritSpeakTimerMilliseconds )
    # while skill can increase and player is not dead
    while not Player.IsGhost and Player.GetSkillValue( 'Spirit Speak' ) < Player.GetSkillCap( 'Spirit Speak' ):
        if not Timer.Check( 'spiritSpeakTimer' ):
            # Cooldown has finished, we can use the skill again and reset the timer
            Player.UseSkill( 'Spirit Speak' )
            Timer.Create( 'spiritSpeakTimer', spiritSpeakTimerMilliseconds )

    Player.HeadMessage( colors[ 'green' ], 'Congratulations! Your Spirit Speak is now at its skill cap!' )


def TrainItemIdentification():
    '''
    Trains Item Identification with the selected target
    '''
    global knife

    Timer.Create( 'itemIdentificationTimer', 1 )

    while Player.GetRealSkillValue( 'Item ID' ) < Player.GetSkillCap( 'Item ID' ):
        knife = Items.FindByID(0x0F52,0,Player.Backpack.Serial,True)
        if not Timer.Check( 'itemIdentificationTimer' ):
            Player.UseSkill( 'Item ID' )
            Target.WaitForTarget( 2000, True )
            Target.TargetExecute( knife )
            Timer.Create( 'itemIdentificationTimer', itemIdentificationTimerMilliseconds )
        Misc.Pause( 50 )

    if Player.GetRealSkillValue( 'Item ID' ) >= Player.GetSkillCap( 'Item ID' ):
        Player.HeadMessage( colors[ 'green' ], 'Item Identification training complete!' )


def TrainArmsLore():
    '''
    Trains Arms Lore with the selected target
    '''
    global knife

    Timer.Create( 'armsLoreTimer', 1 )

    while Player.GetRealSkillValue('Arms Lore') < Player.GetSkillCap('Arms Lore'):
        knife = Items.FindByID(0x0F52,0,Player.Backpack.Serial,True)
        if not Timer.Check( 'armsLoreTimer' ):
            Player.UseSkill( 'Arms Lore' )
            Target.WaitForTarget( 2000, False )
            Target.TargetExecute( knife )
            Timer.Create( 'armsLoreTimer', armsLoreTimerMilliseconds )

    if Player.GetRealSkillValue( 'Arms Lore' ) >= Player.GetSkillCap( 'Arms Lore' ):
        Player.HeadMessage( colors[ 'green' ], 'Arms Lore training complete!' )


def TrainAnatomy():
    while Player.GetRealSkillValue('Anatomy') < Player.GetSkillCap('Anatomy'):
        Player.UseSkill('Anatomy')
        Target.WaitForTarget(1000, True)
        Target.PerformTargetFromList('blue_human_next')
        Misc.Pause(4200)

        
def TrainEvalInt():
    while Player.GetRealSkillValue('Eval Int') < Player.GetSkillCap('Eval Int'):
        Player.UseSkill('Eval Int')
        Target.WaitForTarget(1000, True)
        Target.PerformTargetFromList('blue_human_next')
        Misc.Pause(1200)
        
        
def TrainAnimalLore():
    while Player.GetRealSkillValue('Animal Lore') < Player.GetSkillCap('Animal Lore'):
        Player.UseSkill('Animal Lore')
        Target.WaitForTarget(1000, True)
        Target.PerformTargetFromList('horse')
        Misc.Pause(1200)

        
def TrainTasteID():
    '''
    Trains Arms Lore with the selected target
    '''
    global banana

    Timer.Create( 'armsLoreTimer', 1 )

    while Player.GetRealSkillValue('TasteID') < Player.GetSkillCap('TasteID'):
        banana = Items.FindByID(0x171F,0,Player.Backpack.Serial,True)
        if not Timer.Check( 'TasteIDTimer' ):
            Player.UseSkill( 'TasteID' )
            Target.WaitForTarget( 2000, False )
            Target.TargetExecute( banana )
            Timer.Create( 'TasteIDTimer', TasteIDTimerMilliseconds )
            
def TrainDetectHidden():          
    while Player.GetRealSkillValue('Detect Hidden') < Player.GetSkillCap('Detect Hidden'):
        Player.UseSkill('Detect Hidden')
        Target.WaitForTarget(1200, True)
        Target.Self()
        Misc.Pause(3200)
                
def TrainSnooping():
    Player.PathFindTo(1494, 1615, 20)
    while Player.GetRealSkillValue('Snooping') < Player.GetSkillCap('Snooping'):
        Items.UseItem(0x406C0A68)
        


itemIdentificationTimerMilliseconds = 1200
spiritSpeakTimerMilliseconds = 1200
armsLoreTimerMilliseconds = 1200
TasteIDTimerMilliseconds = 1200


SetSkills()

TrainDetectHidden()
TrainEvalInt()
TrainSpiritSpeak()
TrainArmsLore()
TrainItemIdentification()
TrainTasteID()
TrainSnooping()
