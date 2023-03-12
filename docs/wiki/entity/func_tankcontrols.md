# func_tankcontrols
[#固体实体](wiki/solid_entity)

用于指定机枪、大炮、激光炮控制区域的固体实体。机枪[func_tank](wiki/entity/func_tank)、大炮[func_tanklaser](wiki/entity/func_tanklaser)、激光炮[func_tankmortar](wiki/entity/func_tankmortar)需要玩家控制时，用实体框定一个区域，指定目标为上面几种武器的名称，玩家进入实体的区域就能控制该武器。

## 属性 (property)
> **名称** *targetname* = *空* | 字符串

实体的名称，用于被其他实体引发，可参考：[引发机制](wiki/trigger)

> **目标** *target* = *空* | 字符串

目标实体的名称，用于引发其他实体，可参考：[引发机制](wiki/trigger)

## 标记 (flag)
> **死亡模式中禁用** *= 2048*

