# game_zone_player
[#固体实体](wiki/solid_entity)

用于判断玩家所在区域的固体实体。根据不同的条件执行不同的功能，详情看属性。

## 属性 (property)
> **名称** *targetname* = *空* | 字符串

实体的名称，用于被其他实体引发，可参考：[引发机制](wiki/trigger)

> **属主** *master* = *空* | 字符串

填写[multisource](wiki/entity/multisource)的名称，详见[multisource](wiki/entity/multisource)

> **让区域内玩家引发的目标** *intarget* = *空* | 字符串

> **让区域外玩家引发的目标** *outtarget* = *空* | 字符串

> **区域内玩家数量的赋值目标** *incount* = *空* | 字符串

填[game_counter](wiki/entity/game_counter)的名称，会设置它的计数值为在区域内玩家的数量。

> **区域外玩家数量的赋值目标** *outcount* = *空* | 字符串

填[game_counter](wiki/entity/game_counter)的名称，会设置它的计数值为在区域外玩家的数量。

## 标记 (flag)
> **死亡模式中禁用** *= 2048*

