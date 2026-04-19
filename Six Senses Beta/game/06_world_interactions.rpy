# --- Day 1 ---
screen mhallwayd1(): 
    imagebutton:
        idle "invisible_idle"
        xysize (150, 200) 
        xpos 1560 ypos 450
        action Return("go_hallway2")
        tooltip "Go to Hallway 2"
    add "images/ui/arrow_idle.png" xpos 1590 ypos 570 at transform:
        zoom 0.3
        rotate 190
        alpha 0.3
    if scenario_picker1 or scenario_picker2:
        imagebutton:
            idle "invisible_idle"
            xysize (170, 400)
            xpos 400 ypos 400
            action Jump("confirm_next_day")
            tooltip "End the Day"
    else:
        imagebutton:
            idle "invisible_idle"
            xysize (170, 400)
            xpos 400 ypos 400
            action Notify("I haven't found enough evidence to leave yet.")
            tooltip "Evidence Required"
    add "images/ui/arrow_idle.png" xpos 280 ypos 500 at transform:
        zoom 0.3
        rotate -90
        alpha 0.5
    imagebutton:
        idle "characters/dan.png"
        hover "characters/dan.png"
        focus_mask True
        at transform:
            nearest True
            zoom 0.2
        xpos 1260 ypos 460
        action Jump("talk_to_dan") 
        tooltip "Talk to Dan (Janitor)"

screen hallwayd1():
    imagebutton:
        idle "images/ui/door_idle.png" 
        hover "images/ui/door_hover.png"
        at transform:
            nearest True
            zoom 1
        xpos 740 ypos 263
        action Return("go_storage") 
        tooltip "Enter Storage Room"
    imagebutton:
        idle "images/ui/arrow_idle.png"
        hover "images/ui/arrow_hover.png"
        at transform:
            xpos 1990 ypos 430
            anchor (0.5, 0.5)
            zoom 0.5
            rotate -90
            alpha 0.5
        xysize (1000, 1080) 
        xpos 0 ypos 0 
        action Return("go_mhallway")
        tooltip "Go to Main Hallway"
    imagebutton:
        idle "images/ui/arrow_idle.png"
        hover "images/ui/arrow_hover.png"
        at transform:
            xpos -100 ypos 800
            anchor (0.5, 0.5)
            zoom 0.5
            rotate 90
            alpha 0.5
        xysize (1000, 1080) 
        xpos 0 ypos 0
        action Return("go_stairs")
        tooltip "Go to Stairs"

screen stairsd1():
    imagebutton:
        idle "invisible_idle"
        xysize (800, 800) 
        xpos 1100 ypos 130
        action Return("go_cctv_hallway")
        tooltip "Go to CCTV Hallway"
    add "images/ui/arrow_idle.png" xpos 1700 ypos 470 at transform:
        zoom 0.5
        rotate 180
        alpha 0.3
    imagebutton:
        idle "images/ui/arrow_idle.png"
        hover "images/ui/arrow_hover.png"
        at transform:
            nearest True
            zoom 0.5
            alpha 0.3
        xpos 800 ypos 800 
        action Return("go_hallway2")
        tooltip "Return"
    imagebutton:
        idle "invisible_idle"
        xysize (800, 800) 
        xpos 0 ypos 100
        action Return("go_lockers")
        tooltip "Go to Lockers"
    add "images/ui/arrow_idle.png" xpos 10 ypos 470 at transform:
        zoom 0.5
        rotate -70
        alpha 0.3

screen cctv_hallwayd1():
    imagebutton:
        idle "images/ui/arrow_idle.png"
        hover "images/ui/arrow_hover.png"
        at transform:
            nearest True
            zoom 0.3
        xpos 50 ypos 700 
        action Return("go_stairs")
        tooltip "Return"
    imagebutton:
        idle "invisible_idle"
        hover "translucent_hover"
        xysize (85, 700) 
        xpos 435 ypos 250
        action Return("go_cctv_room")
        tooltip "Go to CCTV Room"
        
