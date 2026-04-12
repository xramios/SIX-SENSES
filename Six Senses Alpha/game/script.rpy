# ============================================================================
#                                FONT & STYLE
# ============================================================================

define gui.text_font = "Ithaca-LVB75.ttf"


# ============================================================================
#                           CHARACTER DEFINITIONS
# ============================================================================

define mc = Character("Detective")
define pc = Character("Captain", color="#4A90E2")
define d = Character("Dan", color="#C5B358")
define c = Character("Chandler", color="#F08080")
define t = Character("Toph", color="#50C878")
define a = Character("Austin", color="#9370DB")
define op = Character("911 Operator", color="#C20101")
define s = Character("System", color="#FFFFFF")


# ============================================================================
#                          TRANSITIONS & TRANSFORMS
# ============================================================================

define flash = Fade(.25, 0.0, .75, color="#fff")

image lightning_flash = Solid("#ffffff")
image translucent_hover = Solid("#ffffff40")
image invisible_idle = Solid("#00000000")

transform lift_on_hover:
    yoffset 0
    on hover:
        linear 0.2 yoffset -20
    on idle:
        linear 0.2 yoffset 0

transform police_full_flicker:
    alpha 0.0
    xalign 0.5 yalign 0.5
    block:
        parallel:
            linear 0.15 alpha 0.6
        parallel:
            xzoom 1.0
        pause 0.05
        alpha 0.8 xzoom -1.0
        pause 0.05
        alpha 0.4 xzoom 1.0
        pause 0.05
        alpha 0.9 xzoom -1.0
        pause 0.05
        linear 0.2 alpha 0.0
        pause 0.8
        repeat

transform popup_center:
    xalign 0.5 yalign 0.5
    zoom 0.0
    linear 0.3 zoom 1.0

transform move_to_hud_right:
    parallel:
        linear 0.6 xalign 0.98 yalign 0.02
    parallel:
        linear 0.6 zoom 0.2

transform move_to_hud_left:
    parallel:
        linear 0.6 xalign 0.92 yalign 0.02 
    parallel:
        linear 0.6 zoom 0.2

transform hud_zoom(norm, hov):
    on idle:
        linear 0.1 zoom norm
    on hover:
        linear 0.1 zoom hov

transform DialogueFaces:
    xalign 1.0
    yalign 1.0 
    yoffset -200

# ============================================================================
#                               GLOBAL VARIABLES
# ============================================================================

default show_hud = False
default seen_scene_intro = False
default seen_body = False
default seen_mhallwayd2_intro = False
default scenario_picker1 = False
default scenario_picker2 = False
default scenario_picker1d2 = False
default scenario_picker2d2 = False
default current_location = "hallway"
default evidence_taken = {
    "waterbottle": False,
    "patbag": False,
    "knife": False,
    "cigarette": False,
    "powder": False,
    "id": False,
    "patphone": False,
}
default day1_objective_complete = False
default current_day = 1

image cctv_1 = "images/cctv/cam_hallway.png"
image cctv_2 = "images/cctv/cam_entrance.png"
image cctv_3 = "images/cctv/cam_cctv_hallway.png"
image cctv_4 = "images/cctv/cam_library.png"
image cctv_5 = "images/cctv/cam_locker.png"

default cctv_index = 0
default cctv_list = ["cctv_1", "cctv_2", "cctv_3", "cctv_4", "cctv_5"]

default met_dan = False
default journal_page = 0
default selected_suspects = []
default eliminated_suspects = []


# ============================================================================
#                               DATA & LOGIC
# ============================================================================

