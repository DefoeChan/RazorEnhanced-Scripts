from Scripts.Glossary.colors import colors

IsTamer = False
IsWarrior = False
IsArcher = False
IsMage = False
IsBard = False

if Player.Name == 'Defoe':
    mount = 0x0000AA92
    pet = 0x00175EC1
    runebook = 0x40254F88
    
elif Player.Name == 'Chillichen':
    mount = 0x0000AA92
    pet = 0x00175EC1
    runebook = 0x40C63288
    
elif Player.Name == 'Coronavirus':
    mount = 0x0000AA92
    pet = 0x00175EC1
    runebook = 0x40C62F68
    
elif Player.Name == 'Ubermacht':
    mount = 0x0000AA92
    pet = 0x00175EC1
    runebook = 0x40EE9436

elif Player.Name == 'Kopier':
    mount = 0x0000AA92
    pet = 0x00175EC1
    runebook = 0x40EE9C40
    
elif Player.Name == 'Ludwig Dieter':
    mount = 0x0000AA92
    pet = 0x00175EC1
    runebook = 0x40EE9E00
    
elif Player.Name == 'A':
    mount = 0x0000AA92
    pet = 0x00175EC1
    runebook = 0x435D18E4
    
elif Player.Name == 'B':
    mount = 0x0000AA92
    pet = 0x00175EC1
    runebook = 0x40EE933E
    
elif Player.Name == 'C':
    mount = 0x0000AA92
    pet = 0x00175EC1
    runebook = 0x40EE925A
    
elif Player.Name == 'Dena':
    mount = 0x0000AA92
    pet = 0x00175EC1
    runebook = 0x40C631A6
    
elif Player.Name == 'E':
    mount = 0x0000AA92
    pet = 0x00175EC1
    runebook = 0x40C63320
    
elif Player.Name == 'Felberta':
    mount = 0x0000AA92
    pet = 0x00175EC1
    runebook = 0x40C62A4B
    
elif Player.Name == 'G':
    mount = 0x0000AA92
    pet = 0x00175EC1
    runebook = 0x40C62BC2
    
elif Player.Name == 'H':
    mount = 0x0000AA92
    pet = 0x00175EC1
    runebook = 0x40C62F21
    
elif Player.Name == 'I':
    mount = 0x0000AA92
    pet = 0x00175EC1
    runebook = 0x40C633CC
    
elif Player.Name == 'J':
    mount = 0x0000AA92
    pet = 0x00175EC1
    runebook = 0x40C63206
    
elif Player.Name == 'K':
    mount = 0x0000AA92
    pet = 0x00175EC1
    runebook = 0x40C62AEB
    
elif Player.Name == 'L':
    mount = 0x0000AA92
    pet = 0x00175EC1
    runebook = 0x40C62479
    
elif Player.Name == 'M':
    mount = 0x0000AA92
    pet = 0x00175EC1
    runebook = 0x40C63093
    
elif Player.Name == 'N':
    mount = 0x0000AA92
    pet = 0x00175EC1
    runebook = 0x40C6325A
    
elif Player.Name == 'O':
    mount = 0x0000AA92
    pet = 0x00175EC1
    runebook = 0x40C63018
    
elif Player.Name == 'P':
    mount = 0x0000AA92
    pet = 0x00175EC1
    runebook = 0x40C634A3
    
elif Player.Name == 'Q':
    mount = 0x0000AA92
    pet = 0x00175EC1
    runebook = 0x40C62777
    
elif Player.Name == 'R':
    mount = 0x0000AA92
    pet = 0x00175EC1
    runebook = 0x40C62B5E
    
else:
    mount = 0x0000AA92
    pet = 0x00175EC1
    runebook = 0x40254F88
    
    
from Scripts.Glossary.Rail.BritainCemetery import waypoints

def Pathfind(x, y, z):
    Player.PathFindTo(x, y, z)
    distance = Distance(Player.Position.X, Player.Position.Y, x, y)
    while distance > 1:
        distance = Distance(Player.Position.X, Player.Position.Y, x, y)
        Player.HeadMessage(0, distance)
        Misc.Pause(100)

def Distance(x1, y1, x2, y2):
    return max(abs(x1 - x2) , abs(y1 - y2))
    
def AttackStyle():
    global IsTamer
    global IsWarrior
    global IsArcher
    global IsMage
    global IsBard
    
    if Player.GetRealSkillValue('Animal Taming') > 70 and Player.Followers >= 3:
        IsTamer = True
    if Player.GetRealSkillValue('Swords') >= 30 or Player.GetRealSkillValue('Fencing') >= 30 or Player.GetRealSkillValue('Macing') >= 30:
        IsWarrior = True
    if Player.GetRealSkillValue('Archery') >= 30:
        IsArcher = True
    if Player.GetRealSkillValue('Magery') >= 30 and Player.GetRealSkillValue('EvalInt') >= 30:
        IsMage = True
    if Player.GetRealSkillValue('Provocation') >= 30:
        IsBard = True
        
