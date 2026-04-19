screen detective_hud():
    zorder 10
    if show_hud:
        hbox:
            align (0.98, 0.02)
            spacing 0.5
            if current_location != "evidence_room_hub":
                hbox:
                    align (0.98, 0.02)
                    spacing 0.5
                    imagebutton:
                        idle "images/ui/bag_icon.png"
                        hover "images/ui/bag_icon.png"
                        focus_mask True
                        action [SetVariable("selected_item", None), ShowMenu("inventory_screen")]
                        at hud_zoom(0.2, 0.22)
                    imagebutton:
                        idle "images/ui/journal_icon.png"
                        hover "images/ui/journal_icon.png"
                        focus_mask True
                        action [SetVariable("selected_suspect", None), ShowMenu("journal_screen")]
                        at hud_zoom(0.2, 0.22)
        
        # --- Day 1 ---
        if current_location == "mhallway":
            use mhallwayd1
      
        if current_location == "hallway2":
            use hallwayd1
        
        if current_location == "stairs":
            use stairsd1

        if current_location == "cctv_hallway":
            use cctv_hallwayd1
        
        if current_location == "cctv_room":
            use cctv_roomd1

        if current_location == "storage_room":
            use storage_roomd1

        if current_location == "body":
            use bodyd1

        if current_location == "lockers":
            use lockersd1

        # --- Day 2 ---
        if current_location == "mhallwayd2":
            use mhallwayd2
      
        if current_location == "hallwayd2":
            use hallwayd2
        
        if current_location == "stairsd2":
            use stairsd2

        if current_location == "cctv_hallwayd2":
            use cctv_hallwayd2
        
        if current_location == "storage_roomd2":
            use storage_roomd2

        if current_location == "lockersd2":
            use lockersd2

        if current_location == "mhallwayd2":
            use mhallwayd2

        if current_location == "zlockersd2":
            use zlockersd2

        if current_location == "patlockerd2":
            use patlockerd2

        # --- Day 3 ---
        if current_location == "evidence_room_hub":
            use evidence_room_d3

        if current_location == "precinctd3":
            use precinctd3_ui
    
        $ tooltip = GetTooltip()
        if tooltip:
            frame:
                xalign 0.5 yalign 0.95
                background Solid("#000000CC")
                padding (15, 8)
                text tooltip:
                    size 24
                    color "#FFFFFF"
            
# ============================================================================
#                             INVENTORY SCREEN
# ============================================================================
screen inventory_screen():
    tag menu
    zorder 15
    add Solid("#000000E6")
    label "EVIDENCE BAG" align (0.5, 0.05)
    hbox:
        align (0.5, 0.5)
        spacing 80
        vpgrid:
            cols 4          
            spacing 25       
            allow_underfull True 
            xsize 1000
            for i in range(16):
                if i < len(inventory_list):
                    $ item = inventory_list[i]
                    button:
                        action SetVariable("selected_item", item)
                        xysize (180, 180)
                        background Frame(Solid("#444"), 4, 4)
                        hover_background Solid("#4A90E2")
                        fixed:
                            xysize (150, 150)
                            align (0.5, 0.5)
                            add item.image:
                                size (150, 150)
                                fit "contain"
                                align (0.5, 0.5)
                else:
                    frame:
                        xysize (180, 180) 
                        background Frame(Solid("#222"), 2, 2)
                        text "EMPTY" align (0.5, 0.5) size 18 color "#444"
        frame:
            xsize 600 
            ysize 800 
            background Solid("#111")
            vbox:
                spacing 20
                if selected_item:
                    add Transform(selected_item.image, fit="contain"):
                        xysize (590, 350)
                        xalign 0.5
                    text selected_item.name size 30 color "#4A90E2"
                    text selected_item.description size 25
                    if current_day >= 3:
                        hbox:
                            spacing 20
                            xalign 0.5
                            textbutton "INSPECT":
                                # This saves the item name, closes the inventory, and triggers the inspection label
                                action [SetVariable("item_to_inspect", selected_item.name), Return(), Jump("inspect_item_logic")]
                                style "journal_tab"
                else:
                    text "Select item..." align (0.5, 0.5) color "#888"
    textbutton "RETURN" action Return() align (0.5, 0.95)

