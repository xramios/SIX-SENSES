define gui.text_font = "Ithaca-LVB75.ttf"

# --- Character Definitions ---
define mc = Character("Detective")
define pc = Character("Captain", color="#4A90E2")
define d = Character("Dan", color="#C5B358")
define c = Character("Chandler", color="#F08080")
define t = Character("Toph", color="#50C878")
define a = Character("Austin", color="#9370DB")
define op = Character("911 Operator", color="#C20101")
define s = Character("System", color="#FFFFFF")

# --- Transitions ---
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

screen item_get_message(message):
    zorder 100
    frame:
        at popup_center
        xpos 960 ypos 200
        anchor (0.5, 0.5)
        padding (20, 20)
        background Solid("#000000CC")
        text message color "#FFF" size 30
    
    # This screen hides itself after 2 seconds
    timer 3.0 action Hide("item_get_message")

transform popup_center:
    xalign 0.5 yalign 0.5
    zoom 0.0
    linear 0.3 zoom 1.0

transform move_to_hud_left:
    linear 0.8 xalign 0.47 yalign 0.02 zoom 0.15

transform move_to_hud_right:
    linear 0.8 xalign 0.53 yalign 0.02 zoom 0.37

# --- Variables ---
default show_hud = False
default seen_scene_intro = False
default seen_body = False
default scenario_picker1 = False
default scenario_picker2 = False
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

# =========================
# DATA & LOGIC
# =========================
init python: #Database System
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
                    # Show the little popup message we made earlier
                    renpy.show_screen("item_get_message", message="Journal Updated: " + name)
                return

# =========================
# DATA & LOGIC - MINIGAME
# =========================
    import random

    class SlidingPuzzle:
        def __init__(self, tiles_val):
            self.tiles = tiles_val
            self.blank_index = self.tiles.index(0) # 0 represents the empty slot

        def switch(self, tile_index):
            # Check if the clicked tile is adjacent to the blank space
            # (Math for a 3x3 grid)
            if tile_index in [self.blank_index-1, self.blank_index+1, self.blank_index-3, self.blank_index+3]:
                # Special check for grid edges so they don't jump rows
                if not (self.blank_index % 3 == 0 and tile_index == self.blank_index - 1) and \
                   not (self.blank_index % 3 == 2 and tile_index == self.blank_index + 1):
                    
                    # Swap the tile with the blank space
                    self.tiles[self.blank_index], self.tiles[tile_index] = self.tiles[tile_index], self.tiles[self.blank_index]
                    self.blank_index = tile_index
                    renpy.restart_interaction()

        def is_solved(self):
            return self.tiles == [1, 2, 3, 4, 5, 6, 7, 8, 0]

    # Initialize the puzzle state
    def start_puzzle():
        initial_tiles = [1, 2, 3, 4, 5, 6, 7, 8, 0]
        random.shuffle(initial_tiles)
        return SlidingPuzzle(initial_tiles)

default my_puzzle = None

