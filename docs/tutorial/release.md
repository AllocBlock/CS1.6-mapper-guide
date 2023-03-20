# 地图发布
## 本节中你会了解
- 发布你的地图要打包哪些资源

## 分享地图
- 制作完的地图当然也要和朋友分享！但是哪些文件是需要的，哪些是不需要的，本节会教你如何打包你的地图，非常简单！

### 直接打包发送
- 如果你是直接把地图发给朋友，那么只需要把各种文件整理好就可以了，除了编译得到的bsp文件，还有你用的wad纹理、mdl模型、spr图标、wav音效、tag天空盒等等，按照原本的路径打包即可。
    - **注意**：像是halflife.wad、cstrike.wad这种大家都有的官方纹理不需要打包，不然文件太大了

```
- cstrike_schinese
	- maps
		- myMap.bsp
	- models
		- myModelFolder
			- myModel1.mdl
		- myModel2.mdl
		- myModel3.mdl
	- sprites
        - mySprFolder
            - mySpr1.spr
        - mySpr2.spr
	- sound
		- mySoundFolder
			- mySound1.wav
		- mySound2.wav
	- gfx
		- env
			- mySkyft.tga
			- mySkybk.tga
			- mySkylf.tga
			- mySkyrt.tga
			- mySkyup.tga
			- mySkydn.tga
    - myWad1.wad
    - myWad2.wad
```

### 服务器：res文件
- 如果你想把地图放到服务器上，让玩家进服务器自动下载，你需要制作一个.res文件，用它记录使用的每个资源的位置，进服的玩家会自动下载这些资源
- 新建一个文本文档，命名为```YourMapName.bsp```，注意```YourMapName```要改成你**bsp相同的名称**
    - 打开开始编辑，你要记录每个资源的路径，以上面的```myMap```地图为例，添加res文件后的目录结构是这样的：

```
- cstrike_schinese
	- maps
		- myMap.bsp
		- myMap.res
	- models
		- myModelFolder
			- myModel1.mdl
		- myModel2.mdl
		- myModel3.mdl
    - sprites
        - mySprFolder
            - mySpr1.spr
        - mySpr2.spr
	- sound
		- mySoundFolder
			- mySound1.wav
		- mySound2.wav
	- gfx
		- env
			- mySkyft.tga
			- mySkybk.tga
			- mySkylf.tga
			- mySkyrt.tga
			- mySkyup.tga
			- mySkydn.tga
    - myWad1.wad
    - myWad2.wad
```
- 而res文件中需要填写以下内容
    - 注意res自己的路径也需要写

```
maps/myMap.res
maps/myMap.bsp
models/myModelFolder/myModel1.mdl
models/myModel2.mdl
models/myModel3.mdl
sound/mySoundFolder/mySound1.wav
sound/mySound2.wav
sprites/mySprFolder/mySpr1.spr
sprites/mySpr2.spr
gfx/env/mySkyft.tga
gfx/env/mySkybk.tga
gfx/env/mySkylf.tga
gfx/env/mySkyrt.tga
gfx/env/mySkyup.tga
gfx/env/mySkydn.tga
myWad1.wad
myWad2.wad
```
- 这样地图和相关资源就会自动下载啦！