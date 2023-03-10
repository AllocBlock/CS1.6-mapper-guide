# env_laser
[#点实体](wiki/point_entity)

产生激光效果的点实体。可造成伤害。

?> 相关实体 [env_beam](wiki/entity/env_beam)：闪电效果；

## 属性 (property)
> **名称** *targetname* = *空* | 字符串

实体的名称，用于被其他实体引发，可参考：[引发机制](wiki/trigger)

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

> **实体角度 (倾斜 旋转 滚动)** *angles* = *0 0 0* | 角度

旋转角度

> **激光目标** *LaserTarget* = *空* | 字符串

激光终点的实体名称，一般使用[info_target](wiki/entity/info_target)

> **亮度 (0 - 255)** *renderamt* = *100* | 整数

> **颜色 (R G B)** *rendercolor* = *0 0 0* | 颜色

> **光线宽度 (0-255)** *width* = *20* | 整数

> **噪点数量 (0-255)** *NoiseAmplitude* = *0* | 整数

越大弯折越多，=0则是直线

> **图标动画纹理文件** *texture* = *sprites/laserbeam.spr* | 字符串

> **结束动画** *EndSprite* = *空* | 字符串

> **纹理滚动速度 (0-100)** *TextureScroll* = *35* | 整数

> **开始帧序号** *framestart* = *0* | 整数

> **每秒伤害力** *damage* = *100* | 字符串

## 标记 (flag)
> **开始时发射** *= 1*

> **发射处冒火花** *= 16*

> **接受处冒火花** *= 32*

> **绘制烧焦痕迹** *= 64*

> **死亡模式中禁用** *= 2048*

