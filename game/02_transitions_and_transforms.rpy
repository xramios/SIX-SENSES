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