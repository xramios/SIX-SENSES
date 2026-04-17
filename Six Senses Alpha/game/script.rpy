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
    
    show text "{size=50}you wake up hazy, your phone across the room ringing endlessly{/size}" as intro1:
        xalign 0.5 yalign 0.8
    with dissolve

    play sound "audio/phonecall.mp3" loop
    $ renpy.pause(3.0)

    hide intro1 with dissolve
    stop sound

    show text "{size=50}you answer the call, its the chief{/size}" as intro1:
        xalign 0.5 yalign 0.8
    with dissolve

    hide intro1 with dissolve
    pc "Detective, are you available right now?– no– it doesn't matter, come to the location i sent-ASAP"
    with dissolve

    hide intro1 with dissolve
    window hide

    show text "{size=50}groggy and confused at not even being able to answer-{/size}" as intro2:
        xalign 0.5 yalign 0.8
    with dissolve
    
    $ renpy.pause(0.8)
    hide intro2 with dissolve

    show text "{size=50}you hurriedly grab your keys and rush out the door{/size}" as intro3:
        xalign 0.5 yalign 0.8
    with dissolve

    $ renpy.pause(1.0)
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
    
    pc "You’re finally here, [mc]."
    
    pc "It’s gruesome in there... *sighs*"
    pc "But we don't have time to dawdle—so let me fill you in."

    stop music fadeout 1.0
    scene prologue-call with flash
    
    op "9-1-1, what’s your emergency?"
    
    d "Hello? M-may... may—"

    pc "A call was made to 9-1-1 at 5:56 AM in the morning."
    
    scene prologue-call2 with dissolve
    
    pc "The janitor, Dan-found the body in around 5:53 AM."
    
    pc "Scene’s... rough. Whoever did this didn't hold back."

    scene main_hallway with fade

    show chief_normal at right:
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

    $ add_item("Crime Photo", "A photo of the 6th floor storage room.", "images/crime_scene.png")
    s "{u}Crime Photo{/u} added to your Bag."

    call screen inventory_screen
    s "System: Items will be stored there."

    show image "images/ui/journal_icon.png" as icon_jou at popup_center
    s "System: Journal Unlocked."
    pause
    show image "images/ui/journal_icon.png" as icon_jou at move_to_hud_right
    s "System: Check your journal."

    $ add_suspect("Dan (Janitor)", "The man who found the body. Seems shaken.", "images/characters/dan.png")
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
    show dan_face at Transform(ypos=0.3, zoom=1.5, xpos=0.70) with dissolve
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
    if result == "cctv_monitor":
        jump cctv_room_monitor
    elif result == "go_cctv_hallway":
        jump cctv_hallway
    jump cctv_room

label cctv_room_monitor:
    scene cctv_room
    call screen cctv_monitor
    $ chosen_cam_index = _return   
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
    "The footage shows Dan gripping Pat firmly by the hand, pulling him down the hallway with urgency."
    "Pat resists slightly, stumbling to keep up as he tries to pull back."
    "Dan doesn’t let go, tightening his grip and dragging Pat toward the storage room."
    "Without hesitation, Dan yanks the door open and pulls Pat inside. The door shuts quickly behind them."
    
    $ add_suspect("Dan (Janitor)", "Seen on CCTV leading Pat to storage room.", "images/characters/dan.png")
    $ record_clue("Dan (Janitor)", "Video Evidence|Camera 1 shows Dan dragging Pat into storage room against his will.")
    
    mc "Dan lied. He said he just found the body this morning, but here he is with Pat the night before."
    
    jump cctv_room_monitor

label cctv_reveal_cam4:
    scene black with fade
    show text "{size=50}CCTV FOOTAGE - CAMERA 4{/size}" at truecenter with dissolve
    pause 1.0
    hide text with dissolve
    
    scene cctv_4_reveal with fade
    "You discovered CCTV footage from the night of the incident."
    "It shows Toph stepping out of the 6th-floor elevator, rushing down the hallway."
    "He looks anxious, checking over his shoulder several times before going out of frame."
    
    $ add_suspect("Toph", "Seen on CCTV near the crime scene on the night of the incident.", "images/characters/toph.png")
    $ record_clue("Toph", "Video Evidence|Camera 4 shows Toph exiting elevator and rushing toward storage room area, acting nervous.")
    
    mc "Toph was here that night. Why didn't he come forward?"
    
    jump check_both_cctv_solved

