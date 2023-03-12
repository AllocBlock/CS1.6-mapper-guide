# func_grencatch
[#固体实体](wiki/solid_entity)

用于实现手雷引发的固体实体。有手雷进入该区域时，会引发它的目标。

!> 本实体只能使用一次/一回合。引发一次后，或者到新的回合后，实体会失效。

## 属性 (property)
> **[注意!!只能使用一次或一回合]** *classname* = *空* | 字符串

> **名称** *targetname* = *空* | 字符串

实体的名称，用于被其他实体引发，可参考：[引发机制](wiki/trigger)

> **引发的目标** *triggerongrenade* = *空* | 字符串

> **手雷类型** *grenadetype* = *flash* | 单选

- 闪光弹 = *flash*
- 烟雾弹 = *smoke*

## 标记 (flag)
> **死亡模式中禁用** *= 2048*

