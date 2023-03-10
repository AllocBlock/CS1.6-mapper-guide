# trigger_hurt
[#固体实体](wiki/solid_entity)

用于造成伤害/治疗的固体实体。规定一片区域，玩家在这片区域中时会持续受到伤害，伤害每隔0.5秒产生一次。

## 属性 (property)
> **名称** *targetname* = *空* | 字符串

实体的名称，用于被其他实体引发，可参考：[引发机制](wiki/trigger)

> **目标** *target* = *空* | 字符串

目标实体的名称，用于引发其他实体，可参考：[引发机制](wiki/trigger)

> **引发前延时** *delay* = *0* | 小数

将要引发目标时，不再是立刻引发，而是延迟一段时间再引发。单位为秒，精确到0.1秒。

> **每秒伤害力** *dmg* = *10* | 整数

每秒造成的伤害大小。填负数则是每秒加多少血。

> **伤害类型** *damagetype* = *空* | 单选

- 普通 = *空*
- 撞击挤压(1) = *1*
- 子弹(2) = *2*
- 砍(4) = *4*
- 烧(8) = *8*
- 冻结(16) = *16*
- 跌落(32) = *32*
- 爆炸(64) = *64*
- 棍打(128) = *128*
- 震动(256) = *256*
- 声波(512) = *512*
- 激光(1024) = *1024*
- 淹(16384) = *16384*
- 瘫痪(32768) = *32768*
- 瓦斯(65536) = *65536*
- 毒(131072) = *131072*
- 辐射(262144) = *262144*
- 水淹恢复(524288) = *524288*
- 化学(1048576) = *1048576*
- 慢烧(2097152) = *2097152*
- 慢冻结(4194304) = *4194304*

## 标记 (flag)
> **只引发目标一次** *= 1*

> **开始时关闭** *= 2*

> **只伤害非玩家** *= 8*

> **只有玩家能引发目标** *= 16*

> **只伤害玩家** *= 32*

> **死亡模式中禁用** *= 2048*

