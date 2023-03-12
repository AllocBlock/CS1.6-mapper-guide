# path_corner
[#点实体](wiki/point_entity)

用于制作常规路径的点实体。在[func_guntarget](wiki/entity/func_guntarget)、[func_train](wiki/entity/func_train)、[trigger_camera](wiki/entity/trigger_camera)等实体中会用到。

?> 相关实体 [path_track](wiki/entity/path_track)：路径（火车）；

## 属性 (property)
> **名称** *targetname* = *空* | 字符串

实体的名称，用于被其他实体引发，可参考：[引发机制](wiki/trigger)

> **实体角度 (倾斜 旋转 滚动)** *angles* = *0 0 0* | 角度

旋转角度

> **下一个路径点** *target* = *空* | 字符串

下一个路径点的名称。

> **到达时引发的目标** *message* = *空* | 字符串

> **在此等待的时间(秒)** *wait* = *0* | 整数

> **新的移动速度** *speed* = *0* | 整数

速度，单位/秒

> **?新的转动速度** *yaw_speed* = *0* | 整数

## 标记 (flag)
> **到达后暂停移动** *= 1*

勾选后，实体到达这个路径点后会暂停，再次引发实体后才会继续移动。

> **传送到此路径点** *= 2*

勾选后，实体会直接传送到这个路径点，而非慢慢移动过来。

> **只引发目标一次** *= 4*

> **死亡模式中禁用** *= 2048*

