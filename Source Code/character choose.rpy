# 角色选择界面
screen character_select():
    tag menu
    modal True
    zorder 200
    
    # 使用暗色半透明背景
    add Solid("#000000B2")
    
    frame:
        xalign 0.5
        yalign 0.5
        xpadding 80
        ypadding 60
        background Frame("images/image.png", 30, 30)
        
        vbox:
            spacing 40
            xalign 0.5
            
            # 标题
            label _("选择故事视角"):
                xalign 0.5
                text_size 42
                text_color "#FFFFFF"
            
            # 角色选择区域
            hbox:
                spacing 100
                xalign 0.5
                
                # 朔也选项
                vbox:
                    spacing 20
                    imagebutton:
                        idle "images/sakuya_idle.png"
                        hover "images/sakuya_hover.png"
                        action [SetVariable("selected_character", "sakuya"), Hide("character_select"), Jump("start_sakuya")]
                        xalign 0.5
                    text _("朔也"):
                        xalign 0.5
                        size 36
                        color "#20c239"
                        hover_color "#FFB6C1"
                
                # 绪奈选项
                vbox:
                    spacing 20
                    imagebutton:
                        idle "images/tsumugi_idle.png"
                        hover "images/tsumugi_hover.png"
                        action [SetVariable("selected_character", "tsumugi"), Hide("character_select"), Jump("start_tsumugi")]
                        xalign 0.5
                    text _("绪奈"):
                        xalign 0.5
                        size 36
                        color "#d843cc"
                        hover_color "#FFB6C1"
            
            # 取消按钮
            textbutton _("返回主菜单"):
                xalign 0.5
                action [Hide("character_select"), ShowMenu("main_menu")]
                text_size 32
                text_color "#FFFFFF"
                text_hover_color "#FFB6C1"

# 角色选择后的跳转点
label start_sakuya:
    # 设置全局变量，标记当前是朔也线
    $ persistent.current_route = "sakuya"
    # 跳转到朔也线的开始
    jump sakuya_prologue_i

label start_tsumugi:
    # 设置全局变量，标记当前是绪奈线
    $ persistent.current_route = "tsumugi"
    # 跳转到绪奈线的开始
    jump sakuya_prologue_o

