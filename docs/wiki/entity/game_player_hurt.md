# game_player_hurt
[#点实体](wiki/point_entity)

用于造成伤害/治疗的点实体。引发后会对引发者造成伤害，或者加血。

## 属性 (property)
> **名称** *targetname* = *空* | 字符串

实体的名称，用于被其他实体引发，可参考：[引发机制](wiki/trigger)

> **属主** *master* = *空* | 字符串

填写[multisource](wiki/entity/multisource)的名称，详见[multisource](wiki/entity/multisource)

> **目标** *target* = *空* | 字符串

目标实体的名称，用于引发其他实体，可参考：[引发机制](wiki/trigger)

> **引发者受到的伤害** *dmg* = *999* | 字符串

造成的伤害大小。填负数则是加多少血。

## 标记 (flag)
> **引发后删除** *= 1*

勾选后，实体引发其目标后会删除自己，此后都不能使用了（刷新回合依旧不能使用，只有重新载入地图）。

> **死亡模式中禁用** *= 2048*

