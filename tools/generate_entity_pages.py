from valvefgd import FgdParse
from enum import Enum
import json
import os
from entity_info import ENTITIY_INFO, PROPERTY_INFO, FLAG_INFO

def load_json(file):
    with open(file, "r", encoding="utf8") as f:
        return json.loads(f.read())

class EntityType(Enum):
    Unknown = 0
    Point = 1
    Solid = 2

class ValueType(Enum):
    Unknown = 0
    String = 1
    Integer = 2
    Decimal = 3
    Path = 4
    Angle = 5
    Color = 6
    Single_Choice = 7
    Multiple_Choices = 8

class FGDChoice:
    def __init__(self, display_name : str, value : int) -> None:
        self.display_name = display_name
        self.value = value

    def get_dict(self):
        return self.__dict__.copy()

class FGDProperty:
    def __init__(self) -> None:
        self.name = ''
        self.display_name = ''
        self.value_type = ValueType.String
        self.default_value = None
        self.choices : list[FGDChoice] = []

    def get_dict(self):
        d = self.__dict__.copy()
        d['value_type'] = d['value_type'].name
        if len(d['choices']) > 0:
            d['choices'] = list(map(lambda choice: choice.get_dict(), d['choices']))
        else:
            del d['choices']
        return d

class FGDFlag:
    def __init__(self) -> None:
        self.display_name = ''
        self.value = -1
        self.default_value = False

    def get_dict(self):
        return self.__dict__.copy()

class FGDEntity:
    def __init__(self) -> None:
        self.type = EntityType.Point
        self.name = ''
        self.short_description = ''
        self.full_description = ''
        self.properties : list[FGDProperty] = []
        self.flags : list[FGDFlag] = []
        self.tags = [] # 给实体效果分类，比如特效、功能、控制
        self.tips = []
        self.warnings = []
        self.alerts = []
        self.example = None

    def get_dict(self):
        d = self.__dict__.copy()
        d['type'] = d['type'].name
        d['properties'] = list(map(lambda prop: prop.get_dict(), d['properties']))
        d['flags'] = list(map(lambda flag: flag.get_dict(), d['flags']))
        return d

def get_type_enum(lib_type):
    if lib_type == "SolidClass":
        return EntityType.Solid
    elif lib_type == 'PointClass':
        return EntityType.Point
    else:
        raise RuntimeError("Not Target type")

IGNORED_ENITIES = [
    "worldspawn",
    "test_effect",
]

IGNORED_PROPERTY = [
    "zhlt_invisible",
    "zhlt_noclip",
    "zhlt_lightflags",
    "zhlt_customshadow",
    "light_origin",
]

DECIMAL_PROPERTIES = [
    "delay", "framerate", "scale", "persistence"
]

PATH_PROPERTIES = [
    "sound", "studio"
]

def get_property_type(lib_property):
    if lib_property.name in DECIMAL_PROPERTIES:
        return ValueType.Decimal
    if lib_property.value_type in PATH_PROPERTIES:
        return ValueType.Path
    elif lib_property.name == 'angles': # 也支持Choices
        return ValueType.Angle
    elif lib_property.value_type == 'integer':
        return ValueType.Integer
    elif lib_property.value_type == 'choices':
        if '可相加' in lib_property.display_name: # 比较糙，如果名称里有则标为多选
            return ValueType.Multiple_Choices
        else:
            return ValueType.Single_Choice
    elif lib_property.value_type == 'color255':
        return ValueType.Color
    else:
        return ValueType.String

