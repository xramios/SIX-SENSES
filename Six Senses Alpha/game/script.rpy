define gui.text_font = "Ithaca-LVB75.ttf"
default seen_scene_intro = False
# --- Character Definitions ---
define mc = Character("[player_name]")
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

transform popup_center:
    xalign 0.5 yalign 0.5
    zoom 0.0
    linear 0.3 zoom 1.0

transform move_to_hud_left:
    linear 0.8 xalign 0.47 yalign 0.02 zoom 0.15

transform move_to_hud_right:
    linear 0.8 xalign 0.53 yalign 0.02 zoom 0.37

# --- Variables ---
default player_name = "Detective"
default show_hud = False
default current_location = "hallway"

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

# =========================
# SCREENS (The GUI)
# =========================
screen detective_hud():
    zorder 100
    if show_hud:
        # TOP HUD
        hbox:
            align (0.5, 0.02)
            spacing 40
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

        # WORLD INTERACTIONS
        if current_location == "mhallway":
            imagebutton:
                idle "invisible_idle"
                hover "translucent_hover"
                xysize (150, 200) 
                xpos 1550 ypos 450
                action Return("go_hallway2")
                tooltip "Go to Hallway 2"
            

        if current_location == "hallway2":
            imagebutton:
                idle "images/ui/door_idle.png" 
                hover "images/ui/door_hover.png"
                at transform:
                    nearest True
                    zoom 3.05
                xpos 869 ypos 360
                action Return("go_storage_scenario1") 
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
                xysize (300, 1500) 
                xpos 0 ypos 0
                action Return("go_stairs")
                tooltip "Go to Stairs"
        
        if current_location == "stairs":
            imagebutton:
                idle "invisible_idle"
                hover "translucent_hover"
                xysize (800, 800) 
                xpos 1200 ypos 0
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
            
        if current_location == "storage_room_scenario1":
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
                    rotate -20
                    anchor (0.5, 0.5)
                xpos 800 ypos 250
                action Return("go_body_scenario1")
                tooltip("Examine the body")

        if current_location == "body_scenario1":
            imagebutton:
                idle "images/ui/arrow_idle.png"
                hover "images/ui/arrow_hover.png"
                at transform:
                    nearest True
                    zoom 0.3
                xpos 50 ypos 700 
                action Return("go_storage_scenario1")
                tooltip "Return"
            imagebutton:
                idle "images/cs/bloods body.png"
                hover "images/cs/bloods_body.png"
                at transform:
                    nearest True
                    zoom 0.3
                xpos 50 ypos 700 
                action Return("go_storage_scenario1")
                tooltip "Return"

transform hud_zoom(norm, hov):
    on idle:
        linear 0.1 zoom norm
    on hover:
        linear 0.1 zoom hov

screen inventory_screen():
    tag menu
    add Solid("#000000E6")
    label "EVIDENCE BAG" align (0.5, 0.15)
    hbox:
        align (0.5, 0.5)
        spacing 40
        vpgrid:
            cols 3 spacing 15 allow_underfull True xsize 480
            for i in range(12):
                if i < len(inventory_list):
                    $ item = inventory_list[i]
                    button:
                        action SetVariable("selected_item", item)
                        xysize (150, 150)
                        background Frame(Solid("#444"), 4, 4)
                        hover_background Solid("#666")
                        add item.image align (0.5, 0.5)
                else:
                    frame:
                        xysize (150, 150) background Frame(Solid("#222"), 2, 2)
                        text "EMPTY" align (0.5, 0.5) size 14 color "#444"
        frame:
            xsize 400 ysize 500 background Solid("#111")
            vbox:
                spacing 20
                if selected_item:
                    add selected_item.image xalign 0.5
                    text selected_item.name size 28 color "#4A90E2"
                    text selected_item.description size 18
                else:
                    text "Select item..." align (0.5, 0.5) color "#888"
    textbutton "RETURN" action Return() align (0.5, 0.95)

screen journal_screen():
    tag menu
    add Solid("#0b121a")
    label "SUSPECT FILES" align (0.5, 0.15)
    hbox:
        align (0.5, 0.5) spacing 40
        vbox:
            spacing 10
            for person in journal_list:
                button:
                    action SetVariable("selected_suspect", person)
                    xsize 300 ysize 60 background Solid("#222")
                    hover_background Solid("#4A90E2")
                    text person.name align (0.5, 0.5)
        frame:
            xsize 500 ysize 500 background Solid("#111")
            if selected_suspect:
                vbox:
                    add selected_suspect.image xalign 0.5
                    text selected_suspect.name size 30 color "#F08080"
                    text selected_suspect.bio size 18
            else:
                text "Select file..." align (0.5, 0.5)
    textbutton "RETURN" action Return() align (0.5, 0.95)

# =========================
# PROLOGUE
# =========================
label start:
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
    
    pc "You’re finally here, [player_name]."
    
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

# =========================
# GAMEPLAY 
# =========================
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
    if result == "go_storage_scenario1":
        jump storage_room_scenario1
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
    jump stairs

label cctv_hallway:
    play music "audio/ambiance_crime_scene_d1.mp3" loop
    $ current_location = "cctv_hallway"
    scene cctv_hallway with fade

    $ result = renpy.call_screen("detective_hud")

    if result == "go_stairs":
        jump stairs
    jump cctv_hallway

label storage_room_scenario1:
    play music "audio/ambiance_crime_scene_d1.mp3" loop
    $ current_location = "storage_room_scenario1"
    scene crime_scene with fade
    
    if not seen_scene_intro:
        "You enter the room- and as you see the scene laid out, you cover mouth on instinct"
        window hide
        mc "I just cant get used to this"
        $ seen_scene_intro = True

    $ result = renpy.call_screen("detective_hud")
    if result == "go_hallway2":
        jump hallway2
    elif result == "go_body_scenario1":
        jump body_scenario1
    jump storage_room_scenario1

label body_scenario1:
    play music "audio/ambience_crime_scene_d1.mp3" loop 
    $ current_location = "body_scenario1"
    scene zbody with fade

    "Looking at the body, so many things are happening holy pack tangina."
    window hide

    $ result = renpy.call_screen("detective_hud")
    if result == "go_storage_scenario1":
        jump storage_room_scenario1
    jump body_scenario1