screen cctv_roomd1():
    imagebutton:
        idle "invisible_idle"
        hover "translucent_hover"
        xysize (400, 300) 
        xpos 800 ypos 300
        action Return("cctv_monitor")
    imagebutton:
        idle "images/ui/arrow_idle.png"
        hover "images/ui/arrow_hover.png"
        at transform:
            nearest True
            zoom 0.3
        xpos 50 ypos 700 
        action Return("go_cctv_hallway")
        tooltip "Return"

screen storage_roomd1():
    imagebutton:
        idle "images/ui/arrow_idle.png"
        hover "images/ui/arrow_hover.png"
        at transform:
            nearest True
            zoom 0.3
        xpos 50 ypos 700 
        action Return("go_hallway2")
        tooltip "Exit Storage Room"
    if not scenario_picker1:
        imagebutton:
            idle "images/cs/body.png"
            hover "images/cs/bodyh.png"
            focus_mask True
            at transform:
                nearest True
                zoom 1
            xpos 616 ypos 537
            action Return("go_body")
            tooltip("Examine the body")
    else:
        imagebutton:
            idle "images/cs/chalkbody.png"
            hover "images/cs/chalkbody.png"
            focus_mask True
            at transform:
                nearest True
                zoom 1
            xpos 0 ypos 0
            action Return("go_body")
            tooltip("Examine the body")
    if not evidence_taken["waterbottle"]:
        imagebutton:
            idle "images/cs/waterbottle.png"
            hover "images/cs/waterbottleh.png"
            focus_mask True
            at transform:
                nearest True
                zoom 1
            xpos 690 ypos 743
            action [
                Function(add_item, "Half-Empty Bottle", "The bottle is empty, likely tossed aside by someone while he was tearing through Pat's things. It’s just another piece of debris from the suspect's frantic search, a silent witness to how out of control the situation has become.", "images/cs/waterbottle.png"),
                SetDict(evidence_taken, "waterbottle", True),
                Show("item_get_message", message="You found a Water bottle. It’s looks like its been crushed underfoot, the thin plastic crinkling loudly as you lift it from the mess on the ground.")
            ]
            tooltip "Water Bottle"
    if not evidence_taken["patbag"]:
        imagebutton:
            idle "images/cs/patbag.png"
            hover "images/cs/patbagh.png"
            focus_mask True
            at transform:
                nearest True
                zoom 1
            xpos 355 ypos 798
            action [
                Function(add_item, "Bag", "You examine the bag’s hollow interior. It belongs to Pat, but it’s clear someone went through it with violent intent. Someone must have ransacked this, scattering her belongings everywhere in a desperate, failed search for something.", "images/cs/patbag.png"),
                SetDict(evidence_taken, "patbag", True),
                Show("item_get_message", message="You found a bag. It’s completely empty, the zipper pulled wide and the lining turned partially inside out.")
            ]
            tooltip "Bag"
    if not evidence_taken["patphone"]:
        imagebutton:
            idle "images/cs/patphone.png"
            hover "images/cs/patphoneh.png"
            focus_mask True
            at transform:
                nearest True
                zoom 1
            xpos 700 ypos 965
            action [
                Function(add_item, "Phone", "The victim’s smartphone face-down on the tiles. The screen is cracked, as if it were thrown or dropped, but the screen itself is still working- with notifications filling the display.", "images/cs/patphone.png"),
                SetDict(evidence_taken, "patphone", True),
                Show("item_get_message", message="You found a phone. As you try to get inside the phone, it’s locked behind a passcode. And as if taunting you, the lock-screen shows a plethora of messages and missed calls.")
            ]
            tooltip "Phone"
    if not evidence_taken["powder"]:
        imagebutton:
            idle "images/cs/powder.png"
            hover "images/cs/powderh.png"
            focus_mask True
            at transform:
                nearest True
                zoom 1
            xpos 949 ypos 810
            action [
                Function(add_item, "Drugs", "Found laid on the floor next to a plastic bottle. These appear to be high-grade synthetics. Their presence puts a heavy suspicion on whoever was carrying them, although it is also possible they were force-fed to the individual.", "images/cs/powder.png"),
                SetDict(evidence_taken, "powder", True),
                Show("item_get_message", message="You found some Drugs. You find a bag of party drugs laid on the floor. They appear to be high-grade synthetics. This puts a heavy suspicion on whoever was carrying them.")
            ]
            tooltip "Drugs"
    if not evidence_taken["id"]:
        imagebutton:
            idle "images/cs/id.png"
            hover "images/cs/idh.png"
            focus_mask True
            at transform:
                nearest True
                zoom 1
            xpos 1190 ypos 865
            action [
                Function(add_item, "ID", "You hold the frayed lanyard. The blood on the fabric is a grim reminder of the struggle that took place here. It was tossed aside like trash, likely during the moment Pat was overpowered.", "images/cs/id.png"),
                SetDict(evidence_taken, "id", True),
                Show("item_get_message", message="You found an ID. It’s roughed up and stained with fresh blood, looking less like a lost item and more like something that was forcibly ripped away and thrown.")
            ]
            tooltip "ID"

