# env_shooter
[#点实体](wiki/point_entity)

用于喷射模型或图标的点实体。

?> 必须引发：本实体需要被引发才会产生效果。

## 属性 (property)
> **名称** *targetname* = *空* | 字符串

实体的名称，用于被其他实体引发，可参考：[引发机制](wiki/trigger)

> **实体角度 (倾斜 旋转 滚动)** *angles* = *0 0 0* | 角度

旋转角度

> **渲染模式** *rendermode* = *空* | 单选

- 普通0 - 无光 = *空*
- 纯颜色1 (仅固体实体) = *1*
- 纹理2 - 微光(全亮) = *2*
- 发光3 (仅图标动画) = *3*
- 固体4 - 无光 = *4*
- 附加5 = *5*

常用的有三个。普通：平时正常的样式；固体：配合{开头的纹理实现透明（如梯子）；发光：配合黑底的纹理实现半透明（如光柱）；

> **渲染效果** *renderfx* = *空* | 单选

- 普通 (0) = *空*
- 脉冲 缓慢 (1) = *1*
- 脉冲 快速 (2) = *2*
- 脉冲 缓慢大范围 (3) = *3*
- 脉冲 快速大范围 (4) = *4*
- 滤波 缓慢 (9) = *9*
- 滤波 快速 (10) = *10*
- 滤波 极快 (11) = *11*
- 闪烁 缓慢 (12) = *12*
- 闪烁 快速 (13) = *13*
- 恒定的发光模式 (14) = *14*
- 扭曲 (仅模型) (15) = *15*
- 扭曲+渐隐 (16) = *16*
- 发光外壳(仅模型)(19) = *19*

> **透明度 (0-255 0=完全透明)** *renderamt* = *255* | 整数

> **渲染色 (R G B)** *rendercolor* = *空* | 颜色

> **喷射数量** *m_iGibs* = *3* | 整数

喷射总数量，喷完就不再喷了

> **喷射间隔 (0=同时喷出)** *delay* = *0* | 小数

将要引发目标时，不再是立刻引发，而是延迟一段时间再引发。单位为秒，精确到0.1秒。

> **喷射速度** *m_flVelocity* = *200* | 整数

> **方向变化程度** *m_flVariance* = *0.15* | 字符串

> **落地后保留时间** *m_flGibLife* = *4* | 字符串

> **模型(mdl)或图标动画(spr)文件** *shootmodel* = *models/can.mdl* | 路径

模型/图标文件路径。模型放入models文件夹内，路径格式类似 ```models/myModels/myModel.mdl```，注意前面有 ```models/```。图标放入sprites文件夹内，路径格式类似 ```sprites/mySprites/mySprite.spr```，注意前面有 ```sprites/```。

> **皮肤 (模型)** *skin* = *0* | 整数

> **缩放比例 (图标动画)** *scale* = *1.0* | 小数

> **材质声音** *shootsounds* = *-1* | 单选

- 无 = *-1*
- 玻璃 = *0*
- 木头 = *1*
- 金属 = *2*
- 肉 = *3*
- 混凝土 = *4*

## 标记 (flag)
> **死亡模式中禁用** *= 2048*

> **可多次引发** *= 1*
