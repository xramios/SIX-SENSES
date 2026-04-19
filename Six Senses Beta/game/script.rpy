define gui.text_font = "Ithaca-LVB75.ttf"

label start:
    python:
        for person in journal_list:
            if not hasattr(person, 'status'):
                person.status = "Person of Interest"
            if not hasattr(person, 'descriptions'):
                person.descriptions = []

    $ add_suspect("Pat (Victim)", "Found in the storage room. Cause of death unknown.", "images/characters/pat.png")

    scene black with dissolve
    show headphones:
        xalign 0.5 yalign 0.33
        zoom 0.5
        alpha 0.0
        linear 2.0 alpha 0.7
    show text "{size=50}use headphones for best experience{/size}" at truecenter
    with dissolve
    $ renpy.pause(3.0)

    $ renpy.pause(1.5)
    play music "audio/rain.mp3"
    scene windowhome with dissolve
    
    show text "{size=50}You wake up hazy. Your phone buzzes across the room—endless, insistent.{/size}" as intro1:
        xalign 0.5 yalign 0.8
    with dissolve

    play sound "audio/phonecall.mp3" loop
    $ renpy.pause(3.0)

    hide intro1 with dissolve
    stop sound

    show text "{size=50}You answer. It's the Chief.{/size}" as intro1:
        xalign 0.5 yalign 0.8
    with dissolve
    $ renpy.pause(1.5)


    hide intro1 with dissolve
    pc "Detective, are you available right now? No—doesn't matter. Get to the location I sent. ASAP."
    with dissolve

    hide intro1 with dissolve
    window hide

    show text "{size=50}Groggy and confused—you couldn't even get a word in—you grab your keys and rush out the door.{/size}" as intro3:
        xalign 0.5 yalign 0.8
    with dissolve
    $ renpy.pause(2.0)
    
    $ renpy.pause(0.8)
    hide intro2 with dissolve

    show text "{size=50}you hurriedly grab your keys and rush out the door{/size}" as intro3:
        xalign 0.5 yalign 0.8
    with dissolve
    $ renpy.pause(1.5)
    hide intro3 with dissolve

    scene black
    play sound "audio/exitinghome.mp3"
    $ renpy.pause(18.0)
    
    scene car
    play sound "audio/carengine.mp3"
    $ renpy.pause(5)

    play sound "audio/thunderclap.mp3"
    
    $ renpy.pause(0.5)
    show expression "#fff" as lightning
    with None
    pause 0.1
    hide lightning
    
    scene black

    show sfc at truecenter:
        zoom 0.5
        alpha 0.0
        linear 2.0 alpha 0.7

    show text "{size=25}Story adaptation from Silangan Film Circle{/size}":
        xalign 0.5 yalign 0.59
        alpha 0.0
        pause 0.5
        linear 1.0 alpha 1.0

    $ renpy.pause(3.5)
    hide sfc
    hide text
    with dissolve

    play music "audio/eeriebackground.mp3" fadein 1.0

    $ renpy.pause(1)

    show text "{size=70}December 18, 2025.{/size}" at truecenter
    with dissolve

    $ renpy.pause(3)

    hide text

    show police_lights at police_full_flicker

    show text "{size=60}5:23 AM{/size}" at truecenter
    with dissolve

    $ renpy.pause(3)

    hide text

    show text "{size=50}A body was found in the storage room.{/size}" at truecenter
    with dissolve

    stop music
    stop sound
    scene elevator with fade

    play music "audio/police_siren.mp3" loop
    
    "As you walk inside, the uniformed officers lead you to the 6th floor."

    scene main_hallway with fade    
    "the chief notices you and comes over"

    show captain at right: 
        zoom 0.7
    with moveinright
    
    pc "You’re finally here, Detective."
    
    pc "It’s gruesome in there... *sighs*"
    pc "But we don't have time to dawdle—so let me fill you in."

    stop music fadeout 1.0
    scene prologue-call with flash
    
    op "9-1-1, what’s your emergency?"
    d "Hello? M-may... may—"

    pc "That was Dan, the janitor. He called it in at 5:25 AM."
    
    scene prologue-call2 with dissolve
    
    pc "The janitor, Dan-found the body in around 5:23 AM."
    
    pc "Scene’s... rough. Whoever did this didn't hold back."

    scene main_hallway with fade

    show captain at right:
        zoom 0.7
    pc "We may not have much information, but it’s better than nothing."


# ============================================================================
#                               TUTORIAL
# ============================================================================

label tutorial:
    scene main_hallway
    show image "images/ui/bag_icon.png" as icon_inv at popup_center
    s "System: Inventory Unlocked."
    pause
    show image "images/ui/bag_icon.png" as icon_inv at move_to_hud_left
    s "System: Go to your inventory."

    $ add_item("Crime Photo", "A photo of the 6th floor storage room.", "images/Str_room.png")
    s "{u}Crime Photo{/u} added to your Bag."

    call screen inventory_screen
    s "System: Items will be stored there."

    show image "images/ui/journal_icon.png" as icon_jou at popup_center
    s "System: Journal Unlocked."
    pause
    show image "images/ui/journal_icon.png" as icon_jou at move_to_hud_right
    s "System: Check your journal."

    $ add_suspect("Dan (Janitor)", "The man who found the body. Seems shaken.", "images/characters/danicon.png")
    $ record_clue("Dan (Janitor)", "Observation|He was trembling when he spoke to the Captain.")
        
    call screen journal_screen
    s "All discovered clues, notes, and observations will be recorded there."
    s "new suspects and profiles will be unlocked as you progress through the story"

    hide icon_jou
    hide icon_inv

    $ show_hud = True
    show screen detective_hud
    s "System: You are ready to begin."
    
    $ show_hud = False
    scene str_intro with fade
    mc "The moment I stepped into the crime scene..."
    mc "....my eyes started scanning everything."
    show str_intro2 
    mc "Blood stains."
    mc "Footprints."
    show str_intro3
    mc "Objects out of place."
    mc "Details most people overlook"
    scene black with fade
    show text Text("Sense Activated — SIGHT", size=70, color="#00FFFF") at truecenter    
    with dissolve
    s "Observe the environment carefully"
    jump storage_room

# ============================================================================
#                                  DAY 1
# ============================================================================

label mhallway:
    play music "audio/ambiance_hallway_d1.mp3" loop
    $ current_location = "mhallway"
    $ show_hud = True
    scene main_hallway with fade

    $ result = renpy.call_screen("detective_hud")

    if result == "go_hallway2":
        jump hallway2
    elif result == "go_dan":
        jump dan
    elif result == "go_day2":
        jump day2
    jump mhallway

label talk_to_dan:
    $ show_hud = False 
    show dan_face at Transform(ypos=400, zoom=0.65, xpos=1000) with dissolve
    if not met_dan:
        d "P-please... I already told the Captain everything I saw."
        mc "I'm just following up, Dan. You're the one who found the body, right?"
        d "Yes. I was just coming in to swap the trash liners... and there she was."
        $ add_suspect("Dan (Janitor)", "The man who found the body. Seems shaken.", "images/suspects/dan_port.png")
        $ met_dan = True
    else:
        d "I... I really want to go home, Detective. This place gives me the creeps now."

    menu:
        "Ask about the foaming mouth":
            mc "Did you notice anything strange about her face? Like froth or foam?"
            d "I didn't get that close! I saw the blood and... and I ran for the phone."
            $ record_clue("Dan (Janitor)", "Statement|Claims he didn't look closely at the face.")

        "Ask about the bruising":
            mc "Did you see anyone else in the hallway when you arrived?"
            d "No one. It was dead silent. Just the humming of the vending machines."

        "Leave him alone":
            mc "That's all for now, Dan. Stay close by."
            d "I'm not going anywhere... my legs are still shaking too much."
            hide dan_face with dissolve
            jump resume_investigation
    jump talk_to_dan

label resume_investigation:
    $ show_hud = True
    call screen detective_hud

label hallway2:
    play music "audio/ambiance_crime_scene_d1.mp3" loop
    $ current_location = "hallway2"
    $ show_hud = True
    scene hallway2 with fade

    $ result = renpy.call_screen("detective_hud")
    if result == "go_storage":
        jump storage_room
    elif result == "go_mhallway":
        jump mhallway
    elif result == "go_stairs":
        jump stairs
    jump hallway2

label stairs:
    play music "audio/ambiance_crime_scene_d1.mp3" loop
    $ current_location = "stairs"
    scene stairs with fade

    $ result = renpy.call_screen("detective_hud")
    if result == "go_hallway2":
        jump hallway2
    elif result == "go_cctv_hallway":
        jump cctv_hallway
    elif result == "go_lockers":
        jump lockers
    jump stairs

label cctv_hallway:
    play music "audio/ambiance_hallway_d1.mp3" loop
    $ current_location = "cctv_hallway"
    scene cctv_hallway with fade

    $ result = renpy.call_screen("detective_hud")

    if result == "go_stairs":
        jump stairs
    elif result == "go_cctv_room":
        if scenario_picker2 == False:
            jump cctv_room
        elif scenario_picker2 == True:
            if current_day == 1:
                mc "its locked- but there seems to be someone inside..."
            elif current_day == 2:
                mc "It's locked."
    jump cctv_hallway

