# game_text
[#点实体](wiki/point_entity)

用于显示文本的点实体。文本直接显示在屏幕HUD上。

?> 必须引发：本实体需要被引发才会产生效果。

!> 如果没有勾选了“对所有玩家”，注意玩家引发时要正确传递引发者属性（比如不能用[trigger_relay](wiki/entity/trigger_relay)做中继），否则游戏会立刻卡死并闪退。

## 属性 (property)
> **名称** *targetname* = *空* | 字符串

实体的名称，用于被其他实体引发，可参考：[引发机制](wiki/trigger)

> **属主** *master* = *空* | 字符串

填写[multisource](wiki/entity/multisource)的名称，详见[multisource](wiki/entity/multisource)

> **信息文本** *message* = *空* | 字符串

要显示的文本，支持中文（老的编译器可能会出问题，如果中文无法编译，尝试用V大最新的编译器），用\n表示换行。

> **水平位置(0-1.0=左到右 -1中心)** *x* = *-1* | 字符串

文本的水平位置，0（最左）~1（最右），填-1表示居中。

> **垂直位置(0-1.0=上到下 -1中心)** *y* = *-1* | 字符串

文本的垂直位置，0（最上）~1（最下），填-1表示居中。

> **文本效果** *effect* = *空* | 单选

- 淡入淡出 = *空*
- 闪烁 = *1*
- 打字机效果 = *2*

> **颜色1** *color* = *100 100 100* | 颜色

> **颜色2** *color2* = *240 110 0* | 颜色

> **淡入时间/打字时间** *fadein* = *0.5* | 字符串

> **淡出时间** *fadeout* = *1.5* | 字符串

> **保持时间** *holdtime* = *1.2* | 字符串

> **打字机颜色渐变时间** *fxtime* = *0.25* | 字符串

> **文本频道** *channel* = *1* | 单选

- 频道 1 = *1*
- 频道 2 = *2*
- 频道 3 = *3*
- 频道 4 = *4*

同一频道的文本，新文本在显示时会挤掉老文本，所以妥善设置，避免在同一时间显示相同频道的文本。

## 标记 (flag)
> **对所有玩家** *= 1*

勾选后，引发时对游戏里所有玩家显示文本。

> **死亡模式中禁用** *= 2048*