def load_fgd(file):
    fgd = FgdParse(file)
    entities = []
    for lib_ent in fgd.entities:
        if lib_ent.class_type == "BaseClass":
            continue
        if lib_ent.name in IGNORED_ENITIES:
            continue

        entity = FGDEntity()
        entity.type = get_type_enum(lib_ent.class_type)
        entity.name = lib_ent.name
        entity.short_description = lib_ent.description
        if entity.name in ENTITIY_INFO:
            info = ENTITIY_INFO[entity.name]
            if "tags" in info:
                entity.tags += info["tags"]
            if "short_description" in info:
                entity.short_description = info["short_description"]
            if "full_description" in info:
                entity.full_description = info["full_description"]
            if "tips" in info:
                entity.tips += info["tips"]
            if "alerts" in info:
                entity.alerts += info["alerts"]

        for lib_prop in lib_ent.properties:
            prop = FGDProperty()
            prop.name = lib_prop.name
            if prop.name in IGNORED_PROPERTY:
                continue
            prop.display_name = lib_prop.display_name.strip()
            prop.value_type = get_property_type(lib_prop)
            prop.default_value = lib_prop.default_value
            if lib_prop.choices is not None:
                prop.choices = list(map(lambda choice: FGDChoice(choice.display_name.strip(), choice.value), lib_prop.choices))
            entity.properties.append(prop)

        for lib_flag in lib_ent.spawnflags:
            flag = FGDFlag()
            flag.display_name = lib_flag.display_name.strip()
            flag.value = lib_flag.value
            flag.default_value = lib_flag.default_value
            entity.flags.append(flag)

        entities.append(entity)

    entities.sort(key=lambda ent : ent.name)
    return entities

def save_file(text, target_dir, file_name):
    path = os.path.join(target_dir, file_name)
    with open(path, "w", encoding="utf8") as f:
        f.write(text)

def get_entity_type_link(type : EntityType):
    if type == EntityType.Solid:
        return "[#固体实体](wiki/solid_entity)"
    elif type == EntityType.Point:
        return "[#点实体](wiki/point_entity)"
    else:
        raise RuntimeError("Not Target type")

def get_prop_description(entity_name, prop_name):
    if prop_name in PROPERTY_INFO:
        if entity_name in PROPERTY_INFO[prop_name]:
            return PROPERTY_INFO[prop_name][entity_name]
        elif 'description' in PROPERTY_INFO[prop_name]:
            return PROPERTY_INFO[prop_name]['description']
        else:
            return None
    else:
        return None

def get_flag_description(entity_name, prop_name):
    if prop_name in FLAG_INFO:
        if entity_name in FLAG_INFO[prop_name]:
            return FLAG_INFO[prop_name][entity_name]
        elif 'description' in FLAG_INFO[prop_name]:
            return FLAG_INFO[prop_name]['description']
        else:
            return None
    else:
        return None

def value_to_str(v):
    if v is None or v == '':
        return '空'
    else:
        return str(v)

def value_type_to_str(v):
    if v == ValueType.String:
        return "字符串"
    elif v == ValueType.Integer:
        return "整数"
    elif v == ValueType.Decimal:
        return "小数"
    elif v == ValueType.Path:
        return "路径"
    elif v == ValueType.Angle:
        return "角度"
    elif v == ValueType.Color:
        return "颜色"
    elif v == ValueType.Single_Choice:
        return "单选"
    elif v == ValueType.Multiple_Choices:
        return "多选"

def genrate_entity_list(entities : list[FGDEntity], link_path):
    text = ""
    for entity in entities:
        text += f"- [{entity.name}]({link_path}/{entity.name}) : {entity.short_description}\n"
    text += "\n"
    return text

