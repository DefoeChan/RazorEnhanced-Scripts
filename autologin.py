#### auto login for server downtime  ####

from time import sleep
from datetime import datetime
import clr, time, sys, System

clr.AddReference('System')
clr.AddReference('System.Drawing')
clr.AddReference('System.Windows.Forms')
clr.AddReference('System.Data')
clr.AddReference('IronPython')
from System.Threading import ThreadStart, Thread
from System.Collections.Generic import List
from System import Byte
from System.Drawing import Point, Color, Size
from System.Windows.Forms import *
import sys
sys.path.append(r'C:\Program Files\IronPython 2.7\Lib')
import ctypes
User32 = ctypes.WinDLL('User32.dll')


Journal.Clear()
serverdowntime = 1200000   #20 mins 1,200,000

class SimpleTextBoxForm(Form):
    def __init__(self):
        self.Text = "Mourns Autologin"
        self.Width = 190
        self.Height = 225
        self.BackColor = Color.FromArgb(25,25,25)
        self.ForeColor = Color.FromArgb(231,231,231)
        self.FormBorderStyle = FormBorderStyle.FixedDialog
        self.TopMost = True
        self.CenterToScreen()
        
        self.button = Button()
        self.button.Text = 'Auto Recon'
        self.button.Width = 80
        self.button.Height = 40
        self.button.Location = Point(5,125)
        self.button.BackColor = Color.FromArgb(25,100,25)
        self.button.ForeColor = Color.FromArgb(231,231,231)
        self.button.Click += self.start
        
        self.button1 = Button()
        self.button1.Text = 'Switch Char'
        self.button1.Width = 80
        self.button1.Height = 40
        self.button1.Location = Point(85,125)
        self.button1.BackColor = Color.FromArgb(25,100,25)
        self.button1.ForeColor = Color.FromArgb(231,231,231)
        self.button1.Click += self.switchChar
        
        self.textbox = TextBox()
        if Misc.ReadSharedValue("UserName"):
            self.textbox.Text =  Misc.ReadSharedValue("UserName")
        else:
            self.textbox.Text = "User Name"
        self.textbox.Location = Point(10,25 )
        self.textbox.Width = 150
                              
        self.textbox3 = TextBox()
        if Misc.ReadSharedValue("password"):
            self.textbox3.Text = "*********"
        else:
            self.textbox3.Text = "Password"
        self.textbox3.Location = Point(10,55 )
        self.textbox3.Width = 150
        
        self.char = ComboBox()
        self.char.Location = Point(10,85)
        self.char.DataSource = 'Character Number',1,2,3,4,5,6
        
        self.box = GroupBox()
        self.box.BackColor = Color.FromArgb(25,25,25)
        self.box.ForeColor = Color.FromArgb(25,200,23)
        self.box.Size = Size(165, 175)
        self.box.Location = Point(2, 2)
        self.box.Text = Player.Name
        
        self.Controls.Add(self.textbox)
        self.Controls.Add(self.textbox3)
        self.Controls.Add(self.button)
        self.Controls.Add(self.button1)
        self.Controls.Add(self.char)
        self.Controls.Add(self.box)
        
    def start(self,s,a):
        Misc.SendMessage('Starting',78)
        if self.textbox.Text != "User Name":
            Misc.SetSharedValue("UserName",self.textbox.Text)
        if self.textbox3.Text != "Password":
            if self.textbox3.Text != "*********":
                Misc.SetSharedValue("password",self.textbox3.Text)
        t = Thread(ThreadStart(self.loginThread))
        t.Start()
        Form.Close(form)
        
    def login(self):
        number = int(self.char.Text)
        acctNameLoc = [350,325]
        passWordLoc = [350,375]
        def enterPassword():
            User32.SetCursorPos(passWordLoc[0],passWordLoc[1])
            User32.mouse_event(2, 0, 0, 0,0) # left down
            User32.mouse_event(4, 0, 0, 0,0) # left up
            for letter in Misc.ReadSharedValue('password'):
                SendKeys.SendWait("{}".format(letter))
                Misc.Pause(100)
            SendKeys.SendWait("{enter}")
            Misc.Pause(1000)
            SendKeys.SendWait("{enter}")##########selects last shard
            Misc.Pause(1000)
            
        def enterUserName():
            User32.SetCursorPos(acctNameLoc[0],acctNameLoc[1])
            User32.mouse_event(2, 0, 0, 0,0) # left down
            User32.mouse_event(4, 0, 0, 0,0) # left up
            for r in range(15):
                SendKeys.SendWait("{backspace}") 
            for letter in self.textbox.Text:
                SendKeys.SendWait("{}".format(letter))
                Misc.Pause(100)
                
        def selectChar(number):
            if number == 1:
                ycoord = 160
            elif number == 2:
                ycoord = 210
            elif number == 3:
                ycoord = 260
            elif number == 4:
                ycoord = 300
            elif number == 5:
                ycoord = 340
            elif number == 6:
                ycoord = 380    
            User32.SetCursorPos(350,ycoord)
            Misc.Pause(1000)
            User32.mouse_event(2, 0, 0, 0,0) # left down
            User32.mouse_event(4, 0, 0, 0,0) # left up 
            User32.mouse_event(2, 0, 0, 0,0) # left down
            User32.mouse_event(4, 0, 0, 0,0) # left up   
            SendKeys.SendWait("{enter}") 
        enterUserName()
        enterPassword()
        selectChar(number)
        
    def switchChar(self,s,a):
        if self.textbox.Text != "User Name":
            Misc.SetSharedValue("UserName",self.textbox.Text)
        if self.textbox3.Text != "Password":
            if self.textbox3.Text != "*********":
                Misc.SetSharedValue("password",self.textbox3.Text)
        Misc.Disconnect()
        Misc.Pause(1500)
        self.login()
                            
    def loginThread(self):  ##### 10 second check to make sure ur logged in       
        oldValue = 0
        while True:
            if Journal.GetLineText("approximately 2 minutes"):
                Player.HeadMessage(30,"Server Going Down")
                Misc.Pause(2000)
                Timer.Create('downtime',30000)           
                Misc.Disconnect()
            Misc.SendMessage('Auto Login Running')
            if oldValue == Misc.ReadSharedValue('check'):
                if Timer.Check('downtime'):
                    Misc.Pause(serverdowntime)
                self.login()
                break          
            oldValue = Misc.ReadSharedValue('check')
            Misc.Pause(10000)
            
Misc.SetSharedValue('check',1)                                        
form = SimpleTextBoxForm()
Application.Run(form)
while True:
    doublecheck = Player.Hits
    x = Misc.ReadSharedValue('check')
    Misc.SetSharedValue('check',x + 1) #### counter to assure connected
    Misc.Pause(4000)
        