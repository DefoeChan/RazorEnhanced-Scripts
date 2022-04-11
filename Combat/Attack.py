from Scripts.Glossary.colors import colors

pks = Target.GetTargetFromList( 'pks' )
mobs = Target.GetTargetFromList( 'mobs' )
greys = Target.GetTargetFromList( 'greys' )

if pks != None:
    Player.HeadMessage( colors[ 'red' ], 'PKs nearby!' )
    if Target.HasTarget():
        Target.TargetExecute( pks )
    else:
        Player.Attack( pks )
        
        Target.SetLast( pks )
        
elif mobs != None:
    Player.HeadMessage( colors[ 'red' ], 'Mobs nearby!' )
    if Target.HasTarget():
        Target.TargetExecute( mobs )
    else:
        Player.Attack( mobs )
        
    Target.SetLast( mobs )
    while not Mobiles.FindBySerial(mobs) == None:
        Misc.Pause(500)
elif greys != None:
    Player.HeadMessage( colors[ 'red' ], 'Greys ' + str(greys.Serial) + ' nearby!' )
    if Target.HasTarget():
        Target.TargetExecute( greys.Serial )
    else:
        Player.Attack( greys )
        
    Target.SetLast( greys )
    while not Mobiles.FindBySerial(greys.Serial) == None:
        Misc.Pause(500)
    Player.HeadMessage( colors[ 'green' ], 'The enemy is dead.' )
else:
    Misc.Pause( 100 )