def HomeBank():
    global status
    if Player.DistanceTo(Items.FindBySerial(0x41BDCCC7)) <= 2:
        Organizer.RunOnce('gold', Player.Backpack.Serial, 0x41BDCCC7, 300)
        Organizer.RunOnce('reagents', Player.Backpack.Serial, 0x40A7B9F2, 300)
        if Player.GetRealSkillValue('Magery') >= 30:
            Restock.RunOnce('reagents', 0x40A7B9F2, Player.Backpack.Serial, 300)
        if Player.GetRealSkillValue('Healing') >= 30 or Player.GetRealSkillValue('Veterinary') >= 30:
            Restock.RunOnce('bandages', 0x40A7B9F2, Player.Backpack.Serial, 300)
    while Player.Hits < Player.HitsMax or Player.Mana < Player.ManaMax or Player.Stam < Player.StamMax: Misc.Pause(1000)
    status = 'Ready'
    
def Deploying():
    global status
    
    
def SearchDestroy(enemy):
    Player.HeadMessage( colors[ 'red' ], 'Attacking ' + str(enemy.Name) + '!' )
    if Target.HasTarget():
        Target.TargetExecute( emeny.Serial )
    else:
        Player.Attack( enemy )
        Target.SetLast( enemy )
        while not Mobiles.FindBySerial(enemy.Serial) == None:
            if IsWarrior or IsArcher:
                Chase(enemy)
                Misc.Pause(1000)
#            if IsArcher:
#                #enemylastposition = enemy.Position
#                Misc.Pause(500)
            if IsTamer:
                Misc.Pause(500)
            if IsMage:
                if Player.Followers < 4 and Player.Mana >= 50 and \
                    Items.BackpackCount(0x0F7B) > 2 and \
                    Items.BackpackCount(0x0F86) > 2 and \
                    Items.BackpackCount(0x0F8D) > 2 and \
                    Items.BackpackCount(0x0F8C) > 2:
                    Spells.CastMagery('Summon Daemon')
                    Misc.Pause(4000)
                    Player.ChatSay(0, "All guard")
                Misc.Pause(500)
    for waypoint in waypoints:
        Pathfind(waypoint[0], waypoint[1], waypoint[2])    
#    if IsArcher:
#        Player.PathFindTo(ememylastposition)
#    CheckBackpack()
    
    
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
        EnemyPosition = enemy.Position # Your main characters position
        SelfPosition = Player.Position # This characters position
        LocDiffX = EnemyPosition.X - SelfPosition.X #The difference of x coordinates
        LocDiffY = EnemyPosition.Y - SelfPosition.Y #The difference of y coordinates
        cantGetThere += 1
        if cantGetThere >= cantGetThereMax:
            Player.PathFindTo(enemy.Position.X, enemy.Position.Y, enemy.Position.Z)
            Timer.Create('pathfindingtimer', 10000)
            while not Player.InRangeMobile(enemy, 1) and Timer.Check('pathfindingtimer'):
                Misc.Pause(1000)
                if not Player.InRangeMobile(enemy, 30):
                    break
            Player.Attack( enemy )
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
            #Player.HeadMessage( colors[ 'green' ], 'pf false' )
            cantGetThere = 0
            Misc.Pause(200)
        Player.Attack( enemy )
        Player.HeadMessage( colors[ 'red' ], cantGetThere )
        Misc.Pause(50)
    Player.HeadMessage( colors[ 'green' ], 'The enemy is dead.' )
    Target.AttackTargetFromList('mobs')
    Misc.Pause(3000)

        
def CheckBackpack():
    global status
    if Player.Weight >= Player.MaxWeight - 20: status = 'GoingHome' # Weight
    if Items.BackpackCount(0x0EED) >= 10000: status = 'GoingHome' # Gold
    if IsWarrior:
        if Items.BackpackCount(0x0E21) < 10: status = 'GoingHome' # Bandages
        if Items.BackpackCount(0x0E21) < 10: status = 'GoingHome' # Bandages
    Player.HeadMessage( colors[ 'red' ], 'Going Home!' )
        
# Main        
AttackStyle()
status = 'Hunting'
status = 'Hunting'
while status == 'Hunting':
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
    

if status == 'GoingHome':
    Player.HeadMessage( colors[ 'red' ], 'Going Home Now!' )