# ============================================================================
#                              JOURNAL SCREEN
# ============================================================================
screen journal_screen():
    tag menu
    zorder 15
    add Solid("#0b121a")

    frame:
        xsize 1200 ysize 800
        align (0.5, 0.5)
        background Frame(Solid("#f4ecd8"), 4, 4)
        padding (20, 20)
        hbox:
            ypos -60
            xalign 0.0
            spacing 2
            textbutton "Cover" action SetVariable("journal_page", 0) style "journal_tab"
            textbutton "Report" action SetVariable("journal_page", 1) style "journal_tab"
            for i, person in enumerate(journal_list):
                textbutton person.name:
                    action SetVariable("journal_page", i + 2)
                    style "journal_tab"
            if current_day >= 6:
                textbutton "FINAL" action SetVariable("journal_page", len(journal_list) + 2) style "journal_tab"

        if journal_page == 0:
            vbox:
                align (0.5, 0.5)
                text "SIX SENSES" size 80 color "#222"
                text "CASE FILE #109" size 20 color "#555" xalign 0.5
        elif journal_page == 1:
            hbox:
                spacing 20
                xfill True
                frame:
                    xsize 680
                    ysize 680
                    background None
                    padding (5, 10, 5, 10)
                    viewport:
                        yinitial 0.0
                        mousewheel True
                        scrollbars "vertical"
                        child_size (None, None)
                        vbox:
                            spacing 10
                            text "{size=40}INITIAL CASE REPORT{/size}" color "#222"
                            null height 5
                            text "{size=30}I. Basic Information{/size}" color "#4A90E2"
                            text "Case Title: The Storage Room Murder Case" size 25 color "#333"
                            text "Case Type: Principal Murder" size 25 color "#333"
                            text "Location: 6th Floor Storage Room, TVH Bldg" size 25 color "#333"
                            text "Date Reported: Jan. 5, 2026 | 7:00 AM" size 25 color "#333"
                            text "Reporting Party: Daniel Bautista, Maintenance" size 25 color "#333"
                            text "Responding Unit: Detective" size 25 color "#333"
                            null height 10
                            text "{size=30}II. Victim's Information{/size}" color "#4A90E2"
                            text "Name: Pat Estacio" size 25 color "#333"
                            text "Age: 21" size 25 color "#333"
                            text "Gender: Female" size 25 color "#333"
                            text "Height / Weight: --" size 25 color "#333"
                            text "Living Situation: Resides independently near the university, maintaining regular contact with her family while managing her own daily needs." size 25 color "#333"
                            text "Occupation: Fine Arts Student" size 25 color "#333"
                            text "Health Status: Physically healthy prior to the incident, No known chronic illnesses, History of recreational drug exposure (non-dependent)" size 25 color "#333"
                            text "Social Behavior:" size 25 color "#333"
                            text "  • Socially active and highly visible on campus" size 25 color "#333"
                            text "  • Charismatic and well-integrated within peer groups" size 25 color "#333"
                            text "  • Regularly attended parties and social gatherings" size 25 color "#333"
                            text "  • Maintained multiple close and romantic relationships" size 25 color "#333"
                            text "  • Status-conscious and responsive to peer perception" size 25 color "#333"
                            text "Last Seen Alive: By her classmates at 8:00 PM, their last class at Room 600, 6th Floor." size 25 color "#333"
                            null height 10
                            text "Condition at Discovery:" size 25 color "#333"
                            text "  • (Pending autopsy report)" size 25 color "#333"
                vbox:
                    xsize 500
                    yalign 0.0
                    spacing 8
                    text "Evidence Photo" size 20 color "#222" xalign 0.5
                    add Transform("images/str_room.png", fit="contain"):
                        size (384, 216)
                        xalign 0.5

        elif journal_page <= len(journal_list) + 1:
            $ current_person = journal_list[journal_page - 2]
            hbox:
                spacing 50
                vbox:
                    xsize 500
                    spacing 10
                    text current_person.name size 35 color "#222" xalign 0.5
                    if "Pat" in current_person.name:
                        frame:
                            background Solid("#8B0000")
                            padding (15, 5)
                            xsize 300
                            xalign 0.5
                            text "DECEASED / VICTIM" size 18 color "#fff" bold True xalign 0.5
                        null height 10
                        text "File: Case #109-B" size 14 color "#555" italic True xalign 0.5
                    else:
                        textbutton "[current_person.status] ▼":
                            style "status_toggle_button"
                            action If(current_person.status == "Person of Interest",
                                     SetField(current_person, "status", "Suspect"),
                                     SetField(current_person, "status", "Person of Interest"))
                            xalign 0.5
                    add Transform(current_person.image, fit="contain"):
                        size (400, 500)
                        xalign 0.5
                viewport:
                    yinitial 0.0
                    mousewheel True
                    scrollbars "vertical"
                    xsize 520
                    ysize 680
                    frame:
                        xfill True
                        background None
                        padding (0, 0, 20, 0) 
                        vbox:
                            spacing 15
                            for entry in current_person.descriptions:
                                if "|" in entry:
                                    $ header, body = entry.split("|")
                                    text header size 30 color "#4A90E2"
                                    text body size 25 color "#333"
                                else:
                                    text entry size 25 color "#333"
                            null height 20

        else:
            vpgrid:
                cols 2
                spacing 20
                align (0.5, 0.4)
                for person in journal_list:
                    hbox:
                        spacing 10
                        textbutton "X":
                            action ToggleSetMembership(eliminated_suspects, person)
                            text_size 30
                        textbutton person.name:
                            action ToggleSetMembership(selected_suspects, person)
                            if person in eliminated_suspects:
                                text_strikethrough True
                                text_color "#888"
                            elif person in selected_suspects:
                                text_color "#f00"
                            else:
                                text_color "#222"

    # Navigation buttons
    if journal_page > 0:
        textbutton " < " action SetVariable("journal_page", journal_page - 1) align (0.05, 0.5) text_size 60
    if journal_page < (len(journal_list) + (2 if current_day >= 6 else 1)):
        textbutton " > " action SetVariable("journal_page", journal_page + 1) align (0.95, 0.5) text_size 60

    textbutton "RETURN" action Return() align (0.5, 0.95)

