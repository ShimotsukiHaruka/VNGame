label chapter8_i:
    # Stopping existing audio to prevent overlap
    stop music fadeout 1.0
    stop sound fadeout 1.0
    if renpy.loadable("audio/void.mp3"):
        play music "audio/void.mp3" fadein 6.0
    else:
        play music "audio/1.mp3" fadein 6.0
    if renpy.loadable("audio/breath_slow.mp3"):
        play sound "audio/breath_slow.mp3" loop volume 0.2 noloop
    else:
        play sound "audio/1.mp3" loop volume 0.2

    # Scene: My room at dawn, setting the melancholic tone
    scene bg s_room_dawn:
        zoom 1.5
    with fade
    show s middle aged empty at center with dissolve:
        zoom 0.7
    I "十年过去了，我已步入中年，权威无人挑战，可内心却如虚空般空虚。雪还在下，又是多少个冬天了？"
    
    I "我凝视昏暗的天花板，窗外透着黎明的冷光。时间如雪，覆盖一切，却冻结了我的心。"
    I "我的手指在床单上无意识地摩挲，像在寻找什么早已遗失的东西。这些年，我统治着家族，权力如铁，却如虚空般空洞。那些曾经的温暖，如今只剩冰冷的回忆。"

    # Extended flashback sequence with more visual memories
    show expression "#ffffff20" as flash1
    show cg snow_child:
        zoom 1.7
        matrixcolor TintMatrix("#ffddaa") * SaturationMatrix(0.6) * BrightnessMatrix(0.1)
    with fade
    I "儿时的雪地，我与她嬉戏，笑声如铃，回荡在纯白的天地间。那时的我们，无忧无虑，世界仿佛只属于我们两人。"
    hide cg snow_child
    hide flash1
    with dissolve
    show expression "#ffffff20" as flash2
    show cg hairpin:
        zoom 1.5
        matrixcolor TintMatrix("#ffddaa") * SaturationMatrix(0.6) * BrightnessMatrix(0.1)
    with fade
    I "她的发簪，闪着微光，承载了多少未说出口的承诺与温柔的瞬间。我曾许诺守护你一生，却不知命运的残酷。"
    hide cg hairpin
    hide flash2
    with dissolve
    show expression "#ffffff20" as flash3
    show cg broken_pin:
        zoom 1.5
        matrixcolor TintMatrix("#ffddaa") * SaturationMatrix(0.6) * BrightnessMatrix(0.1)
    with fade
    I "断裂的发簪，像我们之间再也无法缝合的裂痕，象征着破碎的梦想。一切都碎了，如这雪地上的足迹，被风雪抹去。"
    hide cg broken_pin
    hide flash3
    with dissolve
    show expression "#ffffff20" as flash4
    show bg garden_spring:
        zoom 1.5
        matrixcolor TintMatrix("#ffddaa") * SaturationMatrix(0.6) * BrightnessMatrix(0.1)
    with fade
    I "年轻时的我们，手牵手在樱花树下，许下永恒的誓言。那些誓言，如今听来如梦如幻，一切皆是无常。"
    hide cg bg garden_spring
    hide flash4
    with dissolve
    I "那些画面，像是别人的故事，早已不痛了。可为什么，心底仍有隐隐作痛？物哀之美，在这转瞬即逝的回忆中悄然绽放。"

    # Transition to the mansion corridor with extended interaction and new choice
    scene bg mansion_corridor_earlyam:
        zoom 1.4
    with fade
    show s middle aged empty at center with moveinright:
        zoom 0.7
    I "我走向书房，步伐沉重如拖着枷锁，每一步都回荡在空荡的走廊中。"
    show young_retainer at small_lowered_right3 with dissolve
    young_retainer "（恭敬）主公，晨安。今日的安排包括与长老的会议，以及处理边境事务。"
    I "我的目光掠过家臣，淡然回应：嗯。"
    I "家臣的话语如风，吹过耳边，却留不下痕迹。"
    young_retainer "（小心翼翼）主公，近来您似乎……有些疲惫，可需召医者？或许一些休息能……"
    menu:
        I "他的话触动了我内心的某处。我该如何回应？"
        "冷淡拒绝，继续前行":
            I "冷淡地打断：不必。退下。"
        "询问关于绪奈的旧事":
            I "停下脚步，低声问：你方才提到绪奈……说吧，究竟是何事？"
            young_retainer "（不安）主公，只是仆人间的一些传言……说她在鸭川生活，孤身一人，似有隐情。"
            I "我心头一震，鸭川？她为何独自在那里？但我压下情绪，冷冷道：够了，退下。"
    young_retainer "（犹豫）主公，关于绪奈小姐的旧事，有仆人提起……"
    I "锐利地喝止：住口！不许再提。"
    hide young_retainer with dissolve
    I "家臣低头退去，我的眼神空洞，仿佛连愤怒都已无力。我继续前行，脑海中回荡着过去的片段，一切皆是无常的悲哀。"

    # New scene: In the archive room, reflecting on my legacy with more depth and choice
    scene bg archive_room_dim:
        zoom 1.4
    with fade
    I "书房旁的档案室，堆满了家族的卷宗，尘埃在微光中飞舞，如时间的灰烬。这些纸张，记载了胜利、权谋、牺牲……却没有我的心。家族的荣耀，是以多少鲜血换来？"
    I "我翻开一卷泛黄的贺年状，字迹熟悉却陌生，每一页都承载着历史的重量。"
    show cg old_letter:
        zoom 1.4
    with dissolve
    I "上面是她的笔迹，字里行间是当年的温柔与期盼，诉说着对未来的憧憬。我曾以为，守护这一切是为了你。可如今，你在哪里？这些荣耀，又有何用？"
    menu:
        I "我手中握着这封信，心绪翻涌。我该如何面对这些回忆？"
        "继续翻阅，寻找更多线索":
            I "我继续翻阅卷宗，试图找到更多关于她的痕迹。几页之后，一张旧画映入眼帘，是我们年少时的合影，笑容纯净如雪。"
            show cg old_painting:
                zoom 1.4
            with dissolve
            I "我凝视画中的她，心如刀绞。这份美好，为何如此短暂？"
            hide cg old_painting with dissolve
        "将信烧毁，埋葬过去":
            I "我点燃一盏油灯，想将信纸投入火焰。却终究是舍不得，又将点燃的油灯熄灭了。"
    hide cg old_letter with dissolve
    I "我慢慢地将书信放回，动作轻得像怕惊扰了尘封的记忆。尘埃落定，室中更显寂寥。或许，我确实该烧掉这一切，让过去随风而去，一切归于虚空。"

    # Extended scene: The small garden with Ona, deeper conversation and choice
    scene bg small_garden:
        zoom 1.5
        matrixcolor TintMatrix("#ffddaa") * SaturationMatrix(0.6) * BrightnessMatrix(0.1)
    with fade
    show o middle aged back:
        zoom 0.55
        matrixcolor TintMatrix("#ffddaa") * SaturationMatrix(0.6) * BrightnessMatrix(0.1)
        xalign 0.8
        yalign 0.2
    with dissolve
    I "绪奈在鸭川的草房中，岁月磨平了她的悲伤，她的目光如枯井般平静。她抬头望向我们家的屋脊，平静无波。"
    I "她手中空无一物，过去的碎片早已遗失，只剩空荡的双手。她低语：主公，您还在追逐什么？权力？荣耀？还是那遥不可及的救赎？"
    I "她转过身，目光穿过园中的枯枝，似在寻找答案。风吹起她的衣角，带着一丝凄凉。"
    show s middle aged empty at left:
        zoom 0.7
        matrixcolor TintMatrix("#ffddaa") * SaturationMatrix(0.6) * BrightnessMatrix(0.1)
    with moveinleft
    I "我不知何时出现在草房中，我们的目光短暂交汇，如陌生人般疏离。她看我的眼神，像在看一个陌生人。那些年的羁绊，如今何在？"
    I "低沉地问：绪奈，这些年……你可曾怨我？怨我没能守护你？"
    O "（平静）怨？早已忘了如何怨恨。主公，您呢？您可曾怨恨自己？那些选择，是您亲手做出的。"
    I "痛苦地回应：我……我以为那是正确的。可如今，一切都空了。"
    O "（叹息）空了也好。至少，不会再痛。"
    menu:
        I "我沉默，喉咙哽咽，想说些什么。她的身影如此遥远，我该如何回应？"
        "诉说内心的悔恨":
            I "绪奈，我后悔了。那些年，我选择了权力，却失去了你。我的错，毁了一切。"
            O "（轻声）主公，悔恨无用。时间如流水，逝去不返。"
            I "我低头，枯叶飘落，心中的悲哀更深。悲哀啊，这无常的命运。"
        "默默转身，离开草房":
            I "我无法回答，转身离去。她的身影在风中渐远，如同我无法触及的过去。"
    play sound "audio/thunder_distant.mp3" loop volume 0.5 noloop
    C "随着一声惊雷，我被猛地惊醒，又是一场噩梦..."
    hide o middle aged back with dissolve
    hide s middle aged empty with dissolve

    # New scene: Visiting the ancestral shrine with extended reflection and choice
    scene bg ancestral_shrine:
        zoom 1.4
    with fade
    I "祠堂内，我点燃一炷香，青烟袅袅，升腾向未知的虚空。祖先的牌位，冷冷注视着我。他们的荣耀，我的负担。我继承了权力，却遗失了灵魂。"
    I "我跪下，额头触地，似在祈求，又似在忏悔。香烟缭绕，模糊了我的视线。我赢得了所有，却输给了自己。父亲的阴影，始终笼罩着我。"
    I "香灰落下，寂静中只有我的呼吸声，急促而沉重。或许，该是结束的时候了。家族的诅咒，该由我来终结，一切归于寂静的悲美。"
    menu:
        I "我起身，凝视祖先的牌位。内心挣扎，我该如何面对家族的过去？"
        "向祖先祈求宽恕":
            I "我低声祈祷：祖先啊，若我有罪，请宽恕我。我只想结束这无尽的痛苦。"
            I "青烟袅袅，仿佛回应，却又无声。这无常的世界，无人能解。"
        "诅咒家族的命运":
            I "我怒视牌位，低吼：这家族的荣耀，不过是诅咒！为何要我背负这一切？"
            I "我的声音在祠堂中回荡，却无人应答，只有寂静的悲哀。"

    # Scene: My study at midnight, leading to the discovery
    scene bg s_study_late:
        zoom 1.4
    with fade
    I "深夜，我独坐，抚摸抽屉中的木盒，盒子表面布满灰尘。里面是什么？早已忘了。或许，是最后的秘密。"
    I "我犹豫片刻，终于打开木盒，里面不是玉佩，而是一封泛黄的信，密封多年。"
    show cg sealed_letter:
        zoom 1.4
    with dissolve
    I "这是……绪奈的字迹？为什么在这里？"
    hide cg sealed_letter with dissolve

    # Branching point: Choice leading to two endings
    menu:
        I "我盯着信封，心跳加速。我该何去何从？"
        "打开信件，面对真相":
            jump ending_3
        "忽略信件，沉浸虚空":
            jump ending_4

