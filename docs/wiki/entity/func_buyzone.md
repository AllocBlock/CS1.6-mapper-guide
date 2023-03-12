# func_buyzone
[#固体实体](wiki/solid_entity)

用于指定购买区域的固体实体。

?> 注意，如果地图里没有这个实体，会自动在玩家出生点周围指定一块默认购买区域。如果你不希望玩家购买武器，可以放一个这个实体在玩家到不了的地方

## 属性 (property)
> **名称** *targetname* = *空* | 字符串

实体的名称，用于被其他实体引发，可参考：[引发机制](wiki/trigger)

> **队伍** *team* = *空* | 单选

- 双方 = *空*
- 匪徒 = *1*
- 警察 = *2*

## 标记 (flag)
> **死亡模式中禁用** *= 2048*
