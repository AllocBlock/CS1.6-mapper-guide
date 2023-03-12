# multisource
[#点实体](wiki/point_entity)

本实体的使用比较特殊，它的主要作用有两个：制作被锁定的物体、实现多个实体共同引发才生效的功能。

本实体有两种状态：开和关，默认是处于关的状态的。下面介绍两个作用的实现思路：

---
### 制作被锁定的物体：被锁住的门

玩家在接触被锁住的门时能听到“锁住的声音”对应的音效，且门不会打开

1. 制作一个[env_global](wiki/entity/env_global)，名称叫```unlock```，“设置全局状态实体”填```door_lock_state```，引发模式填```开```。这个实体被引发时会把叫做```door_lock_state```的全局状态设为“开启”。
2. 制作一个[multisource](wiki/entity/multisource)，名称叫```lock```，“读取全局状态实体”填```door_lock_state```。这个实体会读取叫做```door_lock```的全局状态，只有为“开启”时才能使用。
3. 制作一扇门，属主填```lock```。

这样完成后，这扇门是否锁着归[multisource](wiki/entity/multisource)管，而[multisource](wiki/entity/multisource)会去查询```door_lock_state```状态是否为“开启”，引发[env_global](wiki/entity/env_global)就能把```door_lock_state```状态设为“开启”，从而解锁门。

---
### 实现多个实体共同引发才生效的功能：两个开关同时按下才能打开的门。

1. 制作一个门，名称叫```door```。
2. 制作一个[multisource](wiki/entity/multisource)，名称叫```both```，目标为```door```，其他不用填。
3. 制作两个开关，目标都填```both```，复位前延时填2秒。

这样玩家必须在2秒内同时按下两个按钮才能打开门

## 属性 (property)
> **名称** *targetname* = *空* | 字符串

实体的名称，用于被其他实体引发，可参考：[引发机制](wiki/trigger)

> **目标** *target* = *空* | 字符串

目标实体的名称，用于引发其他实体，可参考：[引发机制](wiki/trigger)

> **读取全局状态实体** *globalstate* = *空* | 字符串

全局状态的名称，全局状态是一个能跨地图传输的信息，它用一个字符串标识，每个全局状态有开和关两种状态。比如你填入```my_state```，引发模式选开，那么引发这个实体就会把叫做```my_state```的全局状态设置为开，这个```my_state```为开还能在下一张地图内读取。配合[env_global](wiki/entity/env_global)实体使用，它能设置全局状态。

## 标记 (flag)
> **死亡模式中禁用** *= 2048*

