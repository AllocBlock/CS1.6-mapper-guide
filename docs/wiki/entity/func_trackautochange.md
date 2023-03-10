# func_trackautochange
[#固体实体](wiki/solid_entity)

用于制作火车自动立体变轨平台的固体实体。可控制火车做上下、旋转的变轨（半条命1里有很多这种变轨系统），只能用于玩家不能控制的[func_tracktrain](wiki/entity/func_tracktrain)实体，要玩家控制的变轨可使用[func_trackchange](wiki/entity/func_trackchange)。实体默认停在“第一路径”的位置。**待补充：具体的用法还不太清楚，欢迎使用过它的朋友补充。**

?> 相关实体 [func_trackchange](wiki/entity/func_trackchange)：玩家控制火车的立体变轨平台；

?> 必须引发：本实体需要被引发才会产生效果。

?> 需要轴心：需要配合origin纹理![origin](../../images/tex_origin.png ":no-zoom")使用。TODO：待补充

## 属性 (property)
> **名称** *targetname* = *空* | 字符串

实体的名称，用于被其他实体引发，可参考：[引发机制](wiki/trigger)

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

> **实体效果 (数字可相加)** *effects* = *空* | 多选

- 无 = *空*
- 1 (粒子漩涡) = *1*
- 2 (枪口火焰) = *2*
- 4 (强光) = *4*
- 8 (弱光) = *8*
- 16 (假定环境光线向上) = *16*
- 32 (不插入下一帧) = *32*
- 64 (发光图标) = *64*
- 128 (不可见/无网络传输) = *128*

> **纹理发光样式** *style* = *空* | 单选

- 普通 = *空*
- 捆绑到同名光源 = *-3*
- 闪烁的荧光 = *10*
- 脉冲 缓慢 强大 = *2*
- 脉冲 缓慢 = *11*
- 脉冲 温和 = *5*
- 闪烁 A = *1*
- 闪烁 B = *6*
- 烛光 A = *3*
- 烛光 B = *7*
- 烛光 C = *8*
- 滤波 快速 = *4*
- 滤波 缓慢 = *9*
- 水下光线 = *12*

> **最小灯光等级 (0.0-2.0)** *_minlight* = *空* | 字符串

> **移动声音 (sound/plats/)** *movesnd* = *空* | 单选

- 无 = *空*
- 大电梯 bigmove1.wav = *1*
- 大电梯 bigmove2.wav = *2*
- 电梯 elevmove1.wav = *3*
- 电梯 elevmove2.wav = *4*
- 电梯 elevmove3.wav = *5*
- 货物 freightmove1.wav = *6*
- 货物 freightmove2.wav = *7*
- 沉重 heavymove1.wav = *8*
- 齿条 rackmove1.wav = *9*
- 齿条 railmove1.wav = *10*
- 杂乱 squeekmove1.wav = *11*
- 怪异 talkmove1.wav = *12*
- 怪异 talkmove2.wav = *13*

> **停止声音 (sound/plats/)** *stopsnd* = *空* | 单选

- 无 = *空*
- 大电梯 bigstop1.wav = *1*
- 大电梯 bigstop2.wav = *2*
- 货物 freightstop1.wav = *3*
- 沉重 heavystop2.wav = *4*
- 齿条 rackstop1.wav = *5*
- 齿条 railstop1.wav = *6*
- 杂乱 squeekstop1.wav = *7*
- 怪异 talkstop1.wav = *8*

> **音量 (0.0-1.0)** *volume* = *0.85* | 字符串

> **移动高度** *height* = *0* | 整数

变轨平台移动的高度。

> **转动角度** *rotation* = *0* | 整数

变轨平台旋转的角度。

> **火车实体** *train* = *空* | 字符串

> **第一路径** *toptrack* = *空* | 字符串

火车变轨前[path_track](wiki/entity/path_track)路径点的名称。

> **第二路径** *bottomtrack* = *空* | 字符串

火车变轨后[path_track](wiki/entity/path_track)路径点的名称。

> **移动/转动速度** *speed* = *0* | 整数

速度，单位/秒

## 标记 (flag)
> **?自动激活火车** *= 1*

> **?重新连接路径** *= 2*

> **先连接第二路径** *= 8*

勾选后，初始状态平台在第二路径，而非默认的第一路径。

> **只旋转** *= 16*

勾选后，变轨平台只旋转，不会升高降低。

> **绕X轴旋转** *= 64*

勾选后，变成以X轴为转轴旋转。默认情况下是绕Z轴旋转的。

> **绕Y轴旋转** *= 128*

勾选后，变成以X轴为转轴旋转。默认情况下是绕Z轴旋转的。

> **死亡模式中禁用** *= 2048*

