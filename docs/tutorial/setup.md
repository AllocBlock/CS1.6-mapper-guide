# 工具下载和配置

## 本节中你会了解
- 制作地图需要的基础工具：```Valve Hammer Editor 3.5``` （VHE、hammer）
- 准备工作：如何配置制图工具

## 制图工具
要制作地图，先要有趁手的工具。Valve Hammer Editor（简称VHE或hammer）是V社开发用于制作CS地图的软件，我们制作地图大部分内容都在这个软件里进行。VHE3.5是为CS1.6地图开发的最新版本（再往上的VHE4+是为CSS、CSGO制作地图的，互相不通用）。关于VHE的更多信息，[可以看这里](wiki/vhe)。
> J.A.C.K. （Jack hammer）是VHE的替代品，他是非官方开发的软件，主要功能和VHE相同，但是提供了很多方便的操作，详情可以看这里[J.A.C.K. :: Official Website (hlfx.ru)](https://jack.hlfx.ru/en/)，本文依旧针对VHE做讲解，但大部分内容是互通的。

首先在电脑上下载这个软件，这里提供了一个版本的VHE[【下载hammer工具包】](resources/CS地图制作工具包%202023.03.21.zip)，它除了基础的hammer3.5以外，还打包了其他可能用到的工具，包括：
- **hammer3.5**：最重要的制图工具，modchina同盟社版，X-man汉化
- **最新fgd**：V大 *cs16_0.8.2.0_vl.fgd*
- **最新编译程序**：V大 *vhlt v34*，64位
- **超级地图编译器**：第三方编译器，能方便地调整编译选项，发布前的最后一次编译一般用它，X-man开发
- **spr、mdl、bsp查看工具**：*Sprite Explorer*、*HLMV*、*BSP Viewer*
- **地形制作工具**：方便地制作山体，导出map，*GenSurf*和*Terrain Generator*两款
- **纹理制作工具**：制作自己的wad纹理，*Wally*
- **纹理提取工具**：从bsp里提取打包的纹理，*wintextract*
- **反编译工具**：从bsp反编译得到map源文件，*winbspc*

下载解压后的目录结构是这样的：

![](../images/vhe_toolkit_folder.png)

其中“地图制作Hammer3.5.exe“就是主要的制图工具。

## 配置hammer
- 打开“地图制作Hammer3.5.exe“，你可以看到这样的界面
	- ![](../images/hammer_layout.png)
- 在正式开始做图之前，需要先配置hammer，一共要配置的有：
	- wad纹理：地图场景要用到的贴图纹理，**至少要添加一个**
	- fgd：全称是Forge Game Data，它包含了CS全部实体的信息，**必须配置，否则实体列表是空的**
	- 编译程序：hammer里制作的地图是地图源文件（rmf或map格式），需要编译程序生成bsp才能在CS里游玩

- 首先点击菜单栏的“工具"→”参数设置“，会弹出如下窗口
	- ![](../images/hammer_setting.png)`
- **配置wad纹理**：选择“纹理”选项卡，点击“添加”来添加纹理
	- 一般会选择halflife.wad（在CS主目录的valve文件夹里，它包含了半条命1使用的很多纹理）和zhlt.wad（在工具包的tools文件夹里，包含了一些特殊纹理）
	- ![](../images/hammer_setting_wad.png)
- **配置fgd**：切换到“游戏参数”选项卡，点击“添加”，只需添加V大最新的FGD（工具包的fgd文件夹中已经有了）
	- ![](../images/hammer_setting_fgd.png)
- **配置编译程序**：切换到“编译程序”选项卡
	- 设置CSG、BSP、VIS、RAD程序（都在工具包的tools文件夹里，名称分别是hlcsg_x64.exe、hlbsp_x64.exe、hlvis_x64.exe、hlrad_x64.exe）
	- “存放编译好地图的目录”可以填CS的maps文件夹，这样bsp直接放到maps里，不需要手动复制过去
	- “游戏执行程序”就是cstrike.exe的路径，如果勾了编译后自动启动游戏，就会用指定的这个CS程序，也可以不设置
	- ![](../images/hammer_setting_compile.png)
- 点击下方的“确定”，完成设置
- 到此为止，所有的准备工作已经做完了！下一节里，我们会开始制作第一张地图！