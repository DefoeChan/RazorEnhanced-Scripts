playerSerial = 0x0013370F
distanceToPlayer = 2
        
if not Player.InRangeMobile(playerSerial, distanceToPlayer):
    mobile = Mobiles.FindBySerial(playerSerial)
    Player.PathFindTo(mobile.Position.X, mobile.Position.Y, mobile.Position.Z) 
    
Misc.Pause(100)