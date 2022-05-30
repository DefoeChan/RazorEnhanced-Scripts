import json
import sys

Misc.Pause( 5000 )
if Player.GetRealSkillValue( 'Healing' ) < 50:
    Misc.SendMessage( 'No Healing, stopping script',33)
    Misc.Pause( 200 )
    sys.exit()
    
def server():
    while 1 > 0:
        if Journal.SearchByName('Ready to deploy', 'Kopier'):
            Player.ChatGuild('Patrol/HY101')
        Journal.Clear()
        Misc.Pause(5000)    

if Player.Name == 'Defoe':
    server()

if Player.GetRealSkillValue('Animal Taming') >= 100 and Player.Name != 'Defoe':
    Player.ChatGuild('Patrol/HY101')

#with open('C:\\Program Files (x86)\\UOForever\\UO\\server.json', 'w') as f:
#    f.write('line')
#