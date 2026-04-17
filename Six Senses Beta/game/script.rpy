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
    "The footage shows Dan gripping Pat firmly by the hand, pulling him down the hallway with urgency."
    "Pat resists slightly, stumbling to keep up as he tries to pull back."
    "Dan doesn’t let go, tightening his grip and dragging Pat toward the storage room."
    "Without hesitation, Dan yanks the door open and pulls Pat inside. The door shuts quickly behind them."
    
    $ add_suspect("Dan (Janitor)", "Seen on CCTV leading Pat to storage room.", "images/characters/danicon.png")
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
                $ add_suspect("Dan (Janitor)", "Janitor seen leading victim to storage room on CCTV.", "images/characters/danicon.png")
        # Add Unknown Student (temporary name)
        if not any(s.name == "Unknown Student" for s in journal_list):
            $ add_suspect("Toph Bernales", "Appears later in CCTV footage near storage room. Identity unknown.", "images/suspects/Toph.png")
            $ record_clue("Toph Bernales", "Video Evidence|Seen on CCTV entering storage room area after Dan and victim.")
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
    pc "…"
    mc "…"
    
    # Conditional logic if player examined the body on Day 1
    if scenario_picker2:
        pc "The forensic team saw the cctv footage and got a hold of 4 different cctv tapes you should take a look at."
        mc "Good. I'll review them immediately."
        $ record_clue("Case Summary", "Evidence Updates|Forensics recovered 4 CCTV tapes from the crime scene.")
    
    pc "The evidence room is ready. Lay everything out. Maybe seeing it all together will spark something."
    hide captain with moveoutright
    jump evidence_room

label evidence_room:
    $ current_location = "evidence_room"
    scene evidence_room_bg with fade
    
    "System" "You enter the evidence room."
    "System" "Your bag hangs open. You lift it and plop it on the floor below the corkboard."
    "System" "Photos, bagged items, notes — it's all still inside, waiting to be sorted."
    "System" "Three avenues stand out."
    "System" "You can examine trace evidence, review CCTV tapes, or attempt to hack the victim's phone."
    "System" "You may now interact with the evidence."
    
    $ show_hud = True
    call screen detective_hud

# --- Day 3 Interaction Hub ---
label evidence_room_hub:
    $ current_location = "evidence_room"
    scene evidence_room_bg with fade
    $ show_hud = True
    call screen detective_hud
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
    
    scene phone_bank_toph_chandler with dissolve # Replace with your actual image
    "System" "A screenshot of Toph sending Chandler a bank transfer."
    pause
    
    scene phone_bank_toph_pat with dissolve # Replace with your actual image
    "System" "A screenshot of Toph sending Pat a bank transfer."
    pause
    
    $ record_clue("Toph", "Financial|Sent bank transfers to both Pat and Chandler.")
    $ record_clue("Chandler", "Financial|Received a bank transfer from Toph.")
    jump phone_unlocked_hub

# --- CCTV Tapes ---
label cctv_tape_view:
    $ show_hud = False
    scene black with fade
    
    if tape_num == 1:
        show text "{size=50}CCTV: DAN LEADING PAT TO THE STORAGE ROOM{/size}" at truecenter with dissolve
        pause 2.0
        scene cctv_dan_pat with fade
        "The footage shows Dan gripping Pat firmly by the hand, pulling him down the hallway with urgency."
        "Pat resists slightly, stumbling to keep up as he tries to pull back."
        "Dan doesn’t let go, tightening his grip and dragging Pat toward the storage room."
        "Without hesitation, Dan yanks the door open and pulls Pat inside. The door shuts quickly behind them."
        $ record_clue("Dan (Janitor)", "CCTV Tape 1|Forcibly dragged Pat into the storage room.")

    elif tape_num == 2:
        show text "{size=50}CCTV: CHANDLER ON CALL{/size}" at truecenter with dissolve
        pause 2.0
        scene cctv_chandler with fade
        "The footage shows Chandler exiting the area, walking out of frame without looking back."
        "Moments later, Austin slowly leans out from behind the corner, cautiously peeking in the direction Chandler went."
        "He scans the hallway, lingering for a second as if making sure it’s clear, before stepping out slightly further, still keeping part of his body hidden."
        $ add_suspect("Chandler", "Seen on CCTV near the crime scene.", "images/suspects/chandler.png")
        $ add_suspect("Austin", "Seen tailing Chandler on CCTV.", "images/suspects/austin.png")
        $ record_clue("Chandler", "CCTV Tape 2|Seen leaving the hallway area while on a phone call.")

    elif tape_num == 3:
        show text "{size=50}CCTV: AUSTIN PEEKING{/size}" at truecenter with dissolve
        pause 2.0
        scene cctv_austin with fade
        "The footage shows Chandler exiting the area, walking out of frame without looking back."
        "Moments later, Austin slowly leans out from behind the corner, cautiously peeking in the direction Chandler went."
        "He scans the hallway, lingering for a second as if making sure it’s clear, before stepping out slightly further, still keeping part of his body hidden."
        $ record_clue("Austin", "CCTV Tape 3|Cautiously tracking Chandler's movements.")

    elif tape_num == 4:
        show text "{size=50}CCTV: TOPH AT ELEVATOR{/size}" at truecenter with dissolve
        pause 2.0
        scene cctv_toph_elevator with fade
        "The footage shows Toph suspiciously waiting inside the elevator while holding his phone."
        $ record_clue("Toph", "CCTV Tape 4|Seen nervously waiting in the elevator.")

    pause 1.0
    jump computer_access

