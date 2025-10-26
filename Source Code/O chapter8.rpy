label chapter8_o:
    # Stopping existing audio to prevent overlap
    stop music fadeout 1.0
    stop sound fadeout 1.0
    if renpy.loadable("audio/void.mp3"):
        play music "audio/void.mp3" fadein 6.0
    else:
        play music "audio/1.mp3" fadein 6.0
    if renpy.loadable("audio/river_flow.mp3"):
        play sound "audio/river_flow.mp3" loop volume 0.2 loop
    else:
        play sound "audio/1.mp3" loop volume 0.2

    # Scene: Ona’s life in Kamogawa, by the river at dusk
    scene bg kamogawa_river_dusk:
        zoom 1.5
    with fade
    O "十年了，我在鸭川的草房中，独自面对这无尽的寂静。河水流淌，映着暮色的微光，像在诉说无常的悲哀。"
    show o middle aged back at center with dissolve:
        zoom 0.5
    O "我凝视河面，风吹过，水波轻荡，仿佛带走了我的泪水。朔也，我的爱人，你如今在哪里？"
    O "离开浅川家后，我来到这里，试图逃避那不堪的过去。却发现，记忆如影随形，永不消散。"

    # Flashback: Memories of Sayo and the past
    show expression "#ffffff20" as flash1
    show cg snow_child:
        zoom 1.7
        matrixcolor TintMatrix("#ffddaa") * SaturationMatrix(0.6) * BrightnessMatrix(0.1)
    with fade
    O "我记得儿时的雪地，我们嬉戏，笑声如铃。那时的你，眼中只有纯净的光，世界属于我们两人。"
    hide cg snow_child
    hide flash1
    with dissolve
    show expression "#ffffff20" as flash2
    show cg hairpin:
        zoom 1.5
        matrixcolor TintMatrix("#ffddaa") * SaturationMatrix(0.6) * BrightnessMatrix(0.1)
    with fade
    O "那枚发簪，你送我的信物，承载着未说出口的誓言。我曾以为，你会守护我一生，可命运如此无情。"
    hide cg hairpin
    hide flash2
    with dissolve
    O "家主的威胁，如刀悬在心头。他用我的家族逼我屈从，那一夜的耻辱，撕裂了我的灵魂。黑暗的房间，粗暴的触碰，如刀割般永难忘怀。"
    O "我无法告诉你真相，恐惧让我沉默。我的爱从未改变，却只能带着遗憾逃离。如今，这物哀的离别，成了我心中永恒的痛。"

    # Scene: Ona’s daily life in Kamogawa
    scene bg small_garden:
        zoom 1.5
    with fade
    show o middle aged back at center with dissolve:
        zoom 0.5
    O "我的草房简陋，窗外是鸭川的流水，屋内只有孤寂相伴。我日复一日，纺布、烧饭，生活如水般平静，却也如水般空虚。"
    O "有时，我会凝视河边的樱树，想起我们在樱花下的誓言。那些美好，如花瓣飘落，转瞬即逝。"
    menu:
        O "我手中握着旧日的发簪，心绪翻涌。我该如何面对这些回忆？"
        "将发簪藏起，试图忘却":
            O "我将发簪藏进木盒，试图埋葬过去。可每当夜深，那份思念仍如潮水涌来。物哀啊，这心痛无处可逃。"
        "佩戴发簪，怀念过去":
            O "我将发簪别在发间，感受它的冰凉。你的影子仿佛就在身旁，却永远遥不可及。这无常的命运，令人心碎。"
            show cg hairpin:
                zoom 1.5
            with dissolve
            O "我低头，泪水滑落，发簪闪着微光，如同你未曾离去。"
            hide cg hairpin with dissolve

    # Scene: Rumors of Sayo’s fate reach Kamogawa
    scene bg kamogawa_village:
        zoom 1.5
    with fade
    show o middle aged back at center with dissolve:
        zoom 0.5
    O "村中传来传言，关于浅川家的变故。有人说你已不在人世，有人说你被背叛，有人说你亲手结束了家族的诅咒。"
    O "我站在河边，风吹过，带来冰冷的寒意。我不知真相，只知心如刀绞。朔也，你是否真的已离去？"
    menu:
        O "这些传言，如风中落叶，扰乱我的心。我该如何面对？"
        "追寻真相，询问旅人":
            O "我找到一个路过的旅人，询问浅川家的消息。他低声说：主公已死，或自尽，或葬身火海，无人知晓详情。"
            O "我愣住，心如死灰。你的死讯，如刀刺入胸膛。这无常的世界，为何如此残酷？"
            $ heard_sayo_death = True
        "拒绝相信，继续等待":
            O "我不愿相信这些传言。你或许还在某处，活着，守护着你的荣耀。我选择等待，哪怕希望渺茫。"
            $ heard_sayo_death = False

    # Branching point: Ona’s response to Sayo’s fate
    if heard_sayo_death:
        O "你的死讯，如樱花凋零，美丽却令人心碎。我该如何继续这无意义的人生？"
        jump ona_ending_choice
    else:
        O "我选择相信你还活着，某天会出现在鸭川的河边。我继续我的生活，平静却空虚，带着对你的思念。"
        jump ending_7

