# 游戏菜单界面
screen game_menu(title, scroll=None, yinitial=0.0):
    style_prefix "game_menu"
    
    add gui.game_menu_background
    
    frame:
        style "game_menu_outer_frame"
        
        hbox:
            frame:
                style "game_menu_navigation_frame"
            
            frame:
                style "game_menu_content_frame"
                
                if scroll == "viewport":
                    viewport:
                        yinitial yinitial
                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True
                        
                        side "c r":
                            vbox:
                                transclude
                            
                elif scroll == "vpgrid":
                    vpgrid:
                        cols 1
                        yinitial yinitial
                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True
                        
                        transclude
                        
                else:
                    transclude
    
    # 标题
    label title:
        text_color "#FFFFFF"
        text_size 36
        xalign 0.5
        yalign 0.1
             
# 主菜单界面
screen main_menu():
    tag menu
    add "gui/main_menu.png":
        zoom 1.3

    if main_menu:
        if gui.show_name:
            vbox:
                xalign 0.1
                yalign 0.2
                text "[config.name!t]":
                    style "main_menu_title"
                    size 70
                    color "#FFFFFF"
                text "[config.version]":
                    style "main_menu_version"
                    size 35
                    color "#FFFFFF"
        
        vbox:
            style_prefix "navigation"
            xalign 0.85
            yalign 0.5
            spacing 30
            
            textbutton _("开始游戏"):
                action ShowMenu("character_select")
                text_size 36
                text_color "#FFFFFF"
                text_hover_color "#FFB6C1"
                text_selected_color "#FF6B6B"
            textbutton _("加载游戏"):
                action ShowMenu("load")
                text_size 36
                text_color "#FFFFFF"
                text_hover_color "#FFB6C1"
                text_selected_color "#FF6B6B"
            textbutton _("章节选择"):
                action ShowMenu("chapter_select")
                text_size 36
                text_color "#FFFFFF"
                text_hover_color "#FFB6C1"
                text_selected_color "#FF6B6B"
            textbutton _("设置"):
                action ShowMenu("preferences")
                text_size 36
                text_color "#FFFFFF"
                text_hover_color "#FFB6C1"
                text_selected_color "#FF6B6B"
            textbutton _("关于"):
                action ShowMenu("about")
                text_size 36
                text_color "#FFFFFF"
                text_hover_color "#FFB6C1"
                text_selected_color "#FF6B6B"
            textbutton _("帮助"):
                action ShowMenu("help")
                text_size 36
                text_color "#FFFFFF"
                text_hover_color "#FFB6C1"
                text_selected_color "#FF6B6B"
            textbutton _("退出"):
                action Quit(confirm=False)
                text_size 36
                text_color "#FFFFFF"
                text_hover_color "#FFB6C1"
                text_selected_color "#FF6B6B"
        
        if gui.show_name:
            text _("Made with {a=https://www.renpy.org/}Ren'Py{/a} [renpy.version_only].\n[gui.about!t]"):
                style "main_menu_version"
                size 24
                xalign 0.95
                yalign 0.95
                color "#FFFFFF"
