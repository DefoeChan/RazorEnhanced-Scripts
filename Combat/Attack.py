from Scripts.Glossary.colors import colors

def AttackMelee(enemy):
    Player.HeadMessage( colors[ 'red' ], 'Greys ' + str(enemy.Name) + ' nearby!' )
    if Target.HasTarget():
        Target.TargetExecute( emeny.Serial )
    else:
        Player.Attack( enemy )
        Target.SetLast( enemy )
        while not Mobiles.FindBySerial(enemy.Serial) == None:
            mobilePosition = enemy.Position
            Player.PathFindTo( mobilePosition.X, mobilePosition.Y , mobilePosition.Z )
#            while PathFinding = True
            Misc.Pause(3000)
    Player.HeadMessage( colors[ 'green' ], 'The enemy is dead.' )
    
    
def FollowMobile( mobile, maxDistanceToMobile = 1.5, startPlayerStuckTimer = False ):
    '''
    Uses the X and Y coordinates of the animal and player to follow the animal around the map
    Returns True if player is not stuck, False if player is stuck
    '''

    if not Timer.Check( 'catchUpToAnimalTimer' ):
        return False

    mobilePosition = mobile.Position
    playerPosition = Player.Position
    directions = []
    if mobilePosition.X > playerPosition.X and mobilePosition.Y > playerPosition.Y:
        directions.append( 'Down' )
    if mobilePosition.X < playerPosition.X and mobilePosition.Y > playerPosition.Y:
        directions.append( 'Left' )
    if mobilePosition.X > playerPosition.X and mobilePosition.Y < playerPosition.Y:
        directions.append( 'Right' )
    if mobilePosition.X < playerPosition.X and mobilePosition.Y < playerPosition.Y:
        directions.append( 'Up' )
    if mobilePosition.X > playerPosition.X and mobilePosition.Y == playerPosition.Y:
        directions.append( 'East' )
    if mobilePosition.X < playerPosition.X and mobilePosition.Y == playerPosition.Y:
        directions.append( 'West' )
    if mobilePosition.X == playerPosition.X and mobilePosition.Y > playerPosition.Y:
        directions.append( 'South' )
    if mobilePosition.X == playerPosition.X and mobilePosition.Y < playerPosition.Y:
        directions.append( 'North' )

    if startPlayerStuckTimer:
        Timer.Create( 'playerStuckTimer', playerStuckTimerMilliseconds )

    playerPosition = Player.Position
    for direction in directions:
        PlayerWalk( direction )

    newPlayerPosition = Player.Position
    if playerPosition == newPlayerPosition and not Timer.Check( 'playerStuckTimer' ):
        # Player has been stuck in the same position for a while, try to find them a way out of the stuck position
        if Player.Direction == 'Up':
            for i in range ( 5 ):
                Player.Walk( 'Down' )
        elif Player.Direction == 'Down':
            for i in range( 5 ):
                Player.Walk( 'Up' )
        elif Player.Direction == 'Right':
            for i in range( 5 ):
                Player.Walk( 'Left' )
        elif Player.Direction == 'Left':
            for i in range( 5 ):
                Player.Walk( 'Right' )
        Timer.Create( 'playerStuckTimer', playerStuckTimerMilliseconds )
    elif playerPosition != newPlayerPosition:
        Timer.Create( 'playerStuckTimer', playerStuckTimerMilliseconds )

    if Player.DistanceTo( mobile ) > maxDistanceToMobile:
        # This pause may need further tuning
        # Dont want to create a ton of infinite calls if the player is stuck, but also dont want to not be able to catch up to animals
        Misc.Pause( 100 )
        FollowMobile( mobile, maxDistanceToMobile )
        #pathfindToMobile( mobile )

    return True

pks = Target.GetTargetFromList( 'pks' )
mobs = Target.GetTargetFromList( 'mobs' )
greys = Target.GetTargetFromList( 'greys' )

if pks != None:
    AttackMelee(pks)
elif mobs != None:
    AttackMelee(mobs)
elif greys != None:
    AttackMelee(greys)
else:
    Misc.Pause( 100 )

