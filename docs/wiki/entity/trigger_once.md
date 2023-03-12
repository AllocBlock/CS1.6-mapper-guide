# trigger_once
[#固体实体](wiki/solid_entity)

用于实现推力的固体实体。规定一片区域，玩家进入区域后会受到推力，可模拟风的效果。

## 属性 (property)
> **名称** *targetname* = *空* | 字符串

实体的名称，用于被其他实体引发，可参考：[引发机制](wiki/trigger)

> **属主** *master* = *空* | 字符串

填写[multisource](wiki/entity/multisource)的名称，详见[multisource](wiki/entity/multisource)

> **目标** *target* = *空* | 字符串

目标实体的名称，用于引发其他实体，可参考：[引发机制](wiki/trigger)

> **引发前延时** *delay* = *0* | 小数

将要引发目标时，不再是立刻引发，而是延迟一段时间再引发。单位为秒，精确到0.1秒。

> **删除的目标 (无法复原)** *killtarget* = *空* | 字符串

删除指定的实体，刷新不会恢复删除的实体，只有重新载入地图才能恢复。

## 标记 (flag)
> **人质可以引发** *= 1*

> **玩家不能引发** *= 2*

> **pushable引发** *= 4*

> **死亡模式中禁用** *= 2048*

