from Scripts.Glossary.colors import colors

def AttackMelee(enemy):
    Player.HeadMessage( colors[ 'red' ], 'Greys ' + str(enemy.Name) + ' nearby!' )
    if Target.HasTarget():
        Target.TargetExecute( emeny.Serial )
    else:
        Player.Attack( enemy )
        Target.SetLast( enemy )
        while not Mobiles.FindBySerial(enemy.Serial) == None:
            Misc.Pause(500)
    Player.HeadMessage( colors[ 'green' ], 'The enemy is dead.' )

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