screen bodyd1():
    imagebutton:
        idle "images/ui/arrow_idle.png"
        hover "images/ui/arrow_hover.png"
        at transform:
            nearest True
            zoom 0.3
        xpos 50 ypos 700 
        action Return("go_storage")
        tooltip "Return"
    imagebutton:
        idle "images/cs/wound1.png"
        hover "images/cs/wound1h.png"
        focus_mask True
        at transform:
            nearest True
            zoom 1
        xpos 0 ypos 0
        action Function(record_clue, "Pat (Victim)", "TORSO STAB – (LOWER RIGHT TORSO) | Puncture wound in the lower abdomen. May have hit parts of the bowel. Even if not immediately fatal, could have led to severe infection")
        tooltip "Examine the Stab Wound"
    imagebutton:
        idle "images/cs/wound2.png"
        hover "images/cs/wound2h.png"
        focus_mask True
        at transform:
            nearest True
            zoom 1
        xpos 0 ypos 0
        action Function(record_clue, "Pat (Victim)", "TORSO STAB – (MID-LEFT TORSO) | Deep stab wound on the left side of the torso. Likely the main source of internal bleeding. Possible damage to the spleen or left kidney, exact injury needs confirmation")
        tooltip "Examine the Stab Wound"
    imagebutton:
        idle "images/cs/wound3.png"
        hover "images/cs/wound3h.png"
        focus_mask True
        at transform:
            nearest True
            zoom 1
        xpos 0 ypos 0
        action Function(record_clue, "Pat (Victim)", "STAB – (UPPER CHEST) | High pectoral penetration. Likely caused lung damage.")
        tooltip "Examine the Stab Wound"
    imagebutton:
        idle "images/cs/bruise1.png"
        hover "images/cs/bruise1h.png"
        focus_mask True
        at transform:
            nearest True
            zoom 1
        xpos 0 ypos 0
        action Function(record_clue, "Pat (Victim)", "FOREARM BRUISE | Bruising on the forearms consistent with defensive wounds. Suggests the victim tried to resist during the attack.")
        tooltip "Examine the Forearm Bruise"
    imagebutton:
        idle "images/cs/burnmarks.png"
        hover "images/cs/burnmarksh.png"
        focus_mask True
        at transform:
            nearest True
            zoom 1
        xpos 0 ypos 0
        action Function(record_clue, "Pat (Victim)", "BURN MARK | Single circular burn on the left wrist — likely a cigarette.")
        tooltip "Examine the Burn Mark"
    imagebutton:
        idle "images/cs/bruise2.png"
        hover "images/cs/bruise2h.png"
        focus_mask True
        at transform:
            nearest True
            zoom 1
        xpos 0 ypos 0
        action Function(record_clue, "Pat (Victim)", "NECK BRUISE | Bruising around the neck. Could be from being restrained, held down, or possibly strangled during the assault.")
        tooltip "Examine the Neck Bruise"
    imagebutton:
        idle "images/cs/mouthfoam.png"
        hover "images/cs/mouthfoamh.png"
        focus_mask True
        at transform:
            nearest True
            zoom 1
        xpos 0 ypos 0
        action Function(record_clue, "Pat (Victim)", "MOUTH FOAM | Presence of foam around the mouth—could indicate drowning or aspiration. The positioning suggests the victim may have been forced to ingest something. Could be related to the drugs i found in the storage room, or maybe something else entirely.")
        tooltip "Examine the mouth foam"

