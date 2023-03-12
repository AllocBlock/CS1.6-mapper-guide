# info_player_deathmatch
[#点实体](wiki/point_entity)

用于指定土匪（T）的点实体。放在哪里玩家就会出生在哪里，注意不要卡在墙里或地下，否则玩家出生也会卡住。

## 属性 (property)
> **名称** *targetname* = *空* | 字符串

实体的名称，用于被其他实体引发，可参考：[引发机制](wiki/trigger)

> **属主** *master* = *空* | 字符串

填写[multisource](wiki/entity/multisource)的名称，详见[multisource](wiki/entity/multisource)

> **目标** *target* = *空* | 字符串

目标实体的名称，用于引发其他实体，可参考：[引发机制](wiki/trigger)

> **实体角度 (倾斜 旋转 滚动)** *angles* = *0 0 0* | 角度

旋转角度

> **显示的动作 (仅编辑器中)** *sequence* = *0* | 单选

- dummy = *0*
- idle1 = *1*
- crouch_idle = *2*
- walk = *3*
- run = *4*
- crouchrun = *5*
- jump = *6*
- longjump = *7*
- swim = *8*
- treadwater = *9*
- crouch_aim_carbine = *10*
- crouch_shoot_carbine = *11*
- crouch_reload_carbine = *12*
- ref_aim_carbine = *13*
- ref_shoot_carbine = *14*
- ref_reload_carbine = *15*
- crouch_aim_onehanded = *16*
- crouch_shoot_onehanded = *17*
- crouch_reload_onehanded = *18*
- ref_aim_onehanded = *19*
- ref_shoot_onehanded = *20*
- ref_reload_onehanded = *21*
- crouch_aim_dualpistols_1 = *22*
- crouch_shoot_dualpistols_1 = *23*
- crouch_shoot2_dualpistols_1 = *24*
- crouch_reload_dualpistols_1 = *25*
- ref_aim_dualpistols_1 = *26*
- ref_shoot_dualpistols_1 = *27*
- ref_shoot2_dualpistols_1 = *28*
- ref_reload_dualpistols_1 = *29*
- crouch_aim_rifle = *30*
- crouch_shoot_rifle = *31*
- crouch_reload_rifle = *32*
- ref_aim_rifle = *33*
- ref_shoot_rifle = *34*
- ref_reload_rifle = *35*
- crouch_aim_mp5 = *36*
- crouch_shoot_mp5 = *37*
- crouch_reload_mp5 = *38*
- ref_aim_mp5 = *39*
- ref_shoot_mp5 = *40*
- ref_reload_mp5 = *41*
- crouch_aim_shotgun = *42*
- crouch_shoot_shotgun = *43*
- crouch_reload_shotgun = *44*
- ref_aim_shotgun = *45*
- ref_shoot_shotgun = *46*
- ref_reload_shotgun = *47*
- crouch_aim_m249 = *48*
- crouch_shoot_m249 = *49*
- crouch_reload_m249 = *50*
- ref_aim_m249 = *51*
- ref_shoot_m249 = *52*
- ref_reload_m249 = *53*
- I_am_a_stupid_placeholder = *54*
- so_am_I = *55*
- ref_aim_grenade = *56*
- ref_shoot_grenade = *57*
- crouch_aim_grenade = *58*
- crouch_shoot_grenade = *59*
- crouch_aim_c4 = *60*
- crouch_shoot_c4 = *61*
- ref_aim_c4 = *62*
- ref_shoot_c4 = *63*
- ref_reload_c4 = *64*
- crouch_aim_dualpistols_2 = *65*
- crouch_shoot_dualpistols_2 = *66*
- crouch_shoot2_dualpistols_2 = *67*
- crouch_reload_dualpistols_2 = *68*
- ref_aim_dualpistols_2 = *69*
- ref_shoot_dualpistols_2 = *70*
- ref_shoot2_dualpistols_2 = *71*
- ref_reload_dualpistols_2 = *72*
- crouch_aim_knife = *73*
- crouch_shoot_knife = *74*
- ref_aim_knife = *75*
- ref_shoot_knife = *76*
- crouch_aim_ak47 = *77*
- crouch_shoot_ak47 = *78*
- crouch_reload_ak47 = *79*
- ref_aim_ak47 = *80*
- ref_shoot_ak47 = *81*
- ref_reload_ak47 = *82*
- crouch_aim_shieldgren = *83*
- crouch_shoot_shieldgren = *84*
- ref_aim_shieldgren = *85*
- ref_shoot_shieldgren = *86*
- crouch_aim_shieldknife = *87*
- crouch_shoot_shieldknife = *88*
- ref_aim_shieldknife = *89*
- ref_shoot_shieldknife = *90*
- crouch_aim_shieldgun = *91*
- crouch_shoot_shieldgun = *92*
- crouch_reload_shieldgun = *93*
- ref_aim_shieldgun = *94*
- ref_shoot_shieldgun = *95*
- ref_reload_shieldgun = *96*
- crouch_aim_shielded = *97*
- ref_aim_shielded = *98*
- gut_flinch = *99*
- head_flinch = *100*
- death1 = *101*
- death2 = *102*
- death3 = *103*
- head = *104*
- gutshot = *105*
- left = *106*
- back = *107*
- right = *108*
- forward = *109*
- crouch_die = *110*

> **显示的模型 (仅编辑器中)** *model* = *models/player/guerilla/guerilla.mdl* | 单选

- 玩家尺寸 = *0*
- Arctic = *models/player/arctic/arctic.mdl*
- Guerilla = *models/player/guerilla/guerilla.mdl*
- Leet = *models/player/leet/leet.mdl*
- Terror = *models/player/terror/terror.mdl*

## 标记 (flag)
> **死亡模式中禁用** *= 2048*

