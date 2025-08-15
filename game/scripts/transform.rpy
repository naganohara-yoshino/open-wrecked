############### 转场的一些预定义 ###############

define dissolve_1 = Dissolve(1.0)
define fade1 = Fade(1.0,3.0,1.0)

## 可以控制的震动 下面是两个官方的例子
## (0, 10), (0, -10) 是移动幅度，改数字可以增加幅度。
## repeat 就是重复几次，true就是一直重复，改成数字比如3，就是重复3次
# define vpunch = Move((0, 10), (0, -10), .10, bounce=True, repeat=True, delay=.275)
# define hpunch = Move((15, 0), (-15, 0), .10, bounce=True, repeat=True, delay=.275)

define vpunch_1 = Move((0, 30), (0, -30), .2, bounce=True, repeat=3, delay=1.575)

## 向下移动
transform move_down_t:
    alpha 0.0
    ypos -50
    parallel:
        easein_quart 1.0 alpha 1.0
    parallel:
        easein_quart 1.0 ypos 0

## 向上移动
transform move_up_t:
    alpha 0.0
    ypos 50
    parallel:
        easein_quart 1.0 alpha 1.0
    parallel:
        easein_quart 1.0 ypos 0

## 向左移动
transform move_left_t:
    alpha 0.0
    xpos 50
    parallel:
        easein_quart 1.0 alpha 1.0
    parallel:
        easein_quart 1.0 xpos 0

## 向右移动
transform move_right_t:
    parallel:
        easein_quart 1.0 alpha 1.0
    parallel:
        easein_quart 1.0 xpos 1300
    parallel:
        yoffset 0
        linear 0.2 yoffset 40
        linear 0.2 yoffset 0
        repeat 2

## 背景模糊
transform bg_blur_t:
    blur 30
    parallel:
        linear 2 blur 0

## 镜头拉近
transform zoom_in_t:
    zoom 1.0
    align (0.5, 0.5)
    parallel:
        linear 1.0 zoom 1.2

## 镜头拉远
transform zoom_out_t:
    zoom 1.2
    align (0.5, 0.5)
    parallel:
        linear 1.0 zoom 1.0

## 上下动
transform y_move_t:
    yoffset 0
    linear 0.1 yoffset 40
    linear 0.1 yoffset 0
    repeat 2

## 左右动
transform x_move_t:
    xoffset 0
    linear 0.1 xoffset 40
    linear 0.1 xoffset 0
    repeat 2

## 往前走
transform z_move_forward_t:
    zoom 0.9
    linear 0.3 zoom 1.0

## 往后退
transform z_move_backward_t:
    zoom 1.1
    linear 0.3 zoom 0.9

## 红蓝颜色变化
transform red_blue_tint:
    matrixcolor TintMatrix("#f00")
    linear 1.0 matrixcolor TintMatrix("#00f")
    linear 1.0 matrixcolor TintMatrix("#f00")
    repeat

## 老照片效果
transform old_photo_t:
    matrixcolor SepiaMatrix()

## 去色
transform black_white_t:
    matrixcolor SaturationMatrix(0.0)

## 这两个颜色参数可以修改，可以变成各种效果
## 改成一个颜色，就会让立绘变成纯色
## 染色
transform coloriz_t:
    linear 1.0 matrixcolor ColorizeMatrix("#a46565", "#2034e9")

transform _left:
    xpos 1000

transform _right:
    xpos 3840-1000


############### 使用指南 ###############

#   scene street day at coloriz_t
#   with dissolve
#   "染色效果"

#   scene street day at black_white_t
#   with dissolve
#   "去色效果"

#   scene street day at old_photo_t
#   with dissolve
#   "老照片效果"

#   scene street day
#   show room at move_down_t
#   "背景图背景从上方渐入"

#   scene room
#   show street day at move_up_t
#   "背景从下方渐入"

#   scene street day   
#   show room at move_left_t
#   "背景从左侧渐入"

#   scene room    
#   show street day at move_right_t
#   "背景从右侧渐入"

#   scene room at bg_blur_t 
#   "背景模糊变清楚"

#   scene room at zoom_in_t
#   "镜头拉近" 

#   scene room at zoom_out_t
#   "镜头拉远" 

##   "下面是立绘的演出"

#   show eileen happy at center, y_move_t
#   "上下动，可以指定改几次，幅度和快慢"

#   show eileen happy at center, x_move_t
#   "左右动，可以指定改几次，幅度和快慢"

#   show eileen happy at center, z_move_forward_t
#   "往前走"

#   show eileen happy at center, z_move_backward_t
#   "往后退"
    

## 控制是否能被跳过
label bg_transition_disable:
    python:
        _dismiss_pause = False
        quick_menu = False
    return

label bg_transition_enable:
    python:
        _dismiss_pause = True
        quick_menu = True
    return

#   睁闭眼睛特效
init python:
    def eyewarp(x):
        return x**1.33
    eye_open = ImageDissolve("gui/transition/eye.png", 0.5, ramplen=128, reverse=False, time_warp=eyewarp)
    eye_shut = ImageDissolve("gui/transition/eye.png", 0.5, ramplen=128, reverse=True, time_warp=eyewarp)
image black:
    Solid("#000")
image white:
    Solid("#FFF")


