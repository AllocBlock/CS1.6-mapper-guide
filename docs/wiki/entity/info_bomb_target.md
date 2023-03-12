# info_bomb_target
[#点实体](wiki/point_entity) #游戏模式

用于指定炸弹（C4）放置区域的点实体，点实体周围距离256（也可能是128）单位以内的范围变成炸弹安置区域。

?> 相关实体 [func_escapezone](wiki/entity/func_escapezone)：T逃脱区域；[func_hostage_rescue](wiki/entity/func_hostage_rescue)：人质获救区域；[func_bomb_target](wiki/entity/func_bomb_target)：炸弹（C4）放置区域；[func_vip_safetyzone](wiki/entity/func_vip_safetyzone)：VIP逃脱区域；[info_hostage_rescue](wiki/entity/info_hostage_rescue)：人质获救区域（不推荐使用）；

?> 不建议使用，炸弹放置范围不好控制，推荐使用[func_bomb_target](wiki/entity/func_bomb_target)。

?> 注意，放置这个实体会改变游戏模式，T出生会有一个人带有C4，在指定地点安放C4，CT要阻止T放置C4，或拆卸C4。

## 属性 (property)
> **名称** *targetname* = *空* | 字符串

实体的名称，用于被其他实体引发，可参考：[引发机制](wiki/trigger)

## 标记 (flag)
> **死亡模式中禁用** *= 2048*

