label chapter7_o:
    # 停止现有音频以防止重叠
    stop music fadeout 1.0
    stop sound fadeout 1.0
    $ 婚礼选择1 = ""
    $ 婚礼选择2 = ""
    $ 婚礼选择3 = ""
    $ 婚礼选择4 = ""
    $ 婚礼选择5 = ""
    $ 心碎值 = 0
    $ 愧疚值 = 0
    
    if renpy.loadable("audio/storm_furious.mp3"):
        play music "audio/storm_furious.mp3" fadein 5.0
    else:
        play music "audio/1.mp3" fadein 5.0
    scene black with fade      
    C "（浅川家灯红绸白，热闹却如刀割心。宾客笑语，香炉沉香如锁，压呼吸。）"
    C "（正厅婚礼，我远看，少主羽织袴英挺，却眼空洞，动作如傀儡，无喜。）"
    scene bg wedding:
        zoom 1.6
    with fade
    C "（美咲白无垢端庄，微笑完美，却眼藏怜悯无奈。）"


    # 仪式后的独处时刻
    scene bg tea_room:
        zoom 1.5
    with fade
    
    C "（茶室寂静，宴闹衬压抑。美咲沏茶，我偷看到她动作流畅，茶香掩不住心痛。）"
    show wife silhouette at small_lowered_left4 with dissolve
    show s young formal pained at small_lowered_right4 with dissolve
    wife "（温和）朔也君，请用茶。"
    wife "（停顿）我知道，你心不在这里。听闻绪奈的事。"

    I "（震惊，沉寂）……您知道，何必……"

    wife "（摇头）何必应婚事？"
    wife "（苦笑）朔也君，世事不随心。你不得已，我无可奈何。"
    wife "（抚茶碗）萨摩需联姻，浅川需喘息。我们棋子。"

    menu:
        "「希望他承认」":
            O "（独白）他会承认爱我吗？心痛……"
            I "（坦诚）是。我爱她，至死方休。道歉，加藤小姐。"
            $ 婚礼选择1 = "坦诚"
            $ 心碎值 += 3
            $ 愧疚值 += 2
            
        "「希望他克制」":
            O "（独白）他会保持距离……我懂……"
            I "（克制）过去无需提。尽责任，给尊重。但心死水。"
            $ 婚礼选择1 = "克制"
            $ 心碎值 += 2
            $ 愧疚值 += 1
            
        "「希望他沉默」":
            O "（独白）他沉默……如我心碎……"
            I "（沉默）……"
            $ 婚礼选择1 = "沉默"
            $ 心碎值 += 4
            $ 愧疚值 += 3

    wife "（微笑）不必道歉，无需强迫。我未期待放下。"
    wife "（认真）试了解，给时间。不恩爱，可成盟友，面对风浪。世道苛刻，你我身不由己。"

    menu:
        "「希望他拒绝」":
            O "（独白）他会拒绝……为我……痛……"
            I "（摇头）对不起。心满，容不下。不公平。"
            $ 婚礼选择2 = "拒绝"
            $ 心碎值 += 2
            $ 愧疚值 += 3
            
        "「希望他承诺」":
            O "（独白）他承诺责任……但无爱……我该满足……"
            I "（承诺）尊重您，护您。但爱无法给。"
            $ 婚礼选择2 = "责任"
            $ 心碎值 += 1
            $ 愧疚值 += 2
            
        "「希望他脆弱」":
            O "（独白）他脆弱……为什么这样对我们……"
            I "（哽咽）为什么这样对我们……她没错……"
            $ 婚礼选择2 = "脆弱"
            $ 心碎值 += 4
            $ 愧疚值 += 1

    # 绪奈视角 - 隐藏祝福
    scene bg garden_rain_view:
        zoom 1.4
    with fade
    
    C "（僻角，我藏松树后，和服发白，与华彩刺眼。捂嘴，泪滑，颤抖压哭。）"
    O "（独白）看到了……他婚服好看……如想象……"
    O "（痛楚）但身边不是我……"
    O "（绝望）也好……门当户对……我不再绊脚……"

    C "（攥香囊，樱花瓣，抓回忆。）"

    menu:
        "「流泪祝福」":
            O "（擦泪，难笑）幸福啊，少主……"
            O "（独白）只要他幸福，我无憾。"
            $ 婚礼选择3 = "祝福"
            $ 心碎值 += 3
            
        "「无法承受逃离」":
            O "（转身踉跄）看不下去……心痛……"
            O "（独白）心要裂……"
            $ 婚礼选择3 = "逃离"
            $ 心碎值 += 5
            
        "「不甘怨恨」":
            O "（掐掌）为什么我承受……我们错什么……"
            O "（愧疚）不……这是最好……"
            $ 婚礼选择3 = "怨恨"
            $ 心碎值 += 4

    # 宴会 - 朔也煎熬
    scene bg wedding2:
        zoom 1.7
    with fade
    C "（宴会上，他机械应对，清酒无味。目光飘窗外，飘我方向。）"

    I "（独白）绪奈……你在哪……在哭吗……对不起……"
    I "（独白）祝福如讽刺，婚服枷锁，盛宴刑场……"

    # 父亲警告

    father "（走近，低声）朔也，注意举止。宾客重要。"
    father "（锐利）过去过去。从今，你职责是美咲丈夫，继承人。"

    menu:
        "「看到他顺从」":
            O "（独白）他会顺从……为家族……我该高兴……"
            I "（垂眼）是，父亲。我明白。"
            $ 婚礼选择4 = "顺从"
            $ 心碎值 += 1
            $ 愧疚值 += 1
            jump ending_6
            
        "「看到反抗」":
            O "（独白）他反抗……心好痛……"
            I "（抬眼）职责……我的心呢？"
            father "（冷）武士不私情困。你心属浅川家。"
            $ 婚礼选择4 = "反抗"
            $ 心碎值 += 3
            
        "「看到麻木」":
            O "（独白）他麻木……如我心死……"
            I "（无表情）是。我做好傀儡。"
            $ 婚礼选择4 = "麻木"
            $ 心碎值 += 5

    # 深夜独白
    scene bg corridor_night:
        zoom 1.3
    with fade
    show s young pained at center with move:
        zoom 0.6
    C "（夜深，他站新房外，未进。风吹脸，我想象他痛苦。）"

    I "（取手帕，枯草环）"
    I "（抚摸）‘说好了’……呵呵……食言了……绪奈……对不起……懦夫……"

    menu:
        "「珍藏」":
            O "（独白）他会珍藏……如我碎玉……"
            I "（按心口）不会忘记……永远……"
            $ 婚礼选择5 = "珍藏"
            $ 心碎值 += 3
            
        "「挣扎」":
            O "（独白）他想丢却舍不得……如我心……"
            I "（举手，垂下）连丢勇气都没有……"
            $ 婚礼选择5 = "挣扎"
            $ 心碎值 += 4
            
        "「誓言」":
            O "（独白）他立誓……但无意义……痛……"
            I "（锐利）我誓……终有一日……"
            I "（叹）罢了……无意义……"
            $ 婚礼选择5 = "誓言"
            $ 心碎值 += 5

    # 绪奈心碎
    scene bg small_garden:
        zoom 1.5
    with fade
    C "（鸭川旁的草房，我蜷榻榻米。窗喜庆余音剜心。摊掌，碎玉——破碎象征。）"

    O "（握碎玉，割皮肤，血珠渗，无痛。）"
    O "（喃喃）结束了……他是家主……我是绪奈……"

    C "（取樱花玉簪，看久，没戴，包裹锁箱底，封感情。）"

    # 最终 - 无望黎明
    scene bg corridor_night:
        zoom 1.3
    with fade
    show s young pained at center with move:
        zoom 0.6
    play sound "audio/birds_chirping.mp3" loop volume 0.2 noloop
    C "（黎明天白。他站廊下一夜未眠。望天边，心停昨日。）"

    I "（望天，无光）"
    I "（独白）就这样吧……期望如此……就这样……"
    scene black with fade

    C "（婚礼无赢家。他心死，愧对绪奈，自憎。美咲名分无心，余生如冰。）"
    C "（绪奈角角落舔伤，将爱委屈不甘无声咽下，‘祝福’深爱之人。）"
    C "（浅川荣耀续，危机解，皆得所。只有樱树摇曳，记得誓言，记得夜晚碎心。）"
    C "（从此，他人生分二。白日稳重少主；深夜回忆悔恨囚徒。绪奈名成秘密，触碰伤口，无声挽歌。）"
    C "（命运转动，无人逃。挣扎反抗眼泪哀求，湮灭家族时代，无声叹息。）"

    $ persistent.chapter7_completed = True
    $ persistent.婚礼选择1 = 婚礼选择1
    $ persistent.婚礼选择2 = 婚礼选择2
    $ persistent.婚礼选择3 = 婚礼选择3
    $ persistent.婚礼选择4 = 婚礼选择4
    $ persistent.婚礼选择5 = 婚礼选择5
    $ persistent.心碎值 = 心碎值
    $ persistent.愧疚值 = 愧疚值
    $ persistent.perspective = "O"
    if persistent.chapters_unlocked < 8:
        $ persistent.chapters_unlocked = 8
    call screen chapter_complete(7)

    if 心碎值 >= 10:
        jump ending_6
    else:
        # 正常流程或另一个结局
        return

label ending_6:
    C "（朔也变傀儡，只服从，无感情。）"
    C "（他机械执行，无笑无泪，如行尸。）"
    father "（满意）好儿子，你懂了。"
    I "（空洞）是，父亲。"
    # 未婚妻和家臣密谋片段
    scene bg tea_room:
        zoom 1.5
    with fade    
    show wife silhouette at left with dissolve:
        zoom 0.7
    show young_retainer at small_lowered_right5 with dissolve
    wife "（低声）他碍事。除他，控制浅川家。"
    young_retainer "（点头）是。暗杀启动。"
    wife "（冷笑）他死后，我们掌控。"
    C "（朔也不知，命运定。）"
    $ persistent.endings_unlocked["ending_6"] = True
    $ progress = check_hidden_ending()
    C "（达成结局：任人宰割！当前收集：[progress]/9。）"
    C "(完)"
    stop music fadeout 1.0
    stop sound fadeout 1.0
    call screen chapter_select()
    return