screen lockersd1():
    imagebutton:
        idle "images/ui/arrow_idle.png"
        hover "images/ui/arrow_hover.png"
        at transform:
            nearest True
            zoom 0.3
        xpos 50 ypos 700 
        action Return("go_stairs")
        tooltip "Return"
                
# --- Day 2 ---
screen mhallwayd2():
    imagebutton:
        idle "invisible_idle"
        xysize (150, 200) 
        xpos 1560 ypos 450
        action Return("go_hallwayd2")
        tooltip "Go to Hallway 2"
    add "images/ui/arrow_idle.png" xpos 1590 ypos 570 at transform:
        zoom 0.3
        rotate 190
        alpha 0.3
    if evidence_taken["cigarette"] or evidence_taken["knife"]:
        imagebutton:
            idle "invisible_idle"
            xysize (170, 400)
            xpos 400 ypos 400
            action Jump("confirm_next_day2")
            tooltip "End the Day"
    else:
        imagebutton:
            idle "invisible_idle"
            xysize (170, 400)
            xpos 400 ypos 400
            action Notify("I haven't found enough evidence to leave yet.")
            tooltip "Evidence Required"
    add "images/ui/arrow_idle.png" xpos 280 ypos 500 at transform:
        zoom 0.3
        rotate -90
        alpha 0.5

screen hallwayd2():
    imagebutton:
        idle "images/ui/door_idle.png" 
        hover "images/ui/door_hover.png"
        at transform:
            nearest True
            zoom 1
        xpos 740 ypos 263
        action Return("go_storaged2") 
        tooltip "Enter Storage Room"
    imagebutton:
        idle "images/ui/arrow_idle.png"
        hover "images/ui/arrow_hover.png"
        at transform:
            xpos 1990 ypos 430
            anchor (0.5, 0.5)
            zoom 0.5
            rotate -90
            alpha 0.5
        xysize (1000, 1080) 
        xpos 0 ypos 0
        action Return("go_mhallwayd2")
        tooltip "Go to Main Hallway"
    imagebutton:
        idle "images/ui/arrow_idle.png"
        hover "images/ui/arrow_hover.png"
        at transform:
            xpos -100 ypos 800
            anchor (0.5, 0.5)
            zoom 0.5
            rotate 90
            alpha 0.5
        xysize (1000, 1080) 
        xpos 0 ypos 0
        action Return("go_stairsd2")
        tooltip "Go to Stairs"

