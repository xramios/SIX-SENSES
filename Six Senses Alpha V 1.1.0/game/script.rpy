define gui.text_font = "Ithaca-LVB75.ttf"
# --- Character Definitions ---
define mc = Character("[player_name]")
define pc = Character("Captain", color="#4A90E2")
define d = Character("Dan", color="#C5B358")
define c = Character("Chandler", color="#F08080")
define t = Character("Toph", color="#50C878")
define a = Character("Austin", color="#9370DB")
define op = Character("911 Operator", color="#C20101")

# --- Transitions ---
define flash = Fade(.25, 0.0, .75, color="#fff")

# --- Variables ---
default player_name = "Detective"
default show_hud = False
default current_location = "hallway"

# =========================
# DATA & LOGIC
# =========================
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
                idle "images/ui/bag_idle.png"
                hover "images/ui/bag_idle.png"
                action [SetVariable("selected_item", None), ShowMenu("inventory_screen")]
                at hud_zoom(0.17, 0.22)
            imagebutton:
                idle "images/ui/journal_idle.png"
                hover "images/ui/journal_idle.png"
                action [SetVariable("selected_suspect", None), ShowMenu("journal_screen")]
                at hud_zoom(0.40, 0.45)

        # WORLD INTERACTIONS
        if current_location == "hallway":
            imagebutton:
                idle "images/ui/door_idle.png" 
                hover "images/ui/door_hover.png"
                at transform:
                    nearest True
                    zoom 3.05
                xpos 869 ypos 360
                action Return("go_storage") 
                tooltip "Enter Storage Room"

        if current_location == "storage_room":
            imagebutton:
                idle "images/ui/arrow_idle.png"
                hover "images/ui/arrow_hover.png"
                at transform:
                    nearest True
                    zoom 0.3
                xpos 50 ypos 700 
                action Return("go_hallway")
                tooltip "Exit Storage Room"
            
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

    pc "Detective, are you available right now? no-it doesn't matter, come to the location I sent you, ASAP."
    with dissolve

    hide intro1 with dissolve

    show text "{size=50}groggy and confused at not even being able to answer, you hurriedly change and grab your things{/size}" as intro2:
        xalign 0.5 yalign 0.8
    with dissolve
    
    $ renpy.pause(3.0)
    hide intro2 with dissolve

    scene black
    play sound "audio/exitinghome.mp3"
    $ renpy.pause(18.0)

    scene car
    play sound "audio/carengine.mp3"
    $ renpy.pause(0.5)

    show sfc:
        xalign 0.5 yalign 0.33
        zoom 0.5
        alpha 0.0
        linear 2.0 alpha 0.7

    show text "{size=25}Story adaptation from Silangan Film Circle{/size}":
        xalign 0.5 yalign 0.45
        alpha 0.0
        pause 0.5
        linear 1.0 alpha 1.0

    $ renpy.pause(7)
    
    hide sfc
    hide text
    with dissolve

    stop music
    stop sound
    scene main_hallway with fade

    play music "audio/police_siren.mp3" loop
    
    "As you walk inside, the uniformed officers lead you to the 6th floor."
    "Police tape and personnel overflow from the storage room."

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
# DAY 1 START
# =========================
    play music "audio/ambiance_noise_d1.mp3" loop

    scene main_hallway with fade

    $ show_hud = True
    show screen detective_hud
    with dissolve

    "System: Your Inventory and Journal are now accessible at the top of your screen."
    
    # ADDING A SUSPECT (Tutorial)
    $ journal_list.append(Suspect("Dan (Janitor)", "The man who found the body. Seems shaken.", "images/suspects/dan_port.png"))
    "System: New Suspect added to Journal: {u}Dan.{/u}"
    
    # ADDING AN ITEM
    $ inventory_list.append(Item("Crime Photo", "A photo of the 6th floor storage room.", "images/items/photo.png"))
    "System: {u}Crime Photo{/u} added to your Bag."

    pc "Ready to start the investigation, [player_name]?"

# =========================
# GAMEPLAY LOOP
# =========================
label hallway:
    play music "audio/ambiance_hallway_d1.mp3" loop
    $ current_location = "hallway"
    $ show_hud = True
    scene main_hallway with fade

    $ result = renpy.call_screen("detective_hud")
    
    $ add_suspect("Dan (Janitor)", "Found the body. Shaken.", "images/suspects/dan_port.png")
    $ add_item("Crime Photo", "The 6th floor storage room.", "images/items/photo.png")
    
    if result == "go_storage":
        jump storage_room
    jump hallway

label storage_room:
    play music "audio/ambiance_crime_scene_d1.mp3" loop
    $ current_location = "storage_room"
    scene crime_scene with fade
    
    "This is the storage room. Look around."
    
    # This waits for the button click safely
    $ result = renpy.call_screen("detective_hud")
    
    if result == "go_hallway":
        jump hallway
    jump storage_room