label cctv_room:
    play music "audio/ambiance_hallway_d1.mp3" loop
    $ current_location = "cctv_room"
    scene cctv_room with fade
    $ result = renpy.call_screen("detective_hud")
    if not seen_cctv_room_intro:
        $ seen_cctv_room_intro = True
        "You enter the control room. It's clean enough—organized."
        "Now, which tape do I need…"
        mc "You scan the labeled shelves. Two slots are empty. The labels are still there, but the tapes are gone."
        mc "Still… would've been nice if they left a note."
    if result == "cctv_monitor":
        jump cctv_room_monitor
    elif result == "go_cctv_hallway":
        jump cctv_hallway
    jump cctv_room

label cctv_room_monitor:
    scene cctv_room
    call screen cctv_monitor
    $ chosen_cam_index = _return
    $ scenario_picker1 = True
    if chosen_cam_index == "exit":
        jump cctv_room
    if chosen_cam_index == 0:
        $ cam_num = 1
        $ already_solved = cctv_cam1_solved
    else:
        $ cam_num = 4
        $ already_solved = cctv_cam4_solved
    
    if already_solved:
        mc "I've already enhanced this footage. Nothing new here."
        jump cctv_room_monitor
    
    mc "Let's try to enhance the feed for camera [cam_num]..."
    $ my_puzzle = start_puzzle()
    call screen cctv_puzzle_screen(my_puzzle, cam_num)
    $ puzzle_result = _return 
    
    if puzzle_result == "win":
        if cam_num == 1:
            $ cctv_cam1_solved = True
            jump cctv_reveal_cam1
        else:
            $ cctv_cam4_solved = True
            jump cctv_reveal_cam4
    else:
        mc "I couldn't get a clear signal."
        jump cctv_room_monitor

label cctv_reveal_cam1:
    scene black with fade
    show text "{size=50}CCTV FOOTAGE - CAMERA 1{/size}" at truecenter with dissolve
    pause 1.0
    hide text with dissolve
    
    scene cctv_1_reveal with fade
    $ cctv_cam1_solved = True
    "The footage shows Dan gripping Pat firmly by the hand, pulling him down the hallway with urgency."
    "Pat resists slightly, stumbling to keep up as he tries to pull back."
    "Dan doesn’t let go, tightening his grip and dragging Pat toward the storage room."
    "Without hesitation, Dan yanks the door open and pulls Pat inside. The door shuts quickly behind them."
    
    $ add_suspect("Dan (Janitor)", "Seen on CCTV leading Pat to storage room.", "images/characters/danicon.png")
    $ record_clue("Dan (Janitor)", "Video Evidence | Camera 1 shows Dan dragging Pat into storage room against his will.")
    mc "The defensive bruises on Pat's forearms..."
    mc "They align perfectly with the CCTV. That was from Dan forcefully gripping and dragging her into the storage room."
    mc "Dan lied. He said he just found the body this morning, but here he is with Pat the night before."
    
    jump cctv_room_monitor

label cctv_reveal_cam4:
    scene black with fade
    show text "{size=50}CCTV FOOTAGE - CAMERA 4{/size}" at truecenter with dissolve
    pause 1.0
    hide text with dissolve
    scene cctv_4_reveal with fade
    $ cctv_cam4_solved = True
    "The recording shows footage from a different camera, timestamped earlier that night."
    "Toph waits at the elevator, rushing to get out. He looks anxious, checking over his shoulder several times before moving out of frame."
    
    $ add_suspect("Toph", "Seen on CCTV near the crime scene on the night of the incident.", "images/characters/toph.png")
    $ record_clue("Toph", "Video Evidence| Camera 4 shows Toph exiting elevator and rushing toward storage room area, acting nervous.")
    
    jump check_both_cctv_solved

label check_both_cctv_solved:
    if cctv_cam1_solved and cctv_cam4_solved:
        if not scenario_picker2:
            $ scenario_picker1 = True
            mc "Two different cameras. Two different people."
            mc "But what were they both doing here that night?"
            $ add_item("CCTV Recording 1", "Dan Leading Pat to the Storage Room", "images/cs/CCTVTape.png")
            $ evidence_taken["cctv_tape1"] = True
            $ add_item("CCTV Recording 2", "Toph Looking Suspicious — Waiting at the Elevator", "images/cs/CCTVTape.png")
            $ evidence_taken["cctv_tape2"] = True
            show screen item_get_message(message="You add the 2 security tapes to your inventory.")
            
    jump cctv_room_monitor

label storage_room:
    play music "audio/ambiance_crime_scene_d1.mp3" loop
    $ current_location = "storage_room"
    scene storage_roomd1 with fade
    $ show_hud = True
    
    if not seen_scene_intro:
        show str_room
        $ result = renpy.hide_screen("detective_hud")
        $ Pause (0.2)
        mc "..."
        mc "The victim."
        mc "Right in the middle of the room."
        mc "But the answers might not be."
        $ seen_scene_intro = True
        hide str_room

    $ result = renpy.call_screen("detective_hud")
    if result == "go_hallway2":
        jump hallway2
    elif result == "go_body":
        if scenario_picker1 == False:
            jump body
        elif scenario_picker1 == True:
           pc "The body seems to have been taken care of by the forensic team, you'll get another chance to examine the body at a later date."
    jump storage_room

label body:
    play music "audio/ambience_crime_scene_d1.mp3" loop 
    $ current_location = "body"
    $ scenario_picker2 = True
    scene zbody with fade

    if not seen_body:
        $ result = renpy.hide_screen("detective_hud")
        $ Pause (0.2)
        "The body of Pat is slumped against the concrete, head lolling at an unnatural angle."
        mc "I just can't get used to this."
        $ seen_body = True
    
    window hide
    $ record_clue("Pat (Victim)", "Time of Death|Estimated between 3:00 AM and 4:30 AM.")

    $ result = renpy.call_screen("detective_hud")
    if result == "go_storage":
        jump storage_room
    jump body

label lockers:
    play music "audio/ambiance_hallway_d1.mp3" loop
    $ current_location = "lockers"
    $ show_hud = True
    scene lockers with fade

    $ result = renpy.call_screen("detective_hud")

    if result == "go_stairs":
        jump stairs
    elif result == "go_zlockers":
        jump zlockers
    jump lockers

label confirm_next_day:
    mc "I've gathered some leads... should I head back to the station for the night?"
    
    menu:
        "Yes, go back to the police station.":
            mc "I hope I didn't overlook anything important in the rush."
            $ show_hud = False
            scene elevator with fade
            play sound "audio/elevator_ding.mp3"
            pause 1.0
            "The elevator doors slide shut, cutting off the crime scene behind you. "
            "The silence of the ride down is heavy with the weight of what you found..."
            stop music fadeout 2.0
            scene black with dissolve
            pause 2.0
            jump policestation

        "No, I need to keep looking.":
            mc "Wait. My gut tells me there's more to see here. I should keep scanning."
            jump mhallway

# ============================================================================
#                               DEBREIFING DAY 1
# ============================================================================

