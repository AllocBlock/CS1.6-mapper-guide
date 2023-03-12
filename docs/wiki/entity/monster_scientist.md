# monster_scientist
[#点实体](wiki/point_entity)

用于放置人质的点实体。就是解救人质模式里的人质。和[hostage_entity](wiki/entity/hostage_entity)的唯一区别如下：

?> 以下内容摘自天书

这个实体和hostage_entity在cs里的作用是一样的，唯一的区别是：当cs地图使用于shalf-life游戏时，hostage_entity放置将会在游戏时存在，而hostage_entity将不会存在。（哈，谁在乎！！！）

## 属性 (property)
> **名称** *targetname* = *空* | 字符串

实体的名称，用于被其他实体引发，可参考：[引发机制](wiki/trigger)

> **实体角度 (倾斜 旋转 滚动)** *angles* = *0 0 0* | 角度

旋转角度

> **渲染模式** *rendermode* = *空* | 单选

- 普通0 - 无光 = *空*
- 纯颜色1 (仅固体实体) = *1*
- 纹理2 - 微光(全亮) = *2*
- 发光3 (仅图标动画) = *3*
- 固体4 - 无光 = *4*
- 附加5 = *5*

常用的有三个。普通：平时正常的样式；固体：配合{开头的纹理实现透明（如梯子）；发光：配合黑底的纹理实现半透明（如光柱）；

> **渲染效果** *renderfx* = *空* | 单选

- 普通 (0) = *空*
- 脉冲 缓慢 (1) = *1*
- 脉冲 快速 (2) = *2*
- 脉冲 缓慢大范围 (3) = *3*
- 脉冲 快速大范围 (4) = *4*
- 滤波 缓慢 (9) = *9*
- 滤波 快速 (10) = *10*
- 滤波 极快 (11) = *11*
- 闪烁 缓慢 (12) = *12*
- 闪烁 快速 (13) = *13*
- 恒定的发光模式 (14) = *14*
- 扭曲 (仅模型) (15) = *15*
- 扭曲+渐隐 (16) = *16*
- 发光外壳(仅模型)(19) = *19*

> **透明度 (0-255 0=完全透明)** *renderamt* = *255* | 整数

> **渲染色 (R G B)** *rendercolor* = *空* | 颜色

> **实体效果 (数字可相加)** *effects* = *空* | 多选

- 无 = *空*
- 1 (粒子漩涡) = *1*
- 2 (枪口火焰) = *2*
- 4 (强光) = *4*
- 8 (弱光) = *8*
- 16 (假定环境光线向上) = *16*
- 32 (不插入下一帧) = *32*
- 64 (发光图标) = *64*
- 128 (不可见/无网络传输) = *128*

> **显示的动作 (仅编辑器中)** *sequence* = *0* | 单选

- walk = *0*
- walk_scared = *1*
- run = *2*
- run1 = *3*
- run2 = *4*
- 180_Left = *5*
- 180_Right = *6*
- flinch = *7*
- flinch1 = *8*
- laflinch = *9*
- raflinch = *10*
- llflinch = *11*
- rlflinch = *12*
- idle1 = *13*
- idle3 = *14*
- idle4 = *15*
- idle5 = *16*
- idle6 = *17*
- idle7 = *18*
- crouchstand = *19*
- crouch_idle = *20*
- crouch_idle2 = *21*
- crouch_idle3_1 = *22*
- crouch_idle3_2 = *23*
- panic = *24*
- fear1 = *25*
- fear2 = *26*
- eye_wipe = *27*
- pull_needle = *28*
- return_needle = *29*
- give_shot = *30*
- diesimple = *31*
- dieforward = *32*
- dieforward1 = *33*
- diebackward = *34*
- headshot = *35*
- gutshot = *36*
- lying_on_back = *37*
- lying_on_stomach = *38*
- dead_sitting = *39*
- dead_table1 = *40*
- dead_table2 = *41*
- dead_table3 = *42*
- barnacled1 = *43*
- barnacled2 = *44*
- barnacled3 = *45*
- barnacled4 = *46*
- console = *47*
- checktie = *48*
- dryhands = *49*
- tieshoe = *50*
- writeboard = *51*
- studycart = *52*
- lean = *53*
- pondering = *54*
- pondering2 = *55*
- pondering3 = *56*
- buysoda = *57*
- pause = *58*
- yes = *59*
- no = *60*
- push_button = *61*
- converse1 = *62*
- converse2 = *63*
- retina = *64*
- talkleft = *65*
- talkright = *66*
- deskidle = *67*
- coffee = *68*
- franticbutton = *69*
- startle = *70*
- sitlookleft = *71*
- sitlookright = *72*
- sitscared = *73*
- sitting2 = *74*
- sitting3 = *75*
- cprscientist = *76*
- cprscientistrevive = *77*
- cowering_in_corner = *78*
- sstruggleidle = *79*
- sstruggle = *80*
- headcrabbed = *81*
- c1a0_catwalkidle = *82*
- c1a0_catwalk = *83*
- ceiling_dangle = *84*
- ventpull1 = *85*
- ventpull2 = *86*
- ventpullidle1 = *87*
- ventpullidle2 = *88*
- sitidle = *89*
- sitstand = *90*
- keypad = *91*
- lookwindow = *92*
- wave = *93*
- pulldoor = *94*
- beatdoor = *95*
- fallingloop = *96*
- crawlwindow = *97*
- divewindow = *98*
- locked_door = *99*
- push_button2 = *100*
- unlock_door = *101*
- quicklook = *102*
- handrailidle = *103*
- handrail = *104*
- hanging_idle = *105*
- fall = *106*
- scientist_get_pulled = *107*
- hanging_idle2 = *108*
- fall_elevator = *109*
- scientist_idlewall = *110*
- ickyjump_sci = *111*
- haulscientist = *112*
- c1a4_wounded_idle = *113*
- c1a4_dying_speech = *114*
- tentacle_grab = *115*
- helicack = *116*
- windive = *117*
- scicrashidle = *118*
- scicrash = *119*
- onguard = *120*
- seeya = *121*
- rocketcrawl = *122*
- portal = *123*
- gluonshow = *124*
- crouch = *125*
- kneel = *126*
- pepsiidle = *127*
- pepsifall = *128*

> **模型文件[可能不起作用!]** *model* = *models/hostage.mdl* | 单选

- models/scientist.mdl = *models/scientist.mdl*
- models/hostage.mdl = *models/hostage.mdl*

> **身体子模型 (scientist.mdl)** *body* = *0* | 单选

- 0 戴眼镜的 = *0*
- 1 爱因斯坦 = *1*
- 2 黑人 = *2*
- 3 白人 = *3*
- 4 戴眼镜的+注射器 = *4*
- 5 爱因斯坦+注射器 = *5*
- 6 黑人+注射器 = *6*
- 7 白人+注射器 = *7*

> **皮肤 (hostage.mdl)** *skin* = *0* | 单选

- 0 橙色工作服 = *0*
- 1 衬衣和领带 = *1*

## 标记 (flag)
> **死亡模式中禁用** *= 2048*

