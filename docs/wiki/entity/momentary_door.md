# momentary_door
[#固体实体](wiki/solid_entity)

用于制作连续的推拉门的固体实体。和[func_door](wiki/entity/func_door)类似，但它不是只有打开和关闭两种状态，而是由阀门控制逐渐打开关闭（阀门拧一点就开一点，要一直拧才会逐渐完全打开）。只能由[momentary_rot_button](wiki/entity/momentary_rot_button)引发。

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

> **锁住时的声音 (sound/buttons/)** *locked_sound* = *空* | 单选

- 无 = *空*
- 电钮1 button1.wav = *1*
- 电钮2 button2.wav = *2*
- 电钮3 button3.wav = *3*
- 电钮4 button4.wav = *4*
- 电钮5 button5.wav = *5*
- 电钮6 button6.wav = *6*
- 电钮7 button7.wav = *7*
- 电钮8 button8.wav = *8*
- 电钮9 button9.wav = *9*
- 电钮10 button10.wav = *10*
- 电钮11 button11.wav = *11*
- 门闩锁住 latchlocked1.wav = *12*
- 门闩解锁 latchunlocked1.wav = *13*
- 普通电灯开关 lightswitch2.wav = *14*
- 转门1 lever1.wav = *21*
- 转门2 lever2.wav = *22*
- 转门3 lever3.wav = *23*
- 转门4 lever4.wav = *24*
- 转门5 lever5.wav = *25*

> **解锁时的声音 (sound/buttons/)** *unlocked_sound* = *空* | 单选

- 无 = *空*
- 电钮1 button1.wav = *1*
- 电钮2 button2.wav = *2*
- 电钮3 button3.wav = *3*
- 电钮4 button4.wav = *4*
- 电钮5 button5.wav = *5*
- 电钮6 button6.wav = *6*
- 电钮7 button7.wav = *7*
- 电钮8 button8.wav = *8*
- 电钮9 button9.wav = *9*
- 电钮10 button10.wav = *10*
- 电钮11 button11.wav = *11*
- 门闩锁住 latchlocked1.wav = *12*
- 门闩解锁 latchunlocked1.wav = *13*
- 普通电灯开关 lightswitch2.wav = *14*
- 转门1 lever1.wav = *21*
- 转门2 lever2.wav = *22*
- 转门3 lever3.wav = *23*
- 转门4 lever4.wav = *24*
- 转门5 lever5.wav = *25*

> **锁住时的语句** *locked_sentence* = *空* | 单选

- 无 = *空*
- 信息（拒绝访问） = *1*
- 安全锁定 = *2*
- 防爆门效果 = *3*
- 防火门效果 = *4*
- 防化门效果 = *5*
- 防射线门效果 = *6*
- 信息（围堵） = *7*
- 维护门效果 = *8*
- 破损关门效果 = *9*

> **解锁时的语句** *unlocked_sentence* = *空* | 单选

- 无 = *空*
- 信息（访问通过） = *1*
- 安全打开 = *2*
- 防爆门效果 = *3*
- 防火门效果 = *4*
- 防化门效果 = *5*
- 防射线门效果 = *6*
- 信息（围堵） = *7*
- 维护门效果 = *8*

> **移动声音 (sound/doors/)** *movesnd* = *空* | 单选

- 无声 = *空*
- 电动机 doormove1.wav = *1*
- 气动 doormove2.wav = *2*
- 气动滚轴 doormove3.wav = *3*
- 真空 doormove4.wav = *4*
- 液压 doormove5.wav = *5*
- 大滚轴 doormove6.wav = *6*
- 轨道门 doormove7.wav = *7*
- 爽快的金属门 doormove8.wav = *8*
- 吱吱响1 doormove9.wav = *9*
- 吱吱响2 doormove10.wav = *10*

> **停止声音 (sound/doors/)** *stopsnd* = *空* | 单选

- 无声 = *空*
- 叮当响 doorstop1.wav = *1*
- 叮当混响 doorstop2.wav = *2*
- 齿轮 doorstop3.wav = *3*
- 结实的门 doorstop4.wav = *4*
- 轻型气闸 doorstop5.wav = *5*
- 金属滑动 doorstop6.wav = *6*
- 金属锁 doorstop7.wav = *7*
- 轻快金属 doorstop8.wav = *8*

> **露出的尺寸** *lip* = *0* | 整数

## 标记 (flag)
> **开始时打开** *= 1*

> **死亡模式中禁用** *= 2048*