# =========================
# SCREENS (The HUD)
# =========================
screen detective_hud():
    zorder 10
    if show_hud:
        # TOP HUD
        hbox:
            align (0.98, 0.02)
            spacing 20
            imagebutton:
                idle "images/ui/bag_icon.png"
                hover "images/ui/bag_icon.png"
                action [SetVariable("selected_item", None), ShowMenu("inventory_screen")]
                at hud_zoom(0.15, 0.22)
            imagebutton:
                idle "images/ui/journal_icon.png"
                hover "images/ui/journal_icon.png"
                action [SetVariable("selected_suspect", None), ShowMenu("journal_screen")]
                at hud_zoom(0.37, 0.45)
        
        if day1_objective_complete:
            textbutton "FINISH INVESTIGATION":
                align (0.5, 0.92) # Bottom center
                style "finish_day_button"
                action Return("end_the_day")
            
        # WORLD INTERACTIONS
        if current_location == "mhallway":
            imagebutton:
                idle "invisible_idle"
                hover "translucent_hover"
                xysize (150, 200) 
                xpos 1560 ypos 450
                action Return("go_hallway2")
                tooltip "Go to Hallway 2"
            

        if current_location == "hallway2":
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
                idle "invisible_idle"
                hover "translucent_hover"
                xysize (500, 1500) 
                xpos 1600 ypos 0
                action Return("go_mhallway")
                tooltip "Go to Main Hallway"
            imagebutton:
                idle "invisible_idle"
                hover "translucent_hover"
                xysize (300, 1300) 
                xpos 0 ypos 0
                action Return("go_stairs")
                tooltip "Go to Stairs"
        
        if current_location == "stairs":
            imagebutton:
                idle "invisible_idle"
                hover "translucent_hover"
                xysize (800, 800) 
                xpos 1100 ypos 130
                action Return("go_cctv_hallway")
                tooltip "Go to CCTV Hallway"
            imagebutton:
                idle "images/ui/arrow_idle.png"
                hover "images/ui/arrow_hover.png"
                at transform:
                    nearest True
                    zoom 0.3
                xpos 50 ypos 700 
                action Return("go_hallway2")
                tooltip "Return"
            imagebutton:
                idle "invisible_idle"
                hover "translucent_hover"
                xysize (600, 800) 
                xpos 175 ypos 100
                action Return("go_lockers")
                tooltip "Go to Lockers"

        if current_location == "cctv_hallway":
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
        
        if current_location == "cctv_room":
            imagebutton:
                idle "invisible_idle"
                hover "translucent_hover"
                xysize (400, 300) # Adjust to fit your monitor size
                xpos 800 ypos 300 # Adjust to your monitor position
                action Return("solve_cctv")
            imagebutton:
                idle "images/ui/arrow_idle.png"
                hover "images/ui/arrow_hover.png"
                at transform:
                    nearest True
                    zoom 0.3
                xpos 50 ypos 700 
                action Return("go_cctv_hallway")
                tooltip "Return"

        if current_location == "storage_room":
            imagebutton:
                idle "images/ui/arrow_idle.png"
                hover "images/ui/arrow_hover.png"
                at transform:
                    nearest True
                    zoom 0.3
                xpos 50 ypos 700 
                action Return("go_hallway2")
                tooltip "Exit Storage Room"
            imagebutton:
                idle "images/cs/body.png"
                hover "images/cs/bodyh.png"
                at transform:
                    nearest True
                    zoom 1
                xpos 616 ypos 537
                action Return("go_body")
                tooltip("Examine the body")
            if not evidence_taken["waterbottle"]:
                imagebutton:
                    idle "images/cs/waterbottle.png"
                    hover "images/cs/waterbottleh.png"
                    at transform:
                        nearest True
                        zoom 1
                    xpos 690 ypos 743
                    action [
                        Function(add_item, "Half-Empty Bottle", "Found near the victim's head. It looks like it was dropped in a hurry . The label is partially torn, and the plastic is heavily crinkled as if it were squeezed tightly.", "images/cs/waterbottle.png"),
                        SetDict(evidence_taken, "waterbottle", True),
                        Show("item_get_message", message="You found a Water bottle. It looks like it was dropped in a hurry . The label is partially torn, and the plastic is heavily crinkled as if it were squeezed tightly.")
                    ]
                    tooltip "Water Bottle"
            if not evidence_taken["patbag"]:
                imagebutton:
                    idle "images/cs/patbag.png"
                    hover "images/cs/patbagh.png"
                    at transform:
                        nearest True
                        zoom 1
                    xpos 355 ypos 798
                    action [
                        Function(add_item, "Bag", "placeholder", "images/cs/patbag.png"),
                        SetDict(evidence_taken, "patbag", True),
                        Show("item_get_message", message="You found a bag. Placeholder")
                    ]
                    tooltip "Bag"
            if not evidence_taken["patphone"]:
                imagebutton:
                    idle "images/cs/patphone.png"
                    hover "images/cs/patphoneh.png"
                    at transform:
                        nearest True
                        zoom 1
                    xpos 700 ypos 965
                    action [
                        Function(add_item, "Phone", "placeholder", "images/cs/patphone.png"),
                        SetDict(evidence_taken, "patphone", True),
                        Show("item_get_message", message="You found a phone. Placeholder")
                    ]
                    tooltip "Phone"
            if not evidence_taken["powder"]:
                imagebutton:
                    idle "images/cs/powder.png"
                    hover "images/cs/powderh.png"
                    at transform:
                        nearest True
                        zoom 1
                    xpos 949 ypos 810
                    action [
                        Function(add_item, "Drugs", "placeholder", "images/cs/powder.png"),
                        SetDict(evidence_taken, "powder", True),
                        Show("item_get_message", message="You found some Drugs. Placeholder")
                    ]
                    tooltip "Drugs"
            if not evidence_taken["id"]:
                imagebutton:
                    idle "images/cs/id.png"
                    hover "images/cs/idh.png"
                    at transform:
                        nearest True
                        zoom 1
                    xpos 1200 ypos 810
                    action [
                        Function(add_item, "ID", "placeholder", "images/cs/id.png"),
                        SetDict(evidence_taken, "id", True),
                        Show("item_get_message", message="You found an ID. Placeholder")
                    ]
                    tooltip "ID"
                

        if current_location == "body":
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
                idle "images/cs/wound.png"
                hover "images/cs/woundh.png"
                at transform:
                    nearest True
                    zoom 1
                xpos 1080 ypos 650 
                action Return("go_storage")
                tooltip "Return"
            
        if current_location == "lockers":
            imagebutton:
                idle "invisible_idle"
                hover "translucent_hover"
                xysize (600, 800) 
                xpos 175 ypos 100
                action Return("go_patlocker")
                tooltip "Go to Lockers"
            imagebutton:
                idle "images/ui/arrow_idle.png"
                hover "images/ui/arrow_hover.png"
                at transform:
                    nearest True
                    zoom 0.3
                xpos 50 ypos 700 
                action Return("go_stairs")
                tooltip "Return"
        if current_location == "patlocker":
            imagebutton:
                idle "images/ui/arrow_idle.png"
                hover "images/ui/arrow_hover.png"
                at transform:
                    nearest True
                    zoom 0.3
                xpos 50 ypos 700 
                action Return("go_lockers")
                tooltip "Return"

