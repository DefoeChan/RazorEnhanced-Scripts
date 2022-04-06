import Misc, Items
from Scripts.utilities.colors import colors

containerToSort = 0x4002C1C3
containerToSort = Items.FindBySerial( containerToSort )
Items.UseItem( containerToSort )
Misc.Pause( 100 )

circleOneBag = 0x4003359D
circleTwoBag = 0x400335A2
circleThreeBag = 0x400335A1
circleFourBag = 0x400335A3
circleFiveBag = 0x4003359C
circleSixBag = 0x4003359F
circleSevenBag = 0x4003359E
circleEightBag = 0x400335A0

from Scripts.glossary.spells import spells
from Scripts.glossary.items.spellScrolls import spellScrolls
spellScrollIDs = [ spellScrolls[ scroll ].itemID for scroll in spellScrolls ]
from Scripts.utilities.items import MoveItem

for item in containerToSort.Contains:
    if item.ItemID in spellScrollIDs:
        scrollType = None
        for scroll in spellScrolls:
            if spellScrolls[ scroll ].itemID == item.ItemID:
                scrollType = spellScrolls[ scroll ]
                break
        
        spell = spells[ scrollType.name.replace( ' scroll', '' ) ]
        if spell.circle == 1:
            MoveItem( Items, Misc, item, circleOneBag )
        elif spell.circle == 2:
            MoveItem( Items, Misc, item, circleTwoBag )
        elif spell.circle == 3:
            MoveItem( Items, Misc, item, circleThreeBag )
        elif spell.circle == 4:
            MoveItem( Items, Misc, item, circleFourBag )
        elif spell.circle == 5:
            MoveItem( Items, Misc, item, circleFiveBag )
        elif spell.circle == 6:
            MoveItem( Items, Misc, item, circleSixBag )
        elif spell.circle == 7:
            MoveItem( Items, Misc, item, circleSevenBag )
        elif spell.circle == 8:
            MoveItem( Items, Misc, item, circleEightBag )

Misc.SendMessage("Done!", colors['green'])