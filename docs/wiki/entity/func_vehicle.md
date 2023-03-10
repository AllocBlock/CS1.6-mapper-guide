# func_vehicle
[#固体实体](wiki/solid_entity)

用于制作载具的固体实体。玩家可以控制载具前后左右移动，用于制作汽车、飞机等。

?> 必须引发：本实体需要被引发才会产生效果。

?> 需要轴心：需要配合origin纹理![origin](../../images/tex_origin.png ":no-zoom")使用。TODO：待补充

?> 配合路径：需要配合路径使用，如何制作路径可参考[制作路径]()

?> 朝左放置：实体默认头朝向X轴反方向（即俯视图向左侧），在制作时确保载具的朝向也是这样。然后进入游戏里，载具的朝向有两种方法控制：

1. 调整实体角度属性。但这会有一个bug，这个属性只在第一回合生效，之后的回合，载具会回到初始位置，但是朝向却保留了上回合结束的状态...特别是如果载具上回合停在斜坡上，这回合刚开始载具就是歪的，不建议使用。
2. 制作两个[path_track](wiki/entity/path_track)路径点A和B，路径点A的“下一个路径点”属性填B的名称，然后载具的“路径点”填A的名字，这样每回合开始载具会回到路径点A，头朝向路径点B。

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

> **纹理发光样式** *style* = *空* | 单选

- 普通 = *空*
- 捆绑到同名光源 = *-3*
- 闪烁的荧光 = *10*
- 脉冲 缓慢 强大 = *2*
- 脉冲 缓慢 = *11*
- 脉冲 温和 = *5*
- 闪烁 A = *1*
- 闪烁 B = *6*
- 烛光 A = *3*
- 烛光 B = *7*
- 烛光 C = *8*
- 滤波 快速 = *4*
- 滤波 缓慢 = *9*
- 水下光线 = *12*

> **最小灯光等级 (0.0-2.0)** *_minlight* = *空* | 字符串

> **内容物 (非固体时)** *skin* = *空* | 单选

- 无 = *空*
- 空 = *-1*
- 水 = *-3*
- 毒液 = *-4*
- 熔岩 = *-5*
- 水2 = *-6*
- 梯 (攀爬区域) = *-16*

> **路径点** *target* = *空* | 字符串

目标实体的名称，用于引发其他实体，可参考：[引发机制](wiki/trigger)

> **声音样式 (sound/plats/)** *sounds* = *空* | 单选

- 无 = *空*
- vehicle1.wav = *1*
- vehicle2.wav = *2*
- vehicle3.wav = *3*
- vehicle4.wav = *4*
- vehicle6.wav = *5*
- vehicle7.wav = *6*

> **音量 (0-10)** *volume* = *10* | 整数

> **初始速度** *startspeed* = *0* | 整数

游戏一开始时的速度，会保持直到[path_track](wiki/entity/path_track)或者玩家改变了速度。

> **运动速度** *speed* = *128* | 整数

其实指能达到的最大速度

> **转弯时的倾斜角度** *bank* = *0* | 整数

转弯时最大倾斜角度，可以类比摩托车转弯压弯的效果。

> **挤压伤害** *dmg* = *0* | 整数

被撞到时造成的伤害大小。

> **车身长度** *length* = *256* | 整数

> **车身宽度** *width* = *64* | 整数

> **轴心距离路径点高度** *height* = *4* | 整数

默认情况下，载具的轴心出现在指定路径点的位置，这时有可能车轮陷在地下，调高这个数值来整体抬高载具。**待补充：利用好这个属性可以制作飞机等飞在天上的载具，但具体怎么做不清楚，如果有朋友制作过，欢迎补充。**

## 标记 (flag)
> **不倾斜** *= 1*

> **不能控制** *= 2*

勾选后，载具不能被玩家控制。

> **内容物非固体** *= 8*

> **死亡模式中禁用** *= 2048*