label precinctd3:
    $ current_location = "precinctd3"
    scene police_station with fade
    play music "audio/station_ambiance.mp3" loop fadein 1.0
    
    $ show_hud = True
    call screen detective_hud
    
    # Safety loop in case the player closes a menu here
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
#                                   Day 4
# ============================================================================

label day4intro:
    $ current_day = 4
    scene black with fade
    pause 1.0

    # You can change the Sense here to whatever fits Day 4!
    show text "{size=70}Day 4{/size}" at truecenter with dissolve
    pause 2.0
    hide text with dissolve

    scene police_station with fade
    play music "audio/station_ambiance.mp3" loop fadein 1.0
    
    "You arrive at the precinct early the next morning."
    show captain at right:
        zoom 0.7
    with moveinright
    
    pc "Morning, Detective. Tell me you found something solid in those phone logs and tapes."
    mc "I did, Captain. We have enough to start asking some very difficult questions."
    
# ============================================================================
#                                   DAY 5
# ============================================================================

label day5intro:
    $ current_day = 5
    scene black with fade
    pause 1.0

    show text "{size=70}Day 5{/size}" at truecenter with dissolve
    pause 2.0
    hide text with dissolve

    scene police_station with fade
    play music "audio/station_ambiance.mp3" loop fadein 1.0
    
    show captain at right:
        zoom 0.7
    with moveinright
    
    pc "Alright, Detective. We pulled them all in."
    pc "Dan, Toph, Austin, and Chandler. They're sitting in the interrogation room right now."
    pc "Don't let them off easy. We need answers."
    
    hide captain with moveoutright
    
    scene black with dissolve
    s "System: You step into the interrogation room."
    
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
    scene interrogation_bg with dissolve # Replace with your BG
    show dan_face at center
    
    s "System: You step into the interrogation."
    s "System: Choose your first question."
    
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

    # --- POINT CALCULATION SYSTEM ---
    python:
        toph_pts = 0
        chandler_pts = 0
        austin_pts = 0
        dan_pts = 0

        # TOPH POINTS
        if evidence_taken.get("powder", False): toph_pts += 5
        if has_clue("Toph", "Tape 4"): toph_pts += 10
        if evidence_taken.get("cigarette", False): toph_pts += 20
        if evidence_taken.get("knife", False): toph_pts += 20
        if has_clue("Toph", "extorting"): toph_pts += 10
        if has_clue("Toph", "Financial"): toph_pts += 5

        # CHANDLER POINTS
        if has_clue("Chandler", "Financial"): chandler_pts += 5
        if has_clue("Chandler", "call for help"): chandler_pts += 10
        if evidence_taken.get("cigarette", False): chandler_pts += 20
        if has_clue("Chandler", "Tape 2"): chandler_pts += 20

        # AUSTIN POINTS
        if has_clue("Austin", "Tape 3"): austin_pts += 10

        # DAN POINTS
        if has_clue("Dan", "Tape 1") or cctv_cam1_solved: dan_pts += 10
        if phone_unlocked: dan_pts += 10 # Phone access implies Dan & Toph call data

        # CHECK "ALL" REQUIREMENT (Must manually set all 4 to 'Suspect' in Journal)
        all_suspects_viable = False
        required_names = ["Dan", "Toph", "Austin", "Chandler"]
        viable_count = 0
        for p in journal_list:
            for req in required_names:
                if req in p.name and p.status == "Suspect":
                    viable_count += 1
        
        if viable_count >= 4:
            all_suspects_viable = True

    # --- ARREST DECISION MENU ---
    s "System: Review your evidence. The choices available depend on what you found."
    
    menu:
        "Arrest Toph [toph_pts] PTS" if toph_pts >= 40:
            jump arrest_toph
            
        "Arrest Chandler [chandler_pts] PTS" if chandler_pts >= 30:
            jump arrest_chandler
            
        "Arrest Austin [austin_pts] PTS" if austin_pts >= 5:
            jump arrest_austin
            
        "Arrest Dan [dan_pts] PTS" if dan_pts >= 10:
            jump arrest_dan
            
        "Arrest ALL of them" if all_suspects_viable:
            jump arrest_all

