# trigger_gravity
[#固体实体](wiki/solid_entity)

用于修改重力的固体实体。规定一片区域，玩家进入这片区域后重力会发生变化，变化持续到再次被修改或者新回合开始。

?> 玩家离开区域重力是不会恢复的，可以在出口处放另一个[trigger_gravity](wiki/entity/trigger_gravity)来恢复正常重力。

## 属性 (property)
> **名称** *targetname* = *空* | 字符串

实体的名称，用于被其他实体引发，可参考：[引发机制](wiki/trigger)

> **重力 (1.0=正常 填0无效)** *gravity* = *1* | 整数

## 标记 (flag)
> **死亡模式中禁用** *= 2048*

