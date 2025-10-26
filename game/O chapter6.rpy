label chapter6_o:
    # 停止现有音频以防止重叠
    stop music fadeout 1.0
    stop sound fadeout 1.0
    $ 断簪选择1 = ""
    $ 断簪选择2 = ""
    $ 断簪选择3 = ""
    $ 决绝值 = 0
    $ 误解值 = 0
    $ 婚礼选择1 = ""
    $ 婚礼选择2 = ""
    $ 婚礼选择3 = ""
    $ 婚礼选择4 = ""
    $ 婚礼选择5 = ""
    $ 心碎值 = 0
    $ 愧疚值 = 0

    if renpy.loadable("audio/memory_dull.mp3"):
        play music "audio/memory_dull.mp3" fadein 4.0
    else:
        play music "audio/1.mp3" fadein 4.0
    scene bg garden_rain_view:
        zoom 1.4
    with fade
    
    C "（暴雨倾盆，风吼雷鸣，世界要崩塌。闪电撕夜，照宅邸孤影，雷震人心。我靠门滑落，捂嘴，泪混雨。）"
    C "（他从惩戒逃，背伤雨浸，该痛，但他心痛更甚。只想带我走，立刻！）"
    I "（拍门，颤抖）绪奈！开门！我知道你在！绪奈！"
    I "（哀求）求你……开门……跟我走！现在！"

    O "（靠门，滑落，泪涌）不行……不能开……开了毁他……必须忍……"

    C "（闪电惨白，炸雷爆！轰隆——！我惊叫，漆盒落地。）"
    play sound "audio/object_drop.mp3" volume 0.8 noloop
    C "（盒盖弹，樱花玉簪滚出，哀鸣。）"

    menu:
        "「怕他担心」":
            O "（心慌）少主会担心……但不能开……"
            I "（急）绪奈！你怎么了？！没事吧？！"
            I "（撞门）让我进去！"
            $ 断簪选择1 = "焦急"
            $ 误解值 += 1
            
        "「预感结束」":
            O "（泪流）这声……像我们的结束……"
            I "（心沉）……绪奈，那是什么声？"
            $ 断簪选择1 = "不祥"
            $ 误解值 += 2
            
        "「让他误解」":
            O "（咬唇）让他以为我拒绝……恨我吧……"
            I "（冷声）……你的回答吗？"
            $ 断簪选择1 = "误解"
            $ 误解值 += 3

    C "（我颤抖拾簪，裂痕如心碎。想：碎了好……让他死心……恨我，好过毁他。）"

    O "（内心，平静）碎了……就好……像我们……"

    # 添加被强奸桥段
    C "（回忆涌上：前夜，家主召我去书房。）"
    scene bg study_night2: 
        zoom 1.3
        matrixcolor TintMatrix("#ffddaa") * SaturationMatrix(0.6) * BrightnessMatrix(0.1)
    with dissolve
    show father angry at center with dissolve:
        zoom 0.8
        matrixcolor TintMatrix("#ffddaa") * SaturationMatrix(0.6) * BrightnessMatrix(0.1)
    father "（冷笑）你以为能攀上我儿？贱婢！"
    C "（他扑上，我挣扎无用，痛如撕裂。事后，他威胁：说服朔也结婚，否则杀我，毁名誉。）"
    O "（泪涌，体痛心碎）为什么……为什么这样对我……为了少主，我必须离开……隐瞒一切……"
    father "（低沉）若不让他死心，你全家死！"
    O "（内心）不能让少主知……他会毁一切……我必须演戏……让他恨我……"
    scene bg garden_rain_view: 
        zoom 1.3
    with dissolve

    C "（我拉开门闩，风风雨扑，两人对视，他见我苍白。）"
    scene bg garden_rain_view2:
        zoom 1.6
    with fade
    I "（上前）绪奈！我……"
    O "（举裂簪，冷声）少主有何贵干？"

    menu:
        "「怕他急切」":
            O "（心痛）别急……但必须冷……"
            I "（急）带你走！去京都，任何地方！"
            I "（伸手）现在走！"
            $ 断簪选择2 = "急切"
            $ 决绝值 += 1
            
        "「见他刺痛」":
            O "（泪忍）他的痛……比我多……"
            I "（刺伤）少主？绪奈，你……那簪子……"
            $ 断簪选择2 = "刺痛"
            $ 决绝值 += 2
            
        "「担心他看穿」":
            O "（慌）别察觉……我怕……"
            I "（观察）绪奈，告诉我，发生了什么？有人威胁你？"
            $ 断簪选择2 = "冷静"
            $ 决绝值 += 0

    O "（冷笑）约定？少主说那些玩笑做什么？"
    O "（递簪）这个，还您。您的玩物，我不配。别再说困扰的话。"

    C "（‘玩物’刺他心。他后退，脸无血色。）"

    I "（破碎）玩物？我们……在你眼里只是……"
    O "（忍痛，冷刻）不然呢？家臣女敢攀家主？那些逢场作戏，只有您当真。"

    menu:
        "「怕他崩溃」":
            O "（心碎）别这样……但必须让他信……"
            I "（低吼）我不信！看着我说！说你没爱过我！"
            $ 断簪选择3 = "崩溃"
            $ 误解值 += 3
            $ 决绝值 += 2
            
        "「见他心死」":
            O "（泪涌）他的光灭了……我成功了……却痛死……"
            I "（松手）……明白了。"
            I "（叹）打扰了。"
            $ 断簪选择3 = "心死"
            $ 误解值 += 5
            $ 决绝值 += 4
            
        "「恐他看穿」":
            O "（急断）不能让他知……否则他会毁家……"
            I "（看灵魂）绪奈……何必……我知道你不是……"
            O "（急）我就是这样！请死心！"
            $ 断簪选择3 = "看穿"
            $ 误解值 -= 2
            $ 决绝值 += 1

    C "（他目光落裂簪，指尖碰裂痕，像在摸我痛。）"

    I "（收回，转身，疲惫）……保重。"
    C "（他走入雨，背影踉跄，被雨吞。）"

    O "（身影消失，我瘫地，攥簪，血混雨，无痛。）"
    O "（痛哭，被雷盖）对不起……对不起……朔也……只有这样……你才能活……"

    scene black with fade

    C "（那一夜后，他心中部分死。沉默，顺从，接受婚礼。）"
    C "（我封闭。裂簪锁箱底，埋心和爱。）"
    C "（断簪断情。美好断绝，双向牺牲成误解错过。）"
    C "（多年后，他知雨夜真相，一切无法挽回。断簪成痛，提醒爱过错过。）"
    
    scene bg tea_room:
        zoom 1.5
    with fade

    C "（茶室香炉袅袅，气氛沉重）"
    show wife silhouette at small_lowered_left2 with dissolve
    show s young formal pained at small_lowered_right2 with dissolve
    wife "（温和）朔也君，我知你心属，但联姻责任。"
    I "（叹）明白，但心无法违。"
    wife "（微笑）慢慢了解，给时间机会。"
    stop music fadeout 6.0

    $ persistent.chapter6_completed = True
    $ persistent.perspective = "O"
    if persistent.chapters_unlocked < 7:
        $ persistent.chapters_unlocked = 7
    call screen chapter_complete(6)
    return