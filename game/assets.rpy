# 初始化图像和样式
init:
    image 1 = "images/1.png"
    image 2 = "images/3.png"
    image 3 = "images/5.png"

    # 角色 sprite 定义
    image s young neutral = "images/sakuya_young_neutral.png"
    image s young neutral1 = "images/sakuya_young_neutral1.png"
    image s young angry = "images/sakuya_young_angry.png"
    image s young pained = "images/sakuya_young_pained.png"
    image s young formal pained = "images/sakuya_young_formal_pained.png"
    image s young desperate = "images/sakuya_young_desperate.png"
    image s adult neutral empty = "images/sakuya_adult_neutral_empty.png"
    image s middle aged empty = "images/sakuya_middle_aged_empty.png"
    image y young neutral = "images/ona_young_neutral.png"
    image y young neutral1 = "images/ona_young_neutral1.png"
    image y back head down = "images/ona_back_head_down.png"
    image y back head down far = "images/ona_back_head_down_far.png"
    image o scared resolved = "images/ona_scared_resolved.png"
    image o adult back = "images/ona_adult_back.png"
    image o hand closeup = "images/ona_hand_closeup.png"
    image o middle aged back = "images/ona_middle_aged_back.png"
    image o hand calm = "images/ona_hand_calm.png"
    image father angry = "images/father_angry.png"
    image wife silhouette = "images/wife_silhouette.png"
    image young_retainer = "images/young_retainer.png"

    # 背景和 CG 定义
    image library = "images/library.png"
    image bg mansion_corridor_rainy = "images/mansion_corridor_rainy.png"
    image bg study_night2 = "images/study_night2.png"
    image bg outside_o_room_night = "images/outside_o_room_night.png"
    image bg garden_rain_view = "images/garden_rain_view.png"
    image bg mansion_corridor_dim = "images/mansion_corridor_dim.png"
    image bg tea_room = "images/tea_room.png"
    image bg wedding = "images/wedding.png"
    image bg garden_winter = "images/garden_winter.png"
    image bg garden_winter2 = "images/garden_winter2.png"
    image bg simple_room = "images/simple_room.png"
    image bg s_study_night = "images/s_study_night.png"
    image bg s_room_dawn = "images/s_room_dawn.png"
    image bg mansion_corridor_earlyam = "images/mansion_corridor_earlyam.png"
    image bg small_garden = "images/small_garden.png"
    image bg s_study_late = "images/s_study_late.png"
    image bg garden_spring = "images/garden_spring.png"
    image bg old_cherry_tree = "images/old_cherry_tree.png"
    image bg garden_spring_wide = "images/garden_spring_wide.png"
    image cg snow_child = "images/snow_child.png"
    image cg hairpin = "images/hairpin.png"
    image cg broken_pin = "images/broken_pin.png"
    image cherry_blossom_fall = "images/cherry_blossom_fall.png"
    image bg garden_rain_view2 = "images/garden_rain_view2.png"
    image bg corridor_night = "images/bg corridor_night.png"
    image bg kamogawa_river_dusk = "images/river_day.png"
    image bg kamogawa_village = "images/village.png"
    image bg kamogawa_river_night = "images/river_night.png"
    image cg child_listening = "images/child_listening.png"
    image cg old_ona_cherry = "images/old_ona_cherry.png"
    image bg yoshino_cherry_festival = "images/yoshino_cherry_festival.png"
    image bg wedding2 = "images/bg wedding2.png"
    image bg s_room_fire = "images/bg s_room_fire.png"
    image bg fireworks = "images/bg fireworks.png"
    image cg letter_content = "images/cg letter_content.png"
    image bg ancestral_shrine = "images/bg ancestral_shrine.png"
    image cg sealed_letter = "images/cg sealed_letter.png"
    image cg old_painting = "images/cg old_painting.png"
    image bg archive_room_dim = "images/bg archive_room_dim.png"
    image cg old_letter = "images/cg old_letter.png"
    image samurai = "images/samurai.png"
    image bg asakawa_gate_night = "images/bg asakawa_gate_night.png"
    
