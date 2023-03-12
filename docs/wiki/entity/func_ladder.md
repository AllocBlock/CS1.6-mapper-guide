# func_ladder
[#固体实体](wiki/solid_entity)

用于制作梯子的固体实体。玩家接触它的表面后会变成爬梯子的状态。注意这个实体本身不可见，用它做梯子时有几种方法：
1. 制作一个梯子的外表（一般使用{开头的[透明纹理]()，转为func_wall，渲染模式选固体），再用一层[func_ladder](wiki/entity/func_ladder)贴在它的表面
2. 用[func_illusionary](wiki/entity/func_illusionary)制作一个梯子的外表（一般使用{开头的[透明纹理]()，渲染模式选固体），然后放一个[func_ladder](wiki/entity/func_ladder)和它完全重叠

## 属性 (property)
> **名称** *targetname* = *空* | 字符串

实体的名称，用于被其他实体引发，可参考：[引发机制](wiki/trigger)

## 标记 (flag)
> **死亡模式中禁用** *= 2048*