label ona_ending_choice:
    # Scene: Ona decides her fate after hearing of Sayo’s death
    scene bg kamogawa_river_night:
        zoom 1.6
    with fade
    O "夜色笼罩鸭川，河水在月光下泛着冷光。我站在岸边，心如死灰。朔也，你已不在，我的世界也随之崩塌。"
    menu:
        O "我该何去何从？"
        "投入鸭川，与你同生共死":
            jump ending_8
        "返回浅川家，寻求复仇":
            jump ending_9

label ending_8:
    # Ending 1: Ona throws herself into the Kamogawa River
    scene bg kamogawa_river_night:
        zoom 1.6
        matrixcolor TintMatrix("#eb0909") * SaturationMatrix(0.6) * BrightnessMatrix(0.1)
    with fade
    O "我凝视河面，水波如你的眼神，温柔却遥远。朔也，若你已不在，我又何必独活？"
    O "我解开发簪，让它落入河中，随波而去。风吹过，带着我的泪水。这物哀的人生，终将归于寂静。"
    O "我一步步走进冰冷的河水，水流拥抱我，如同你的怀抱。寒意渗入骨髓，我闭上眼，脑海中是你最后的身影。"
    scene black with fade
    O "朔也，我们终于重逢了……"
    stop music fadeout 12.0
    stop sound fadeout 8.0
    O "河水吞噬一切，我的身躯沉入黑暗。这无常的命运，终究将我们连结。"
    $ persistent.endings_unlocked["ending_8"] = True
    $ progress = check_hidden_ending()
    C "达成结局：同生共死！当前收集：[progress]/9"
    C "(完)"
    stop music fadeout 1.0
    stop sound fadeout 1.0
    call screen chapter_select()
    return

label ending_9:
    # Ending 2: Ona returns to Asakawa for revenge, executed by samurai
    scene bg asakawa_gate_night:
        zoom 1.4
        matrixcolor TintMatrix("#eb0909") * SaturationMatrix(0.6) * BrightnessMatrix(0.1)
    with fade
    O "我回到浅川家，夜色中，宅邸如鬼魅般沉默。我要为你的死讨个公道，那些背叛你的人，须付出代价。"
    O "我潜入府中，手握短刀，心中的怒火掩盖了恐惧。物哀啊，这复仇之路，注定无果。"
    show samurai at right with dissolve:
        zoom 0.7
        matrixcolor TintMatrix("#eb0909") * SaturationMatrix(0.6) * BrightnessMatrix(0.1)
    O "卫兵发现了我，他们的刀光如月，冷酷无情。我试图反抗，却无力回天。"
    O "刀刃划过我的颈项，疼痛短暂却刺骨。鲜血喷涌，我倒下，脑海中是你年少的笑颜。"
    hide samurai with dissolve
    scene black with fade
    O "朔也，我的复仇失败了……可我无悔，至少，我为你而战。"
    stop music fadeout 12.0
    stop sound fadeout 8.0
    O "我的血染红了浅川家的石阶，这无常的结局，带着悲美的终结。"
    $ persistent.endings_unlocked["ending_9"] = True
    $ progress = check_hidden_ending()
    C "达成结局：血染故地！当前收集：[progress]/9"
    C "(完)"
    stop music fadeout 1.0
    stop sound fadeout 1.0
    call screen chapter_select()
    return

label ending_7:
    # Ending 3: Ona lives quietly, never marries, honors Sayo
    scene bg small_garden:
        zoom 1.5
    with fade
    show o middle aged back at center with dissolve:
        zoom 0.5
    O "我选择相信你还活着，某天会出现在河边。我继续在鸭川生活，平静如水，却也空虚如水。"
    O "公公的孩子，我视如己出。我教他你的名字，讲你的英勇事迹，让他以你为父。他的眼中，有你的影子。"
    show cg child_listening:
        zoom 1.5
    with dissolve
    O "我对他诉说你的故事：雪中的嬉戏，樱花下的誓言。他笑着听，像是你从未离开。"
    hide cg child_listening with dissolve
    scene bg yoshino_cherry_festival:
        zoom 1.5
    with fade
    O "每年春日，我去吉野的樱花祭，站在花海中，等待那个永不出现的你。樱花飘落，如我的思念，美丽却短暂。"
    O "年复一年，我的发丝渐白，身体日衰。可我从未嫁人，我的心，只属于你。"
    show cg old_ona_cherry:
        zoom 1.5
    with dissolve
    O "最后一年的樱花祭，我坐在树下，风吹落花瓣，覆满我的衣襟。我闭上眼，感受这物哀的终结。"
    hide cg old_ona_cherry with dissolve
    scene black with fade
    O "朔也，我等了一生，未曾后悔。若有来世，愿我们再续樱花下的誓言。"
    stop music fadeout 12.0
    stop sound fadeout 8.0
    O "我的生命如樱花，凋零在寂静中，带着对你的永恒思念。"
    $ persistent.endings_unlocked["ending_7"] = True
    $ progress = check_hidden_ending()
    C "达成结局：百年忘花！当前收集：[progress]/9"
    C "（完）"
    stop music fadeout 1.0
    stop sound fadeout 1.0
    call screen chapter_select()
    return