label policestation:
    scene police_station with fade
    play music "audio/station_ambiance.mp3" loop fadein 1.0

    "You're back at the station. The case files are spread across your desk, and the dim light flickers overhead."
    "Now's the time to review everything you've gathered before heading out again."
    show captain at right:
        zoom 0.7
    with moveinright
    pc "You're back. So... what do we have?"

    # ========== BODY PATH ==========
    if scenario_picker2 and not scenario_picker1:
        mc "I examined the body personally, Captain."
        mc "Multiple stab wounds - one deep in the chest, another in the abdomen, and several on the arms."
        pc "Cause of death?"
        mc "Stabbing, but there's also bruising on the neck that suggests possible strangulation."
        if evidence_taken["powder"] and evidence_taken["waterbottle"]:
            mc "I also found powder and crushed water bottle near the scene."
            if has_pat_clue("foam"):
                mc "The foam around her mouth indicates a reaction to a drug overdose. Maybe the killer forced her to ingeest them."
                mc "And the water bottle? Maybe they used it to help her swallow the pills."
                pc "Jesus... So the killer drugged her, then stabbed her to make sure she didn't survive?"
                $ record_clue("Pat (Victim)", "Connection|Powder + water bottle + mouth foam – forced drug ingestion, then stabbing as overkill.")
        elif evidence_taken["powder"] and has_pat_clue("foam"):
            mc "I found synthetic drugs, and there was foam around her mouth."
            mc "That's a red flag – could be a reaction to the drugs. I'll have the lab test the powder."
            $ record_clue("Pat (Victim)", "Connection|Powder + mouth foam – potential poisoning.")
        elif evidence_taken["waterbottle"] and has_pat_clue("foam"):
            mc "The crushed water bottle and the foam on her mouth – maybe she was forced to drink something laced with poison."
            $ record_clue("Pat (Victim)", "Connection|Water bottle + mouth foam – possible poisoned drink.")
    # ========== CCTV PATH ==========
    elif scenario_picker1 and not scenario_picker2:
        mc "I couldn't examine the body - forensics had already taken it. But I pulled CCTV footages."
        if cctv_cam1_solved and cctv_cam4_solved:
            mc "I was able to enhance one of the feeds."
            mc "It shows Dan leading the victim toward the storage room between 6 and 8 PM."
            mc "There's also another student — appears later in the footage. Looks suspicious."
            mc "One facial match from the student database shows the student name is Toph Bernales"
            pc "So Dan and that student could also be tied in one way or another?"
            mc "Yes, sir. I've added them to the suspect list."
            if not any(s.name == "Dan (Janitor)" for s in journal_list):
                $ add_suspect("Dan (Janitor)", "Janitor seen leading victim to storage room on CCTV.", "images/characters/danicon.png")
        # Add Unknown Student (temporary name)
        if not any(s.name == "Toph" for s in journal_list):
            $ add_suspect("Toph", "Appears later in CCTV footage near storage room. Identity unknown.", "images/suspects/Toph.png")
            $ record_clue("Toph", "Video Evidence|Seen on CCTV entering storage room area after Dan and victim.")
        if evidence_taken["waterbottle"]:
            mc "I did find a crushed water bottle near the scene."
        if evidence_taken["powder"]:
            mc "There was also synthetic drugs. Could be related."
        if evidence_taken["powder"] and evidence_taken["waterbottle"]:
            mc "Both items may have been used on the victim, i'll know once the autopsy results are in."
        if evidence_taken["patbag"]:
            mc "Pat's bag was ransacked – someone was looking for something."
        if evidence_taken["patphone"]:
            mc "Her phone was there. Locked, but we can try to crack it."
        if evidence_taken["id"]:
            mc "Her ID was bloody and tossed aside."
        if evidence_taken["knife"]:
            mc "I also found a butterfly knife hidden in a locker. Handle was wiped clean."
        pc "Good work. This gives us a clearer direction."
        mc "What's our next move, Captain?"
        pc "Go over the evidence again—check if she made any calls or sent messages during that time."
        pc "And have the DNA tested too."
    pc "Alright. Log everything and get some rest. Tomorrow we dig deeper."

    menu:
        "Examine Evidence Bag":
            call screen inventory_screen
            jump policestation

        "Read Case Journal":
            call screen journal_screen
            jump policestation

        "Proceed to next day's investigation":
            jump day2intro
            
# ============================================================================
#                             DAY 2
# ============================================================================
label day2intro:
    $ current_day = 2
    scene black with fade
    pause 1.0

    show text Text("CHAPTER 2: SMELL", size=70, color="#FFFFFF") at truecenter with dissolve
    pause 1.0
    play sound "audio/announcement.mp3"
    s "In light of the recent incident, all classes will remain asynchronous until further notice."
    s "Entry into restricted areas is strictly forbidden. Students found in violation will face immediate disciplinary consequences."
    mc "Right… asynchronous. That explains why it's so empty."
    mc "Still feels strange, though."
    show text Text("Sense Activated — SMELL", size=70, color="#FF00C8") at truecenter with dissolve
    pause 1.0
    jump mhallwayd2

label mhallwayd2:
    play music "audio/ambiance_hallway_d1.mp3" loop 
    $ current_location = "mhallwayd2"
    $ show_hud = True
    scene main_hallway with fade

    if not seen_mhallwayd2_intro:
        $ seen_mhallwayd2_intro = True
        mc "The next morning, I return to the scene. The atmosphere feels different today... quieter, more tense."

    if not cigarette_smell_faint and not evidence_taken["cigarette"]:
        $ cigarette_smell_faint = True
        "A faint, stale smell of cigarette smoke lingers in the air."
    if not blood_smell_faint and not evidence_taken["knife"]:
        $ blood_smell_faint = True
        "Beneath it, a metallic scent – blood. Faint, but there."

    $ result = renpy.call_screen("detective_hud")
    if result == "go_hallwayd2":
        jump hallwayd2
    jump mhallwayd2

label hallwayd2:
    play music "audio/ambiance_hallway_d1.mp3" loop
    $ current_location = "hallwayd2"
    $ show_hud = True
    scene hallway2 with fade

    if not cigarette_smell_strong and not evidence_taken["cigarette"]:
        $ cigarette_smell_strong = True
        "The cigarette smell is much stronger here."
    if not blood_smell_strong and not evidence_taken["knife"]:
        $ blood_smell_strong = True
        "The blood scent is more distinct now. It's coming from somewhere ahead."

    $ result = renpy.call_screen("detective_hud")
    if result == "go_storaged2":
        jump storage_roomd2
    elif result == "go_mhallwayd2":
        jump mhallwayd2
    elif result == "go_stairsd2":
        jump stairsd2
    jump hallwayd2

label stairsd2:
    play music "audio/ambiance_crime_scene_d1.mp3" loop
    $ current_location = "stairsd2"
    scene stairs with fade

    if not blood_smell_overwhelming and not evidence_taken["knife"]:
        $ blood_smell_overwhelming = True
        "The blood smell intensifies sharply – it's coming from the locker area."
    if not cigarette_smell_faded and not evidence_taken["cigarette"]:
        $ cigarette_smell_faded = True
        "The cigarette odor fades here, replaced by dried blood."

    $ result = renpy.call_screen("detective_hud")
    if result == "go_hallwayd2":
        jump hallwayd2
    elif result == "go_cctv_hallwayd2":
        jump cctv_hallwayd2
    elif result == "go_lockersd2":
        jump lockersd2
    jump stairsd2

label cctv_hallwayd2:
    play music "audio/ambiance_hallway_d1.mp3" loop
    $ current_location = "cctv_hallwayd2"
    scene cctv_hallway with fade

    if not cctv_hallway_cigarette_noticed and not evidence_taken["cigarette"]:
        $ cctv_hallway_cigarette_noticed = True
        "The air here carries faint traces of cigarette smoke."

    if not cctv_hallway_blood_noticed and not evidence_taken["knife"]:
        $ cctv_hallway_blood_noticed = True
        "There's also a faint metallic scent of blood, but much less intense than the hallway outside."

    $ result = renpy.call_screen("detective_hud")
    if result == "go_stairsd2":
        jump stairsd2
    jump cctv_hallwayd2

label storage_roomd2:
    play music "audio/ambiance_crime_scene_d1.mp3" loop
    $ current_location = "storage_roomd2"
    $ show_hud = True
    scene storage_roomd2 with fade

    if not evidence_taken["cigarette"]:
        "You step into the room — empty. Too empty."
        mc "The body is gone. The forensic team worked fast."
        "You kneel down, running your fingers over the scuff marks. Someone fought hard here."
        "Then you notice it..."
        mc "Something smells off. Not just the metallic ghost of old blood — something else. Chemical. Sour."
    if evidence_taken["cigarette"]:
        $ cigarette_smell_inside_taken = True
        mc "Finally… a lead"
    $ result = renpy.call_screen("detective_hud")
    if result == "go_hallwayd2":
        jump hallwayd2
    jump storage_roomd2

label bodyd2:
    scene zbody with fade
    "The body is gone, but the chalk outline remains."
    "The forensic team has finished their work."
    jump storage_roomd2

label lockersd2:
    play music "audio/ambiance_hallway_d1.mp3" loop
    $ current_location = "lockersd2"
    $ show_hud = True
    scene lockers with fade     
    if not evidence_taken["knife"]:
        "The blood smell is concentrated here, radiating from one of the lockers."

    $ result = renpy.call_screen("detective_hud")
    if result == "go_stairsd2":
        jump stairsd2
    elif result == "go_zlockersd2":
        jump zlockersd2
    jump lockersd2

label zlockersd2:
    play music "audio/ambiance_hallway_d1.mp3" loop
    $ current_location = "zlockersd2"
    $ show_hud = True
    scene zlockers with fade
    mc "One locker reeks of blood. The scent is overpowering here."
    mc "This is a locker of one of the students. I should check it out."
    $ result = renpy.call_screen("detective_hud")
    if result == "go_lockersd2":
        jump lockersd2
    elif result == "go_patlockerd2":
        jump patlockerd2
    jump zlockersd2

label patlockerd2:
    play music "audio/ambiance_hallway_d1.mp3" loop
    $ current_location = "patlockerd2"
    $ show_hud = True
    scene patlocker
    mc "This locker belongs to a student named Toph Bernales."
    if not evidence_taken["knife"]:
        "The blade is still stained — dark, dried blood clings to the steel. The handle, however, has been wiped clean."
        "You open Toph Bernales' locker and find a butterfly knife, no prints. Someone knew what they were doing."
    if evidence_taken["knife"]:
        mc "…This feels too easy."
        "Something's off. Like eyes on your back."
        "The hair on your neck stands up."
        "You turn — just in time to catch a glimpse of a student bolting down the hall. Footsteps echo off the tile."
        mc "Hey — !"
        mc "Gone. Just like that."
        "You're left standing there, heart pounding, wondering what their deal was."
    $ result = renpy.call_screen("detective_hud")
    if result == "go_lockersd2":
        jump lockersd2
    jump patlockerd2

