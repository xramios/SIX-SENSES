screen detective_hud():
    zorder 10
    if show_hud:
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

# ============================================================================
#                             INVENTORY SCREEN
# ============================================================================

screen inventory_screen():
    tag menu
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
                else:
                    text "Select item..." align (0.5, 0.5) color "#888"
    textbutton "RETURN" action Return() align (0.5, 0.95)


# ============================================================================
#                              JOURNAL SCREEN
# ============================================================================

screen journal_screen():
    tag menu
    add Solid("#0b121a")

    frame:
        xsize 1200 ysize 800
        align (0.5, 0.5)
        background Frame(Solid("#f4ecd8"), 4, 4)
        padding (20, 20)

        # Top tabs
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

        # Content area (no outer scroll)
        if journal_page == 0:
            vbox:
                align (0.5, 0.5)
                text "SIX SENSES" size 80 color "#222"
                text "CASE FILE #109" size 20 color "#555" xalign 0.5
        elif journal_page == 1:
            hbox:
                spacing 20
                xfill True
                xmaximum 1200  # Prevents overflow beyond content frame
                # Left column: case report
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
                # Left column: image and info (fixed, no scroll)
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
                # Right column: descriptions (scrollable only here)
                viewport:
                    yinitial 0.0
                    mousewheel True
                    scrollbars "vertical"
                    xsize 520
                    ysize 680
                    frame:
                        xfill True
                        background None
                        padding (0, 0, 20, 0)  # 20px right padding to avoid scrollbar overlap
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

## ----------------------------------------------------------------------------
## EVIDENCE TABLE SCREEN (Day 3)
## ----------------------------------------------------------------------------
screen evidence_table():
    tag menu
    default selected_evidence = None
    default show_inspect_options = False

    # Background – the evidence room
    add "evidence_room_bg"

    # The table area where items are placed
    fixed:
        # Computer hotspot (click to open computer screen)
        imagebutton:
            idle "images/ui/computer_idle.png"
            hover "images/ui/computer_hover.png"
            xpos 1200 ypos 300
            action ShowMenu("computer_screen")
            tooltip "Use the computer"

        # Exit button (return to story)
        textbutton "Leave Room" action Return() xalign 0.95 yalign 0.05

        # --- Evidence items as imagebuttons (scattered positions) ---
        # Each button checks if the item is already collected and if not selected.
        if "butterfly_knife" in inventory_items:
            if selected_evidence != "butterfly_knife":
                imagebutton:
                    idle "images/evidence/knife_icon.png"
                    hover Transform("images/evidence/knife_icon.png", zoom=1.1)
                    xpos 200 ypos 400
                    action SetScreenVariable("selected_evidence", "butterfly_knife")
                    tooltip "Butterfly Knife"

        if "cigarette" in inventory_items:
            if selected_evidence != "cigarette":
                imagebutton:
                    idle "images/evidence/cigarette_icon.png"
                    hover Transform("images/evidence/cigarette_icon.png", zoom=1.1)
                    xpos 500 ypos 300
                    action SetScreenVariable("selected_evidence", "cigarette")
                    tooltip "Cigarette Butt"

        if "drugs" in inventory_items:   # powder item
            if selected_evidence != "drugs":
                imagebutton:
                    idle "images/evidence/drugs_icon.png"
                    hover Transform("images/evidence/drugs_icon.png", zoom=1.1)
                    xpos 800 ypos 200
                    action SetScreenVariable("selected_evidence", "drugs")
                    tooltip "Synthetic Drugs"

        if "phone" in inventory_items:   # patphone
            if selected_evidence != "phone":
                imagebutton:
                    idle "images/evidence/phone_icon.png"
                    hover Transform("images/evidence/phone_icon.png", zoom=1.1)
                    xpos 1100 ypos 500
                    action SetScreenVariable("selected_evidence", "phone")
                    tooltip "Victim's Phone"

        if "waterbottle" in inventory_items:
            if selected_evidence != "waterbottle":
                imagebutton:
                    idle "images/evidence/bottle_icon.png"
                    hover Transform("images/evidence/bottle_icon.png", zoom=1.1)
                    xpos 300 ypos 600
                    action SetScreenVariable("selected_evidence", "waterbottle")
                    tooltip "Plastic Bottle"

        if "id" in inventory_items:
            if selected_evidence != "id":
                imagebutton:
                    idle "images/evidence/id_icon.png"
                    hover Transform("images/evidence/id_icon.png", zoom=1.1)
                    xpos 600 ypos 700
                    action SetScreenVariable("selected_evidence", "id")
                    tooltip "Victim's ID Lace"

        if "bag" in inventory_items:   # patbag
            if selected_evidence != "bag":
                imagebutton:
                    idle "images/evidence/bag_icon.png"
                    hover Transform("images/evidence/bag_icon.png", zoom=1.1)
                    xpos 900 ypos 600
                    action SetScreenVariable("selected_evidence", "bag")
                    tooltip "Shoulder Bag"

        # If CCTV hard drive is available (only if player didn't access CCTV day1)
        if not (scenario_picker1 or scenario_picker2):
            if "cctv_drive" in inventory_items:
                if selected_evidence != "cctv_drive":
                    imagebutton:
                        idle "images/evidence/harddrive_icon.png"
                        hover Transform("images/evidence/harddrive_icon.png", zoom=1.1)
                        xpos 1200 ypos 200
                        action SetScreenVariable("selected_evidence", "cctv_drive")
                        tooltip "Recovered Hard Drive"

        # --- Center examination area ---
        if selected_evidence:
            frame:
                xalign 0.5 yalign 0.5
                xsize 500 ysize 500
                background Solid("#222")
                padding (20,20)
                vbox:
                    spacing 10
                    # Item image
                    add evidence_image(selected_evidence):
                        xalign 0.5
                        size (300,300) fit "contain"
                    # Item name
                    text evidence_name(selected_evidence) size 30 color "#FFF" xalign 0.5
                    # Buttons
                    hbox:
                        xalign 0.5 spacing 20
                        textbutton "Inspect" action SetScreenVariable("show_inspect_options", True)
                        textbutton "Remove" action SetScreenVariable("selected_evidence", None)
                    if show_inspect_options:
                        vbox:
                            spacing 10
                            text evidence_description(selected_evidence) size 22 color "#CCC"
                            # Additional actions based on item type
                            if selected_evidence == "phone":
                                if not phone_unlocked:
                                    textbutton "Connect to PC" action [Hide("evidence_table"), ShowMenu("phone_hack_minigame")]
                            else:
                                if not evidence_sent_to_lab(selected_evidence):
                                    textbutton "Send to Lab for DNA" action Function(send_to_lab, selected_evidence)
                            textbutton "Back" action SetScreenVariable("show_inspect_options", False)

    # Tooltip display (if you have a tooltip system)
    $ tooltip = GetTooltip()
    if tooltip:
        text tooltip:
            xpos 0.5 ypos 0.95 xanchor 0.5
            size 24 color "#FFF"