init python:
    # 全局字体大小调整
    style.default.size = 28
    style.button_text.size = 30
    style.label_text.size = 36
    
    # 如果没有背景图，使用纯色代替
    if not renpy.loadable("gui/main_menu.png"):
        renpy.image("gui/main_menu.png", Solid("#333", xsize=1920, ysize=1080))
    if not renpy.loadable("gui/chapter_bg.png"):
        renpy.image("gui/chapter_bg.png", Solid("#222", xsize=1920, ysize=1080))
    if not renpy.loadable("gui/chapter1_idle.png"):
        renpy.image("gui/chapter1_idle.png", Solid("#700", xsize=200, ysize=200))
    if not renpy.loadable("gui/chapter1_hover.png"):
        renpy.image("gui/chapter1_hover.png", Solid("#a00", xsize=200, ysize=200))
    if not renpy.loadable("gui/chapter2_idle.png"):
        renpy.image("gui/chapter2_idle.png", Solid("#070", xsize=200, ysize=200))
    if not renpy.loadable("gui/chapter2_hover.png"):
        renpy.image("gui/chapter2_hover.png", Solid("#0a0", xsize=200, ysize=200))
    if not renpy.loadable("gui/chapter3_idle.png"):
        renpy.image("gui/chapter3_idle.png", Solid("#007", xsize=200, ysize=200))
    if not renpy.loadable("gui/chapter3_hover.png"):
        renpy.image("gui/chapter3_hover.png", Solid("#00a", xsize=200, ysize=200))
    if not renpy.loadable("gui/chapter4_idle.png"):
        renpy.image("gui/chapter4_idle.png", Solid("#770", xsize=200, ysize=200))
    if not renpy.loadable("gui/chapter4_hover.png"):
        renpy.image("gui/chapter4_hover.png", Solid("#a70", xsize=200, ysize=200))
    if not renpy.loadable("gui/chapter5_idle.png"):
        renpy.image("gui/chapter5_idle.png", Solid("#707", xsize=200, ysize=200))
    if not renpy.loadable("gui/chapter5_hover.png"):
        renpy.image("gui/chapter5_hover.png", Solid("#a07", xsize=200, ysize=200))
    if not renpy.loadable("gui/chapter6_idle.png"):
        renpy.image("gui/chapter6_idle.png", Solid("#077", xsize=200, ysize=200))
    if not renpy.loadable("gui/chapter6_hover.png"):
        renpy.image("gui/chapter6_hover.png", Solid("#0a7", xsize=200, ysize=200))
    if not renpy.loadable("gui/chapter7_idle.png"):
        renpy.image("gui/chapter7_idle.png", Solid("#707", xsize=200, ysize=200))
    if not renpy.loadable("gui/chapter7_hover.png"):
        renpy.image("gui/chapter7_hover.png", Solid("#70a", xsize=200, ysize=200))
    if not renpy.loadable("gui/chapter8_idle.png"):
        renpy.image("gui/chapter8_idle.png", Solid("#077", xsize=200, ysize=200))
    if not renpy.loadable("gui/chapter8_hover.png"):
        renpy.image("gui/chapter8_hover.png", Solid("#07a", xsize=200, ysize=200))
    if not renpy.loadable("gui/chapter9_idle.png"):
        renpy.image("gui/chapter9_idle.png", Solid("#777", xsize=200, ysize=200))
    if not renpy.loadable("gui/chapter9_hover.png"):
        renpy.image("gui/chapter9_hover.png", Solid("#aaa", xsize=200, ysize=200))
    
    # 如果没有场景图，使用纯色代替
    if not renpy.loadable("bg park"):
        renpy.image("bg park", Solid("#5a8", xsize=1920, ysize=1080))
    if not renpy.loadable("bg cafe"):
        renpy.image("bg cafe", Solid("#ca8", xsize=1920, ysize=1080))
    if not renpy.loadable("bg library"):
        renpy.image("bg library", Solid("#876", xsize=1920, ysize=1080))
    
    # 如果没有角色图像，使用纯色代替
    if not renpy.loadable("alice smile"):
        renpy.image("alice smile", Solid("#f88", xsize=400, ysize=600))
    if not renpy.loadable("bob neutral"):
        renpy.image("bob neutral", Solid("#88f", xsize=400, ysize=600))
    if not renpy.loadable("images/sakuya_young_neutral.png"):
        renpy.image("s young neutral", Solid("#23742e", xsize=400, ysize=600))
    if not renpy.loadable("images/sakuya_young_angry.png"):
        renpy.image("s young angry", Solid("#23742e", xsize=400, ysize=600))
    if not renpy.loadable("images/sakuya_young_pained.png"):
        renpy.image("s young pained", Solid("#23742e", xsize=400, ysize=600))
    if not renpy.loadable("images/sakuya_young_formal_pained.png"):
        renpy.image("s young formal pained", Solid("#23742e", xsize=400, ysize=600))
    if not renpy.loadable("images/sakuya_young_desperate.png"):
        renpy.image("s young desperate", Solid("#23742e", xsize=400, ysize=600))
    if not renpy.loadable("images/sakuya_adult_neutral_empty.png"):
        renpy.image("s adult neutral empty", Solid("#23742e", xsize=400, ysize=600))
    if not renpy.loadable("images/sakuya_middle_aged_empty.png"):
        renpy.image("s middle aged empty", Solid("#23742e", xsize=400, ysize=600))
    if not renpy.loadable("images/ona_young_neutral.png"):
        renpy.image("y young neutral", Solid("#d843cc", xsize=400, ysize=600))
    if not renpy.loadable("images/ona_back_head_down.png"):
        renpy.image("y back head down", Solid("#d843cc", xsize=400, ysize=600))
    if not renpy.loadable("images/ona_back_head_down_far.png"):
        renpy.image("y back head down far", Solid("#d843cc", xsize=400, ysize=600))
    if not renpy.loadable("images/ona_scared_resolved.png"):
        renpy.image("o scared resolved", Solid("#d843cc", xsize=400, ysize=600))
    if not renpy.loadable("images/ona_adult_back.png"):
        renpy.image("o adult back", Solid("#d843cc", xsize=400, ysize=600))
    if not renpy.loadable("images/ona_hand_closeup.png"):
        renpy.image("o hand closeup", Solid("#d843cc", xsize=400, ysize=600))
    if not renpy.loadable("images/ona_middle_aged_back.png"):
        renpy.image("o middle aged back", Solid("#d843cc", xsize=400, ysize=600))
    if not renpy.loadable("images/ona_hand_calm.png"):
        renpy.image("o hand calm", Solid("#d843cc", xsize=400, ysize=600))
    if not renpy.loadable("images/father_angry.png"):
        renpy.image("father angry", Solid("#555", xsize=400, ysize=600))
    if not renpy.loadable("images/wife_silhouette.png"):
        renpy.image("wife silhouette", Solid("#888", xsize=400, ysize=600))
    if not renpy.loadable("images/young_retainer.png"):
        renpy.image("young_retainer", Solid("#666", xsize=400, ysize=600))
    
    # 如果没有背景或 CG，使用纯色代替
    if not renpy.loadable("images/mansion_corridor_rainy.png"):
        renpy.image("bg mansion_corridor_rainy", Solid("#333", xsize=1920, ysize=1080))
    if not renpy.loadable("images/outside_o_room_night.png"):
        renpy.image("bg outside_o_room_night", Solid("#111", xsize=1920, ysize=1080))
    if not renpy.loadable("images/garden_rain_view.png"):
        renpy.image("bg garden_rain_view", Solid("#444", xsize=1920, ysize=1080))
    if not renpy.loadable("images/mansion_corridor_dim.png"):
        renpy.image("bg mansion_corridor_dim", Solid("#555", xsize=1920, ysize=1080))
    if not renpy.loadable("images/tea_room.png"):
        renpy.image("bg tea_room", Solid("#876", xsize=1920, ysize=1080))
    if not renpy.loadable("images/garden_winter.png"):
        renpy.image("bg garden_winter", Solid("#ccc", xsize=1920, ysize=1080))
    if not renpy.loadable("images/simple_room.png"):
        renpy.image("bg simple_room", Solid("#999", xsize=1920, ysize=1080))
    if not renpy.loadable("images/s_study_night.png"):
        renpy.image("bg s_study_night", Solid("#222", xsize=1920, ysize=1080))
    if not renpy.loadable("images/s_room_dawn.png"):
        renpy.image("bg s_room_dawn", Solid("#666", xsize=1920, ysize=1080))
    if not renpy.loadable("images/mansion_corridor_earlyam.png"):
        renpy.image("bg mansion_corridor_earlyam", Solid("#777", xsize=1920, ysize=1080))
    if not renpy.loadable("images/small_garden.png"):
        renpy.image("bg small_garden", Solid("#5a8", xsize=1920, ysize=1080))
    if not renpy.loadable("images/s_study_late.png"):
        renpy.image("bg s_study_late", Solid("#333", xsize=1920, ysize=1080))
    if not renpy.loadable("images/garden_spring.png"):
        renpy.image("bg garden_spring", Solid("#a5a", xsize=1920, ysize=1080))
    if not renpy.loadable("images/old_cherry_tree.png"):
        renpy.image("bg old_cherry_tree", Solid("#a5a", xsize=1920, ysize=1080))
    if not renpy.loadable("images/garden_spring_wide.png"):
        renpy.image("bg garden_spring_wide", Solid("#a5a", xsize=1920, ysize=1080))
    if not renpy.loadable("images/snow_child.png"):
        renpy.image("cg snow_child", Solid("#f0f0f0", xsize=1920, ysize=1080))
    if not renpy.loadable("images/hairpin.png"):
        renpy.image("cg hairpin", Solid("#ddd", xsize=1920, ysize=1080))
    if not renpy.loadable("images/broken_pin.png"):
        renpy.image("cg broken_pin", Solid("#ddd", xsize=1920, ysize=1080))
    if not renpy.loadable("images/cherry_blossom_fall.png"):
        renpy.image("cherry_blossom_fall", Solid("#ffb6c1", xsize=1920, ysize=1080))