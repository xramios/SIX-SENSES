default show_hud = False
default seen_scene_intro = False
default seen_body = False
default seen_mhallwayd2_intro = False
default seen_cctv_room_intro = False
default cctv_cam1_solved = False
default cctv_cam4_solved = False
default scenario_picker1 = False
default scenario_picker2 = False
default cctv_hallway_cigarette_noticed = False
default cctv_hallway_blood_noticed = False
default cigarette_smell_faint = False
default cigarette_smell_faded = False
default cigarette_smell_strong = False
default blood_smell_faint = False
default blood_smell_strong = False
default blood_smell_overwhelming = False
default rubble_moved = False
default current_location = "hallway"
default evidence_taken = {
    "waterbottle": False,
    "patbag": False,
    "knife": False,
    "cigarette": False,
    "powder": False,
    "id": False,
    "patphone": False,
    "cctv_tape1": False,
    "cctv_tape2": False,
}

default day1_objective_complete = False
default current_day = 1

image cctv_1 = "images/cctv/cctv_dan.png"
image cctv_2 = "images/cctv/CCTV_Error.png"
image cctv_3 = "images/cctv/CCTV_Error.png"
image cctv_4 = "images/cctv/corr_cctv_toph.png"
image cctv_5 = "images/cctv/CCTV_Error.png"

default cctv_index = 0
default cctv_list = ["cctv_1", "cctv_2", "cctv_3", "cctv_4", "cctv_5"]

default met_dan = False
default journal_page = 0
default selected_suspects = []
default eliminated_suspects = []

# Day 3 & Hacking Variables
default seen_evidence_room_intro = False
default item_to_inspect = ""
default phone_unlocked = False
default hacking_timer = 240
default hack_level = 1
default hack_found = 0
default target_fp = ""
default hack_snippets = []
default tape_num = 0

default interrogated_dan = False
default interrogated_toph = False
default interrogated_austin = False
default interrogated_chandler = False

# --- FINAL ACCUSATION VARIABLES ---
default possible_crimes = ["Select Crime...", "Murder", "Unlawful Restraint", "Drug Distribution", "Desecration of a Corpse", "Extortion", "Accessory"]

default end_dan_status = "Person of Interest"
default end_dan_crime = "Select Crime..."

default end_toph_status = "Person of Interest"
default end_toph_crime = "Select Crime..."

default end_austin_status = "Person of Interest"
default end_austin_crime = "Select Crime..."

default end_chandler_status = "Person of Interest"
default end_chandler_crime = "Select Crime..."