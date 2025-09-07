screen chat_screen(group_title, dialog):
    # modal True
    zorder 4

    frame:
        xsize 1000
        ysize 2100

        left_padding 40
        right_padding 60
        top_padding 88
        bottom_padding 400

        align (0.5, 0.5)


        background Frame("gui/simulatedphone/simulated_phone.png")

        default message_index = 0
        
        viewport id "vp":
            # draggable True
            mousewheel True
            yinitial 1.0
            xsize 920
            ypos 0.1

            vbox:
                xsize 900
                spacing 40
                
                for i, msg in enumerate(dialog):
                    if i < message_index:
                        $ info = msg.get("extra_display", None)
                        if info:
                            null height 30
                            text info style "info_text" xalign 0.5
                        use message(**msg)

        key "mouseup_1" action If(message_index  == len(dialog),
            [
                Hide("chat_screen", transition = Dissolve(1)), Return(0)
            ],
            [
                IncrementScreenVariable("message_index"),
                Scroll("vp", "vertical increase" , amount="page", delay=0.5),
                Hide("say")
            ])

        text group_title:

            pos (0.1, 0.042)

            font "ht.ttf"
            size 60
    
    #检测跳过——如果renpy.get_skipping()为True，自动触发一个Hide()，隐藏界面
    if renpy.get_skipping():
        timer 0.0000000001 action Hide()



screen message(*, name, avatar, from_myself = False, **kw):
    if not from_myself:
        hbox:
            xsize 810
            xalign 0.0
            spacing 20
            at message_appear

            vbox:
                null height 20
                add avatar:
                    xsize 100
                    ysize 100

            vbox:
                xsize 700
                spacing 20
                vbox:
                    xalign 0.0
                    text name style "info_text"
                vbox:
                    if "image" in kw:
                        use img_bubble(img = kw["image"])
                    elif "content" in kw:
                        use msg_bubble(content = kw["content"])


    else:
        hbox:
            xsize 810
            xalign 1.0
            spacing 20
            at message_appear

            vbox:
                xsize 700
                spacing 20
                vbox:
                    xalign 1.0
                    text name style "info_text"
                vbox:
                    xalign 1.0
                    if "image" in kw:
                        use img_bubble(img = kw["image"])
                    elif "content" in kw:
                        use msg_bubble(content = kw["content"], from_myself = True)

            vbox:
                xalign 0.0
                null height 20
                add avatar 

screen img_bubble(*, img):
    
    python:
        x, _ = renpy.image_size(img)
        mask = Frame("gui/simulatedphone/mask.png", 25, 25, 25, 25)
        result = AlphaMask(img ,mask)
        ratio = 600.0 / x

    vbox:
        xmaximum 600
        if x < 600:
            add result
        else:
            add result zoom ratio



screen msg_bubble(*, content, from_myself = False):
    frame:
        padding (40,40)
        xsize None

        if from_myself:
            background Frame("gui/simulatedphone/rectangle_blue.png", 25, 25, 25, 25)
            text content pos (0, 0) color "#ffffff" style "msg_bubble_text" 
        else:
            background Frame("gui/simulatedphone/rectangle.png", 25, 25, 25, 25)
            text content pos (0, 0) color "#000000" style "msg_bubble_text"

            
            style "msg_bubble_text"



transform message_appear:
    alpha 0.0
    yoffset 70
    parallel:
        ease 0.4 alpha 1.0
    parallel:
        easein_back 0.4 yoffset 0     


transform phone_appear: #Used only when the dialogue have one element
    xcenter 0.5
    yalign 0.5

    on show:
        yoffset 1080
        easein_back 1.0 yoffset 0



style msg_bubble_text:
    font "fonts/ht.ttf"
    size 60

style info_text:
    font "fonts/ht.ttf"
    color "#9B9B9B"
    size 45

# screen img_message(*, name, img, avatar):

## 显示手机时用的模糊
transform blur_background:
        linear 1 blur 30 

transform blur_background_recover:
        linear 1 blur 0

