# game_team_master
[#点实体](wiki/point_entity)

用于确认玩家队伍的点实体，**但因为BUG无法正常使用**。与此相关的game_team_set点实体也无法正常使用。

!> 因为存在BUG已废弃，本实体不能正确辨别玩家队伍，不能正常使用。

## 属性 (property)
> **名称** *targetname* = *空* | 字符串

实体的名称，用于被其他实体引发，可参考：[引发机制](wiki/trigger)

> **属主** *master* = *空* | 字符串

填写[multisource](wiki/entity/multisource)的名称，详见[multisource](wiki/entity/multisource)

> **目标** *target* = *空* | 字符串

目标实体的名称，用于引发其他实体，可参考：[引发机制](wiki/trigger)

> **引发方式** *triggerstate* = *2* | 单选

- 关 = *0*
- 开 = *1*
- 锁定 = *2*

## 标记 (flag)
> **引发后删除** *= 1*

勾选后，实体引发其目标后会删除自己，此后都不能使用了（刷新回合依旧不能使用，只有重新载入地图）。

> **死亡模式中禁用** *= 2048*

