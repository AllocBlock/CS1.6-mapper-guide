# info_teleport_destination
[#点实体](wiki/point_entity)

专用做[trigger_teleport](wiki/entity/trigger_teleport)传送区的目标。本实体的中心对应的是传送后玩家的脚底，所以可以放在贴合地面的位置。

## 属性 (property)
> **名称** *targetname* = *空* | 字符串

实体的名称，用于被其他实体引发，可参考：[引发机制](wiki/trigger)

> **实体角度 (倾斜 旋转 滚动)** *angles* = *0 0 0* | 角度

旋转角度

## 标记 (flag)
> **死亡模式中禁用** *= 2048*