label confirm_next_day2:
    mc "I've gathered enough for today. Time to head back."
    $ show_hud = False
    scene elevator with fade
    play sound "audio/elevator_ding.mp3"
    pause 1.0
    "The elevator doors close."
    stop music fadeout 2.0
    scene black with dissolve
    pause 2.0
    $ current_day = 3
    jump policestation2

label policestation2:
    scene police_station with fade
    play music "audio/station_ambiance.mp3" loop fadein 1.0

    "Back at the station, you review the new findings from the second day of investigation."
    show captain at right:
        zoom 0.7
    with moveinright
    if evidence_taken["cigarette"] and evidence_taken["knife"]:
        pc "Back so soon?"
        pc "So... what do we have?"
        mc "We followed up on yesterday’s findings. I started tracing the victim’s phone but the phone was locked."
        pc "Of course it is. Any way around it?"
        mc "I’ll try to bypass it, but it’ll take time."
        pc "Then don’t wait on it. What else?"
        mc "There’s also a cigarette butt and butterfly knife we almost missed. Both could give us DNA."
        pc "Good Catch. A butterfly knife… in Toph Bernales' locker? Either he's careless… or someone wants him to look that way."
        mc "While I was checking Toph Bernales' locker someone did ran away from the scene."
        mc "He was already gone the moment I realized someone was there."
        mc "If it was Toph Bernales why would he put something the police would easily find?"
        mc "We didn't check all personal items thoroughly… and we haven't confirmed any connections to potential suspects yet."
        pc "Don't lock onto Bernales just yet. Verify everything. If this is planted, we're being played."
    elif evidence_taken["cigarette"] and not evidence_taken["knife"]:
        pc "You’re back. You look worried. So… what do we have?"
        mc "We followed up on yesterday’s findings. I started tracing the victim’s phone but the phone was locked."
        pc "Of course it is. Any way around it?"
        mc "I’ll try to bypass it, but it’ll take time."
        pc "Then don’t wait on it. What else?"
        mc "We recovered a cigarette butt at the scene. We almost missed it—it could still have DNA on it."
        pc "Good catch. A cigarette butt… small, easy to overlook—but that’s how people get sloppy."
        pc "Doesn’t mean it’s our suspect yet. Could belong to anyone who’s been through that area."
        pc "We didn’t check every detail thoroughly… and we still don’t have confirmed connections between the suspects."
        pc "Don’t lock onto it just yet. Verify everything. If it’s relevant, it’ll lead us somewhere. If not, it’s just noise."
    elif evidence_taken["knife"] and not evidence_taken["cigarette"]:
        pc "You’re back. You look worried. So… what do we have?"
        mc "We followed up on yesterday’s findings. I started tracing the victim’s phone but the phone was locked."
        pc "Of course it is. Any way around it?"
        mc "I’ll try to bypass it, but it’ll take time."
        pc "Then don’t wait on it. What else?"
        pc "Good Catch. A butterfly knife… in Toph Bernales' locker? Either he's careless… or someone wants him to look that way."
        mc "While I was checking Toph Bernales' locker someone did ran away from the scene."
        mc "He was already gone the moment I realized someone was there."
        mc "If it was Toph Bernales why would he put something the police would easily find?"
        mc "We didn't check all personal items thoroughly… and we haven't confirmed any connections to potential suspects yet."
        pc "Don't lock onto Bernales just yet. Verify everything. If this is planted, we're being played."
    elif not evidence_taken["cigarette"] and evidence_taken["knife"]:
        pc "You’re back. You look worried. So… what do we have?"
        mc "We followed up on yesterday’s findings. I started tracing the victim’s phone but the phone was locked."
        pc "Of course it is. Any way around it?"
        mc "I’ll try to bypass it, but it’ll take time."
        pc "Then don’t wait on it. What else?"
        mc "We didn’t check all personal items thoroughly… and we haven’t confirmed any connections to potential suspects yet."
    mc "What's our next move, Captain?"
    pc "Go over the evidence again — check if she made any calls or sent messages during that time. And have the DNA from both items tested too."
    pc "Alright. Log everything and get some rest. Tomorrow we dig deeper."
    scene black with dissolve
    pause 2.0
    scene car with fade
    play sound "audio/carengine.mp3"
    pause 7.0
    stop sound fadeout 2.0
    scene windowhome with fade
    mc "I should sleep for now. I need to clear my head and review everything again tomorrow."
    jump day3intro


# ============================================================================
#                                   Day 3
# ============================================================================

label day3intro:
    $ current_day = 3
    scene black with fade
    pause 1.0

    show text "{size=70}Sense Activated — TOUCH{/size}" at truecenter with dissolve
    pause 2.0
    hide text with dissolve

    scene police_station with fade
    "You enter the precinct, the familiar scent of old coffee and stale paperwork filling the air."
    show captain at right:
        zoom 0.7
    with moveinright

    if scenario_picker1:
        pc "The forensic team saw the cctv footage and got a hold of 2 new cctv tapes you should take a look at."
        mc "Good. I'll review them immediately."
    elif scenario_picker2:
        pc "The forensic team saw the cctv footage and got a hold of 4 different cctv tapes you should take a look at."
        mc "Good. I'll review them immediately."
    show text "{size=70}Sense Activated — TOUCH{/size}" at truecenter with dissolve
    pause 2.0
    hide text with dissolve
    pc "The evidence room is ready. Lay everything out. Maybe seeing it all together will spark something."
    hide captain with moveoutright
    jump evidence_room_hub

label evidence_room_hub:
    $ current_location = "evidence_room"
    scene evidence_room_bg with fade
    
    if not seen_evidence_room_intro:
        $ seen_evidence_room_intro = True
        "You enter the evidence room."
        "Your bag hangs open. You lift it and plop it on the floor below the corkboard."
        "Photos, bagged items, notes — it's all still inside, waiting to be sorted."
        "You can choose to click the computer to check the tapes, sort through the trace evidence in your bag, or click the corkboard to check your journal."
        "You may now interact with the evidence."
    
    $ show_hud = True
    call screen evidence_room_d3

# --- Trace Evidence Inspection ---
label inspect_item_logic:
    $ show_hud = False
    scene black with dissolve
    
    if item_to_inspect == "ID":
        "Pat's ID lace lies crumpled in a corner, its fabric roughed up and stained with fresh blood."
        "It looks less like something misplaced and more like it was forcibly torn off and discarded — but whether it happened during a struggle or after the fact is still unclear."
        
    elif item_to_inspect == "Bag":
        "A discarded shoulder bag now in the evidence room, its zipper left wide open and lining still partially turned inside out."
        "The interior is completely empty, confirming it was thoroughly searched — but whether anything was actually taken, or what the intruder was looking for, remains unclear."
        
    elif item_to_inspect == "Drugs":
        "A small bag of high-grade synthetic drugs found on the floor, carelessly left behind."
        "Their presence raises serious suspicion, but it's unclear whether they belonged to the victim, the perpetrator, or someone else."
        
    elif item_to_inspect == "Half-Empty Bottle":
        "An empty bottle found among the scattered belongings, likely discarded during a hurried search."
        "It could have been used to administer the substances found near the body — but whether it played a direct role or is simply part of the mess left behind remains uncertain."
        
    elif item_to_inspect == "Cigarette Butt":
        "A crushed cigarette butt recovered from the floor, its filter still fresh and marked with clear fingerprints."
        "The size and shape match the burns found on Pat's skin, suggesting a possible link — but whether it directly ties to the suspect or was left behind unintentionally remains uncertain."
        
    elif item_to_inspect == "Butterfly Knife":
        "A butterfly knife found inside Toph's locker, its surface wiped clean of fingerprints but still bearing faint traces of dried blood along the blade."
        "The contrast feels unsettling — careful enough to remove identity, but not thorough enough to erase everything — leaving it unclear whether it was hidden in haste or deliberately planted to confuse the investigation."
        
    elif item_to_inspect == "Phone":
        jump phone_interaction
        
    else:
        "You examine the evidence closely, but nothing new stands out."

    jump evidence_room_hub

# --- Phone Messages ---
# --- Phone Interaction Flow ---
label phone_interaction:
    $ show_hud = False
    
    if not phone_unlocked:
        scene black with dissolve
        "System" "You interact with Pat's phone — it seems to be locked."
        "System" "You try to unlock it by connecting the phone to another device."
        jump start_hacking
    else:
        jump phone_unlocked_hub

label phone_unlocked_hub:
    scene black with dissolve
    call screen phone_ui

# --- Phone Apps ---
label phone_app_messages:
    scene black with dissolve
    "System" "You opened the messaging app."
    
    scene phone_messages_bg with dissolve # Replace with your actual image
    "A series of frantic, typed-out messages recovered from Toph’s logs, sent by Pat."
    
    mc "Looking at these messages now — Pat was putting serious pressure on Toph."
    mc "Demanding money, claiming a pregnancy scare, threatening to expose his drug use to his coach and even his father."
    mc "Whether this is motive or just a messy situation… that's what we need to figure out."
    
    $ add_suspect("Toph", "Had a volatile texting history with Pat.", "images/characters/toph.png")
    $ record_clue("Toph", "Motive|Pat was extorting him for money over a pregnancy scare and threatening to expose his drug use.")
    jump phone_unlocked_hub