init python:
    class Item: 
        def __init__(self, name, description, image):
            self.name = name
            self.description = description
            self.image = image

    class Suspect:
        def __init__(self, name, bio, image):
            self.name = name
            self.bio = bio
            self.image = image
            self.descriptions = []
            self.status = "Person of Interest"

    inventory_list = []
    journal_list = []
    selected_item = None
    selected_suspect = None

    def add_item(name, desc, img):
        if not any(x.name == name for x in inventory_list):
            inventory_list.append(Item(name, desc, img))

    def add_suspect(name, bio, img):
        if not any(x.name == name for x in journal_list):
            journal_list.append(Suspect(name, bio, img))

    def record_clue(name, clue_text):
        for person in journal_list:
            if person.name == name:
                if clue_text not in person.descriptions:
                    person.descriptions.append(clue_text)
                    renpy.show_screen("item_get_message", message="Journal Updated: " + name)
                return          

    def has_pat_clue(keyword):
            for person in journal_list:
                if "Pat" in person.name:
                    for clue in person.descriptions:
                        if keyword.lower() in clue.lower():
                            return True
            return False

    class SlidingPuzzle:
        def __init__(self, tiles_val):
            self.tiles = tiles_val
            self.blank_index = self.tiles.index(0)

        def switch(self, tile_index):
            if tile_index in [self.blank_index-1, self.blank_index+1, self.blank_index-3, self.blank_index+3]:
                if not (self.blank_index % 3 == 0 and tile_index == self.blank_index - 1) and \
                   not (self.blank_index % 3 == 2 and tile_index == self.blank_index + 1):
                    self.tiles[self.blank_index], self.tiles[tile_index] = self.tiles[tile_index], self.tiles[self.blank_index]
                    self.blank_index = tile_index
                    renpy.restart_interaction()

        def is_solved(self):
            return self.tiles == [1, 2, 3, 4, 5, 6, 7, 8, 0]

    def start_puzzle():
        import random
        initial_tiles = [1, 3, 0, 4, 5, 6, 7, 8, 2]
        random.shuffle(initial_tiles)
        return SlidingPuzzle(initial_tiles)

default my_puzzle = None


# ============================================================================
#                              POPUP MESSAGES
# ============================================================================

screen item_get_message(message):
    tag popup
    zorder 100
    frame:
        at popup_center
        xpos 960 ypos 200
        anchor (0.5, 0.5)
        padding (20, 20)
        background Solid("#000000CC")
        text message color "#FFF" size 30
    timer 4.0 action Hide("item_get_message")


# ============================================================================
#                                 HUD SCREEN
# ============================================================================

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
        
        if current_location == "cctv_roomd2":
            use cctv_roomd2

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
                    text selected_item.description size 23
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
                spacing 50
                vbox:
                    xsize 500
                    text "Initial Case Report" size 30 color "#222"
                    text "The body was found at 2:00 AM..." color "#333" size 18
                vbox:
                    xsize 500
                    text "Evidence Photo" size 22 color "#222" xalign 0.5
                    add Transform("images/crime_scene.png", fit="contain"):
                        size (450, 350)

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
                                    text header size 25 color "#4A90E2"
                                    text body size 20 color "#333"
                                else:
                                    text entry size 20 color "#333"
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
            imagebutton:
                idle cctv_list[cctv_index]
                hover cctv_list[cctv_index]
                at transform:
                    zoom 0.55
                    xalign 0.5 yalign 0.5
                action Return(cctv_list[cctv_index]) 

    if cctv_index > 0:
        imagebutton:
            idle "images/ui/arrow_left_idle.png"
            hover "images/ui/arrow_left_hover.png"
            at transform:
                nearest True
                zoom 0.4
            xpos 50 ypos 540
            action SetVariable("cctv_index", cctv_index - 1)

    if cctv_index < len(cctv_list) - 1:
        imagebutton:
            idle "images/ui/arrow_right_idle.png"
            hover "images/ui/arrow_right_hover.png"
            at transform:
                nearest True
                zoom 0.4
            xpos 1670 ypos 540
            action SetVariable("cctv_index", cctv_index + 1)

    textbutton "CLOSE SYSTEM":
        align (0.5, 0.95) 
        text_size 30
        action Return("exit")
    