style journal_tab:
    background Solid("#ccc")
    padding (15, 10, 15, 5)
    hover_background "#4A90E2"
    selected_background "#f4ecd8"
    color "#000"
    size 16
    yminimum 50

style status_toggle_button:
    background Solid("#e0e0e0")
    hover_background "#4A90E2"
    color "#000"
    hover_color "#fff"
    padding (10, 5)
    xminimum 150

# ============================================================================
#                           CCTV & PUZZLE SCREENS
# ============================================================================
screen cctv_monitor():
    modal True
    fixed:
        frame:
            background Solid("#00000080")
            padding (1000, 1000)
            xanchor 0.5 yanchor 0.5
            xpos 960 ypos 540
            if cctv_index == 0 or cctv_index == 3:
                imagebutton:
                    idle cctv_list[cctv_index]
                    hover cctv_list[cctv_index]
                    at Transform(zoom=0.55, xalign=0.5, yalign=0.5)
                    action Return(cctv_index)
            else:
                add cctv_list[cctv_index] at Transform(zoom=0.55, xalign=0.5, yalign=0.5)
    if cctv_index > 0:
        imagebutton:
            idle "images/ui/arrow_left_idle.png"
            hover "images/ui/arrow_left_hover.png"
            at Transform(zoom=0.4, nearest=True)
            xpos 50 ypos 540
            action SetVariable("cctv_index", cctv_index - 1)
    if cctv_index < len(cctv_list) - 1:
        imagebutton:
            idle "images/ui/arrow_right_idle.png"
            hover "images/ui/arrow_right_hover.png"
            at Transform(zoom=0.4, nearest=True)
            xpos 1670 ypos 540
            action SetVariable("cctv_index", cctv_index + 1)
    textbutton "CLOSE SYSTEM":
        align (0.5, 0.95) 
        text_size 30
        action Return("exit")
    