screen storage_roomd2():
    imagebutton:
        idle "images/ui/arrow_idle.png"
        hover "images/ui/arrow_hover.png"
        at transform:
            nearest True
            zoom 0.3
        xpos 50 ypos 700 
        action Return("go_hallwayd2")
        tooltip "Exit Storage Room"

    imagebutton:
        idle "images/cs/chalkbody.png"
        hover "images/cs/chalkbody.png"
        focus_mask True
        at transform:
            nearest True
            zoom 1
        xpos 0 ypos 0
        action Show("item_get_message", message="The body seems to have been taken care of by the forensic team. You'll get another chance to examine the body at a later date.")
        tooltip("Examine the body")

    imagebutton:
        idle "images/ui/arrow_idle.png"
        hover "images/ui/arrow_hover.png"
        at transform:
            nearest True
            zoom 0.3
        xpos 50 ypos 700 
        action Return("go_hallwayd2")
        tooltip "Exit Storage Room"

    # Rubble: clickable only if not moved yet
    if not rubble_moved:
        imagebutton:
            idle "images/cs/rubble1.png"
            hover "images/cs/rubble1.png"
            focus_mask True
            action [SetVariable("rubble_moved", True), Show("item_get_message", message="You move the rubble aside... something glints underneath.")]
            tooltip "Move rubble"
    else:
        # After moving, rubble becomes static (non‑clickable)
        add "images/cs/rubble2.png"

    # Cigarette button: visible only after rubble moved and not yet collected
    if rubble_moved and not evidence_taken["cigarette"]:
        imagebutton:
            idle "images/cs/cigarette.png"
            hover "images/cs/cigarette.png"
            focus_mask True
            action [
                Function(add_item, "Cigarette Butt", "You found a crushed cigarette butt on the floor. The filter is still fresh, and the marks match the diameter of the burns on Pat’s skin—all that’s left is to run the fingerprints to confirm exactly whose hand was on it.", "images/cs/cigaretteicon.png"),
                SetDict(evidence_taken, "cigarette", True),
                Show("item_get_message", message="You found a crushed cigarette butt on the floor.")
            ]
            tooltip "Take cigarette butt"
    
    # Other evidence (same as day1, but only if not already taken)
    if not evidence_taken["waterbottle"]:
        imagebutton:
            idle "images/cs/waterbottle.png"
            hover "images/cs/waterbottleh.png"
            focus_mask True
            at transform:
                nearest True
                zoom 1
            xpos 690 ypos 743
            action [
                Function(add_item, "Half-Empty Bottle", "The bottle is empty, likely tossed aside by someone while he was tearing through Pat's things.", "images/cs/waterbottle.png"),
                SetDict(evidence_taken, "waterbottle", True),
                Show("item_get_message", message="You found a Water bottle.")
            ]
            tooltip "Water Bottle"
    if not evidence_taken["patbag"]:
        imagebutton:
            idle "images/cs/patbag.png"
            hover "images/cs/patbagh.png"
            focus_mask True
            at transform:
                nearest True
                zoom 1
            xpos 355 ypos 798
            action [
                Function(add_item, "Bag", "Empty bag, zipper pulled wide.", "images/cs/patbag.png"),
                SetDict(evidence_taken, "patbag", True),
                Show("item_get_message", message="You found a bag.")
            ]
            tooltip "Bag"
    if not evidence_taken["patphone"]:
        imagebutton:
            idle "images/cs/patphone.png"
            hover "images/cs/patphoneh.png"
            focus_mask True
            at transform:
                nearest True
                zoom 1
            xpos 700 ypos 965
            action [
                Function(add_item, "Phone", "Pat's phone. Locked.", "images/cs/patphone.png"),
                SetDict(evidence_taken, "patphone", True),
                Show("item_get_message", message="You found a phone.")
            ]
            tooltip "Phone"
    if not evidence_taken["powder"]:
        imagebutton:
            idle "images/cs/powder.png"
            hover "images/cs/powderh.png"
            focus_mask True
            at transform:
                nearest True
                zoom 1
            xpos 949 ypos 810
            action [
                Function(add_item, "Drugs", "High-grade synthetics.", "images/cs/powder.png"),
                SetDict(evidence_taken, "powder", True),
                Show("item_get_message", message="You found some Drugs.")
            ]
            tooltip "Drugs"
    if not evidence_taken["id"]:
        imagebutton:
            idle "images/cs/id.png"
            hover "images/cs/idh.png"
            focus_mask True
            at transform:
                nearest True
                zoom 1
            xpos 1190 ypos 865
            action [
                Function(add_item, "ID", "Blood-stained ID.", "images/cs/id.png"),
                SetDict(evidence_taken, "id", True),
                Show("item_get_message", message="You found an ID.")
            ]
            tooltip "ID"

screen stairsd2():
    imagebutton:
        idle "invisible_idle"
        xysize (800, 800) 
        xpos 1100 ypos 130
        action Return("go_cctv_hallwayd2")
        tooltip "Go to CCTV Hallway"
    add "images/ui/arrow_idle.png" xpos 1700 ypos 470 at transform:
        zoom 0.5
        rotate 180
        alpha 0.3
    imagebutton:
        idle "images/ui/arrow_idle.png"
        hover "images/ui/arrow_hover.png"
        at transform:
            nearest True
            zoom 0.5
            alpha 0.3
        xpos 800 ypos 800 
        action Return("go_hallwayd2")
        tooltip "Return"
    imagebutton:
        idle "invisible_idle"
        xysize (800, 800) 
        xpos 0 ypos 100
        action Return("go_lockersd2")
        tooltip "Go to Lockers"
    add "images/ui/arrow_idle.png" xpos 10 ypos 470 at transform:
        zoom 0.5
        rotate -70
        alpha 0.3

