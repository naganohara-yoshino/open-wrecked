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