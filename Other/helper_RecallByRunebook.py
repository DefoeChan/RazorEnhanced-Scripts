'''
Te setup: set the runebook_serial variable according to your runebook.
To use: say the exact name of the rune in Runebook and then execute the
    corresponding function: RecallByName or GateByName
'''

import Items, Misc, Player, Gumps, Journal

runebook_serial = 0x4002E606

#Misc.Inspect()

######
class RuneBookTeleport:
    
    runebook_serial = 0
    runebook_gump_id = 89
    search_rune = ""
    found_rune_number = 0
    runes_amount = 0
    
    start_action_recall = 49
    start_action_sacred_journey = 74
    start_action_gate = 99
    
    def __init__(self, runebook_serial):
        self.runebook_serial = runebook_serial
        self.getRunesAmount()
        self.search_rune = self.getRuneText()
        self.getRuneNumberByName()

        if self.found_rune_number == 0:
            Misc.SendMessage("No rune found",0xff0000)
            Gumps.CloseGump(self.runebook_gump_id)
    
    def getRuneText(self):
        all_text = Journal.GetTextBySerial(Player.Serial)
        return all_text[len(all_text) - 1]

    # Get the amount of runes in book
    def getRunesAmount(self):

        Items.UseItem(self.runebook_serial)
        Gumps.WaitForGump(self.runebook_gump_id, 10000)
        data = Gumps.LastGumpGetLineList()
        data_length = len(data)
        if data_length > 21:
            self.runes_amount = (data_length - 85)/3
    
    # Get found rune number.      
    def getRuneNumberByName(self):
        
        first_line = 53 + 2 * self.runes_amount
        for i in range(self.runes_amount):
            #Gumps.LastGumpGetLine(i).lower()
            
            if self.search_rune == Gumps.LastGumpGetLine(first_line + i).lower():
                self.found_rune_number = i + 1
                break
        
    def recall(self):
        if self.found_rune_number != 0:
            Gumps.SendAction(89, self.start_action_recall + self.found_rune_number)
        
    def gate(self):
        if self.found_rune_number != 0:
            Gumps.SendAction(89, self.start_action_gate + self.found_rune_number)

# Cast a Recall
def RecallByName():    
    rbt = RuneBookTeleport(runebook_serial)
    rbt.recall()

# Open a gate
def GateByName():
    rbt = RuneBookTeleport(runebook_serial)
    rbt.gate()
