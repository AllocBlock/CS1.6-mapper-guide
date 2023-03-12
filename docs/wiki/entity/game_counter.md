# game_counter
[#点实体](wiki/point_entity)

用于实现计数器的点实体。本实体每次被引发，内置的计数值都会+1，当达到设定的限定值后，本实体会引发目标。如果设置“引发后复位”，引发目标后计数值会恢复到初始值，能重新开始计数，反复使用。

?> 本实体能传输引发者的信息，这一点优于[trigger_relay](wiki/entity/trigger_relay)点实体，可以用它做[game_text](wiki/entity/game_text)、[env_fade](wiki/entity/env_fade)等的中继。

?> 你可以用[game_counter_set](wiki/entity/game_counter_set)直接设置本实体当前的计数值。

## 属性 (property)
> **名称** *targetname* = *空* | 字符串

实体的名称，用于被其他实体引发，可参考：[引发机制](wiki/trigger)

> **属主** *master* = *空* | 字符串

填写[multisource](wiki/entity/multisource)的名称，详见[multisource](wiki/entity/multisource)

> **目标** *target* = *空* | 字符串

目标实体的名称，用于引发其他实体，可参考：[引发机制](wiki/trigger)

> **初始值** *frags* = *0* | 整数

计数的初始值，一般使用默认的0。

> **限定值** *health* = *10* | 整数

计数的限定值，达到这个值后会引发目标。

## 标记 (flag)
> **引发后删除** *= 1*

勾选后，实体引发其目标后会删除自己，此后都不能使用了（刷新回合依旧不能使用，只有重新载入地图）。

> **引发后复位** *= 2*

勾选后，达到限定值引发目标的同时，会恢复计数到初始值，让实体能反复引发。

> **死亡模式中禁用** *= 2048*