label phone_app_calls:
    scene black with dissolve
    "System" "You opened the call logs."
    
    scene phone_call_log_bg with dissolve # Replace with your actual image
    "You find a recorded voice call at just past 9 PM."
    
    mc "Pulling up a call log here — just past 9 PM."
    mc "Pat's voice is weak, crying. She's begging Chandler for help. Says she's trapped in the storage room."
    
    $ add_suspect("Chandler", "Received a distress call from Pat.", "images/suspects/chandler.png")
    $ record_clue("Chandler", "Connection|Received a call for help from Pat at past 9 PM while she was trapped in the storage room.")
    jump phone_unlocked_hub

label phone_app_bank:
    scene black with dissolve
    "System" "You opened the banking app gallery."
    
    scene phone_bank_toph_pat with dissolve
    "System" "A screenshot of Toph sending Pat a bank transfer."
    pause
    
    mc "Toph was definitely paying Pat. This confirms the extortion messages."
    
    # Record only the Pat transfer here
    $ record_clue("Toph", "Financial (Phone)|Sent a bank transfer to Pat.")
    
    jump phone_unlocked_hub

# --- CCTV Tapes ---
label cctv_tape_view:
    $ show_hud = False
    scene black with fade
    
    # ==========================================
    # PATH: CHECKED CCTV ROOM FIRST (2 Tapes)
    # ==========================================
    if scenario_picker1 and not scenario_picker2:
        if tape_num == 1:
            show text "{size=50}CORRUPTED TAPE: CHANDLER ON CALL{/size}" at truecenter with dissolve
            pause 2.0
            scene cctv_chandler with fade # Note: You can add a glitch effect here if you have one
            "Security recording shows heavy corruption, with intermittent frame loss and visual tearing."
            "In the clearer fragments, a figure consistent with Chandler Soriano is seen in the hallway, appearing to be on a call."
            "Portions of the sequence are missing, but the subject is later observed exiting the frame without looking back."
            "Due to data degradation, the identity of the person on the call and full movement continuity cannot be confirmed."
            $ add_suspect("Chandler", "Seen on corrupted CCTV near the crime scene.", "images/suspects/chandler.png")
            $ record_clue("Chandler", "CCTV Tape 1|Corrupted footage shows him on a call in the hallway before leaving the frame.")
            s "Clue Recorded."

        elif tape_num == 2:
            show text "{size=50}CORRUPTED TAPE: AUSTIN PEEKING{/size}" at truecenter with dissolve
            pause 2.0
            scene cctv_austin with fade
            "The footage shows Chandler exiting the area, walking out of frame without looking back."
            "Moments later, Austin slowly leans out from behind the corner, cautiously peeking in the direction Chandler went."
            "He scans the hallway, lingering for a second as if making sure it’s clear, before stepping out slightly further, still keeping part of his body hidden."
            $ add_suspect("Austin", "Seen tailing Chandler on CCTV.", "images/suspects/austin.png")
            $ record_clue("Austin", "CCTV Tape 2|Seen peeking around the corner after Chandler leaves.")
            s "Clue Recorded."

    # ==========================================
    # PATH: CHECKED THE BODY FIRST (4 Tapes)
    # ==========================================
    elif scenario_picker2:
        if tape_num == 1:
            show text "{size=50}CORRUPTED TAPE: DAN LEADING PAT{/size}" at truecenter with dissolve
            pause 2.0
            scene corr_cctv_dan with fade
            "Security footage recovered from the camera shows partial visual data of the corridor leading to the storage room."
            "The recording is corrupted and intermittently fragmented, with missing frames and visual distortion."
            "Within the salvageable segments, a figure consistent with Dan is seen moving toward the storage room."
            $ add_suspect("Dan (Janitor)", "Janitor seen leading victim to storage room on CCTV.", "images/characters/danicon.png")
            $ record_clue("Dan (Janitor)", "CCTV Tape 1|Corrupted footage shows Dan moving toward the storage room.")
            s "Clue Recorded."
        elif tape_num == 2:
            show text "{size=50}CORRUPTED TAPE: CHANDLER ON CALL{/size}" at truecenter with dissolve
            pause 2.0
            scene cctv_chandler with fade
            "Security recording shows heavy corruption, with intermittent frame loss and visual tearing."
            "In the clearer fragments, a figure consistent with Chandler Soriano is seen in the hallway, appearing to be on a call."
            "Portions of the sequence are missing, but the subject is later observed exiting the frame without looking back."
            "Due to data degradation, the identity of the person on the call and full movement continuity cannot be confirmed."
            $ add_suspect("Chandler", "Seen on corrupted CCTV near the crime scene.", "images/suspects/chandler.png")
            $ record_clue("Chandler", "CCTV Tape 2|Corrupted footage shows him on a call in the hallway before leaving the frame.")
            s "Clue Recorded."

        elif tape_num == 3:
            show text "{size=50}TAPE: AUSTIN PEEKING{/size}" at truecenter with dissolve
            pause 2.0
            scene cctv_austin with fade
            "The footage shows Chandler exiting the area, walking out of frame without looking back."
            "Moments later, Austin slowly leans out from behind the corner, cautiously peeking in the direction Chandler went."
            "He scans the hallway, lingering for a second as if making sure it’s clear, before stepping out slightly further, still keeping part of his body hidden."
            mc "Ahhh, so this was one of the missing tapes."
            $ add_suspect("Austin", "Seen tailing Chandler on CCTV.", "images/suspects/austin.png")
            $ record_clue("Austin", "CCTV Tape 3|Cautiously tracking Chandler's movements.")
            s "Clue Recorded."

        elif tape_num == 4:
            show text "{size=50}TAPE: TOPH AT ELEVATOR{/size}" at truecenter with dissolve
            pause 2.0
            scene cctv_toph with fade
            "The tape shows Toph suspiciously waiting inside the elevator while holding his phone."
            mc "And this must be the other one. Toph, waiting around like he's got somewhere else to be — or someone to meet."
            $ add_suspect("Toph", "Seen on CCTV near the crime scene on the night of the incident.", "images/characters/toph.png")
            $ record_clue("Toph", "CCTV Tape 4|Seen nervously waiting in the elevator.")
            s "Clue Recorded."

    pause 1.0
    jump computer_access

# --- GMAIL: RECOVERED GCASH LOGS ---
label day3_gmail_review:
    $ show_hud = False
    scene windows_bg with dissolve
    
    s "System: You open the Email client."
    
    "There is a new message from the Cyber Forensics Division."
    s "SUBJECT: Recovered Transaction Logs\nMESSAGE: Detective, we managed to pull an external GCash transaction log linked to Toph Bernales's account from the night of the incident. See attached."
    
    scene phone_bank_toph_chandler with dissolve
    s "System: An image of a GCash transfer."
    s "System: Toph sent a 3K bank transfer to Chandler."
    pause
    
    mc "Toph sent Chandler money right around the time of the incident."
    mc "Was he paying him off? Or was Chandler extorting him too?"

    $ record_clue("Toph", "Financial (Email)|Sent a 3K bank transfer to Chandler on the night of the murder.")
    $ record_clue("Chandler", "Financial (Email)|Received a 3K bank transfer from Toph.")

    jump computer_access

label precinctd3:
    $ current_location = "precinctd3"
    scene police_station with fade
    play music "audio/station_ambiance.mp3" loop fadein 1.0
    
    $ show_hud = True
    call screen detective_hud

    jump precinctd3

label confirm_next_day3:
    $ show_hud = False
    mc "I've reviewed the phone logs and the CCTV tapes. That might be all I can do for today."
    
    menu:
        "Call it a night and head home.":
            mc "I need to rest. Tomorrow is going to be a long day."
            jump transition_to_day4
            
        "I need to keep reviewing.":
            mc "Hold on, let me double-check the files just in case."
            jump precinctd3

label transition_to_day4:
    scene black with dissolve
    pause 2.0
    
    scene car with fade
    play sound "audio/carengine.mp3"
    pause 7.0
    stop sound fadeout 2.0
    
    scene windowhome with fade
    mc "The pieces are starting to form a picture, but it's still blurry."
    mc "I should get some sleep."
    
    scene black with dissolve
    pause 2.0
    jump day4intro

# ============================================================================
#                                   DAY 4
# ============================================================================
label day4intro:
    $ current_day = 4
    scene black with fade
    pause 1.0

    play sound "audio/sfx.mp3" # Replace with your preferred text flash SFX
    show text "{size=70}CHAPTER 4: TASTE{/size}" at truecenter with dissolve
    pause 2.0
    hide text with dissolve

    scene police_station with fade
    play music "audio/station_ambiance.mp3" loop fadein 1.0
    
    show captain at right:
        zoom 0.7
    with moveinright

    pc "Detective. The lab just sent over the autopsy and the DNA evidence findings."
    pc "They're uploaded to your computer in the evidence room. Review them immediately."
    mc "Understood, Captain."
    
    hide captain with moveoutright
    jump evidence_room_hub