label check_both_cctv_solved:
    if cctv_cam1_solved and cctv_cam4_solved:
        if not scenario_picker1:
            $ scenario_picker1 = True
            mc "I've now seen both camera feeds. This gives me a much clearer picture of what happened."
            $ record_clue("Case Summary", "CCTV Analysis|Both cameras show Dan forcing Pat into storage room, then later Toph acting suspiciously nearby.")
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
#                             POLICE STATION (REVIEW HUB)
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
            mc "And I was able to enhance one of the feeds."
            mc "It shows Dan leading the victim towards the storage room between 6 and 8 PM."
            mc "There's also another suspected student appearing later in the footage."
            pc "So Dan and that student could also be tied in one way or another?"
            mc "Yes, sir. I've added them to the suspect list."
            if not any(s.name == "Dan (Janitor)" for s in journal_list):
                $ add_suspect("Dan (Janitor)", "Janitor seen leading victim to storage room on CCTV.", "images/characters/dan.png")
        # Add Unknown Student (temporary name)
        if not any(s.name == "Unknown Student" for s in journal_list):
            $ add_suspect("Unknown Student", "Appears later in CCTV footage near storage room. Identity unknown.", "images/suspects/unknown.png")
            $ record_clue("Unknown Student", "Video Evidence|Seen on CCTV entering storage room area after Dan and victim.")
        pc "Good work. This gives us a clearer direction for the investigation."
        mc "What's our next move, Captain?"
        pc "Go over the evidence again—check if she made any calls or sent messages during that time."
        pc "And have the DNA tested too."
        if evidence_taken["waterbottle"]:
            mc "I did find a crushed water bottle near the scene."
        if evidence_taken["powder"]:
                mc "There was also synthetic powder. Could be related."
        if evidence_taken["powder"] and not evidence_taken["waterbottle"]:
            mc "Found synthetic drugs in the storage room."
        if evidence_taken["patbag"]:
            mc "Pat's bag was ransacked – someone was looking for something."
        if evidence_taken["patphone"]:
            mc "Her phone was there. Locked, but we can try to crack it."
        if evidence_taken["id"]:
            mc "Her ID was bloody and tossed aside."
        if evidence_taken["knife"]:
            mc "I also found a butterfly knife hidden in a locker. Handle was wiped clean."

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

    play sound "audio/announcement.mp3"
    s "In light of the recent incident, all classes will remain asynchronous until further notice."
    s "Entry into restricted areas is strictly forbidden. Students found in violation will face immediate disciplinary consequences."
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
    show text Text("Sense Activated — SMELL", size=70, color="#FF00C8") at truecenter
    with dissolve
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
        "The cigarette odor is thick in here – someone has been smoking inside the crime scene."
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
        "The stench of old blood is overwhelming here – something inside has been soaked."
        "You open Toph Bernales' locker and find a butterfly knife, the handle wiped clean."
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
        pc "Good Catch"
        pc"That’s our break. If there’s DNA on those, we’re getting names. Get it checked immediately"
        mc "What's our next move?"
        pc "Go over the evidence again—check if she made any calls or sent messages during that time. And have the DNA from both items tested too."
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
    elif not evidence_taken["cigarette"] and evidence_taken["knife"]:
        pc "You’re back. You look worried. So… what do we have?"
        mc "We followed up on yesterday’s findings. I started tracing the victim’s phone but the phone was locked."
        pc "Of course it is. Any way around it?"
        mc "I’ll try to bypass it, but it’ll take time."
        pc "Then don’t wait on it. What else?"
        mc "We recovered a butterfly knife from Toph Bernales’ locker. It could still have DNA on it."
        pc "Good catch. A butterfly knife… in Toph Bernales’ locker? Either he’s careless… or someone wants him to look that way."
        mc "We didn’t check all personal items thoroughly… and we haven’t confirmed any connections to potential suspects yet."
        pc "Don’t lock onto Bernales just yet. Verify everything. If this is planted, we’re being played."
    pc "Alright. Log everything and get some rest. Tomorrow we dig deeper."
    scene black with dissolve
    pause 2.0
    scene car with fade
    play sound "audio/carengine.mp3"
    pause 5.0
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
    pc "…"
    mc "…"
    pc "The evidence room is ready. Lay everything out. Maybe seeing it all together will spark something."
    hide captain with moveoutright
    jump evidence_room

label evidence_room:
    scene evidence_room_bg with fade
    "You enter the evidence room and spread every collected piece across the large table."
    "The overhead light hums, casting a sterile glow on the objects."
    "You may interact with the evidence."
    call screen evidence_table
    if _return == "success":
        $ phone_unlocked = True
        "The phone unlocks! You can now access its data on the computer."
    jump evidence_room

# Day 4
# Day 5
# Day 6