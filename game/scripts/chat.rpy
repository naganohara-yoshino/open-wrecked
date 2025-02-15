screen chat_screen(group_title, dialog):
    # modal True
    zorder 4

    frame:
        xsize 975
        ysize 2100

        left_padding 35
        right_padding 55
        top_padding 87
        bottom_padding 340

        align (0.5, 0.5)


        background Frame("gui/simulatedphone/simulated_phone.png")

        default message_index = 0
        
        viewport id "vp":
            # draggable True
            mousewheel True
            yinitial 1.0
            xsize 900
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
                Hide("chat_screen", transition = Dissolve(2)),
            ],
            [
                IncrementScreenVariable("message_index"),
                Scroll("vp", "vertical increase" , amount="page", delay=0.5),
                Hide("say")
            ])

        text group_title:

            pos (0.1, 0.042)

            font "fonts/SourceHanSansLite.ttf"
            size 55


screen message(*, name, content, avatar, from_myself = False, **kw):
    if not from_myself:
        hbox:
            xsize 400
            xalign 0.0
            spacing 20
            at message_appear

            vbox:
                null height 20
                add avatar 

            vbox:
                vbox:
                    xalign 0.0
                    text name style "info_text"
                vbox:
                    use msg_bubble(content = content)


    else:
        hbox:
            xsize 770
            xalign 0.5
            spacing 20
            at message_appear



            vbox:
                vbox:
                    xalign 1.0
                    text name style "info_text"
                vbox:
                    use msg_bubble(content = content, from_myself = True)

            vbox:
                null height 20
                add avatar 



screen msg_bubble(*, content, from_myself = False , bubble_width = 700):
    frame:
        padding (40,40)
        xsize bubble_width

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
    font "fonts/SourceHanSansLite.ttf"
    size 60

style info_text:
    font "fonts/SourceHanSansLite.ttf"
    color "#9B9B9B"
    size 45

# screen img_message(*, name, img, avatar):



