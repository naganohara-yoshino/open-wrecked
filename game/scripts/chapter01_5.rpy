label chapter01_5:
    $ quick_menu = False
    scene black with Dissolve(1)
    with Pause(1)
    scene zc1 with Fade(1,0.5,1.5,color = "#ffffff")
    with Pause(3)
    scene black with Fade(2,2,0)
    screen dream:
        frame:
            xsize 3840
            ysize 2160
            vbox:
                xalign 0.5
                yalign 0.5
                spacing 40
                text "梦境" color"#ffffff" size 160 xalign 0.5 yalign 0.5
    show screen dream with Fade(1,0,1)
    with Pause(3)
    hide screen dream with Fade(1,0,0)
    show 8_street with Fade(0,0,2)
    play music "audio/Sad/07.ogg" fadein 4
    $ quick_menu = True
    "“已经入秋了啊——”" with Dissolve(1)
    """
    驻足在这条没有回声的街道上，失意的我妄图追寻梦的延续

    十月的嘉城大街上行人稀疏，此刻我才真正有了一种入秋的实感

    """
    c"把一切都搞砸了吗……"
    """
    就在刚才，我从她的身旁匆忙地逃走，用最狼狈的方式结束了这无休无止的争吵
    
    试图安慰自己，是啊，一连串的失意总是会有个标志的
    
    可这无意义的争吵又是什么，甚至都算不上一个句号
    
    只是在原本就潦草不堪的笔迹上，重重加上删除的横线罢了
    
    并不想回去，绕远路也好，就这么漫无目的地走下去吧
    """
    scene 9_backwall_night with Fade(1,2,1)
    with Pause(1)
    "在嘉城三中的后墙，我被陌生的白发少女绊倒" with Dissolve(1)
    """
    然而她并不乞讨钱财，只是乞求救命的药

    好荒唐啊。骂了她几句不长眼，本想装作没有看见一走了之

    转而一想，为什么要这么刻薄呢。不知为何觉得对不起她
    
    带她去药店买药之后，我们又走回后墙
    
    沉默良久，我尴尬地开口了
    """
    show bl_winter_normal at _left with dissolve
    show cy calm at _right with dissolve
    c"你可真是个怪人啊，秋夜讨药什么的"
    bn"你可真是个好人啊，秋夜给药什么的"
    c"……"
    bn"这份恩情一定会偿还的"
    c"哦？怎么偿还"
    bn"奇迹（き•せ•き）的力量"
    c"""
    哦。
    
    ……如若真的有奇迹的力量就好了……
    """
    bn"你也祈求奇迹吗？"
    c"只是想追寻梦的延续罢了"
    bn"“梦的延续”吗？……"
    hide bl_winter_normal with dissolve
    hide cy with dissolve
    """
    白发少女不知从哪拿出了一把吉他，说是要给我看“梦的延续”
    
    好熟悉的旋律……不知不觉沉醉了
    """
    bn"""
    这便是今天的答谢
    
    但今天的恩情仍然没有偿还，来日必将报答
    """
    c"偿还什么的，其实这一曲也已足够了"
    bn"""
    但这一曲并不是奇迹的力量——
    
    再见了，若有机会……
    """
    "说完她就走了，后面的话都没有听清"
    c"""
    喂，什么意思！
    
    ……如此刻薄的我也配奇迹的力量吗？……
    """
    """
    我朝她的方向说道，但已不见人影了
    
    她那谶言一般的话无从知晓含义
    
    “若有机会”什么的，小孩子也不信吧
   
    该回去了
    """
    scene 8_street with Fade(2,2,2)
    "少女消失后，演奏的歌曲还在延伸——" with Dissolve(1)
    "天地也为之入了迷，周围的景色变得愈加虚幻了"
    show snow
    "——霎时，阴沉的天空中竟卷下一场纷纷扬扬的大雪来" with Dissolve(1)
   

    screen sentence_3:
        vbox:
            xalign 0.5
            yalign 0.5
            button:
                text "十月份的嘉城也会有雪吗"outlines[(absolute(5), "#ffffff", absolute(0), absolute(0))] color"#000000" size 160 
        
    show screen sentence_3 with Dissolve(1)
    with Pause(3)
    hide screen sentence_3 with Dissolve(1)
    with Pause(1)
    "不知哪里来的兴致，我翩翩然踏雪而归" with Dissolve(1)
    """
    多年以来困扰我的关系似乎即将进入尾声。可在这掩盖一切的皑皑大雪之中，是否就能这样和解呢

    脚步愈迷，如舞，如禅
    """