label day4_evidence_review:
    $ show_hud = False
    scene windows_bg 
    
    # --- AUTOPSY REPORT ---
    s "System: You open the Autopsy Report."
    show autopsy_document:
        zoom 0.40
        xalign 0.25 yalign 0.5
    show autopsy_picture:
        zoom 0.40
        xalign 0.75 yalign 0.5
    with dissolve
    pause 2.0
    
    mc "So… multiple stab wounds. Chest, torso, abdomen. Massive internal bleeding did the job."
    mc "Defensive wounds on the forearms. She tried to fight back."
    mc "Neck bruising… inconclusive. Strangulation? Or just from being dragged?"
    mc "Cigarette burn on the wrist. Deliberate. Someone held it there."
    mc "And fractured ribs."
    mc "This wasn't quick. She suffered."

    # Update Journal for Pat
    $ record_clue("Pat (Victim)", "Autopsy|Multiple stab wounds, defensive forearm bruises, neck contusions, fractured ribs, intentional cigarette burn.")

    scene windows_bg with dissolve
    
    # --- EVIDENCE FINDINGS ---
    s "System: You open the Evidence Findings."
    
    # Show the forensic document in the center
    show forensic_document at truecenter:
        zoom 0.40
    with dissolve
    
    s "{b}Cigarette Butt{/b}\nCrushed cigarette butt, filter intact and still relatively fresh. Latent fingerprint impressions are present on the surface and are preliminarily matched to Chandler Soriano, pending full forensic confirmation."
    s "Trace biological material is present on the filter, yielding an unknown saliva DNA profile that does not correspond to Chandler in the current reference database."
    s "Burn characteristics and diameter are consistent with the circular thermal injury observed on the decedent's left wrist. Despite these correlations, the presence of mixed biological evidence prevents definitive attribution, leaving questions regarding handling sequence, possible transfer, or secondary contact unresolved."
    
    s "{b}Butterfly Knife{/b}\nButterfly knife presented for examination. Visible blood staining present along the blade. DNA analysis confirms the blood is consistent with the victim, Pat Estacio. No identifiable latent fingerprints were recovered from the surface, suggesting the weapon was wiped prior to examination."
    
    s "{b}Drugs{/b}\nA small bag of high-grade synthetic drugs recovered from the floor, carelessly left behind. Latent fingerprints recovered from the bag are preliminarily matched to Toph Bernales. The residue around the victim's mouth suggests the contents may have been forced into her — not taken willingly."
    
    s "{b}Half-Empty Plastic Bottle{/b}\nAn empty bottle found among the scattered belongings, likely discarded during a hurried search. Latent fingerprints recovered from the bottle are preliminarily matched to Toph Bernales. The bottle could have been used to wash down the drugs — or force her to swallow them."

    scene black with dissolve
    s "System: You close the file. The taste stays with you."
    
    mc "Chandler's prints are on the cigarette — but the DNA isn't his. Someone else had it in their mouth."
    mc "The knife was wiped clean."
    mc "You can wipe away prints. You can't wipe away a taste."

    # --- ESTABLISHING SUSPECT CONNECTIONS ---
    # These journal updates explicitly link the suspect to their inflicted damage based on your scripts!
    
    $ record_clue("Dan (Janitor)", "Connection (Restraint)|CCTV footage shows him forcibly dragging Pat to the room. Matches the defensive forearm bruises and inconclusive neck contusions found in autopsy.")
    
    $ record_clue("Chandler", "Connection (Burn)|Fingerprints found on the crushed cigarette used to burn Pat's wrist. The unknown saliva DNA suggests the cigarette was shared or transferred.")
    
    $ record_clue("Toph", "Connection (Drugs)|Fingerprints match the drug bag and water bottle. Residue on Pat's mouth implies he forced her to ingest the synthetic drugs.")
    
    $ record_clue("Austin", "Connection (Stalking)|CCTV confirms he was cautiously stalking Chandler and was present in the hallway near the crime scene.")

    pause 1.0
    mc "I have what I need. It's time to bring them in."

label confirm_next_day4:
    $ show_hud = False
    mc "I've reviewed the Autopsy and DNA Findings from the lab tech. That might be all I can do for today."
    
    menu:
        "Call it a night and head home.":
            mc "I need to rest. Tomorrow is going to be a long day."
            jump day5intro
            
        "I need to keep reviewing.":
            mc "Hold on, let me double-check the files just in case."
            jump precinctd3

# ============================================================================
#                                   DAY 5
# ============================================================================

label day5intro:
    $ current_day = 5
    scene black with fade
    pause 1.0

    play sound "audio/sfx.mp3" 
    show text "{size=70}CHAPTER 5: HEARING{/size}" at truecenter with dissolve
    pause 2.0
    hide text with dissolve

    scene police_station with fade
    play music "audio/station_ambiance.mp3" loop fadein 1.0

    "Most of the evidence has been reviewed."
    
    "Your phone buzzes."

    s "TECHNICAL ANALYST (over phone): Warrant went through. Two call logs — Pat and Toph, Toph and Dan. Both from the night of the incident. Took a while, but they're clean now. Listen when you can."

    mc "Got it. Thanks."
    "You hang up."

    show captain at right:
        zoom 0.7
    with moveinright

    pc "Suspects are in holding. I need you in interrogation — now."
    pc "Don't keep them waiting."

    hide captain with moveoutright
    "He walks off."

    jump day5_choice

label day5_choice:
    menu:
        "Listen to the recovered call logs first.":
            jump day5_call_logs
            
        "Proceed directly to interrogation.":
            jump interrogation_hub

label day5_call_logs:
    scene black with dissolve
    "You put your headphones on and play the first audio file."

    # --- Call Log 1 ---
    show text "{size=50}CALL LOG: PAT & TOPH{/size}" at truecenter with dissolve
    pause 2.0
    hide text with dissolve

    "The audio is grainy, but Pat's voice is clear, panicked but aggressive."
    "Pat" "I'm not playing around, Toph. You bring the money, or I'm going to your coach. Your dad too."
    "Toph" "(Muffled) Pat, wait... don't do this. I don't have that kind of cash on me!"
    "Pat" "Figure it out! Tonight, or it's over for you."
    "System" "The call abruptly ends."
    
    $ record_clue("Toph", "Audio Evidence|Call log confirms Pat was actively extorting him for money on the night of the murder.")

    pause 1.0

    # --- Call Log 2 ---
    show text "{size=50}CALL LOG: TOPH & DAN{/size}" at truecenter with dissolve
    pause 2.0
    hide text with dissolve

    "The second recording starts. Toph's voice is shaking this time. Dan's voice is low, hushed."
    "Toph" "Dan? Are you there? She's out of control. I don't know what to do."
    "Dan" "(Whispering) Calm down. Just meet me on the 6th floor. I can handle her. Just get her to the hallway."
    "Toph" "Are you sure? If she screams—"
    "Dan" "She won't. Just do your part."
    
    $ record_clue("Dan (Janitor)", "Audio Evidence|Call log between him and Toph. Dan told Toph to bring Pat to the 6th floor, stating he could 'handle her'.")
    $ record_clue("Toph", "Audio Evidence|Conspired with Dan over the phone to corner Pat on the 6th floor.")

    "You take off your headphones. The conspiracy is undeniable now."
    mc "Dan wasn't just a bystander. Toph brought her right to him."
    pause 1.0
    
    jump interrogation_hub

label interrogation_hub:
    $ show_hud = False
    scene black
    s "System: Choose the suspect to interrogate."
    call screen interrogation_room