# 章节选择界面
screen chapter_select():
    tag menu
    add Transform("gui/chapter_bg.png", zoom=1.5)  # 放大背景
    
    # 标题
    label _("章节选择"):
        xalign 0.5
        yalign 0.08
        text_size 60  # 增大标题字号
        text_color "#C21F5F"
    
    # 章节网格
    grid 3 3:
        xalign 0.5
        yalign 0.5
        xspacing 70  # 增加水平间距
        yspacing 50   # 增加垂直间距
        
        # 第一章
        vbox:
            spacing 25  # 增加图标和文字间距
            xalign 0.5
            yalign 0.5
            if persistent.chapters_unlocked >= 1:
                imagebutton:
                    idle Transform("gui/chapter1_idle.png", zoom=0.15)  # 放大图标
                    hover Transform("gui/chapter1_hover.png", zoom=0.15)
                    action [SetVariable("selected_chapter", 1), Jump("start_game")]
                    xysize (260, 150)  # 增大按钮尺寸
                    xalign 0.5
            else:
                add "gui/chapter_locked.png":
                    xysize (260, 150)
                    xalign 0.5
            text _("序章：雪桜"):
                xalign 0.5
                size 32  # 增大文字
                color "#C21F5F"
                hover_color "#FFFFFF"
        
        # 第二章
        vbox:
            spacing 25
            xalign 0.5
            yalign 0.5
            if persistent.chapters_unlocked >= 2:
                imagebutton:
                    idle Transform("gui/chapter2_idle.png", zoom=0.15)
                    hover Transform("gui/chapter2_hover.png", zoom=0.15)
                    action [SetVariable("selected_chapter", 2), Jump("start_game")]
                    xysize (260, 150)
                    xalign 0.5
            else:
                add "gui/chapter_locked.png":
                    xysize (260, 150)
                    xalign 0.5
            text _("第二章：簪約"):
                xalign 0.5
                size 32
                color "#C21F5F"
                hover_color "#FFFFFF"
        
        # 第三章
        vbox:
            spacing 25
            xalign 0.5
            yalign 0.5
            if persistent.chapters_unlocked >= 3:
                imagebutton:
                    idle Transform("gui/chapter3_idle.png", zoom=0.15)
                    hover Transform("gui/chapter3_hover.png", zoom=0.15)
                    action [SetVariable("selected_chapter", 3), Jump("start_game")]
                    xysize (260, 150)
                    xalign 0.5
            else:
                add "gui/chapter_locked.png":
                    xysize (260, 150)
                    xalign 0.5
            text _("第三章：墨蝕"):
                xalign 0.5
                size 32
                color "#C21F5F"
                hover_color "#FFFFFF"
        
        # 第四章
        vbox:
            spacing 25
            xalign 0.5
            yalign 0.5
            if persistent.chapters_unlocked >= 4:
                imagebutton:
                    idle Transform("gui/chapter4_idle.png", zoom=0.15)
                    hover Transform("gui/chapter4_hover.png", zoom=0.15)
                    action [SetVariable("selected_chapter", 4), Jump("start_game")]
                    xysize (260, 150)
                    xalign 0.5
            else:
                add "gui/chapter_locked.png":
                    xysize (260, 150)
                    xalign 0.5
            text _("第四章：鴉鳴"):
                xalign 0.5
                size 32
                color "#C21F5F"
                hover_color "#FFFFFF"
        
        # 第五章
        vbox:
            spacing 25
            xalign 0.5
            yalign 0.5
            if persistent.chapters_unlocked >= 5:
                imagebutton:
                    idle Transform("gui/chapter5_idle.png", zoom=0.15)
                    hover Transform("gui/chapter5_hover.png", zoom=0.15)
                    action [SetVariable("selected_chapter", 5), Jump("start_game")]
                    xysize (260, 150)
                    xalign 0.5
            else:
                add "gui/chapter_locked.png":
                    xysize (260, 150)
                    xalign 0.5
            text _("第五章：冬嵐"):
                xalign 0.5
                size 32
                color "#C21F5F"
                hover_color "#FFFFFF"
        
        # 第六章
        vbox:
            spacing 25
            xalign 0.5
            yalign 0.5
            if persistent.chapters_unlocked >= 6:
                imagebutton:
                    idle Transform("gui/chapter6_idle.png", zoom=0.15)
                    hover Transform("gui/chapter6_hover.png", zoom=0.15)
                    action [SetVariable("selected_chapter", 6), Jump("start_game")]
                    xysize (260, 150)
                    xalign 0.5
            else:
                add "gui/chapter_locked.png":
                    xysize (260, 150)
                    xalign 0.5
            text _("第六章：雨前"):
                xalign 0.5
                size 32
                color "#C21F5F"
                hover_color "#FFFFFF"
        
        # 第七章
        vbox:
            spacing 25
            xalign 0.5
            yalign 0.5
            if persistent.chapters_unlocked >= 7:
                imagebutton:
                    idle Transform("gui/chapter7_idle.png", zoom=0.15)
                    hover Transform("gui/chapter7_hover.png", zoom=0.15)
                    action [SetVariable("selected_chapter", 7), Jump("start_game")]
                    xysize (260, 150)
                    xalign 0.5
            else:
                add "gui/chapter_locked.png":
                    xysize (260, 150)
                    xalign 0.5
            text _("第七章：断簪"):
                xalign 0.5
                size 32
                color "#C21F5F"
                hover_color "#FFFFFF"
        
        # 第八章
        vbox:
            spacing 25
            xalign 0.5
            yalign 0.5
            if persistent.chapters_unlocked >= 8:
                imagebutton:
                    idle Transform("gui/chapter8_idle.png", zoom=0.15)
                    hover Transform("gui/chapter8_hover.png", zoom=0.15)
                    action [SetVariable("selected_chapter", 8), Jump("start_game")]
                    xysize (260, 150)
                    xalign 0.5
            else:
                add "gui/chapter_locked.png":
                    xysize (260, 150)
                    xalign 0.5
            text _("第八章：余燼"):
                xalign 0.5
                size 32
                color "#C21F5F"
                hover_color "#FFFFFF"
        
        # 第九章
        vbox:
            spacing 25
            xalign 0.5
            yalign 0.5
            if persistent.chapters_unlocked >= 9:
                imagebutton:
                    idle Transform("gui/chapter9_idle.png", zoom=0.15)
                    hover Transform("gui/chapter9_hover.png", zoom=0.15)
                    action [SetVariable("selected_chapter", 9), Jump("start_game")]
                    xysize (260, 150)
                    xalign 0.5
            else:
                add "gui/chapter_locked.png":
                    xysize (260, 150)
                    xalign 0.5
            text _("终章：花忘"):
                xalign 0.5
                size 32
                color "#C21F5F"
                hover_color "#FFFFFF"

