import json

sys.path.append("C:\Program Files\IronPython 2.7\Lib") # path to your modules
import requests

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