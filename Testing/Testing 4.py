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
    
for waypoint in waypoints:
    Pathfind(waypoint[0], waypoint[1], waypoint[2])
    
        
    


    