transform hud_zoom(norm, hov):
    on idle:
        linear 0.1 zoom norm
    on hover:
        linear 0.1 zoom hov

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
                            xysize (150, 150) # Smaller than 180 to allow for padding
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
                        xysize (400, 400)
                        xalign 0.5
                    text selected_item.name size 30 color "#4A90E2"
                    text selected_item.description size 23
                else:
                    text "Select item..." align (0.5, 0.5) color "#888"
    textbutton "RETURN" action Return() align (0.5, 0.95)

# =========================
# Journal Screen
# =========================
default journal_page = 0
default day_count = 1
default journal_list = []
default selected_suspects = []
default eliminated_suspects = []

screen journal_screen():
    tag menu
    add Solid("#0b121a")

    frame:
        xsize 1200 ysize 800
        align (0.5, 0.6) 
        background Frame(Solid("#f4ecd8"), 4, 4) 
        padding (40, 40)

        # --- RIGHT SIDE TABS ---
        hbox:
            ypos -80 # Pulls the tabs UP above the frame
            xalign 0.0 # Aligns them to the left edge of the book
            spacing 2 # Small gap between tabs
            
            textbutton "Cover" action SetVariable("journal_page", 0) style "journal_tab"
            textbutton "Report" action SetVariable("journal_page", 1) style "journal_tab"
            
            # This loop automatically handles new suspects as they are appended
            for i, person in enumerate(journal_list):
                textbutton person.name:
                    action SetVariable("journal_page", i + 2)
                    style "journal_tab"

            if day_count >= 6:
                textbutton "FINAL" action SetVariable("journal_page", len(journal_list) + 2) style "journal_tab"

        # --- PAGE CONTENT ---
        # (This part stays the same as your previous code)
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
                vbox: 
                    xsize 500
                    text current_person.name size 35 color "#222"
            
                    if "Pat" in current_person.name:
                        # Non-clickable status for the victim
                        frame:
                            background Solid("#8B0000") # Blood red
                            padding (15, 5)
                            text "DECEASED / VICTIM" size 18 color "#fff" bold True
                        
                        null height 10
                        text "File: Case #109-B" size 14 color "#555" italic True

                    else:
                        # Regular toggle button for living suspects
                        textbutton "[current_person.status] ▼":
                            style "status_toggle_button"
                            action If(current_person.status == "Person of Interest", 
                                     SetField(current_person, "status", "Suspect"), 
                                     SetField(current_person, "status", "Person of Interest"))

                    add Transform(current_person.image, fit="contain"):
                        size (400, 500)
                vbox: 
                    xsize 500
                    spacing 15
                    for entry in current_person.descriptions: 
                        if "|" in entry:
                            $ header, body = entry.split("|")
                            text header size 22 bold True color "#4A90E2"
                            text body size 18 color "#333"
                        else:
                            text entry size 18 color "#333"
        else:
            # THE KILLER LIST
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

    # Navigation & Return
    if journal_page > 0:
        textbutton " < " action SetVariable("journal_page", journal_page - 1) align (0.1, 0.5) text_size 60
    if journal_page < (len(journal_list) + (2 if day_count >= 6 else 1)):
        textbutton " > " action SetVariable("journal_page", journal_page + 1) align (0.9, 0.5) text_size 60

    textbutton "RETURN" action Return() align (0.5, 0.95)

