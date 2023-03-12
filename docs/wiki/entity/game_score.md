# game_score
[#点实体](wiki/point_entity)

用于给玩家加分、减分的点实体。指计分板里的分数。

## 属性 (property)
> **名称** *targetname* = *空* | 字符串

实体的名称，用于被其他实体引发，可参考：[引发机制](wiki/trigger)

> **属主** *master* = *空* | 字符串

填写[multisource](wiki/entity/multisource)的名称，详见[multisource](wiki/entity/multisource)

> **增加的分数 (负数=减少)** *points* = *1* | 整数

## 标记 (flag)
> **允许负分** *= 1*

默认玩家评分最低为0，勾选后，减分时可以减到负。

> **队友计分** *= 2*

默认是对引发的单个玩家计分，勾选后，变成对玩家所属队伍全员计分。

> **死亡模式中禁用** *= 2048*

