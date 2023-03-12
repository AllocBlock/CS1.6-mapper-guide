# func_escapezone
[#固体实体](wiki/solid_entity) #游戏模式

用于指定炸T逃脱区域的固体实体。

?> 相关实体 [func_hostage_rescue](wiki/entity/func_hostage_rescue)：人质获救区域；[func_bomb_target](wiki/entity/func_bomb_target)：炸弹（C4）放置区域；[func_vip_safetyzone](wiki/entity/func_vip_safetyzone)：VIP逃脱区域；[info_bomb_target](wiki/entity/info_bomb_target)：炸弹（C4）放置区域（不推荐使用）；[info_hostage_rescue](wiki/entity/info_hostage_rescue)：人质获救区域（不推荐使用）；

?> 注意，放置这个实体会改变游戏模式，当T接触到该实体的区域后，T获胜。

## 属性 (property)
> **名称** *targetname* = *空* | 字符串

实体的名称，用于被其他实体引发，可参考：[引发机制](wiki/trigger)

## 标记 (flag)
> **死亡模式中禁用** *= 2048*

