# game_counter_set
[#点实体](wiki/point_entity)

用于设置计数器的点实体。目标是[game_counter](wiki/entity/game_counter)，能直接设置它的计数值。

## 属性 (property)
> **名称** *targetname* = *空* | 字符串

实体的名称，用于被其他实体引发，可参考：[引发机制](wiki/trigger)

> **属主** *master* = *空* | 字符串

填写[multisource](wiki/entity/multisource)的名称，详见[multisource](wiki/entity/multisource)

> **目标** *target* = *空* | 字符串

目标实体的名称，用于引发其他实体，可参考：[引发机制](wiki/trigger)

> **新值** *frags* = *10* | 整数

要设置为的计数值。

## 标记 (flag)
> **引发后删除** *= 1*

勾选后，实体引发其目标后会删除自己，此后都不能使用了（刷新回合依旧不能使用，只有重新载入地图）。

> **死亡模式中禁用** *= 2048*