label ending_3:
    # Ending 1: Discover the letter, reveal truth, rage, patricide, seppuku
    scene bg s_study_late:
        zoom 1.4
    with fade
    show s middle aged empty at center:
        zoom 0.7
    I "我颤抖着拆开信封，展开信纸，字迹娟秀却带着悲伤。一切皆是无常的悲哀。"
    show cg letter_content:
        zoom 1.4
    with dissolve
    I "信的内容缓缓展开："
    I "亲爱的朔也："
    I "当你读到这封信时，我已远去。请原谅我的不辞而别，但这是迫不得已的选择。"
    I "真相是残酷的：你的父亲，家主，用我的家族作为威胁，逼迫我屈从。他……他强奸了我，那一夜的耻辱，如刀割般永难忘怀。那黑暗的房间，粗暴的触碰，撕裂了我的灵魂，一切的美在那一刻凋零。"
    I "我本想告诉你一切，但恐惧让我沉默。我对你的爱，从未改变。那份遗憾，如影随形。我爱慕你，从儿时起，直至如今。那些雪中的嬉戏，樱花下的誓言，皆是永恒的温柔，却被命运的无常所吞噬。"
    I "可一切已无法挽回。我去了鸭川，那里或许有宁静。请不要找我，让我独自承载这份痛苦。让这物哀的离别，成为我们最后的回忆。"
    I "永别了，我的爱人。绪奈。"
    hide cg letter_content with dissolve
    I "我读完信，脸色煞白，继而转为赤红。愤怒如火山爆发，父亲……他竟做出这种事！一切的罪魁祸首，是他！这无常的世界，竟藏着如此丑恶。"
    I "我冲出书房，直奔父亲的寝室，盛怒之中，手持烛台闯入。"
    scene bg study_night2:
        zoom 1.4
        matrixcolor TintMatrix("#eb0909") * SaturationMatrix(0.6) * BrightnessMatrix(0.1)
    with fade
    father "（惊醒）朔也，你……"
    I "我在怒火中失控，烛台砸下，无意中击中要害，父亲倒地不起。鲜血染红地面，我跪地，悔恨涌上心头。我……我杀了父亲？这不是我的本意！可这悲剧，已成定局。"
    I "为了赎罪，只有这一途。我拔出短刀，切腹自尽。刀刃划过腹部，疼痛如潮水涌来，我感觉到自己的肠子滑出腹腔，那温热的、滑腻的感觉，像生命的无常在指间流逝。鲜血涌出，染红了地板，一切渐趋黑暗。物哀啊，这转瞬即逝的人生。"
    stop music fadeout 12.0
    stop sound fadeout 8.0
    scene black with fade
    I "绪奈，下辈子我们会再重逢的..."
    $ persistent.endings_unlocked["ending_3"] = True
    $ progress = check_hidden_ending()
    C "达成结局：切腹谢罪！当前收集：[progress]/9"
    C "（完）"
    stop music fadeout 1.0
    stop sound fadeout 1.0
    call screen chapter_select()
    return
    $ persistent.chapter8_completed = True
    $ persistent.perspective = "I"
    if persistent.chapters_unlocked < 9:
        $ persistent.chapters_unlocked = 9
    call screen chapter_complete(8)
    return