screen cctv_puzzle_screen(puzzle_obj, cam_number):
    modal True
    add Solid("#000a")
    frame:
        align (0.5, 0.5)
        padding (20, 20)
        background Solid("#111")
        grid 3 3:
            spacing 5
            for i in range(9):
                $ tile_num = puzzle_obj.tiles[i]
                if tile_num == 0:
                    null width 320 height 180
                else:
                    $ tile_path = "images/puzzle/cam" + str(cam_number) + "/tile_" + str(tile_num) + ".png"
                    imagebutton:
                        idle Transform(tile_path, zoom=0.5)
                        hover Transform(tile_path, zoom=0.5, alpha=0.8)
                        xysize (320, 180)
                        action [
                            Function(puzzle_obj.switch, i),
                            If(puzzle_obj.is_solved(), Return("win"))
                        ]
    textbutton "CLOSE PUZZLE":
        align (0.5, 0.95)
        action Return("fail")

# --- COMPUTER UI ---
label computer_access:
    $ show_hud = False
    call screen computer_ui
    jump evidence_room_hub

screen computer_ui():
    add "images/ui/windows_bg.png"

    hbox:
        align (0.95, 0.05)
        spacing 30
        
        # File Manager (CCTV Tapes)
        imagebutton:
            idle "images/ui/icon_folder.png"
            hover Transform("images/ui/icon_folder.png", zoom=1.1)
            action Show("file_manager_ui")
            tooltip "File Manager"
            
        # App 2: Documents
        if current_day >= 4:
            imagebutton:
                idle "images/ui/icon_app2.png"
                hover Transform("images/ui/icon_app2.png", zoom=1.1)
                action Jump("day4_evidence_review")
                tooltip "Autopsy & Forensic Reports"
        else:
            imagebutton:
                idle "images/ui/icon_app2.png"
                hover Transform("images/ui/icon_app2.png", zoom=1.1)
                action NullAction()

        # App 3: Gmail (Unlocks Day 4)
        if current_day >= 3:
            imagebutton:
                idle "images/ui/icon_app3.png"
                hover Transform("images/ui/icon_app3.png", zoom=1.1)
                action Jump("day3_gmail_review")
                tooltip "Email (Lab Techs)"
        else:
            imagebutton:
                idle "images/ui/icon_app3.png"
                hover Transform("images/ui/icon_app3.png", zoom=1.1)
                action Notify("No new emails.")
                tooltip "Email (Locked)"

    textbutton "SHUT DOWN":
        action Jump("evidence_room_hub") 
        align (0.05, 0.95) 
        style "journal_tab"