screen cctv_puzzle_screen(puzzle_obj):
    modal True
    add Solid("#000a") 
    frame:
        align (0.5, 0.5)
        padding (20, 20)
        background Solid("#111") 
        grid 3 3:
            spacing 10
            for i in range(9):
                $ tile_num = puzzle_obj.tiles[i]
                if tile_num == 0:
                    null width 200 height 200 
                else:
                    $ tile_path = "images/puzzle/tile_" + str(tile_num) + ".png"
                    imagebutton:
                        idle tile_path
                        xysize (200, 200) 
                        action [
                            Function(puzzle_obj.switch, i), 
                            If(puzzle_obj.is_solved(), Return("win"))
                        ]
    textbutton "CLOSE PUZZLE":
        align (0.5, 0.95)
        action Return("fail")


# ============================================================================
#                                 INTRO
# ============================================================================

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

    pc "A call was made to 9-1-1 at 4:56 AM in the morning."
    
    scene prologue-call2 with dissolve
    
    pc "The janitor, Dan-found the body in around 4:53 AM."
    
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
    python:
        for suspect in journal_list:
            if suspect.name == "Dan (Janitor)":
                suspect.descriptions.append("Observation|He was trembling when he spoke to the Captain.")
                break

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
#                                 DAY 1
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
            $ journal_list[1].descriptions.append("Statement|Claims he didn't look closely at the face.")

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
    $ scenario_picker1 = True
    scene cctv_room with fade
    $ result = renpy.call_screen("detective_hud")

    if result == "cctv_monitor":
        call screen cctv_monitor
        $ chosen_cam = _return   

        if chosen_cam == "exit":
            jump cctv_room
        mc "Let's try to enhance the feed for [chosen_cam]..."
        $ my_puzzle = start_puzzle() 
        call screen cctv_puzzle_screen(my_puzzle)
        $ puzzle_result = _return 
        
        if puzzle_result == "win":
            mc "The image is clear now. I can see what happened."
        else:
            mc "I couldn't get a clear signal."
            jump cctv_room
    elif result == "go_cctv_hallway":
        jump cctv_hallway
    jump cctv_room

label storage_room:
    play music "audio/ambiance_crime_scene_d1.mp3" loop
    $ current_location = "storage_room"
    scene storage_room with fade
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
        if cctv_solved:
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
#                                 DAY 2
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
    
    $ result = renpy.call_screen("detective_hud")

    if result == "go_hallwayd2":
        jump hallwayd2
    jump mhallwayd2

label hallwayd2:
    play music "audio/ambiance_hallway_d1.mp3" loop
    $ current_location = "hallwayd2"
    $ show_hud = True
    scene hallway2 with fade
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
    $ result = renpy.call_screen("detective_hud")
    if result == "go_stairsd2":
        jump stairsd2
    elif result == "go_cctv_roomd2":
        jump cctv_roomd2
    jump cctv_hallwayd2

label cctv_roomd2:
    play music "audio/ambiance_hallway_d1.mp3" loop
    $ current_location = "cctv_roomd2"
    scene cctv_room with fade
    $ result = renpy.call_screen("detective_hud")
    if result == "cctv_monitor":
        call screen cctv_monitor
        $ chosen_cam = _return
        if chosen_cam == "exit":
            jump cctv_roomd2
        mc "Let's try to enhance the feed for [chosen_cam]..."
        $ my_puzzle = start_puzzle()
        call screen cctv_puzzle_screen(my_puzzle)
        $ puzzle_result = _return
        if puzzle_result == "win":
            mc "The image is clear now. I can see what happened."
            # Add clue or evidence here
        else:
            mc "I couldn't get a clear signal."
            jump cctv_roomd2
    elif result == "go_cctv_hallwayd2":
        jump cctv_hallwayd2
    jump cctv_roomd2

label storage_roomd2:
    play music "audio/ambiance_crime_scene_d1.mp3" loop
    $ current_location = "storage_roomd2"
    $ show_hud = True
    scene storage_room with fade
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
    jump policestation


# ============================================================================
#                            FUTURE DAYS (PLACEHOLDERS)
# ============================================================================

# Day 3
# Day 4
# Day 5
# Day 6