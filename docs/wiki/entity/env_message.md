# env_message
[#点实体](wiki/point_entity) #屏幕效果

用于显示文字的点实体。文字直接显示在屏幕HUD上。

?> 必须引发：本实体需要被引发才会产生效果。

!> 崩溃风险：如果本实体设置了只对引发的玩家起效果，要注意部分实体无法正确传递引发者信息（如trigger_relay），这可能导致游戏奔溃/闪退。

!> 不建议使用本实体，因为需要更改游戏目录中的文件。建议使用[game_text](wiki/entity/game_text)替代。

## 属性 (property)
> **名称** *targetname* = *空* | 字符串

实体的名称，用于被其他实体引发，可参考：[引发机制](wiki/trigger)

> **目标** *target* = *空* | 字符串

目标实体的名称，用于引发其他实体，可参考：[引发机制](wiki/trigger)

> **信息名** *message* = *空* | 字符串

?> 摘自天书

设置你需要显示的文本。不能随意写。 

设置方法：
1. 进入你的cstrike或valve目录，里面各有一个名为titles.txt的文本文件，可以调用的文本都在这里面。
2. 打开随便一个titles.txt文件，看内容。我举个例子，引用：
```
Game_required_votes
{
Required number of votes for a new map = %s
}
```

里面都是这样的格式，上面的“Game_required_votes”是文本信息标题，下面的“{”和“}”之间的文本就是屏幕上会显示的文本内容了。你要做的，就是把标题填到这个键值里面。这个例子里面，需要填的就是“Game_required_votes”了，这样，当玩家在游戏里引发实体的时候，屏幕上将会显示：Required number of votes for a new map = %s了。

> **声音文件** *messagesound* = *空* | 路径

> **音量 (0-10)** *messagevolume* = *10* | 字符串

> **范围** *messageattenuation* = *0* | 单选

- 小 (约800) = *0*
- 中 (约1250) = *1*
- 大 (约2000) = *2*
- 播放到各处 = *3*

## 标记 (flag)
> **只播放一次** *= 1*

> **对所有玩家** *= 2*

> **死亡模式中禁用** *= 2048*