# 游戏导航界面
screen navigation():
    vbox:
        style_prefix "navigation"
        xpos gui.navigation_xpos
        yalign 0.5
        spacing 15
        
        if main_menu:
            textbutton _("开始游戏"):
                action Jump("start_game")
                text_size 34
                text_color "#FFFFFF"
                text_hover_color "#FFB6C1"
                text_selected_color "#FF6B6B"
        else:
            textbutton _("历史"):
                action ShowMenu("history")
                text_size 34
                text_color "#FFFFFF"
                text_hover_color "#FFB6C1"
                text_selected_color "#FF6B6B"
            textbutton _("存档"):
                action ShowMenu("save")
                text_size 34
                text_color "#FFFFFF"
                text_hover_color "#FFB6C1"
                text_selected_color "#FF6B6B"
            textbutton _("读档"):
                action ShowMenu("load")
                text_size 34
                text_color "#FFFFFF"
                text_hover_color "#FFB6C1"
                text_selected_color "#FF6B6B"
            textbutton _("设置"):
                action ShowMenu("preferences")
                text_size 34
                text_color "#FFFFFF"
                text_hover_color "#FFB6C1"
                text_selected_color "#FF6B6B"
            textbutton _("章节选择"):
                action ShowMenu("chapter_select")
                text_size 34
                text_color "#FFFFFF"
                text_hover_color "#FFB6C1"
                text_selected_color "#FF6B6B"
        
        textbutton _("主菜单"):
            action MainMenu()
            text_size 34
            text_color "#FFFFFF"
            text_hover_color "#FFB6C1"
            text_selected_color "#FF6B6B"
        textbutton _("关于"):
            action ShowMenu("about")
            text_size 34
            text_color "#FFFFFF"
            text_hover_color "#FFB6C1"
            text_selected_color "#FF6B6B"
        textbutton _("帮助"):
            action ShowMenu("help")
            text_size 34
            text_color "#FFFFFF"
            text_hover_color "#FFB6C1"
            text_selected_color "#FF6B6B"
        
        if not main_menu:
            textbutton _("返回"):
                action Return()
                text_size 34
                text_color "#FFFFFF"
                text_hover_color "#FFB6C1"
                text_selected_color "#FF6B6B"
        
        if renpy.variant("pc"):
            textbutton _("退出"):
                action Quit(confirm=not main_menu)
                text_size 34
                text_color "#FFFFFF"
                text_hover_color "#FFB6C1"
                text_selected_color "#FF6B6B"

