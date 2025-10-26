init python:
    # 停止所有音频
    def stop_all_audio():
        # 主要音频频道
        for channel in ['music', 'sound', 'voice']:
            renpy.music.stop(channel=channel, fadeout=0.5)
        
        # 额外的音频频道（如果有）
        for i in range(1, 10):
            renpy.music.stop(channel=f'audio{i}', fadeout=0.3)
    
    # ESC键处理
    def esc_main_menu():
        stop_all_audio()
        ShowMenu('main_menu')()
    
    # 键位映射
    config.keymap['game_menu'] = ['K_ESCAPE']
    config.underlay.append(renpy.Keymap(game_menu=esc_main_menu))

# 在 script.rpy 或早期加载的文件中
init python:
    if not hasattr(persistent, 'perspective'):
        persistent.perspective = None  # 初始化为 None（尚未选择视角）
        
init:
    transform small_lowered:
        zoom 0.6
        yalign 1.5
        xalign 0.0

init:
    transform small_lowered_left:
        zoom 0.48
        xalign 0.85
        yalign 0.91

init:
    transform small_lowered_right:
        zoom 0.6
        yalign 1.5
        xalign 0.1

init:
    transform small_lowered_left1:
        zoom 0.6
        xalign 0.85
        yalign 1.0

init:
    transform small_lowered_right1:
        zoom 0.6
        yalign 1.0
        xalign 0.06

init:
    transform small_lowered_left2:
        zoom 0.6
        xalign 0.9
        yalign 1.0

init:
    transform small_lowered_right2:
        zoom 0.6
        yalign 0.9
        xalign 0.06

init:
    transform small_lowered_right3:
        zoom 0.55
        yalign 1.45
        xalign 0.8

init:
    transform small_lowered_left4:
        zoom 0.6
        xalign 0.06
        yalign 1.0

init:
    transform small_lowered_right4:
        zoom 0.6
        yalign 0.9
        xalign 0.9

init:
    transform small_lowered_right5:
        zoom 0.6
        yalign 0.9
        xalign 1.0

init python:
    def check_hidden_ending():
        unlocked_count = sum(1 for unlocked in persistent.endings_unlocked.values() if unlocked)
        
        if unlocked_count >= TOTAL_ENDINGS and not persistent.hidden_ending_unlocked:
            persistent.hidden_ending_unlocked = True
            renpy.notify("🎉 所有结局已收集！隐藏结局解锁！")
            renpy.play("audio/sfx_special_unlock.wav", channel="sound")
            renpy.jump("chapter9_o")
            
        return unlocked_count