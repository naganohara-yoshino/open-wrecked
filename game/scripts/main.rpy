## 人名的命名逻辑就是取首字母
define c = Character("潮鸢")
define y = Character("玉米")
define s = Character("萨瓦")
define b = Character("白楽")
define sn = Character("少女")

## 启动动画
image splash = "splash.png"
label splashscreen:
    scene black 
    with Pause(1)
    scene splash with dissolve 
    with Pause(2)
    scene black with dissolve 
    with Pause(1)
    return

label start:
    $ quick_menu = False
    $ _dismiss_pause = False
    stop music
    window hide
    screen start_sentence:
        frame:
            xsize 3840
            ysize 2160
            vbox:
                xalign 0.5
                yalign 0.5
                spacing 40
                text "谁此刻没有屋，就不会再造屋\n谁此刻孤独，就会长久孤独" color"#ffffff" size 120 xalign 0.5 yalign 0.5
                text "——赖内·马利亚·里尔克" color"#ffffff" size 80 xalign 1.0 
    show screen start_sentence with Fade(1,0,1)
    with Pause(5)
    hide screen start_sentence with Fade(1,0,0)
    $ quick_menu = True

    call chapter01

    call chapter01_5
