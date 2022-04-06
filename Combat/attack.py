from Scripts.Glossary.colors import colors

pks = Target.GetTargetFromList( 'pks' )
mobs = Target.GetTargetFromList( 'mobs' )
greys = Target.GetTargetFromList( 'greys' )

if pks != None:
    if Target.HasTarget():
        Target.TargetExecute( pks )
    else:
        Player.Attack( pks )
        
        Target.SetLast( pks )
        Player.HeadMessage( colors[ 'red' ], 'PKs nearby!' )
        
elif mobs != None:
    if Target.HasTarget():
        Target.TargetExecute( mobs )
    else:
        Player.Attack( mobs )
        
    Target.SetLast( mobs )
    Player.HeadMessage( colors[ 'red' ], 'Mobs nearby!' )
    
elif greys != None:
    if Target.HasTarget():
        Target.TargetExecute( greys )
    else:
        Player.Attack( greys )
        
    Target.SetLast( greys )
    Player.HeadMessage( colors[ 'red' ], 'Greys nearby!' )
    
Misc.Pause( 100 )