# 存档界面
screen save():
    tag menu
    use file_slots(_("存档"))

# 读档界面
screen load():
    tag menu
    use file_slots(_("读档"))

# 文件槽位界面
screen file_slots(title):
    default page_name_value = FilePageNameInputValue(pattern=_("第 {} 页"), auto=_("自动存档"), quick=_("快速存档"))
    
    use game_menu(title):
        fixed:
            order_reverse True
            
            button:
                style "page_label"
                key_events True
                xalign 0.5
                action page_name_value.Toggle()
                
                input:
                    style "page_label_text"
                    value page_name_value
                    size 28
                    color "#FFFFFF"
            
            grid gui.file_slot_cols gui.file_slot_rows:
                style_prefix "slot"
                xalign 0.5
                yalign 0.5
                spacing gui.slot_spacing
                
                for i in range(gui.file_slot_cols * gui.file_slot_rows):
                    $ slot = i + 1
                    button:
                        action FileAction(slot)
                        has vbox
                        add FileScreenshot(slot)
                        text FileTime(slot, format=_("{#file_time}%Y-%m-%d %H:%M"), empty=_("空存档位")):
                            style "slot_time_text"
                            size 24
                            color "#FFFFFF"
                        text FileSaveName(slot):
                            style "slot_name_text"
                            size 26
                            color "#FFFFFF"
                        key "save_delete" action FileDelete(slot)

# 章节完成界面
screen chapter_complete(chapter_num):
    modal True
    zorder 200
    
    add "#0008"
    
    frame:
        xalign 0.5
        yalign 0.5
        xpadding 60
        ypadding 60
        
        vbox:
            spacing 30
            label _("第[chapter_num]章完成！"):
                xalign 0.5
                text_size 42
                text_color "#FFFFFF"
            
            if chapter_num < 9:
                text _("新章节已解锁！"):
                    xalign 0.5
                    size 32
                    color "#FFFFFF"
            
            hbox:
                spacing 30
                xalign 0.5
                
                if chapter_num < 9:
                    textbutton _("下一章"):
                        action [SetVariable("selected_chapter", chapter_num + 1), Jump("start_game")]
                        text_size 34
                        text_color "#FFFFFF"
                        text_hover_color "#FFB6C1"
                        text_selected_color "#FF6B6B"
                
                textbutton _("返回菜单"):
                    action [Hide("chapter_complete"), Return()]
                    text_size 34
                    text_color "#FFFFFF"
                    text_hover_color "#FFB6C1"
                    text_selected_color "#FF6B6B"
    
    if chapter_num < 9:
        key "K_RETURN" action [SetVariable("selected_chapter", chapter_num + 1), Jump("start_game")]
    else:
        key "K_RETURN" action MainMenu()