# Helper functions for evidence display (defined in a python block)
init python:
    def evidence_image(item_id):
        mapping = {
            "butterfly_knife": "images/evidence/knife_large.png",
            "cigarette": "images/evidence/cigarette_large.png",
            "drugs": "images/evidence/drugs_large.png",
            "phone": "images/evidence/phone_large.png",
            "waterbottle": "images/evidence/bottle_large.png",
            "id": "images/evidence/id_large.png",
            "bag": "images/evidence/bag_large.png",
            "cctv_drive": "images/evidence/harddrive_large.png"
        }
        return mapping.get(item_id, "")

    def evidence_name(item_id):
        names = {
            "butterfly_knife": "Butterfly Knife",
            "cigarette": "Cigarette Butt",
            "drugs": "Synthetic Drugs",
            "phone": "Victim's Phone",
            "waterbottle": "Plastic Bottle",
            "id": "ID Lace",
            "bag": "Shoulder Bag",
            "cctv_drive": "CCTV Hard Drive"
        }
        return names.get(item_id, item_id)

    def evidence_description(item_id):
        desc = {
            "butterfly_knife": "A butterfly knife found inside Toph’s locker, its surface wiped clean of fingerprints but still bearing faint traces of dried blood along the blade. The contrast feels unsettling—careful enough to remove identity, but not thorough enough to erase everything—leaving it unclear whether it was hidden in haste or deliberately planted to confuse the investigation.",
            "cigarette": "A crushed cigarette butt recovered from the floor, its filter still fresh and marked with clear fingerprints. The size and shape match the burns found on Pat’s skin, suggesting a possible link—but whether it directly ties to the suspect or was left behind unintentionally remains uncertain.",
            "drugs": "A small bag of high-grade synthetic party drugs found on the floor, carelessly left behind. Their presence raises serious suspicion, but it’s unclear whether they belonged to the victim, the perpetrator, or someone else.",
            "phone": "A smartphone recovered from the crime scene, its screen cracked from what looks like a hard drop or impact. Despite the damage, it still powers on—but it’s locked, with notifications lighting up the display just out of reach. It’s unclear whether it was dropped in panic, thrown during a struggle, or deliberately left behind.",
            "waterbottle": "An empty bottle found among the scattered belongings, likely discarded during a hurried search. It could have been used to administer the substances found near the body—but whether it played a direct role or is simply part of the mess left behind remains uncertain.",
            "id": "Pat’s ID lace lies crumpled in a corner, its fabric roughed up and stained with fresh blood. It looks less like something misplaced and more like it was forcibly torn off and discarded—but whether it happened during a struggle or after the fact is still unclear.",
            "bag": "A discarded shoulder bag now in the evidence room, its zipper left wide open and lining still partially turned inside out. The interior is completely empty, confirming it was thoroughly searched—but whether anything was actually taken, or what the intruder was looking for, remains unclear.",
            "cctv_drive": "THIS CCTV SEEMS TO BE TAMPERED SINCE THE CCTV WAS CORRUPTED WHEN THE OTHER OFFICER GAINED ACCESS TO THE CCTV ROOM. BETTER CHECK IT AGAIN JUST TO MAKE SURE."
        }
        return desc.get(item_id, "No description available.")

    # Track which items have been sent to lab
    lab_sent_items = []
    def evidence_sent_to_lab(item_id):
        return item_id in lab_sent_items

    def send_to_lab(item_id):
        if item_id not in lab_sent_items:
            lab_sent_items.append(item_id)
            renpy.show_screen("item_get_message", message="Evidence sent to lab for DNA analysis.")
            # Optionally, you can set a flag for later story impact.

    # Phone unlock state
    phone_unlocked = False

    # List of collected evidence IDs (for display)
    inventory_items = []
    def update_inventory_items():
        global inventory_items
        inv = []
        if evidence_taken.get("knife", False): inv.append("butterfly_knife")
        if evidence_taken.get("cigarette", False): inv.append("cigarette")
        if evidence_taken.get("powder", False): inv.append("drugs")
        if evidence_taken.get("patphone", False): inv.append("phone")
        if evidence_taken.get("waterbottle", False): inv.append("waterbottle")
        if evidence_taken.get("id", False): inv.append("id")
        if evidence_taken.get("patbag", False): inv.append("bag")
        # CCTV drive is added if player didn't get CCTV on day1
        if not (scenario_picker1 or scenario_picker2):
            inv.append("cctv_drive")
        inventory_items = inv