label ending_4:
    # Ending 2: No discovery, betrayal by servants and wife, dies in fire, recalls Ona
    scene bg s_study_late:
        zoom 1.4
    with fade
    show s middle aged empty at center:
        zoom 0.7
    I "我将信放回抽屉，未曾打开，选择了遗忘。何必再搅动过去的尘埃？让它尘封吧。这世界的一切，皆是无常。"
    I "我离开书房，走向寝室，却不知危机已近。"
    scene bg mansion_corridor_earlyam:
        zoom 1.4
        matrixcolor TintMatrix("#423f3f") * SaturationMatrix(0.6) * BrightnessMatrix(0.1)
    with fade
    C "家仆与妻子密谋已久，他们的陷害如网般张开。"
    show young_retainer at small_lowered_right3 with dissolve
    wife "（低声）今夜行动，主公的末日到了。"
    young_retainer"（点头）火已备好，一切将化为灰烬。"
    hide servant_conspirator
    with dissolve
    scene bg s_room_fire:
        zoom 1.6
        matrixcolor TintMatrix("#eb0909") * SaturationMatrix(0.6) * BrightnessMatrix(0.1)
    with fade
    I "火起，我惊醒，四周已被火焰包围。热浪扑面，皮肤灼痛如针刺，烟雾呛入肺中，咳嗽不止。这火焰吞噬一切，如命运的无常将我包围。"
    I "我试图逃脱，却被锁住，火焰舔舐着我的衣袍，疼痛如潮，肉体在火中熔化。在死前，脑海中浮现绪奈的模样。那温柔的笑容，无尽凄凉涌上心头。物哀啊，这人生如樱花，盛开后即凋零。"
    I "我倒下，火海中，一切归于虚空。灼热的痛苦渐趋麻木，只剩回忆的悲美。"
    stop music fadeout 12.0
    stop sound fadeout 8.0
    scene black with fade
    I "要死了吗？"
    I "绪奈，对不起...我是个骗子。"
    $ persistent.endings_unlocked["ending_4"] = True
    $ progress = check_hidden_ending()
    C "达成结局：葬身火海！当前收集：[progress]/9"
    C "（完）"
    stop music fadeout 1.0
    stop sound fadeout 1.0
    call screen chapter_select()
    $ persistent.chapter8_completed = True
    $ persistent.perspective = "I"
    if persistent.chapters_unlocked < 9:
        $ persistent.chapters_unlocked = 9
    return