def generate_pages(entities : list[FGDEntity], target_dir, link_path):
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)

    sortByTypeIndexFile = "entity_index_by_type.md"
    sortByCategoryIndexFile = "entity_index_by_category.md"
    # 主页索引
    indexText = "# 实体目录\n"
    indexText += f"> 实体属性、标记的中文翻译基于V大的fgd：[cs16_0.8.2.0_vl.fgd](resources/cs16_0.8.2.0_vl.fgd ':ignore')\n\n> [按点实体、固体实体分类](wiki/entity/{sortByTypeIndexFile})、[按类型分类](wiki/entity/{sortByCategoryIndexFile})\n\n"
    indexText += genrate_entity_list(entities, link_path)
    save_file(indexText, target_dir, "README.md")

    # 点实体、固体实体索引
    indexText = "# 实体索引（点实体、固体实体）\n"
    indexText += f"> 实体属性、标记的中文翻译基于V大的fgd：[cs16_0.8.2.0_vl.fgd](resources/cs16_0.8.2.0_vl.fgd ':ignore')\n\n> [按名称排序](wiki/entity/README.md)、[按类型分类](wiki/entity/{sortByCategoryIndexFile})\n\n"
    pointEntities = [ent for ent in entities if ent.type == EntityType.Point]
    indexText += "## 点实体\n"
    indexText += genrate_entity_list(pointEntities, link_path)

    solidEntities = [ent for ent in entities if ent.type == EntityType.Solid]
    indexText += "## 固体实体\n"
    indexText += genrate_entity_list(solidEntities, link_path)
    save_file(indexText, target_dir, sortByTypeIndexFile)

    # 基于名称分类的索引
    indexText = "# 实体索引（按类型分类）\n"
    categories = [
        ("env", "环境"),
        ("cycler", "模型、图标"),
        ("func", "功能"),
        ("game", "游戏"),
        ("info", "设置"),
        ("item", "装备"),
        ("light", "灯光"),
        ("path", "路径"),
        ("trigger", "触发"),
    ]
    indexText += f"> 实体属性、标记的中文翻译基于V大的fgd：[cs16_0.8.2.0_vl.fgd](resources/cs16_0.8.2.0_vl.fgd ':ignore')\n\n> [按名称排序的目录](wiki/entity/README.md)、[按点实体、固体实体分类](wiki/entity/{sortByTypeIndexFile})\n\n"

    remainEntities = entities.copy()
    for categoryName, categoryDescription in categories:
        categoryEntities = [ent for ent in remainEntities if ent.name.startswith(categoryName)]
        remainEntities = [ent for ent in remainEntities if ent not in categoryEntities]
        indexText += f"## {categoryName} *{categoryDescription}*\n"
        indexText += genrate_entity_list(categoryEntities, link_path)

    indexText += "## 其他\n"
    indexText += genrate_entity_list(remainEntities, link_path)
    save_file(indexText, target_dir, sortByCategoryIndexFile)


    # 实体详情页索引
    for entity in entities:
        text = f"# {entity.name}\n"
        text += f"{get_entity_type_link(entity.type)}"
        for tag in entity.tags:
            text += f" #{tag}"
        text += f"\n\n"

        desc = entity.full_description if entity.full_description else entity.short_description
        text += f"{desc}\n\n"

        for tip in entity.tips:
            text += f"?> {tip}\n\n"
        for alert in entity.alerts:
            text += f"!> {alert}\n\n"

        text += f"## 属性 (property)\n"
        for prop in entity.properties:
            text += f"> **{prop.display_name}** *{prop.name}* = *{value_to_str(prop.default_value)}* | {value_type_to_str(prop.value_type)}\n\n"
            if prop.value_type == ValueType.Single_Choice or prop.value_type == ValueType.Multiple_Choices:
                for choice in prop.choices:
                    text += f"- {choice.display_name} = *{value_to_str(choice.value)}*\n"
                text += "\n"
            desc = get_prop_description(entity.name, prop.name)
            if desc:
                text += f"{desc}\n\n"
        text += f"## 标记 (flag)\n"
        for flag in entity.flags:
            text += f"> **{flag.display_name}** *= {flag.value}*\n\n"
            desc = get_flag_description(entity.name, flag.display_name)
            if desc is not None:
                text += f"{desc}\n\n"

        save_file(text, target_dir, entity.name + ".md")
        print(f"{entity.name} done.")

entities = load_fgd('./docs/resources/cs16_0.8.2.0_vl.fgd')
generate_pages(entities, "./docs/wiki/entity/", "wiki/entity")