screen cctv_hallwayd2():
    imagebutton:
        idle "images/ui/arrow_idle.png"
        hover "images/ui/arrow_hover.png"
        at transform:
            nearest True
            zoom 0.3
        xpos 50 ypos 700 
        action Return("go_stairsd2")
        tooltip "Return"

screen lockersd2():
    imagebutton:
        idle "invisible_idle"
        hover "translucent_hover"
        xysize (85, 450) 
        xpos 700 ypos 430
        action Return("go_zlockersd2")
        tooltip "Check Lockers"
    imagebutton:
        idle "images/ui/arrow_idle.png"
        hover "images/ui/arrow_hover.png"
        at transform:
            nearest True
            zoom 0.3
        xpos 50 ypos 700 
        action Return("go_stairsd2")
        tooltip "Return"

screen zlockersd2():
    imagebutton:
        idle "images/scenes/patlocker_idle.png"
        hover "images/scenes/patlockerh.png"
        at transform:
            nearest True
            zoom 1
        xpos 738 ypos 0
        action Return("go_patlockerd2")
        tooltip "Check Toph's Lockers"

screen patlockerd2():
    imagebutton:
        idle "images/ui/arrow_idle.png"
        hover "images/ui/arrow_hover.png"
        at transform:
            nearest True
            zoom 0.3
        xpos 50 ypos 700 
        action Return("go_lockersd2")
        tooltip "Return"
    if not evidence_taken["knife"]:
        imagebutton:
            idle "images/cs/bf.png"
            hover "images/cs/bfh.png"
            focus_mask True
            at transform:
                nearest True
                zoom 1
            xpos 0 ypos 0
            action [
                Function(add_item, "Butterfly Knife", "Found hidden inside a locker. Spotless handle – wiped clean.", "images/cs/bficon.png"),
                SetDict(evidence_taken, "knife", True),
                SetVariable("scenario_picker2d2", True),
                Show("item_get_message", message="You found a Butterfly Knife.")
            ]
            tooltip "Butterfly Knife"

screen evidence_room_d3():
    # Bag (Inventory)
    imagebutton:
        idle "images/ui/bag_idle.png"
        hover "images/ui/bag_hover.png"
        xpos 800 ypos 800
        action [SetVariable("selected_item", None), ShowMenu("inventory_screen")]
        tooltip "Search Bag Evidence"
    # Exit to Precinct
    imagebutton:
        idle "images/ui/arrow_idle.png"
        hover "images/ui/arrow_hover.png"
        at transform:
            nearest True
            zoom 0.3
        xpos 50 ypos 700 
        action Jump("precinctd3")
        tooltip "Return to Precinct"
    # Computer
    imagebutton:
        idle "invisible_idle"
        hover "translucent_hover"
        xysize (310, 210)
        xpos 580 ypos 530
        action Jump("computer_access")
        tooltip "Access Computer"

    # Corkboard (Journal)
    imagebutton:
        idle "invisible_idle"
        xysize (400, 350)
        xpos 1350 ypos 260
        action [SetVariable("selected_suspect", None), ShowMenu("journal_screen")]
        tooltip "Review Journal"

screen precinctd3_ui():
    # Button to enter Evidence Room
    imagebutton:
        idle "images/ui/arrow_left_idle.png" 
        hover "images/ui/arrow_left_hover.png"
        at transform:
            nearest True
            zoom 0.35
        xpos 850 ypos 370
        action Jump("evidence_room_hub") 
        tooltip "Enter Evidence Room"
        
    # Exit precinct (End Day)
    if current_day == 3:
        imagebutton:
            idle "images/ui/arrow_idle.png"
            hover "images/ui/arrow_hover.png"
            at transform:
                nearest True
                zoom 0.5
            xpos 1700 ypos 800 
            action Jump("confirm_next_day3")
            tooltip "Head Home (End Day 3)"
    elif current_day == 4:
        imagebutton:
            idle "images/ui/arrow_idle.png"
            hover "images/ui/arrow_hover.png"
            at transform:
                nearest True
                zoom 0.5
            xpos 1700 ypos 800 
            action Jump("confirm_next_day4")
            tooltip "Head Home (End Day 4)"