screen file_manager_ui():
    modal True
    frame:
        xysize (1200, 800)
        align (0.5, 0.5)
        background Solid("#1E1E1EE6")
        
        text "FORENSICS - RECOVERED FILES" size 40 color "#FFF" align (0.5, 0.05)
        
        if scenario_picker2:
            grid 2 2:
                align (0.5, 0.5)
                spacing 50
                
                vbox:
                    imagebutton idle "images/ui/tape_icon.png" action [Hide("file_manager_ui"), SetVariable("tape_num", 1), Jump("cctv_tape_view")] at Transform(zoom=0.30)
                    text "Tape 01.mp4" color "#FFF" xalign 0.5
                vbox:
                    imagebutton idle "images/ui/tape_icon.png" action [Hide("file_manager_ui"), SetVariable("tape_num", 2), Jump("cctv_tape_view")] at Transform(zoom=0.30)
                    text "Tape 02.mp4" color "#FFF" xalign 0.5   
                vbox:
                    imagebutton idle "images/ui/tape_icon.png" action [Hide("file_manager_ui"), SetVariable("tape_num", 3), Jump("cctv_tape_view")] at Transform(zoom=0.30)
                    text "Tape 03.mp4" color "#FFF" xalign 0.5
                vbox:
                    imagebutton idle "images/ui/tape_icon.png" action [Hide("file_manager_ui"), SetVariable("tape_num", 4), Jump("cctv_tape_view")] at Transform(zoom=0.30)
                    text "Tape 04.mp4" color "#FFF" xalign 0.5
                    
        elif scenario_picker1:
            hbox:
                align (0.5, 0.5)
                spacing 100
                
                vbox:
                    imagebutton idle "images/ui/tape_icon.png" action [Hide("file_manager_ui"), SetVariable("tape_num", 1), Jump("cctv_tape_view")] at Transform(zoom=0.30)
                    text "Tape 01.mp4" color "#FFF" xalign 0.5
                vbox:
                    imagebutton idle "images/ui/tape_icon.png" action [Hide("file_manager_ui"), SetVariable("tape_num", 2), Jump("cctv_tape_view")] at Transform(zoom=0.30)
                    text "Tape 02.mp4" color "#FFF" xalign 0.5
                    
        else:
            text "NO FILES RECOVERED." align (0.5, 0.5) color "#888" size 30
            
        textbutton "CLOSE" action Hide("file_manager_ui") align (0.5, 0.95) style "journal_tab"


# --- HACKING MINIGAME ---
label start_hacking:
    scene black with dissolve
    s "System: You connected the phone to your device to bypass the security lock."
    play music "audio/hacking_ambiance.mp3" loop
    
    # Init Level 1 Data
    $ hack_level = 1
    $ hacking_timer = 240
    jump setup_hack_level

label setup_hack_level:
    $ hack_found = 0
    python:
        hack_snippets = []
        for i in range(4):
            hack_snippets.append({"id": i, "img": f"images/hack/correct_{hack_level}_{i}.png", "correct": True, "clicked": False})
        for i in range(4):
            hack_snippets.append({"id": i+4, "img": f"images/hack/wrong_{hack_level}_{i}.png", "correct": False, "clicked": False})
        
        import random
        random.shuffle(hack_snippets)
        target_fp = f"images/hack/target_fp_{hack_level}.png"

    call screen hacking_minigame
    
    if _return == "win":
        if hack_level == 1:
            $ hack_level = 2
            jump setup_hack_level
        else:
            stop music
            play sound "audio/hack_success.mp3"
            scene black with dissolve
            s "System: Security Bypassed. Phone Unlocked."
            $ phone_unlocked = True
            jump phone_unlocked_hub
    else:
        stop music
        play sound "audio/hack_fail.mp3"
        s "System: Connection Timeout. Hack Failed."
        jump evidence_room_hub