# Styling the tabs to look like they are tucked under the book
style journal_tab:
    background Solid("#ccc")
    padding (15, 10, 15, 5) # Left, Top, Right, Bottom
    hover_background "#4A90E2"
    selected_background "#f4ecd8" # Matches the book color when active
    color "#000"
    size 16
    yminimum 50

# =========================
# HUD - MINIGAME
# =========================

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
                    # We use a solid black square for the hole so we can see it
                    null width 200 height 200 
                else:
                    # Create the path. 
                    # CHANGE "images/" to "images/your_subfolder/" if needed!
                    $ tile_path = "images/puzzle/tile_" + str(tile_num) + ".png"
                    
                    imagebutton:
                        idle tile_path
                        # This ensures the button has a size even if the image fails
                        xysize (200, 200) 
                        action [
                            Function(puzzle_obj.switch, i), 
                            If(puzzle_obj.is_solved(), Return("win"))
                        ]

    textbutton "CLOSE PUZZLE":
        align (0.5, 0.95)
        action Return("fail")

# =========================
# INTRO
# =========================
label start:

    python:
        for person in journal_list:
            if not hasattr(person, 'status'):
                person.status = "Person of Interest"
            if not hasattr(person, 'descriptions'):
                person.descriptions = []

    $ add_suspect("Pat (Victim)", "Found in the storage room. Cause of death unknown.", "images/suspects/pat_dead.png")

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

    show chief_normal at right with moveinright
    
    pc "You’re finally here, [mc]."
    
    pc "It’s gruesome in there... *sighs*"
    pc "But we don't have time to dawdle—so let me fill you in."

    # --- Flashback: The Call ---
    stop music fadeout 1.0
    scene prologue-call with flash
    
    op "9-1-1, what’s your emergency?"
    
    d "Hello? M-may... may—"

    pc "A call was made to 9-1-1 at 4:56 AM in the morning."
    
    scene prologue-call2 with dissolve
    
    pc "The janitor, Dan-found the body in around 4:53 AM."
    
    pc "Scene’s... rough. Whoever did this didn't hold back."

    scene main_hallway with fade

    show chief_normal at right
    pc "We may not have much information, but it’s better than nothing."

# =========================
# Tutorial
# =========================
label tutorial:
    scene main_hallway
    show image "images/ui/bag_icon.png" as icon_inv at popup_center
    s "System: Inventory Unlocked."
    
    pause

    show image "images/ui/bag_icon.png" as icon_inv at move_to_hud_left
    s "System: Go to your inventory."

    $ add_item("Crime Photo", "A photo of the 6th floor storage room.", "images/items/photo.png")
    s "{u}Crime Photo{/u} added to your Bag."

    call screen inventory_screen
    s "System: Items will be stored there."

    # --- JOURNAL ---
    show image "images/ui/journal_icon.png" as icon_jou at popup_center
    s "System: Journal Unlocked."

    pause
    
    show image "images/ui/journal_icon.png" as icon_jou at move_to_hud_right
    s "System: Check your journal."

    $ add_suspect("Dan (Janitor)", "The man who found the body. Seems shaken.", "images/suspects/dan_port.png")
    # Starting clue:
    $ journal_list[0].descriptions.append("Observation|He was trembling when he spoke to the Captain.")
    s "New Suspect added to Journal: {u}Dan.{/u}"

    call screen journal_screen
    s "All discovered clues, notes, and observations will be recorded there."
    s "new suspects and profiles will be unlocked as you progress through the story"

    hide icon_jou
    hide icon_inv

    # --- FINAL STEP ---
    # Now show the actual HUD screen which has the real buttons
    $ show_hud = True
    show screen detective_hud
    s "System: You are ready to begin."
    
    scene storage_room with fade
    mc "The moment I stepped into the crime scene..."
    mc "....my eyes started scanning everything."
    mc "Blood stains."
    mc "Footprints."
    mc "Objects out of place."
    mc "Details most people overlook"
    show text Text("Sense Activated — SIGHT", size=70, color="#00FFFF") at truecenter    
    with dissolve
    s "Observe the environment carefully"
    jump storage_room

