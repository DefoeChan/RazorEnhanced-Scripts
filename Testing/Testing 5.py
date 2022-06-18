from Scripts.Glossary.colors import colors

def pathToMobile(mob):
    Misc.SendMessage('lets go')
    mobile = Mobiles.FindBySerial(0x00294CEB)
    mobilePosition = mobile.Position
    mobileCoords = PathFinding.Route()
    mobileCoords.MaxRetry = 0
    mobileCoords.StopIfStuck = True
    mobileCoords.UseResync = False
    mobileCoords.DebugMessage = False
    mobileCoords.X = mobilePosition.X 
    mobileCoords.Y = mobilePosition.Y
    
    #PathFinding.Go(mobileCoords)
    path = PathFinding.GetPath(mobileCoords.X, mobileCoords.Y, 0)
    
def Chase(enemy):
    
    enemy = Mobiles.FindBySerial(0x00294CEB)
    cantGetThereMax = 50
    cantGetThere = 0
    PathFind = False
    
    LocParty = enemy.Position
    LocSelf = Player.Position
    LocDiffX = LocParty.X - LocSelf.X
    LocDiffY = LocParty.Y - LocSelf.Y

    if LocDiffX >= 2 or LocDiffX <= -2 or LocDiffY >= 2 or LocDiffY <= -2: PathFind = True

    while PathFind == True:
        EnemyPosition = enemy.Position # Your main characters position
        SelfPosition = Player.Position # This characters position
        LocDiffX = EnemyPosition.X - SelfPosition.X #The difference of x coordinates
        LocDiffY = EnemyPosition.Y - SelfPosition.Y #The difference of y coordinates
        cantGetThere += 1
        if cantGetThere >= cantGetThereMax:
            Player.PathFindTo(enemy.Position.X, enemy.Position.Y, enemy.Position.Z)
            Timer.Create('pathfindingtimer', 10000)
            while not Player.InRangeMobile(enemy, 1) and Timer.Check('pathfindingtimer'):
                Misc.Pause(50)
                if not Player.InRangeMobile(enemy, 20):
                    break
        #Find the most direct path to make the coordinates meet    
        if LocDiffX < -1:
            if LocDiffY < -1:
                Player.Run('Up', False)
            elif LocDiffY == -1 or LocDiffY == 0:
                Player.Run('West', False)
            else:
                Player.Run('Left', False)
        elif LocDiffX > 1:
            if LocDiffY > 1:
                Player.Run('Down', False)
            elif LocDiffY == 1 or LocDiffY == 0:
                Player.Run('East', False)
            else:
                Player.Run('Right', False)
        elif LocDiffY < -1:
            Player.Run('North', False)
        elif LocDiffY > 1:
            Player.Run('South', False)
        else:
            PathFind = False
            Player.HeadMessage( colors[ 'green' ], 'Arrived.' )
            Player.Attack( enemy )
            cantGetThere = 0
            Misc.Pause(100)
        #Player.HeadMessage( colors[ 'red' ], cantGetThere )
        Misc.Pause(100)
    #Player.HeadMessage( colors[ 'green' ], 'The enemy is dead.' )
#    Target.AttackTargetFromList('mobs')
    
    
while True:
    Chase(0x00294CEB)
    Misc.Pause(100)
#    target = Target.GetTargetFromList( 'greys' )
#    if target != None:
#        Player.Attack(target)
#        pathToMobile(target)
#        Player.Attack(target)
#    Misc.Pause(100)