default show_hud = False
default seen_scene_intro = False
default seen_body = False
default seen_mhallwayd2_intro = False
default cctv_cam1_solved = False
default cctv_cam4_solved = False
default cctv_cam4_hidden = False
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
}
default day1_objective_complete = False
default current_day = 1

image cctv_1 = "images/cctv/pat_dragged.png"
image cctv_2 = "images/cctv/CCTV_Error.png"
image cctv_3 = "images/cctv/CCTV_Error.png"
image cctv_4 = "images/cctv/cctv_elevator.png"
image cctv_5 = "images/cctv/CCTV_Error.png"

default cctv_index = 0
default cctv_list = ["cctv_1", "cctv_2", "cctv_3", "cctv_4", "cctv_5"]

default met_dan = False
default journal_page = 0
default selected_suspects = []
default eliminated_suspects = []

# Day 3 & Hacking Variables
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