# -----------------------------------------------------------
#                        DAN'S INTERROGATION
# -----------------------------------------------------------
label interrogate_dan:
    scene interrogation_bg with dissolve
    show dan_face at center
    
    s "System: You step into the interrogation room. The door clicks shut behind you."
    mc "Let's begin. State your full name, age, and role at the university."
    d "Dan… Danielle Bautista. I'm a janitor. I've been here two years."
    
    $ q1 = False
    $ q2 = False
    $ q3 = False
    $ q4 = False
    $ answered = 0
    
    while answered < 4:
        menu:
            "State your full name, age, and role in the university." if not q1:
                $ q1 = True
                $ answered += 1
                d "Dan… Danielle Bautista."
                play sound "audio/typewriter.mp3"
                
            "Where do you live?" if not q2:
                $ q2 = True
                $ answered += 1
                d "At Caloocan."
                mc "I'm sorry, I couldn't hear you clearly. Where?"
                d "At Caloocan."
                play sound "audio/typewriter.mp3"
                
            "How long have you been working here?" if not q3:
                $ q3 = True
                $ answered += 1
                d "I have been working here for two years."
                play sound "audio/typewriter.mp3"
                
            "What are your usual duties on campus?" if not q4:
                $ q4 = True
                $ answered += 1
                d "Janitor."
                play sound "audio/typewriter.mp3"

    s "System: New choices pop out."
    $ q1 = False
    $ q2 = False
    $ q3 = False
    $ q4 = False
    $ answered = 0
    
    while answered < 4:
        menu:
            "What time do you normally clock out?" if not q1:
                $ q1 = True
                $ answered += 1
                d "Till 8 pm."
                play sound "audio/typewriter.mp3"
                
            "How did you first meet the victim?" if not q2:
                $ q2 = True
                $ answered += 1
                d "I always see her at the hallway, she greets me when she needs a hand in opening the classroom."
                play sound "audio/typewriter.mp3"
                
            "How long have you known the victim?" if not q3:
                $ q3 = True
                $ answered += 1
                "Dan thinks deeply…"
                d "Probably 2 years."
                play sound "audio/typewriter.mp3"
                
            "How would you describe your relationship with her?" if not q4:
                $ q4 = True
                $ answered += 1
                d "What relationship? I’m just a janitor here."
                "He said it looking annoyed."
                play sound "audio/typewriter.mp3"

    s "System: New choices pop out."
    $ q1 = False
    $ q2 = False
    $ q3 = False
    $ q4 = False
    $ answered = 0

    while answered < 4:
        menu:
            "Did you ever have disagreements or conflicts with her?" if not q1:
                $ q1 = True
                $ answered += 1
                d "How would I have a disagreement with her… I am just a janitor."
                play sound "audio/typewriter.mp3"
                
            "When was the last time you saw her?" if not q2:
                $ q2 = True
                $ answered += 1
                d "This morning, I went to their classroom in the hallway."
                mc "Before the incident??"
                d "That’s what I mean."
                play sound "audio/typewriter.mp3"
                
            "Where were you earlier before that?" if not q3:
                $ q3 = True
                $ answered += 1
                d "Nung umaga?"
                mc "No, before 8:30 pm."
                d "At the hallway."
                mc "What were you doing?"
                d "I’m a janitor—what do you think I do? Of course I would be cleaning."
                play sound "audio/typewriter.mp3"
                
            "Did you speak to the victim that evening?" if not q4:
                $ q4 = True
                $ answered += 1
                d "No."
                "System: (Lie detected)"
                play sound "audio/typewriter.mp3"

    s "System: New choices pop out."
    $ q1 = False
    $ q2 = False
    $ answered = 0
    
    while answered < 2:
        menu:
            "Was there a reason you needed to speak to her privately?" if not q1:
                $ q1 = True
                $ answered += 1
                d "I said we didn’t talk."
                play sound "audio/typewriter.mp3"
                
            "Who can confirm your whereabouts during that time?" if not q2:
                $ q2 = True
                $ answered += 1
                d "Ask the janitors. The students."
                play sound "audio/typewriter.mp3"

    $ interrogated_dan = True
    $ record_clue("Dan (Janitor)", "Interrogation|Denied speaking to Pat, contradicting CCTV evidence.")
    scene black with dissolve
    jump interrogation_hub

# -----------------------------------------------------------
#                        TOPH'S INTERROGATION
# -----------------------------------------------------------
label interrogate_toph:
    scene interrogation_bg with dissolve
    show toph_face at center 
    
    s "System: You step into the interrogation."
    s "System: Choose your first question."
    
    $ q1 = False
    $ q2 = False
    $ q3 = False
    $ q4 = False
    $ answered = 0
    
    while answered < 4:
        menu:
            "State your full name, age, and course." if not q1:
                $ q1 = True
                $ answered += 1
                "Toph" "Toph Bernales, they call me Toph. I am a nursing student and an athlete, I am 22 years old."
                
            "Where do you live?" if not q2:
                $ q2 = True
                $ answered += 1
                "Toph" "I live there at the dorm near the school. I also share a room with my close friend and he’s also my teammate in basketball."
                
            "Tell me your Thursday schedule." if not q3:
                $ q3 = True
                $ answered += 1
                "Toph" "Thursday schedule? Uhmm… around 7:30 to 12 I was around the classroom, and from 12 to 1:30 I was just roaming around the campus. Then around 2 to 3:30 I was just practicing my butterfly knife skills. Then from 5:30 to 8 uhm I was at basketball practice."
                
            "Why do you have a butterfly knife?" if not q4:
                $ q4 = True
                $ answered += 1
                "Toph" "Uhm… its nothing its just a hobby like performing tricks."

    s "System: New choices pop out."
    $ q1 = False
    $ q2 = False
    $ q3 = False
    $ q4 = False
    $ answered = 0
    
    while answered < 4:
        menu:
            "Have you ever thought of hurting someone with your knife?" if not q1:
                $ q1 = True
                $ answered += 1
                "Toph" "Hurt someone?? No! I have never thought of hurting anyone using the butterfly knife."
                
            "How did you first meet the victim?" if not q2:
                $ q2 = True
                $ answered += 1
                "Toph" "Pat? The first time I saw her, Austin was sketching her face—what a weirdo. But somehow, we got closer since we kept running into each other around campus."
                
            "How long did you know her?" if not q3:
                $ q3 = True
                $ answered += 1
                "Toph" "I’ve known her for 8 months but we’ve been broken up for a month."
                
            "What led to the end of your relationship?" if not q4:
                $ q4 = True
                $ answered += 1
                "Toph" "Uhm how do i say this.. We experienced a pregnancy scare then we have an argument that led to us breaking up."

    s "System: New choices pop out."
    $ q1 = False
    $ q2 = False
    $ q3 = False
    $ q4 = False
    $ answered = 0
    
    while answered < 4:
        menu:
            "When was the last time you saw her?" if not q1:
                $ q1 = True
                $ answered += 1
                "Toph" "No, I didnt see her."
                
            "Did you speak to the victim that evening?" if not q2:
                $ q2 = True
                $ answered += 1
                "Toph" "No… no…"
                
            "Where were you earlier that night?" if not q3:
                $ q3 = True
                $ answered += 1
                "Toph" "At the gym we were training for the basketball game."
                
            "Who can confirm your whereabouts during that time?" if not q4:
                $ q4 = True
                $ answered += 1
                "Toph" "Uhmmm… Our coach."

    $ interrogated_toph = True
    $ record_clue("Toph", "Interrogation|Claims he was at basketball practice, ending at 8 PM. Denied seeing her.")
    scene black with dissolve
    jump interrogation_hub

# -----------------------------------------------------------
#                       AUSTIN'S INTERROGATION
# -----------------------------------------------------------
label interrogate_austin:
    scene interrogation_bg with dissolve
    show austin_face at center 
    
    s "System: You step into the interrogation."
    s "System: Choose your first question."
    
    $ q1 = False
    $ q2 = False
    $ q3 = False
    $ q4 = False
    $ answered = 0
    
    while answered < 4:
        menu:
            "State your full name, age, and course." if not q1:
                $ q1 = True
                $ answered += 1
                "Austin" "Austin Encantadia, 21, Fine arts student."
                mc "Speak properly. Speak louder—the camera can’t hear you."
                
            "Where do you live?" if not q2:
                $ q2 = True
                $ answered += 1
                "Austin" "I live somewhere around there, just outside the main campus."
                
            "Tell me your Thursday schedule." if not q3:
                $ q3 = True
                $ answered += 1
                "Austin" "Um, s-so what I’d do is come in early since I live nearby, and then I’d, um, go to my classes and d-d-do some drawing, um, and then I’d, um, look over m-most of the materials I use for my drawings."
                
            "Why do you arrive so early?" if not q4:
                $ q4 = True
                $ answered += 1
                "Austin" "Because that’s where my mom is—there’s no one else around, and we’re happy since we don’t have anyone else with us."

    s "System: New choices pop out."
    $ q1 = False
    $ q2 = False
    $ q3 = False
    $ q4 = False
    $ answered = 0
    
    while answered < 4:
        menu:
            "What do you usually draw?" if not q1:
                $ q1 = True
                $ answered += 1
                "Austin" "Beauty is what I usually draw."
                
            "How well did you know Pat?" if not q2:
                $ q2 = True
                $ answered += 1
                "Austin" "Um… how did I get to know her… I-I always, um, kept reminding her… showing her how beautiful she is… making sure she knew what I thought about her beauty."
                
            "How many times have you drawn her?" if not q3:
                $ q3 = True
                $ answered += 1
                "Austin" "The day I saw her, it felt like something started running through my mind—I kept wanting it to be her, her, just her."
                
            "Do you admire her?" if not q4:
                $ q4 = True
                $ answered += 1
                "Austin" "I don’t think ‘like’ is enough to explain what I feel for her."
                mc "Never mind.. Never mind."

    s "System: New choices pop out."
    $ q1 = False
    $ q2 = False
    $ q3 = False
    $ q4 = False
    $ q5 = False
    $ answered = 0
    
    while answered < 5:
        menu:
            "Did you ever speak to her directly?" if not q1:
                $ q1 = True
                $ answered += 1
                "Austin" "I talked to her? Of course I did. I told her… I told her what I wanted to say to her."
                
            "Did you ever speak to her directly? (Follow up)" if q1 and not q2:
                $ q2 = True
                $ answered += 1
                "Austin" "Like I said earlier… hehe… I told her everything… hehe… every single thing."
                
            "Did you speak to the victim that evening?" if not q3:
                $ q3 = True
                $ answered += 1
                "Austin" "Like I said earlier… hehe… I told her everything… hehe… every single thing."
                
            "Where were you earlier that night?" if not q4:
                $ q4 = True
                $ answered += 1
                "Austin" "Usually, um, I-I just go to certain places… like I said… looking for something beautiful to, to look at for my drawings."
                
            "Who can confirm your whereabouts during that time?" if not q5:
                $ q5 = True
                $ answered += 1
                "Austin" "Did someone see me? No one… no one."

    $ interrogated_austin = True
    $ record_clue("Austin", "Interrogation|Obsessed with the victim. Has no alibi for the night of the murder.")
    scene black with dissolve
    jump interrogation_hub

