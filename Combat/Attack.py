from Scripts.Glossary.colors import colors

def SearchDestroy(enemy):
    Player.HeadMessage( colors[ 'red' ], 'Greys ' + str(enemy.Name) + ' nearby!' )
    if Target.HasTarget():
        Target.TargetExecute( emeny.Serial )
    else:
        Player.Attack( enemy )
        Target.SetLast( enemy )
        while not Mobiles.FindBySerial(enemy.Serial) == None:
            Chase(enemy)
#            Player.HeadMessage( colors[ 'green' ], 'Chasing' )
#            Player.PathFindTo( enemyPosition.X, enemyPosition.Y , enemyPosition.Z )
#            while PathFinding = True
            Misc.Pause(1000)
    Player.HeadMessage( colors[ 'green' ], 'The enemy is dead.' )
    
    
def Chase(enemy):
    cantGetThereMax = 50
    cantGetThere = 0
    PathFind = False
    
    LocParty = enemy.Position
    LocSelf = Player.Position
    LocDiffX = LocParty.X - LocSelf.X
    LocDiffY = LocParty.Y - LocSelf.Y

    if LocDiffX >= 2 or LocDiffX <= -2 or LocDiffY >= 2 or LocDiffY <= -2: PathFind = True

    while PathFind == True:
        LocParty = enemy.Position # Your main characters position
        LocSelf = Player.Position # This characters position
        LocDiffX = LocParty.X - LocSelf.X #The difference of x coordinates
        LocDiffY = LocParty.Y - LocSelf.Y #The difference of y coordinates
        cantGetThere += 1
        if cantGetThere >= cantGetThereMax:
            Player.PathFindTo(enemy.Position.X, enemy.Position.Y, enemy.Position.Z)
            while PathFinding == True:
                Misc.Pause(500)
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
            cantGetThere = 0
        Misc.Pause(100)
        Player.HeadMessage( colors[ 'red' ], cantGetThere )


pks = Target.GetTargetFromList( 'pks' )
mobs = Target.GetTargetFromList( 'mobs' )
greys = Target.GetTargetFromList( 'greys' )

if pks != None:
    SearchDestroy(pks)
elif mobs != None:
    SearchDestroy(mobs)
elif greys != None:
    SearchDestroy(greys)
else:
    Misc.Pause( 100 )

