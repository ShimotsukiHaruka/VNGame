label chapter9_o:
    # 停止现有音频以防止重叠
    stop music fadeout 1.0
    stop sound fadeout 1.0
    if renpy.loadable("audio/time_passing.mp3"):
        play music "audio/time_passing.mp3" fadein 20.0
    else:
        play music "audio/1.mp3" fadein 10.0
    if renpy.loadable("audio/birds_chirping.mp3"):
        play sound "audio/birds_chirping.mp3" loop volume 0.4 channel "sound1"
    else:
        play sound "audio/1.mp3" loop volume 0.4 channel "sound1"
    if renpy.loadable("audio/wind_gentle.mp3"):
        play sound "audio/wind_gentle.mp3" loop volume 0.3 channel "sound2"
    else:
        play sound "audio/1.mp3" loop volume 0.3 channel "sound2"
    scene bg garden_spring: 
        zoom 1.3
    with fade
    C "（岁月流逝，浅川家几经变迁，故事湮没）"
    show bg old_cherry_tree: 
        zoom 0.5
    with dissolve
    C "（老樱树依旧伫立，花开如云，瓣落如雪）"
    show cherry_blossom_fall: 
        zoom 0.6
    with dissolve
    C "（树下，孩童嬉笑，武士与女眷驻足，无人知晓旧事）"
    unknown_child "（欢笑）好多花！"
    unknown_woman "（轻声）真美，年年如此。"
    unknown_man "（点头）是啊，永恒不变。"
    show bg garden_spring_wide: 
        zoom 1.3
    with dissolve
    C "（雪中相遇、信物之约、风雨决裂，皆成尘土）"
    show bg garden_spring_wide: 
        zoom 1.3
    with dissolve
    C "（爱与憾，归于春泥，了无痕迹）"
    scene black with fade
    C "（美是真实，凋零必然，遗忘绝对。这便是花忘。）"
    stop sound fadeout 10.0 channel "sound1"
    stop sound fadeout 10.0 channel "sound2"
    stop music fadeout 15.0
    $ persistent.perspective = "O"
    $ persistent.chapter8_completed = True
    if persistent.chapters_unlocked < 9:
        $ persistent.chapters_unlocked = 9
    
    call easter_egg from _call_easter_egg
    
    return