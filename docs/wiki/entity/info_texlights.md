# info_texlights
[#点实体](wiki/point_entity)

和lights.rad发光纹理设置文件的功能相同，给这个纹理添加键值来设置编译时的发光纹理，添加键值的方法类似[multi_manager](wiki/entity/multi_manager)。

添加的格式为

```
key: 纹理名称
value: R G B 亮度
```

比如你希望mylight1纹理发红色的亮度为1000的光，则添加一个叫做```mylight1```的键，值为```255 0 0 1000```

## 属性 (property)
## 标记 (flag)