## ----------------------------------------------------------------------------
## COMPUTER SCREEN (Evidence Room)
## ----------------------------------------------------------------------------
screen computer_screen():
    tag menu
    default tab = "suspects"   # suspects, cctv, autopsy, phone
    add Solid("#0a0f1a")  # dark background

    frame:
        xsize 1400 ysize 900
        align (0.5, 0.5)
        background Frame(Solid("#1e2a3a"), 10,10)
        padding (20,20)

        # Tabs
        hbox:
            spacing 5
            textbutton "Suspect Profiles" action SetScreenVariable("tab", "suspects")
            if scenario_picker1 or scenario_picker2:
                # Player examined body day1 -> get more detailed CCTV report now
                textbutton "CCTV Analysis" action SetScreenVariable("tab", "cctv")
            else:
                # Player examined CCTV day1 -> get more detailed autopsy report now
                textbutton "Autopsy Report" action SetScreenVariable("tab", "autopsy")
            if phone_unlocked:
                textbutton "Phone Data" action SetScreenVariable("tab", "phone")

        # Content area
        if tab == "suspects":
            use suspect_profiles()
        elif tab == "cctv":
            use cctv_report()
        elif tab == "autopsy":
            use autopsy_report()
        elif tab == "phone":
            use phone_data()

        textbutton "Close" action Return() align (1.0, 0.0)

screen suspect_profiles():
    vpgrid:
        cols 1
        spacing 10
        xfill True
        ysize 800
        scrollbars "vertical"
        for person in journal_list:
            frame:
                background Solid("#2a3a4a")
                padding (10,10)
                hbox:
                    spacing 20
                    add Transform(person.image, size=(150,150), fit="contain")
                    vbox:
                        text person.name size 28 color "#FFF"
                        text "Status: " + person.status size 22 color "#CCC"
                        for clue in person.descriptions:
                            text "• " + clue size 20 color "#AAA"