# 设置界面
screen preferences():
    tag menu
    use game_menu(_("设置")):
        vbox:
            style_prefix "prefs"
            xalign 0.5
            yalign 0.5
            spacing 30
            
            hbox:
                box_wrap True
                
                if renpy.variant("pc"):
                    vbox:
                        style_prefix "radio"
                        label _("显示模式"):
                            text_size 34
                            text_color "#FFFFFF"
                        textbutton _("窗口"):
                            action Preference("display", "window")
                            text_size 32
                            text_color "#FFFFFF"
                            text_hover_color "#FFB6C1"
                        textbutton _("全屏"):
                            action Preference("display", "fullscreen")
                            text_size 32
                            text_color "#FFFFFF"
                            text_hover_color "#FFB6C1"
                
                vbox:
                    style_prefix "check"
                    label _("跳过"):
                        text_size 34
                        text_color "#FFFFFF"
                    textbutton _("未读文本"):
                        action Preference("skip", "toggle")
                        text_size 32
                        text_color "#FFFFFF"
                        text_hover_color "#FFB6C1"
                    textbutton _("选项后继续"):
                        action Preference("after choices", "toggle")
                        text_size 32
                        text_color "#FFFFFF"
                        text_hover_color "#FFB6C1"
                    textbutton _("转场特效"):
                        action InvertSelected(Preference("transitions", "toggle"))
                        text_size 32
                        text_color "#FFFFFF"
                        text_hover_color "#FFB6C1"
            
            null height (4 * gui.pref_spacing)
            
            hbox:
                style_prefix "slider"
                box_wrap True
                
                vbox:
                    label _("文字速度"):
                        text_size 34
                        text_color "#FFFFFF"
                    bar value Preference("text speed")
                    label _("自动前进时间"):
                        text_size 34
                        text_color "#FFFFFF"
                    bar value Preference("auto-forward time")
                
                vbox:
                    if config.has_music:
                        label _("音乐音量"):
                            text_size 34
                            text_color "#FFFFFF"
                        hbox:
                            bar value Preference("music volume")
                    
                    if config.has_sound:
                        label _("音效音量"):
                            text_size 34
                            text_color "#FFFFFF"
                        hbox:
                            bar value Preference("sound volume")
                            if config.sample_sound:
                                textbutton _("测试"):
                                    action Play("sound", config.sample_sound)
                                    text_size 30
                                    text_color "#FFFFFF"
                                    text_hover_color "#FFB6C1"
                    
                    if config.has_voice:
                        label _("语音音量"):
                            text_size 34
                            text_color "#FFFFFF"
                        hbox:
                            bar value Preference("voice volume")
                            if config.sample_voice:
                                textbutton _("测试"):
                                    action Play("voice", config.sample_voice)
                                    text_size 30
                                    text_color "#FFFFFF"
                                    text_hover_color "#FFB6C1"
                    
                    if config.has_music or config.has_sound or config.has_voice:
                        null height gui.pref_spacing
                        textbutton _("全部静音"):
                            action Preference("all mute", "toggle")
                            style "mute_all_button"
                            text_size 32
                            text_color "#FFFFFF"
                            text_hover_color "#FFB6C1"

# 历史记录界面
screen history():
    tag menu
    predict False
    
    use game_menu(_("历史记录")):
        vbox:
            style_prefix "history"
            xfill True
            yalign 0.0
            
            for h in _history_list:
                window:
                    has fixed:
                        yfit True
                    
                    if h.who:
                        label h.who:
                            style "history_name"
                            text_color "#FFFFFF"
                            if "color" in h.who_args:
                                text_color h.who_args["color"]
                    
                    text h.what:
                        color "#FFFFFF"
            
            if not _history_list:
                label _("尚无对话历史记录。"):
                    text_color "#FFFFFF"

# 关于界面
screen about():
    tag menu
    use game_menu(_("关于")):
        vbox:
            style_prefix "about"
            xalign 0.5
            yalign 0.5
            spacing 30
            
            text "[config.name!t]":
                color "#FFFFFF"
            text _("版本 [config.version!t]"):
                color "#FFFFFF"
            text _("基于 {a=https://www.renpy.org/}Ren'Py{/a} [renpy.version_only] 引擎制作"):
                color "#FFFFFF"
            text _("版权所有 © Taylor Xiao"):
                color "#FFFFFF"
            text _("本游戏纯属虚构，如有雷同，纯属巧合。"):
                color "#FFFFFF"
            
            if gui.about:
                text "[gui.about!t]":
                    color "#FFFFFF"

# 帮助界面
screen help():
    tag menu
    use game_menu(_("帮助")):
        vbox:
            style_prefix "help"
            xalign 0.5
            yalign 0.5
            spacing 30
            
            text _("键盘快捷键："):
                color "#FFFFFF"
            text _("回车/空格 - 前进对话"):
                color "#FFFFFF"
            text _("Ctrl - 跳过对话"):
                color "#FFFFFF"
            text _("H - 隐藏界面"):
                color "#FFFFFF"
            text _("S - 截图"):
                color "#FFFFFF"
            text _("V - 切换语音"):
                color "#FFFFFF"
            text _("Esc - 回到标题界面"):
                color "#FFFFFF"
            
            null height 20
            
            text _("鼠标操作："):
                color "#FFFFFF"
            text _("左键点击 - 前进对话"):
                color "#FFFFFF"
            text _("滚轮 - 查看历史记录"):
                color "#FFFFFF"
            text _("右键点击 - 快速存档"):
                color "#FFFFFF"