screen hacking_minigame():
    modal True
    add "images/ui/hack_bg.png"
    
    # Timer Logic
    timer 1.0 action If(hacking_timer > 0, SetVariable("hacking_timer", hacking_timer - 1), Return("fail")) repeat True
    
    # UI Elements
    text "CONNECTION TIMEOUT" size 20 color "#FFF" pos (100, 100)
    text "[hacking_timer] SEC" size 50 color "#F00" pos (100, 130)
    
    text "CLONE TARGET" size 20 color "#FFF" pos (800, 100)
    add target_fp pos (800, 150)
    
    text "COMPONENTS DETECTED: [hack_found] / 4" size 20 color "#FFF" pos (100, 250)
    
    # 2x4 Grid of snippets
    grid 2 4:
        pos (100, 300)
        spacing 20
        for snippet in hack_snippets:
            if not snippet["clicked"]:
                imagebutton:
                    idle Transform(snippet["img"], size=(150, 150))
                    hover Transform(snippet["img"], size=(150, 150), matrixcolor=BrightnessMatrix(0.2))
                    action [
                        SetDict(snippet, "clicked", True),
                        If(snippet["correct"], 
                           true=[Play("sound", "audio/correct_submit.mp3"), SetVariable("hack_found", hack_found + 1), SetVariable("hacking_timer", hacking_timer + 20), If(hack_found == 3, Return("win"))],
                           false=[Play("sound", "audio/wrong_submit.mp3"), SetVariable("hacking_timer", hacking_timer - 15)])
                    ]
            else:
                if snippet["correct"]:
                    add Transform(snippet["img"], size=(150, 150), matrixcolor=TintMatrix("#0F0"))
                else:
                    add Transform(snippet["img"], size=(150, 150), matrixcolor=TintMatrix("#F00"))
                    
    textbutton "ABORT HACK" action Return("fail") align (0.05, 0.95) style "journal_tab"

screen phone_ui():
    modal True
    # add "images/ui/phone_bg.png" align (0.5, 0.5)

    frame:
        xysize (400, 700)
        align (0.5, 0.5)
        background Solid("#111111E6")
        
        text "PAT'S PHONE" align (0.5, 0.05) size 30 color "#FFF"
        
        vbox:
            align (0.5, 0.4)
            spacing 40
            
            textbutton "Messages (Pat & Toph)":
                action Jump("phone_app_messages")
                style "journal_tab"
                xsize 300
                
            textbutton "Call Logs (Chandler)":
                action Jump("phone_app_calls")
                style "journal_tab"
                xsize 300
                
            textbutton "Banking Screenshots":
                action Jump("phone_app_bank")
                style "journal_tab"
                xsize 300

        textbutton "PUT AWAY":
            action Jump("evidence_room_hub")
            align (0.5, 0.95)
            style "journal_tab"

screen interrogation_room():
    modal True
    add "images/ui/interrogation_bg.png" 
    text "INTERROGATION ROOM" size 40 color "#FFF" align (0.5, 0.05)

    hbox:
        align (0.5, 0.5)
        spacing 50

        # DAN
        vbox:
            spacing 10
            imagebutton:
                idle "images/suspects/dan_port.png"
                hover Transform("images/suspects/dan_port.png", matrixcolor=BrightnessMatrix(0.2))
                insensitive Transform("images/suspects/dan_port.png", matrixcolor=SaturationMatrix(0.0))
                action If(not interrogated_dan, Jump("interrogate_dan"), NullAction())
            text "DAN" color "#FFF" xalign 0.5

        # TOPH
        vbox:
            spacing 10
            imagebutton:
                idle "images/characters/toph.png"
                hover Transform("images/characters/toph.png", matrixcolor=BrightnessMatrix(0.2))
                insensitive Transform("images/characters/toph.png", matrixcolor=SaturationMatrix(0.0))
                action If(not interrogated_toph, Jump("interrogate_toph"), NullAction())
            text "TOPH" color "#FFF" xalign 0.5

        # AUSTIN
        vbox:
            spacing 10
            imagebutton:
                idle "images/suspects/austin.png"
                hover Transform("images/suspects/austin.png", matrixcolor=BrightnessMatrix(0.2))
                insensitive Transform("images/suspects/austin.png", matrixcolor=SaturationMatrix(0.0))
                action If(not interrogated_austin, Jump("interrogate_austin"), NullAction())
            text "AUSTIN" color "#FFF" xalign 0.5

        # CHANDLER
        vbox:
            spacing 10
            imagebutton:
                idle "images/suspects/chandler.png"
                hover Transform("images/suspects/chandler.png", matrixcolor=BrightnessMatrix(0.2))
                insensitive Transform("images/suspects/chandler.png", matrixcolor=SaturationMatrix(0.0))
                action If(not interrogated_chandler, Jump("interrogate_chandler"), NullAction())
            text "CHANDLER" color "#FFF" xalign 0.5

    # Leave button appears only when everyone is interrogated
    if interrogated_dan and interrogated_toph and interrogated_austin and interrogated_chandler:
        textbutton "FINISH INTERROGATIONS":
            align (0.5, 0.9)
            action Jump("post_interrogation_hub")
            style "journal_tab"
    else:
        text "Question all suspects to proceed." align (0.5, 0.9) color "#888" size 20