screen cctv_report():
    viewport:
        scrollbars "vertical"
        mousewheel True
        vbox:
            spacing 15
            text "CCTV FOOTAGE ANALYSIS" size 40 color "#4A90E2"
            text "Recovered from hard drive:" size 30
            if cctv_cam1_solved:
                text "Camera 1: Shows Dan forcing Pat into storage room at approx. 7:45 PM." size 25
            if cctv_cam4_solved:
                text "Camera 4: Shows Toph Bernales exiting elevator and moving toward storage area at 10:12 PM, looking nervous." size 25
            if not (cctv_cam1_solved or cctv_cam4_solved):
                text "No usable footage recovered. The hard drive appears corrupted." size 25
            text "Timeline reconstruction suggests the victim was alive when Dan entered but deceased by the time Toph arrived." size 25

screen autopsy_report():
    viewport:
        scrollbars "vertical"
        mousewheel True
        vbox:
            spacing 15
            text "AUTOPSY REPORT – PAT ESTACIO" size 40 color "#4A90E2"
            text "Cause of Death: Exsanguination due to multiple stab wounds." size 25
            text "Toxicology: High levels of synthetic opioids (matching powder found at scene)." size 25
            text "Defensive wounds: Bruising on forearms and neck, indicating a struggle." size 25
            text "Foam at mouth: Consistent with drug ingestion shortly before death." size 25
            text "Stab wounds: Three distinct wounds – chest (pneumothorax), abdomen (possible bowel perforation), and upper chest." size 25
            text "Conclusion: Victim was drugged, then stabbed multiple times. Overkill suggests personal motive." size 25

screen phone_data():
    viewport:
        scrollbars "vertical"
        mousewheel True
        vbox:
            spacing 15
            text "PHONE DATA – UNLOCKED" size 40 color "#4A90E2"
            text "Last outgoing call: 2:47 AM to 'Toph'" size 25
            text "Text messages recovered:" size 25
            text "\"Toph: Where are you? I need to talk.\"" size 22
            text "\"Pat: Storage room. Come alone.\"" size 22
            text "Photos: Several deleted images recovered, showing Pat and Toph together." size 25

## ----------------------------------------------------------------------------
## PHONE HACK MINIGAME (Pipe Rotation)
## ----------------------------------------------------------------------------
screen phone_hack_minigame():
    modal True
    zorder 200
    default grid_size = 4
    default pipes = []   # will hold (type, rotation) for each cell
    default solved = False

    on "show" action Function(initialize_pipes, grid_size)

    add Solid("#000a")

    frame:
        align (0.5, 0.5)
        padding (30,30)
        background Solid("#1a1a2e")
        vbox:
            spacing 20
            text "Unlock the phone by connecting the circuit." size 35 color "#FFF" xalign 0.5
            grid grid_size grid_size:
                spacing 5
                for idx in range(grid_size * grid_size):
                    $ pipe = pipes[idx]
                    button:
                        xysize (100,100)
                        background None
                        action Function(rotate_pipe, idx)
                        add pipe_image(pipe[0], pipe[1]):
                            size (100,100)
            hbox:
                xalign 0.5 spacing 20
                textbutton "Check Connection" action If(check_connection(pipes, grid_size), Return("success"), Notify("Not connected yet."))
                textbutton "Give Up" action Return("fail")

    if solved:
        timer 0.1 action Return("success")

init python:
    import random
    pipe_types = ["straight", "corner", "tee", "cross"]
    # Rotation 0-3 (0=0°, 1=90°, 2=180°, 3=270°)

    def initialize_pipes(size):
        store.pipes = []
        for i in range(size * size):
            # For simplicity, we can start with a solvable pattern or random.
            # Let's start with a known solvable pattern (straight line)
            if i % size == 0 or i % size == size-1:
                store.pipes.append(("straight", 0))  # horizontal
            else:
                store.pipes.append(("straight", 0))
        # For actual gameplay, you'd want a random solvable configuration.
        # You can use a maze generation algorithm to create a path.

    def rotate_pipe(idx):
        pipe = store.pipes[idx]
        new_rot = (pipe[1] + 1) % 4
        store.pipes[idx] = (pipe[0], new_rot)
        renpy.restart_interaction()

    def pipe_image(ptype, rot):
        # You'll need images named like "pipe_straight_0.png", "pipe_corner_0.png", etc.
        return "images/minigame/pipe_{}_{}.png".format(ptype, rot)

    def check_connection(pipes, size):
        # Implement a simple flood fill from start (0,0) to end (size-1, size-1)
        # This is a placeholder; you'll need actual logic.
        # For now, just return True to test.
        return True