# -----------------------------------------------------------
#                      CHANDLER'S INTERROGATION
# -----------------------------------------------------------
label interrogate_chandler:
    scene interrogation_bg with dissolve
    show chandler_face at center 
    
    s "System: You step into the interrogation."
    s "System: Choose your first question."
    
    $ q1 = False
    $ q2 = False
    $ q3 = False
    $ q4 = False
    $ answered = 0
    
    while answered < 4:
        menu:
            "State your full name, age, and course." if not q1:
                $ q1 = True
                $ answered += 1
                "Chandler" "Chandler Soriano, 19 years old, nursing."
                play sound "audio/typewriter.mp3"
                
            "Where do you live?" if not q2:
                $ q2 = True
                $ answered += 1
                "Chandler" "Around North Caloocan."
                play sound "audio/typewriter.mp3"
                
            "Tell me your Thursday schedule." if not q3:
                $ q3 = True
                $ answered += 1
                "Chandler" "I had an early class back then—around 7 in the morning—so I stayed until the evening. I’d just spend my vacant periods doing whatever, sometimes for about two hours."
                play sound "audio/typewriter.mp3"
                
            "What is your relationship with her?" if not q4:
                $ q4 = True
                $ answered += 1
                "Chandler" "She’s my girlfriend."
                play sound "audio/typewriter.mp3"

    s "System: New choices pop out."
    $ q1 = False
    $ q2 = False
    $ q3 = False
    $ q4 = False
    $ answered = 0
    
    while answered < 4:
        menu:
            "How did your relationship with the victim (Pat) begin?" if not q1:
                $ q1 = True
                $ answered += 1
                "Chandler" "We got to know each other through one of my friends. Toph—uh—we went to a bar back then, we were planning to drink, and that’s when he met her. They got to know each other and eventually had a relationship. But because they had some issues between them, Toph introduced me to Pat, and from there, things just kept going."
                play sound "audio/typewriter.mp3"
                
            "How long were you and Pat together?" if not q2:
                $ q2 = True
                $ answered += 1
                "Chandler" "We’ve been in a relationship exactly for one month."
                mc "Exactly?"
                "Chandler" "Yes."
                play sound "audio/typewriter.mp3"
                
            "When was the last time you saw her?" if not q3:
                $ q3 = True
                $ answered += 1
                "Chandler" "Um, I haven’t seen her yet, because we have different schedules. Sometimes she has class, and if she’s not in class, then I’m the one in class."
                play sound "audio/typewriter.mp3"
                
            "Where were you that night?" if not q4:
                $ q4 = True
                $ answered += 1
                "Chandler" "Ah, I was waiting for her back then because I had a vacant period, so I waited for her."
                play sound "audio/typewriter.mp3"

    s "System: New choices pop out."
    $ q1 = False
    $ q2 = False
    $ q3 = False
    $ answered = 0
    
    while answered < 3:
        menu:
            "Did you speak to the victim that evening?" if not q1:
                $ q1 = True
                $ answered += 1
                "Chandler" "No, I never got to talk to her at all."
                
            "What were your plans that night?" if not q2:
                $ q2 = True
                $ answered += 1
                "Chandler" "As I said, we were supposed to go on a date since it was our one-month anniversary. We had plans to go out—that’s it."
                
            "Did someone see you at the school that night?" if not q3:
                $ q3 = True
                $ answered += 1
                "Chandler" "That night??"
                mc "At the school."
                "Chandler" "That night??"
                "Chandler" "I don’t really know. I’m not sure if anyone saw me—I’m not sure."

    $ interrogated_chandler = True
    $ record_clue("Chandler", "Interrogation|Was waiting for Pat on the night she died. Claims no one saw him.")
    scene black with dissolve
    jump interrogation_hub

# -----------------------------------------------------------
#                      POST INTERROGATION
# -----------------------------------------------------------
label post_interrogation_hub:
    scene police_station with fade
    show captain at right
    
    pc "Well? Did they give you anything useful?"
    mc "They gave me a lot of contradictions, Captain. I need to review my notes and put the pieces together."
        
# ============================================================================
#                                HELPER FUNCTIONS
# ============================================================================
init python:
    # A function to check if a specific clue was added to a specific character's journal
    def has_clue(person_name, keyword):
        for person in journal_list:
            if person_name.lower() in person.name.lower():
                for clue in person.descriptions:
                    if keyword.lower() in clue.lower():
                        return True
        return False

# ============================================================================
#                             CHAPTER 6: INTUITION
# ============================================================================

label chapter6:
    $ current_day = 6
    scene black with fade
    pause 1.0

    show text "{size=70}Day 6{/size}" at truecenter with dissolve
    pause 2.0
    hide text with dissolve

    scene police_station with fade
    play music "audio/station_ambiance.mp3" loop fadein 1.0
    
    show captain at right
    
    pc "All suspects have been interrogated. The decision is yours now."
    pc "Get it wrong, and the guilty walks free."

    # Call the new interactive screen
    call screen final_accusation

label evaluate_final_accusation:
    python:
        # 1. Did the player mark everyone as a Suspect?
        all_suspects = (end_dan_status == "Suspect" and end_toph_status == "Suspect" and end_austin_status == "Suspect" and end_chandler_status == "Suspect")

        # 2. Check if the assigned crimes match the TRUTH
        dan_correct = (end_dan_status == "Suspect" and end_dan_crime == "Unlawful Restraint")
        toph_correct = (end_toph_status == "Suspect" and end_toph_crime == "Drug Distribution")
        austin_correct = (end_austin_status == "Suspect" and end_austin_crime == "Stalking")
        chandler_correct = (end_chandler_status == "Suspect" and end_chandler_crime == "Murder")

        # Count total correct accusations
        correct_count = sum([dan_correct, toph_correct, austin_correct, chandler_correct])

    # --- ENDING BRANCHES ---

    # TRUE ENDING: All 4 are suspects, all 4 crimes are exactly right.
    if all_suspects and correct_count == 4:
        jump true_ending

    # GOOD ENDING: All 4 are suspects. Chandler is correct (Murder), but the other 3 have the WRONG crime.
    elif all_suspects and chandler_correct and not dan_correct and not toph_correct and not austin_correct:
        jump good_ending

    # NEUTRAL ENDING: 1 to 3 people got correct crimes, BUT Chandler got away (not caught/incorrect crime).
    elif not chandler_correct and correct_count >= 1 and correct_count <= 3:
        jump neutral_ending

    # BAD ENDING: 0 people correctly arrested.
    else:
        jump bad_ending


# -----------------------------------------------------------
#                         ENDINGS
# -----------------------------------------------------------

label true_ending:
    mc "I am arresting all of them."
    pc "All of them?"
    mc "They’re connected. The evidence doesn’t point to one person, it points to the whole group."
    mc "Austin stalked her. Dan restrained her. Toph supplied the drugs. And Chandler finished it."
    
    scene black with fade
    pause 2.0
    show text "{size=50}TRUE ENDING REACHED\nFlawless Deduction{/size}" at truecenter with dissolve
    pause 3.0
    return

label good_ending:
    mc "I am arresting all of them. But Chandler is the one who pulled the trigger."
    pc "We got Chandler on Murder. But the charges on the others won't stick in court... you pinned the wrong secondary crimes on them."
    pc "They walk. But at least Pat's killer is behind bars."
    
    scene black with fade
    pause 2.0
    show text "{size=50}GOOD ENDING REACHED\nPartial Justice{/size}" at truecenter with dissolve
    pause 3.0
    return

label neutral_ending:
    mc "I've made my arrests."
    pc "You got some of the accomplices, Detective... but the timeline doesn't fit. Chandler is walking free."
    pc "The mastermind got away."
    
    scene black with fade
    pause 2.0
    show text "{size=50}NEUTRAL ENDING REACHED\nThe Killer Escaped{/size}" at truecenter with dissolve
    pause 3.0
    return

label bad_ending:
    mc "I..."
    pc "You don't have it, do you? Your charges are a mess. None of this will hold up in court."
    pc "The DA is throwing the case out. They all walk."
    
    scene black with fade
    pause 2.0
    show text "{size=50}BAD ENDING REACHED\nCase Dismissed{/size}" at truecenter with dissolve
    pause 3.0
    return