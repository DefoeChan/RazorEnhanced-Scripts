from Scripts.Glossary.colors import colors

pks = Target.GetTargetFromList( 'pks' )
if pks != None:
    if Target.HasTarget():
        Target.TargetExecute( pks )
    else:
        Player.Attack( pks )
        
        Target.SetLast( pks )
else:
    Player.HeadMessage( colors[ 'red' ], 'No PKs nearby!' )
    
mobs = Target.GetTargetFromList( 'mobs' )
if mobs != None:
    if Target.HasTarget():
        Target.TargetExecute( mobs )
    else:
        Player.Attack( mobs )
        
    Target.SetLast( mobs )
else:
    Player.HeadMessage( colors[ 'red' ], 'No mobs nearby!' )
    
Misc.Pause( 100 )
