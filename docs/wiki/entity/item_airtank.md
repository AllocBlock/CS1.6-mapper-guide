# item_airtank
[#点实体](wiki/point_entity)

用于放置氧气罐的点实体。一般放在水下，靠近后可以补充氧气（重置缺氧计时），攻击后会爆炸然后产生类似闪光弹爆炸的效果（玩家屏幕全白一段时间）。

!> 被破坏后会永远消失，除非重新载入地图。

## 属性 (property)
> **[注意!!只能使用一次或一回合]** *classname* = *空* | 字符串

> **名称** *targetname* = *空* | 字符串

实体的名称，用于被其他实体引发，可参考：[引发机制](wiki/trigger)

> **目标** *target* = *空* | 字符串

目标实体的名称，用于引发其他实体，可参考：[引发机制](wiki/trigger)

> **引发前延时** *delay* = *0* | 小数

将要引发目标时，不再是立刻引发，而是延迟一段时间再引发。单位为秒，精确到0.1秒。

> **删除的目标 (无法复原)** *killtarget* = *空* | 字符串

删除指定的实体，刷新不会恢复删除的实体，只有重新载入地图才能恢复。

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

> **初始移动速度 (X Y Z)** *velocity* = *0 0 0* | 字符串

> **初始转动速度 (倾斜 旋转 滚动)** *avelocity* = *0 0 0* | 字符串

## 标记 (flag)
> **死亡模式中禁用** *= 2048*

