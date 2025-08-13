label debugger_menu:
    '测试菜单'
    menu:
        '第一章':
            jump chapter01
        '第二章':
            jump chapter02
        '快速跳转':
            jump jumper

label jumper:
    $ jump_label = renpy.input(prompt="输入label以进入：")
    "我们确定了，您要进入的是[jump_label]"
    $ renpy.jump(jump_label)
    return

label test_1:
    scene 5_busy_city_2
    show ym ting_2
    '~~'