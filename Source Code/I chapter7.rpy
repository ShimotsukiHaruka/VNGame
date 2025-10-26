label chapter7_i:
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
    C "（浅川家张灯结彩，红绸白幔交织，热闹却压抑。宾客华服笑语，但香炉沉香如枷锁，缠绕呼吸。）"
    C "（正厅婚礼进行，朔也纹付羽织袴英挺，却眼空洞，动作机械如木偶，无喜悦。）"
    scene bg wedding:
        zoom 1.6
    with fade
    C "（美咲白无垢端庄，微笑完美，却眼藏怜悯无奈。）"


    # 仪式后的独处时刻
    scene bg tea_room:
        zoom 1.5
    with fade
    
    C "（茶室寂静，宴会喧闹更显压抑。美咲沏茶，动作流畅，茶香化不开冰。）"
    show wife silhouette at small_lowered_left4 with dissolve
    show s young formal pained at small_lowered_right4 with dissolve
    wife "（推茶碗，温和）朔也君，请用茶。"
    wife "（停顿，低垂目光）我知道，你心不在这里。听闻绪奈小姐的事。"

    I "（抬头震惊，随即沉寂）……您知道，何必……"

    wife "（摇头）何必应婚事？"
    wife "（苦笑）朔也君，世事不随心。你有不得已，我亦无可奈何。"
    wife "（抚茶碗）萨摩需联姻巩固，浅川需结合喘息。我们是棋子。"

    menu:
        "「承认爱绪奈」":
            I "（闭眼，坦诚痛）是。我爱她，至死方休。道歉，加藤小姐。"
            $ 婚礼选择1 = "坦诚"
            $ 心碎值 += 3
            $ 愧疚值 += 2
            
        "「保持距离」":
            I "（避目光，克制）过去事无需提。尽丈夫责任，给尊重。但心如死水。"
            $ 婚礼选择1 = "克制"
            $ 心碎值 += 2
            $ 愧疚值 += 1
            
        "「沉默」":
            I "（沉默，盯茶影）……"
            $ 婚礼选择1 = "沉默"
            $ 心碎值 += 4
            $ 愧疚值 += 3

    wife "（微笑）不必道歉，无需强迫。我未期待立刻放下。"
    wife "（认真）试了解，给时间。即使不恩爱，可成盟友，面对风浪。世道苛刻，你我身不由己。"

    menu:
        "「拒绝」":
            I "（摇头）对不起。您好，但我心满，容不下旁人。不公平。"
            $ 婚礼选择2 = "拒绝"
            $ 心碎值 += 2
            $ 愧疚值 += 3
            
        "「承诺责任」":
            I "（承诺）尊重您，护您，尽所能。但爱无法给。"
            $ 婚礼选择2 = "责任"
            $ 心碎值 += 1
            $ 愧疚值 += 2
            
        "「脆弱」":
            I "（哽咽）为什么这样对我们……她没错……"
            $ 婚礼选择2 = "脆弱"
            $ 心碎值 += 4
            $ 愧疚值 += 1

    # 绪奈视角 - 隐藏祝福
    scene bg garden_rain_view:
        zoom 1.4
    with fade
    
    C "（僻角，绪奈藏松树后，和服发白，与华彩对比刺眼。捂嘴，泪滑落，颤抖压哭泣。）"
    O "（独白）看到了……他婚服好看……如想象……"
    O "（痛楚）但身边不是我……"
    O "（绝望）也好……门当户对……我不再绊脚石……"

    C "（攥香囊，樱花瓣，抓回忆。）"

    menu:
        "「祝福」":
            O "（擦泪，难看笑）幸福啊，少主……不，朔也大人……"
            O "（独白）只要他幸福，我无憾。"
            $ 婚礼选择3 = "祝福"
            $ 心碎值 += 3
            
        "「逃离」":
            O "（转身踉跄）看不下去……心痛……"
            O "（独白）心要裂开……"
            $ 婚礼选择3 = "逃离"
            $ 心碎值 += 5
            
        "「怨恨」":
            O "（掐掌）为什么我承受……我们错什么……"
            O "（愧疚淹没）不……这是最好……"
            $ 婚礼选择3 = "怨恨"
            $ 心碎值 += 4

    # 宴会 - 朔也煎熬
    scene bg wedding2:
        zoom 1.7
    with fade
    C "（宴会上，我机械应对祝福，清酒无味。目光飘窗外，飘她方向。）"

    I "（独白，醉朦）绪奈……你在哪……在哭吗……对不起……"
    I "（独白）祝福如讽刺，婚服枷锁，盛宴刑场……"

    # 父亲警告
    father "（走近，低声）朔也，注意举止。宾客重要。"
    father "（锐利）过去过去。从今，你职责是美咲丈夫，继承人。"

    menu:
        "「点头」":
            I "（垂眼）是，父亲。我明白。"
            $ 婚礼选择4 = "顺从"
            $ 心碎值 += 1
            $ 愧疚值 += 1
            jump ending_2
            
        "「反抗」":
            I "（抬眼，血丝）职责……我的心呢？"
            father "（冷）武士不被私情困。你心属浅川家。"
            $ 婚礼选择4 = "反抗"
            $ 心碎值 += 3
            
        "「麻木」":
            I "（无表情）是。我做好傀儡。"
            $ 婚礼选择4 = "麻木"
            $ 心碎值 += 5

    # 深夜独白
    scene bg corridor_night:
        zoom 1.3
    with fade
    show s young pained at center with move:
        zoom 0.8
    C "（宴散，夜深。我站在新房外，未进。风吹脸，却吹不散苦闷。望冷月，像唯一懂我痛的存在。）"

    I "（取手帕，枯樱花草环）"
    I "（抚摸，沙哑）‘说好了’……呵呵……食言了……绪奈……对不起……懦夫……"

    menu:
        "「攥胸口」":
            I "（按心口）不会忘记……永远……"
            $ 婚礼选择5 = "珍藏"
            $ 心碎值 += 3
            
        "「想丢却舍不得」":
            I "（举手，垂下）连丢勇气都没有……我还能做什么……"
            $ 婚礼选择5 = "挣扎"
            $ 心碎值 += 4
            
        "「立誓」":
            I "（锐利）我誓……终有一日……强大……"
            I "（叹）罢了……无意义……"
            $ 婚礼选择5 = "誓言"
            $ 心碎值 += 5

    # 绪奈心碎
    scene bg small_garden:
        zoom 1.5
    with fade
    C "（鸭川旁的草房房，绪奈蜷榻榻米。窗喜庆余音如刀剜心。摊掌，碎玉——发簪部分，破碎象征。）"

    O "（握碎玉，割皮肤，血珠渗，无痛。）"
    O "（喃喃）结束了……他是家主大人……我是绪奈……"

    C "（取樱花玉簪，看久，没戴，包裹锁箱底，封感情。）"

    # 最终 - 无望黎明
    scene bg corridor_night:
        zoom 1.3
    with fade
    show s young pained at center with move:
        zoom 0.8
    play sound "audio/birds_chirping.mp3" loop volume 0.2 noloop
    C "（黎明天白。我站廊下一夜未眠。望天边，心停昨日。）"

    I "（望天，无光）"
    I "（独白）就这样吧……期望如此……就这样……"
    scene black with fade

    C "（婚礼无赢家。我心死，愧对绪奈，自憎。美咲有名分无心，余生相敬如宾。）"
    C "（绪奈角角落舔伤，将爱委屈不甘无声咽下，‘祝福’深爱之人。）"
    C "（浅川荣耀续，危机解，皆得所。只有樱树摇曳，记得誓言，记得夜晚碎心。）"
    C "（从此，我人生分二。白日稳重少主；深夜回忆悔恨囚徒。绪奈名成秘密，触碰伤口，无声挽歌。）"
    C "（命运转动，无人逃。挣扎反抗眼泪哀求，湮灭家族时代，无声叹息。）"

    $ persistent.chapter7_completed = True
    $ persistent.婚礼选择1 = 婚礼选择1
    $ persistent.婚礼选择2 = 婚礼选择2
    $ persistent.婚礼选择3 = 婚礼选择3
    $ persistent.婚礼选择4 = 婚礼选择4
    $ persistent.婚礼选择5 = 婚礼选择5
    $ persistent.心碎值 = 心碎值
    $ persistent.愧疚值 = 愧疚值
    $ persistent.perspective = "I"
    if persistent.chapters_unlocked < 8:
        $ persistent.chapters_unlocked = 8
    call screen chapter_complete(7)

    if 心碎值 >= 10:
        jump ending_2
    else:
        # 正常流程或另一个结局
        return

label ending_2:
    C "（朔也彻底变傀儡，只服从命令，无感情。）"
    C "（他机械执行家族事，无笑无泪，如行尸。）"
    father "（满意）好儿子，你终于懂了。"
    I "（空洞）是，父亲。"
    # 未婚妻和家臣密谋片段
    scene bg tea_room:
        zoom 1.5
    with fade    
    show wife silhouette at left with dissolve:
        zoom 0.7
    show young_retainer at small_lowered_right5 with dissolve
    wife "（低声）他就是个傀儡。我们只需等老家主去世，就能控制浅川家。你找机会给他下毒，毒到他半身不遂。"
    young_retainer "（点头）是。美人，你可要做到你答应我的事啊。"
    wife "（冷笑）他死后，一切就都是我们的了。"
    C "（朔也不知，命运已定。）"
    $ persistent.endings_unlocked["ending_2"] = True
    $ progress = check_hidden_ending()
    C "（达成结局：傀儡余生！当前收集：[progress]/9）"
    C "(完)"
    stop music fadeout 1.0
    stop sound fadeout 1.0
    call screen chapter_select()
    return