# =========================
# DAY 1
# =========================
    $ show_hud = False
    scene black with fade
    show text "{size=70}DAY 1{/size}" at truecenter
    with dissolve

    $ renpy.pause(3)

label mhallway:
    play music "audio/ambiance_hallway_d1.mp3" loop
    $ current_location = "mhallway"
    $ show_hud = True
    scene main_hallway with fade

    $ result = renpy.call_screen("detective_hud")
    
    if result == "go_hallway2":
        jump hallway2
    jump mhallway

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
            pc "its locked- but there seems to be someone inside..."
    jump cctv_hallway

label cctv_room:
    play music "audio/ambiance_hallway_d1.mp3" loop
    $ current_location = "cctv_room"
    $ scenario_picker1 = True
    scene cctv_room with fade

    $ result = renpy.call_screen("detective_hud")

    if result == "solve_cctv":
        $ my_puzzle = start_puzzle() # Create the puzzle
        $ puzzle_result = renpy.call_screen("cctv_puzzle_screen", my_puzzle)
        
        if puzzle_result == "win":
            mc "The image cleared up! I can see the suspect now."
            $ add_item("Clear CCTV Footage", "A restored image of the culprit.", "images/items/cctv_fix.png")
        else:
            mc "It's too corrupted. I'll have to try again later."
        jump cctv_room

    elif result == "go_cctv_hallway":
        jump cctv_hallway

label storage_room:
    play music "audio/ambiance_crime_scene_d1.mp3" loop
    $ current_location = "storage_room"
    scene storage_room with fade
    
    if not seen_scene_intro:
        $ result = renpy.hide_screen("detective_hud")
        $ Pause (0.2)
        mc "..."

        mc "The victim."

        mc "Right in the middle of the room."

        mc "But the answers might not be."
        $ seen_scene_intro = True

    $ result = renpy.call_screen("detective_hud")
    if result == "go_hallway2":
        jump hallway2
    elif result == "go_body":
        if scenario_picker1 == False:
            jump body
        elif scenario_picker1 == True:
           pc "The CSI guys are already checking the body while you we're gone. Check other stuff incase you miss other details. They'll send what they got from the body in the 3rd Day."
    jump storage_room

label body:
    play music "audio/ambience_crime_scene_d1.mp3" loop 
    $ current_location = "body"
    $ scenario_picker2 = True
    scene zbody with fade

    if not seen_body:
        $ result = renpy.hide_screen("detective_hud")
        $ Pause (0.2)
        mc "Looking at the body, so many things are happening holy pack tangina."
        $ seen_body = True
    
    window hide

    $ record_clue("Pat (Victim)", "Time of Death|Estimated between 3:00 AM and 4:30 AM.")
    $ record_clue("Pat (Victim)", "Wounds|Defensive wounds found on the forearms.")

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
    elif result == "go_patlocker":
        jump patlocker
    jump lockers

label patlocker:
    play music "audio/ambiance_hallway_d1.mp3" loop
    $ current_location = "patlocker"
    scene patlocker with fade

    $ result = renpy.call_screen("detective_hud")

    if result == "go_lockers":
        jump lockers
    jump patlocker

# =========================
# DAY 2
# =========================
label day2:
    scene black with fade
    $ show_hud = False
    scene black with fade
    show text "{size=70}DAY 2{/size}" at truecenter
    with dissolve

    $ renpy.pause(3)