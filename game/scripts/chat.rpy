screen chat_screen(dialog):
    modal True
    zorder 4
    frame:

        xpadding 50
        top_padding 50
        bottom_padding 430
        xpos 1000
        ypos 20
        xsize 1036
        ysize 2160
        
        background Frame("images/OTHER/qq.png")

        default message_index = 1
        
        viewport id "vp":
            # draggable True
            mousewheel True
            yinitial 1.0
            xsize 1000
            ypos 0.1

            vbox:
                xsize 600
                spacing 50
                
                for i, msg in enumerate(dialog):
                    if i < message_index:
                        use message(**msg)

        key "mouseup_1" action [
            IncrementScreenVariable("message_index"),
            Scroll("vp", "vertical increase" , amount="page", delay=0.5)
        ]






screen message(*, name, content, avatar, from_myself = False):
    if not from_myself:
        hbox:
            xsize 1000
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

            null width 30

    else:
        hbox:
            xsize 1000
            xalign 1.0
            spacing 20
            at message_appear


            null width 30

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
            background Frame("images/OTHER/Rectangleb.png", 25, 25, 25, 25)
            text content pos (0, 0) color "#ffffff" style "msg_bubble_text" 
        else:
            background Frame("images/OTHER/Rectangle.png", 25, 25, 25, 25)
            text content pos (0, 0) color "#000000" style "msg_bubble_text"

            
            style "msg_bubble_text"



transform message_appear:
    alpha 0.0
    yoffset 70
    parallel:
        ease 0.4 alpha 1.0
    parallel:
        easein_back 0.4 yoffset 0     



style msg_bubble_text:
    font "fonts/SourceHanSansLite.ttf"
    size 70

style info_text:
    font "fonts/SourceHanSansLite.ttf"
    color "#9B9B9B"
    size 55

# screen img_message(*, name, img, avatar):



