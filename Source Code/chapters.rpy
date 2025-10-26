# 游戏内容
label start:
    call screen character_select
    return
label start_game:
    if selected_chapter == 1:
        if persistent.perspective == "I":
            jump sakuya_prologue_i
        elif persistent.perspective == "O":
            jump sakuya_prologue_o
        else:
            # 新游戏，提示选择视角
            menu:
                "选择视角："
                "朔也的视角":
                    $ persistent.perspective = "I"
                    jump sakuya_prologue_i
                "绪奈的视角":
                    $ persistent.perspective = "O"
                    jump sakuya_prologue_o
    elif selected_chapter == 2 and persistent.chapters_unlocked >= 2:
        if persistent.perspective == "I":
            jump chapter2_i
        elif persistent.perspective == "O":
            jump chapter2_o
        else:
            $ persistent.perspective = "I"  # 默认I视角
            jump chapter2_i
    elif selected_chapter == 3 and persistent.chapters_unlocked >= 3:
        if persistent.perspective == "I":
            jump chapter3_i
        elif persistent.perspective == "O":
            jump chapter3_o
        else:
            $ persistent.perspective = "I"
            jump chapter3_i
    elif selected_chapter == 4 and persistent.chapters_unlocked >= 4:
        if persistent.perspective == "I":
            jump chapter4_i
        elif persistent.perspective == "O":
            jump chapter4_o
        else:
            $ persistent.perspective = "I"
            jump chapter4_i
    elif selected_chapter == 5 and persistent.chapters_unlocked >= 5:
        if persistent.perspective == "I":
            jump chapter5_i
        elif persistent.perspective == "O":
            jump chapter5_o
        else:
            $ persistent.perspective = "I"
            jump chapter5_i
    elif selected_chapter == 6 and persistent.chapters_unlocked >= 6:
        if persistent.perspective == "I":
            jump chapter6_i
        elif persistent.perspective == "O":
            jump chapter6_o
        else:
            $ persistent.perspective = "I"
            jump chapter6_i
    elif selected_chapter == 7 and persistent.chapters_unlocked >= 7:
        if persistent.perspective == "I":
            jump chapter7_i
        elif persistent.perspective == "O":
            jump chapter7_o
        else:
            $ persistent.perspective = "I"
            jump chapter7_i
    elif selected_chapter == 8 and persistent.chapters_unlocked >= 8:
        if persistent.perspective == "I":
            jump chapter8_i
        elif persistent.perspective == "O":
            jump chapter8_o
        else:
            $ persistent.perspective = "I"
            jump chapter8_i
    elif selected_chapter == 9 and persistent.chapters_unlocked >= 9:
        if persistent.perspective == "I":
            jump chapter9_i
        elif persistent.perspective == "O":
            jump chapter9_o
        else:
            $ persistent.perspective = "I"
            jump chapter9_i
    else:
        # 未解锁或无效章节，返回主菜单
        jump main_menu
# 角色定义
define O = Character("佐佐木绪奈", color="#d843cc")
define I = Character("浅川朔也", color="#20c239")
define C = Character("")
define father = Character("浅川武弘", color="#ddd128")
define wife = Character("加藤美咲", color="#f02f11")
define young_retainer = Character("年轻家臣", color="#161515")
define unknown_child= Character("无名小孩",color="#FFFFFF")
define unknown_woman = Character("无名女子",color="#FFFFFF")
define unknown_man= Character("无名武士",color="#FFFFFF")

# 资源路径
define bgm = "audio/1.mp3"

# 章节解锁
default persistent.chapters_unlocked = 1
default persistent.chapter1_completed = False
default persistent.chapter2_completed = False
default persistent.chapter3_completed = False
default persistent.chapter4_completed = False
default persistent.chapter5_completed = False
default persistent.chapter6_completed = False
default persistent.chapter7_completed = False
default persistent.chapter8_completed = False
default persistent.chapter9_completed = False

# 当前章节
default selected_chapter = 0