screen final_accusation():
    modal True
    add "images/ui/interrogation_bg.png" 

    text "FINAL ACCUSATION" size 50 color "#FFF" align (0.5, 0.05)
    text "Determine who to arrest and for what crime." size 25 color "#CCC" align (0.5, 0.12)

    hbox:
        align (0.5, 0.5)
        spacing 50

        # --- DAN ---
        vbox:
            spacing 10
            add "images/suspects/dan_port.png" xalign 0.5
            text "DAN" color "#FFF" xalign 0.5

            textbutton end_dan_status:
                action If(end_dan_status == "Person of Interest", SetVariable("end_dan_status", "Suspect"), SetVariable("end_dan_status", "Person of Interest"))
                style "status_toggle_button"
                xalign 0.5

            if end_dan_status == "Suspect":
                textbutton end_dan_crime:
                    # Cycles through the crime list
                    action SetVariable("end_dan_crime", possible_crimes[(possible_crimes.index(end_dan_crime) + 1) % len(possible_crimes)])
                    style "journal_tab"
                    xalign 0.5
                    xsize 250

        # --- TOPH ---
        vbox:
            spacing 10
            add "images/characters/toph.png" xalign 0.5
            text "TOPH" color "#FFF" xalign 0.5

            textbutton end_toph_status:
                action If(end_toph_status == "Person of Interest", SetVariable("end_toph_status", "Suspect"), SetVariable("end_toph_status", "Person of Interest"))
                style "status_toggle_button"
                xalign 0.5

            if end_toph_status == "Suspect":
                textbutton end_toph_crime:
                    action SetVariable("end_toph_crime", possible_crimes[(possible_crimes.index(end_toph_crime) + 1) % len(possible_crimes)])
                    style "journal_tab"
                    xalign 0.5
                    xsize 250

        # --- AUSTIN ---
        vbox:
            spacing 10
            add "images/suspects/austin.png" xalign 0.5
            text "AUSTIN" color "#FFF" xalign 0.5

            textbutton end_austin_status:
                action If(end_austin_status == "Person of Interest", SetVariable("end_austin_status", "Suspect"), SetVariable("end_austin_status", "Person of Interest"))
                style "status_toggle_button"
                xalign 0.5

            if end_austin_status == "Suspect":
                textbutton end_austin_crime:
                    action SetVariable("end_austin_crime", possible_crimes[(possible_crimes.index(end_austin_crime) + 1) % len(possible_crimes)])
                    style "journal_tab"
                    xalign 0.5
                    xsize 250

        # --- CHANDLER ---
        vbox:
            spacing 10
            add "images/suspects/chandler.png" xalign 0.5
            text "CHANDLER" color "#FFF" xalign 0.5

            textbutton end_chandler_status:
                action If(end_chandler_status == "Person of Interest", SetVariable("end_chandler_status", "Suspect"), SetVariable("end_chandler_status", "Person of Interest"))
                style "status_toggle_button"
                xalign 0.5

            if end_chandler_status == "Suspect":
                textbutton end_chandler_crime:
                    action SetVariable("end_chandler_crime", possible_crimes[(possible_crimes.index(end_chandler_crime) + 1) % len(possible_crimes)])
                    style "journal_tab"
                    xalign 0.5
                    xsize 250

    textbutton "SUBMIT ACCUSATIONS":
        align (0.5, 0.95)
        action [Return(), Jump("evaluate_final_accusation")]
        style "journal_tab"