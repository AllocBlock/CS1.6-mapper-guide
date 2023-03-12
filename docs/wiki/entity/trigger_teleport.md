# trigger_teleport
[#固体实体](wiki/solid_entity)

用于实现传送的固体实体。规定一片区域，玩家进入区域后会传送到目标位置。

?> 多个玩家都在传送时，传送完后可能重叠在一起卡住。你可以把终点放在空中，这样传送过去会落到地方避免卡住，另外天花板不能太低，否则卡住后按跳跃也不能解除卡住了。

## 属性 (property)
> **名称** *targetname* = *空* | 字符串

实体的名称，用于被其他实体引发，可参考：[引发机制](wiki/trigger)

> **属主** *master* = *空* | 字符串

填写[multisource](wiki/entity/multisource)的名称，详见[multisource](wiki/entity/multisource)

> **目标** *target* = *空* | 字符串

填[info_teleport_destination](wiki/entity/info_teleport_destination)的名称。

## 标记 (flag)
> **人质可以引发** *= 1*

> **玩家不能引发** *= 2*

> **死亡模式中禁用** *= 2048*