# -----------------------------------------------------------
#                         ENDINGS
# -----------------------------------------------------------

label arrest_toph:
    mc "I am arresting…"
    mc "Toph Bernales."
    
    scene interrogation_bg with dissolve
    show toph_face at center
    
    "Toph" "Wait- what me?"
    "Toph" "Do you know who you’re arresting right now?"
    "Toph" "This is ridiculous."
    
    jump normal_ending_dialogue

label arrest_chandler:
    mc "I am arresting…"
    mc "Chandler Soriano."
    
    scene interrogation_bg with dissolve
    show chandler_face at center
    
    "Chandler" "Now you care???"
    "Chandler" "Where was all this justice before?! HUH?!"
    "Chandler" "You don’t know anything about her… about what she went through!"
    "Chandler" "Her dad ruined my mom… he treated her like a slave… DO YOU HEAR ME?!"
    "Chandler" "And you expect me to just sit there and do nothing?!"
    "Chandler" "She deserved it… after everything they’ve caused."
    
    jump normal_ending_dialogue

label arrest_austin:
    mc "I am arresting…"
    mc "Austin Encantadia."
    
    scene interrogation_bg with dissolve
    show austin_face at center
    
    "Austin" "Huh you don’t see it don’t you?"
    "Austin" "It was never about one of us."
    "Austin" "It was about all of us."
    
    mc "What nonsense are u saying?"
    
    "Austin" "I didn’t just see it…"
    "System" "Austin tilts his head slightly."
    "Austin" "I saw something beautiful."
    
    jump austin_ending_dialogue

label arrest_dan:
    mc "I am arresting…"
    mc "Danielle Bautista."
    
    scene interrogation_bg with dissolve
    show dan_face at center
    
    d "No—no, please…"
    "System" "His voice is shaking."
    d "It wasn’t me… I swear it wasn’t me!"
    d "I just got caught up in all of this… I didn’t know it would go this far!"
    "System" "His breathing gets uneven."
    d "Please… you have to believe me…"
    d "I didn’t mean any of it… I didn’t want any of this to happen…"
    "System" "He is almost crying."
    d "Please don’t take me in… please…"
    
    jump normal_ending_dialogue

label arrest_all:
    mc "I am arresting…"
    
    pc "All of them?"
    mc "..."
    mc "They’re connected."
    mc "The evidence doesn’t point to one person, it points to all of them."
    mc "It was never about one suspect…"
    mc "It was about all of them."
    
    scene black with fade
    pause 2.0
    show text "{size=50}TRUE ENDING REACHED{/size}" at truecenter with dissolve
    pause 3.0
    return

# --- Ending Sequences ---

label normal_ending_dialogue:
    scene police_station with fade
    show captain at right
    
    pc "Suspects have been detained."
    pc "But something about this case still doesn’t sit right with me."
    mc "What do you mean?"
    
    scene black with fade
    pause 2.0
    show text "{size=50}CASE CLOSED?{/size}" at truecenter with dissolve
    pause 3.0
    return

label austin_ending_dialogue:
    scene police_station with fade
    show captain at right
    
    pc "Suspects have been detained."
    pc "But something about this case still doesn’t sit right with me."
    mc "What do you mean?"
    pc "What did Austin mean when he said it was all about us?"
    
    scene black with fade
    pause 2.0
    show text "{size=50}CASE CLOSED?{/size}" at truecenter with dissolve
    pause 3.0
    return