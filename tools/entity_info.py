def get_entity_link(entity_name):
    return f"[{entity_name}](wiki/entity/{entity_name})"

TipNeedOrigin = "需要轴心：需要配合origin纹理![origin](../../images/tex_origin.png \":no-zoom\")使用。TODO：待补充"
TipDefaultDirectionRight = "默认朝右：实体默认朝向X轴正方向（即俯视图向右侧），调整实体角度（hammer中旋转、或设置实体角度属性）可以改变方向。"
TipDefaultDirectionRightNoEditorRotation = "默认朝右：实体默认朝向X轴正方向（即俯视图向右侧），调整实体角度（只能设置实体角度，hammer中旋转无效）可以改变方向。"
TipWorkWithPath = "配合路径：需要配合路径使用，如何制作路径可参考[制作路径]()"

TipMustTrigger = "必须引发：本实体需要被引发才会产生效果。"
TipDoorTriggerFlagEnum = "注意，给门设置名字后，门就不能通过触碰打开了，只能通过引发打开。而“按E键打开”是个例外，可参考以下表格：\n- 名称× 按E键打开×：触碰打开\n- 名称√ 按E键打开×：只能引发打开\n- 名称× 按E键打开√：只有按E打开\n- 名称√ 按E键打开√：引发或按E打开"
TipTankControl = f"玩家控制：如果需要玩家控制，需要勾选“玩家控制”标记，并且配合{get_entity_link('func_tankcontrols')}实体使用，{get_entity_link('func_tankcontrols')}实体用于指定控制机枪的范围，玩家在范围可以控制该机枪。"

AlertRelayStateBug = "引擎BUG：trigger_relay实体的开、关设置对本实体无效，本实体永远以**锁定（toggle）**的方式运行，即引发后从开变成关、或从关变成开"
AlertModelInteractBug = "引擎BUG：对着模型按E会引发交互（会听到交互音效），不建议和按钮放到一起使用"
AlertOnlyOnce = "本实体只能使用一次/一回合。引发一次后，或者到新的回合后，实体会失效。"
AlertActivatorMissingCrash = "崩溃风险：如果本实体设置了只对引发的玩家起效果，要注意部分实体无法正确传递引发者信息（如trigger_relay），这可能导致游戏奔溃/闪退。"
AlertDoorRecoverBug = "门在新一局开始时会自动复位，同时**引发一次它的目标**，所以尽量不用门去引发其他实体。但是可以利用这个bug，实现每局开始的实体复位，详见[实现实体的每局复位]()。"

InfoModelPath = "模型放入models文件夹内，路径格式类似 ```models/myModels/myModel.mdl```，注意前面有 ```models/```。"
InfoSpritePath = "图标放入sprites文件夹内，路径格式类似 ```sprites/mySprites/mySprite.spr```，注意前面有 ```sprites/```。"
InfoPathOnlyCorner = f"填写{get_entity_link('path_corner')}点实体的名称，实体初始在这个点实体的位置，然后会在其对应的路径上运动。关于如何制作路径，可参考[制作路径]()"
InfoLightPattern = f"?> 摘自天书\n\n你可以自己定义灯光的样式。范围为a~z：a为全黑  z为全亮，中间字母依次过渡。比如：你在这里设置：“abcdefghijklmlkjihgfedcba”游戏里灯的亮度将会由黑到亮再到黑这样循环的变化。 \n\n注意：当你需要用到这个自定义样式的时候，必须给该实体起一个名字。你可以不让其他实体来引发他，但名字是必须的。"
InfoPlat = f"这个实体的工作模式比较特殊，这里特别说明一下。这个电梯和你想象的可能不同，这个实体当你站上去后它会上升，带你到高处，然后你下电梯后，他马上会自己跑到最下面，等另一个人上电梯，这个过程是全自动的，你是不能用引发来控制它上升下降的。如果不给他取名字，电梯最开始就在下面等着载人；取了名字的话，最开始它在最上面，要按了按钮它才开始工作，跑到最下面等人。"

ENTITIY_INFO = {
    "ambient_generic": {
        "tags": ["音效"],
        "short_description": "播放声音",
        "full_description": "用于播放声音的点实体，声音以点实体为中心，距离越远声音越小",
        "tips": [
            "播放的声音文件需要满足一定格式（wav、PCM编码）、8bit或16bit、单声道、频率不能太高），可以参考这篇指南[《【CS地图教程】快速音效制作指南》](https://www.bilibili.com/read/cv21285786)制作自己的声音文件"
        ],
        "alerts": [
            AlertRelayStateBug
        ]
    },
    "armoury_entity": {
        "tags": [],
        "short_description": "放置武器",
        "full_description": "用于放置武器的点实体，武器可捡起。",
    },
    "button_target": {
        "tags": [],
        "short_description": "标靶开关（攻击它时引发）", 
        "full_description": "用于制作标靶开关的固体实体，被攻击时会引发，默认情况下按E不会引发。",
        "tips": [
        ]
    },
    "cycler": {
        "tags": ["模型"],
        "short_description": "展示模型（模型有碰撞体积）", 
        "full_description": "用于展示模型的点实体。模型会和玩家碰撞。支持模型动画，动画会循环播放。",
        "tips": [
            f"本实体如果用来显示模型，模型会有碰撞体积，玩家会被模型阻挡，攻击模型后模型会出绿血。如果不希望这种事情发生，可以使用{get_entity_link('cycler_sprite')}"
        ],
        "alerts": [
            AlertModelInteractBug
        ]
    },
    "cycler_sprite": {
        "tags": ["模型", "图标"],
        "short_description": "展示模型、图标（模型无碰撞体积）",
        "full_description": "用于展示模型、图标的点实体。模型不会和玩家碰撞。支持模型动画，动画会循环播放。",
        "tips": [
            f"如果是需要显示图标，建议使用{get_entity_link('env_sprite')}，{get_entity_link('env_sprite')}在hammer里能直接看到效果，方便调整。",
            f"本实体效果类似func_illusionary实体，只显示模型，玩家和子弹可以穿过模型。如果不希望玩家穿过模型，可以使用{get_entity_link('cycler')}，或者放置透明的固体用于阻挡。"
        ],
        "alerts": [
            AlertModelInteractBug
        ]
    },
    "cycler_wreckage": {
        "tags": ["图标"],
        "short_description": "模拟蒸汽效果",
        "full_description": "用于模拟蒸汽效果的点实体。TODO：补充",
    },
    "env_beam": {
        "tags": [],
        "short_description": "闪电效果",
        "full_description": "用于实现闪电的点实体。可造成伤害。",
        "tips": []
    },
    "env_beverage": {
        "tags": [],
        "short_description": "生成拉罐饮料模型",
        "full_description": "用于生成拉罐饮料模型的点实体，可用来做自动售货机。引发后TODO：补充。",
        "tips": [
            TipMustTrigger,
            TipDefaultDirectionRight
        ],
        "alerts": [
            "只有第一次引发时会产生饮料，后面引发不会再产生。"
        ]
    },
    "env_blood": {
        "tags": [],
        "short_description": "喷血效果",
        "full_description": "用于实现喷血效果的点实体。引发后TODO：补充。",
        "tips": [
            TipMustTrigger,
            TipDefaultDirectionRight
        ],
        "alerts": [
            "只有第一次引发时会产生饮料，后面引发不会再产生。"
        ]
    },
    "env_bubbles": {
        "tags": ["默认不可见", "默认可穿过", "可开关"],
        "short_description": "产生泡泡",
        "full_description": "用于产生泡泡的固体实体，从固体覆盖的范围底部产生。唯一的env开头的固体实体。",
        "tips": [
            "引发本实体时才会生成饮料模型",
            TipDefaultDirectionRight
        ],
    },
    "env_explosion": {
        "tags": [],
        "short_description": "产生爆炸",
        "full_description": "用于产生爆炸的点实体，引发会从该位置产生一次爆炸（类似手雷或C4的爆炸），可以产生伤害。",
        "tips": [
            TipMustTrigger,
        ]
    },
    "env_fade": {
        "tags": ["屏幕效果"],
        "short_description": "画面淡入淡出",
        "full_description": "用于实现画面淡入淡出的点实体。默认情况下，实体引发后画面会慢慢被选定的颜色覆盖，完全覆盖后持续一段事件，然后效果会立刻消失并恢复正常画面。",
        "tips": [
            TipMustTrigger,
        ],
        "alerts": [
            AlertActivatorMissingCrash,
            "建议：请尽量勾选“只对引发者有效”标记，以免某人引发本实体让所有玩家都被影响，非常影响体验。但要注意上一条提醒的崩溃问题。"
        ]
    },
    "env_fog": {
        "tags": [],
        "short_description": "产生雾",
        "full_description": "在全图范围内产生雾的点实体。",
        "tips": [
        ],
        "alerts": [
            "和X-man天书中介绍的不同，本实体开启后全图都会笼罩在雾中，而非X-man天书中描述的可以设置覆盖范围。"
        ]
    },
    "env_funnel": {
        "tags": [],
        "short_description": "产生烟雾",
        "full_description": "用于产生烟雾的点实体，烟雾不断从一个点产生，然后上升、消失。一般用于制作烟囱里出来的炊烟。",
        "tips": [
            TipMustTrigger,
        ],
        "alerts": [
            AlertOnlyOnce
        ]
    },
    "env_global": {
        "tags": ["控制"],
        "short_description": "全局状态设置实体",
        "full_description": "用于设置全局状态的点实体。什么是全局状态可以看属性“设置全局状态实体”的介绍。",
        "tips": [
            TipMustTrigger,
        ],
    },
    "env_glow": {
        "tags": [],
        "short_description": "产生光晕",
        "full_description": "产生光晕图标的点实体。一般放在光源处做装饰。",
        "tips": [],
    },
    "env_laser": {
        "tags": [],
        "short_description": "产生激光",
        "full_description": "产生激光效果的点实体。可造成伤害。",
        "tips": [],
    },
    "env_message": {
        "tags": ["屏幕效果"],
        "short_description": "显示屏幕文字",
        "full_description": "用于显示文字的点实体。文字直接显示在屏幕HUD上。",
        "tips": [
            TipMustTrigger,
        ],
        "alerts": [
            AlertActivatorMissingCrash,
            f"不建议使用本实体，因为需要更改游戏目录中的文件。建议使用{get_entity_link('game_text')}替代。"
        ]
    },
    "env_rain": {
        "tags": [],
        "short_description": "下雨效果",
        "full_description": "用于实现下雨效果的点实体。放在地图里就会起效果。",
        "tips": []
    },
    "env_render": {
        "tags": [],
        "short_description": "修改渲染设置",
        "full_description": "用于修改其他实体渲染效果的点实体。引发本实体后，会修改本实体的目标的渲染设置（包括渲染模式、渲染效果、透明度和渲染色），将其修改成本实体设置好的值。",
        "tips": [
            TipMustTrigger,
        ],
    },
    "env_shake": {
        "tags": [],
        "short_description": "地震效果",
        "full_description": "用于实现地震效果的点实体。被地震效果影响时，玩家屏幕会发生抖动。只影响设置范围（以点实体位置为中心）内的玩家。",
        "tips": [
            TipMustTrigger,
        ],
        "alerts": [
            f"回合刷新不会消除地震状态，地震会持续，因此记得合理调整地震时间。"
        ]
    },
    "env_shooter": {
        "tags": [],
        "short_description": "喷射模型或图标",
        "full_description": "用于喷射模型或图标的点实体。",
        "tips": [
            TipMustTrigger,
        ],
    },
    "env_snow": {
        "tags": [],
        "short_description": "下雪效果",
        "full_description": "用于实现下雪效果的点实体。放在地图里就会起效果。",
        "tips": []
    },
    "env_sound": {
        "tags": [],
        "short_description": "改变环境回声音效",
        "full_description": "用于改变环境回声音效的点实体。可以用来模拟空旷空间里的回声。以实体为中心，穿过设置的半径范围的玩家会更新回声状态，**注意：这个状态会持续，直到新回合或者其他env_sound重新设置。**",
    },
    "env_spark": {
        "tags": [],
        "short_description": "产生火花效果",
        "full_description": "用于产生火花效果的点实体。开启状态下，火花会每隔一段时间闪烁一次。可以用引发来开启/关闭。**",
    },
    "env_sprite": {
        "tags": [],
        "short_description": "显示图标（.spr）",
        "full_description": "用于显示图标（.spr）的点实体。可以用引发来开启关闭，开启则显示，关闭则消失。",
        'tips': []
    },
    "func_bomb_target": {
        "tags": ["游戏模式"],
        "short_description": "炸弹（C4）放置区域",
        "full_description": "用于指定炸弹（C4）放置区域的固体实体。",
        "tips": [
            "注意，放置这个实体会改变游戏模式，T出生会有一个人带有C4，在指定地点安放C4，CT要阻止T放置C4，或拆卸C4。"
        ]
    },
    "func_breakable": {
        "tags": [],
        "short_description": "可破碎的物体",
        "full_description": "用于制作可破碎的物体的固体实体。可以制作能被打破、撞破、踩破等效果的物体。注意如果指定了实体名称，则它不再能被玩家破坏，只能被引发破坏。本实体的目标会在破碎时引发（如设置了引发前延时，则是破碎时开始计时）。",
    },
    "func_button": {
        "tags": [],
        "short_description": "可破碎的物体",
        "full_description": "用于制作可破碎的物体的固体实体。可以制作能被打破、撞破、踩破等效果的物体。注意如果指定了实体名称，则它不再能被玩家破坏，只能被引发破坏。本实体的目标会在破碎时引发（如设置了引发前延时，则是破碎时开始计时）。",
        "tips": []
    },
    "func_buyzone": {
        "tags": [],
        "short_description": "购买区域",
        "full_description": "用于指定购买区域的固体实体。",
        "tips": [
            "注意，如果地图里没有这个实体，会自动在玩家出生点周围指定一块默认购买区域。如果你不希望玩家购买武器，可以放一个这个实体在玩家到不了的地方"
        ]
    },
    "func_conveyor": {
        "tags": [],
        "short_description": "传送带",
        "full_description": "用于制作传送带的固体实体。玩家站在传送带上会跟着移动。",
        "tips": [
            "可以配合[滚动纹理]()使用，让传送带看起来在滚动。可参考[【简单解析】WAD文件](https://www.bilibili.com/read/cv4682202)中的滚动纹理部分。",
            "传送带上小跳可以很快地加速。"
        ]
    },
    "func_door": {
        "tags": [],
        "short_description": "推拉门（平移着打开、关闭的门）",
        "full_description": "用于制作推拉门（平移着打开、关闭的门）的固体实体。默认情况下，玩家触碰到门后，门会向设置的方向平移打开。",
        "tips": [
            TipDefaultDirectionRightNoEditorRotation,
            TipDoorTriggerFlagEnum
        ],
        "alerts": [
            AlertDoorRecoverBug
        ]
    },
    "func_door_rotating": {
        "tags": [],
        "short_description": "转门（旋转打开、关闭的门）",
        "full_description": "用于制作转门（旋转打开、关闭的门）的固体实体。默认情况下，玩家触碰到门后，门会向玩家反方向旋转打开。",
        "tips": [
            TipNeedOrigin,
            TipDoorTriggerFlagEnum
        ],
        "alerts": [
            AlertDoorRecoverBug
        ]
    },
    "func_escapezone": {
        "tags": ["游戏模式"],
        "short_description": "T逃脱区域",
        "full_description": "用于指定炸T逃脱区域的固体实体。",
        "tips": [
            "注意，放置这个实体会改变游戏模式，当T接触到该实体的区域后，T获胜。"
        ],
    },
    "func_friction": {
        "tags": [],
        "short_description": "修改地面摩檫力",
        "full_description": "用于修改地面摩檫力的固体实体。玩家进入实体范围后和地面摩檫力会改变，可以用来实现类似冰面的效果。回合开始时摩檫力会重置。",
        "tips": [
            "注意，放置这个实体会改变游戏模式，当T接触到该实体的区域后，T获胜。"
        ]
    },
    "func_grencatch": {
        "tags": [],
        "short_description": "手雷引发区域",
        "full_description": "用于实现手雷引发的固体实体。有手雷进入该区域时，会引发它的目标。",
        "alerts": [
            AlertOnlyOnce
        ]
    },
    "func_guntarget": {
        "tags": [],
        "short_description": "枪靶",
        "full_description": f"用于实现枪靶的固体实体。枪靶可以像{get_entity_link('func_train')}一样移动，在被攻击后会停下来，并引发它的目标。",
        "tips": [],
        "alerts": [
            AlertOnlyOnce
        ]
    },
    "func_healthcharger": {
        "tags": [],
        "short_description": "补血站",
        "full_description": f"用于制作补血站的固体实体。对着补血站按E可以补血，血站会提供50点HP，用完后过需要一段时间恢复，恢复后可以再补血。",
        "tips": []
    },
    "func_hostage_rescue": {
        "tags": [],
        "short_description": "人质获救区域",
        "full_description": "用于指定人质获救区域的固体实体。人质进入该区域后会获救并消失。",
        "tips": [
            "注意，放置这个实体会改变游戏模式，所有人质获救后，CT获胜，否则倒计时结束后T获胜。"
        ],
    },
    "func_illusionary": {
        "tags": [],
        "short_description": "看得见摸不着的实体",
        "full_description": "用于制作看得见摸不着的实体的固体实体。玩家能看见这个实体，但能穿过它，子弹也可以穿过它。",
    },
    "func_ladder": {
        "tags": [],
        "short_description": "梯子",
        "full_description": f"用于制作梯子的固体实体。玩家接触它的表面后会变成爬梯子的状态。注意这个实体本身不可见，用它做梯子时有几种方法：\n1. 制作一个梯子的外表（一般使用{'{'}开头的[透明纹理]()，转为func_wall，渲染模式选固体），再用一层{get_entity_link('func_ladder')}贴在它的表面\n2. 用{get_entity_link('func_illusionary')}制作一个梯子的外表（一般使用{'{'}开头的[透明纹理]()，渲染模式选固体），然后放一个{get_entity_link('func_ladder')}和它完全重叠",
    },
    "func_mortar_field": {
        "tags": [],
        "short_description": "空中支援区域",
        "full_description": f"用于实现空中支援的固体实体。引发时会在它范围内投一堆闪光弹。",
        "tips": [
            TipMustTrigger,
        ]
    },
    "func_pendulum": {
        "tags": [],
        "short_description": "来回摆动的物体",
        "full_description": f"用于制作摆动物体的固体实体。物体会绕着轴心循环摆动，可以制作摆钟、秋千等。",
        "tips": [
            TipNeedOrigin,
        ]
    },
    "func_plat": {
        "tags": [],
        "short_description": "电梯",
        "full_description": f"用于制作电梯的固体实体。站在上面的玩家会随他一起上升到指定高度。\n\n" + InfoPlat,
        "tips": [],
        "alerts": [
            "实体在编辑器里必须放在最高的位置，进入游戏后会自动降到最低位置。"
        ]
    },
    "func_platrot": {
        "tags": [],
        "short_description": "电梯（可旋转）",
        "full_description": f"用于制作可旋转电梯的固体实体。和{get_entity_link('func_plat')}几乎相同，但是可以旋转。站在上面的玩家会随他一起旋转并上升到指定高度。\n\n" + InfoPlat,
        "tips": [
            TipNeedOrigin,
        ],
        "alerts": [
            "实体在编辑器里必须放在最高的位置，进入游戏后会自动降到最低位置。"
        ]
    },
    "func_pushable": {
        "tags": [],
        "short_description": "可推动的物体",
        "full_description": f"用于制作可推动物体的固体实体。玩家可以推着物体走，也可以按E拉住物体。",
        "alerts": [
            "引擎BUG：这个实体在新的回合不会复位，上回合在什么位置，新的回合就会留在那个位置。如果设置了可打碎，则破碎后新回合也不会复原。"
        ]
    },
    "func_recharge": {
        "tags": [],
        "short_description": "补甲站",
        "full_description": f"用于制作加甲站的固体实体。对着补甲站按E可以补充护甲，补甲站会提供50点护甲，用完后过需要一段时间恢复，恢复后可以再补甲。",
        "tips": []
    },
    "func_rot_button": {
        "tags": [],
        "short_description": "会转动的开关",
        "full_description": f"用于制作会转动的开关的固体实体。和普通开关的主要区别是引发时会转动。",
        "tips": [
            TipNeedOrigin,
        ]
    },
    "func_rotating": {
        "tags": [],
        "short_description": "不停转动的物体",
        "full_description": f"用于制作转动物体的固体实体。物体会不停地转动，可以用来制作风扇、转盘等物体。",
        "tips": [
            TipNeedOrigin,
        ]
    },
    "func_tank": {
        "tags": [],
        "short_description": "机枪",
        "full_description": f"用于制作机枪的固体实体。机枪能发出子弹，默认是电脑自动控制，也可以设置为玩家控制。",
        "tips": [
            TipTankControl,
            TipNeedOrigin,
            TipDefaultDirectionRightNoEditorRotation,
        ]
    },
    "func_tankcontrols": {
        "tags": [],
        "short_description": "机枪、大炮、激光炮的控制区域",
        "full_description": f"用于指定机枪、大炮、激光炮控制区域的固体实体。机枪{get_entity_link('func_tank')}、大炮{get_entity_link('func_tanklaser')}、激光炮{get_entity_link('func_tankmortar')}需要玩家控制时，用实体框定一个区域，指定目标为上面几种武器的名称，玩家进入实体的区域就能控制该武器。",
    },
    "func_tanklaser": {
        "tags": [],
        "short_description": "激光枪",
        "full_description": f"用于制作激光枪的固体实体。激光枪能发出激光，默认是电脑自动控制，也可以设置为玩家控制。",
        "tips": [
            TipTankControl,
            f"本实体还需要配置{get_entity_link('env_laser')}激光点实体使用，制作一个{get_entity_link('env_laser')}激光点实体，放在地图任何位置都可以，设置激光的样式，然后设置它的“激光目标”属性为激光枪。激光枪的“env_laser 实体”属性也要填这个激光点实体的名称。",
            TipNeedOrigin,
            TipDefaultDirectionRightNoEditorRotation,
        ]
    },
    "func_tanklaser": {
        "tags": [],
        "short_description": "激光枪",
        "full_description": f"用于制作激光枪的固体实体。激光枪能发出激光，默认是电脑自动控制，也可以设置为玩家控制。",
        "tips": [
            TipTankControl,
            f"本实体还需要配置{get_entity_link('env_laser')}激光点实体使用，制作一个{get_entity_link('env_laser')}激光点实体，放在地图任何位置都可以，设置激光的样式，然后设置它的“激光目标”属性为激光枪。激光枪的“env_laser 实体”属性也要填这个激光点实体的名称。",
            TipNeedOrigin,
            TipDefaultDirectionRightNoEditorRotation,
        ]
    },
    "func_tankmortar": {
        "tags": [],
        "short_description": "大炮",
        "full_description": f"用于制作大炮的固体实体。大炮能制造爆炸（在瞄准位置制造类似手雷、C4的爆炸，造成伤害），默认是电脑自动控制，也可以设置为玩家控制。",
        "tips": [
            TipTankControl,
            f"本实体还需要配置{get_entity_link('env_laser')}激光点实体使用，制作一个{get_entity_link('env_laser')}激光点实体，放在地图任何位置都可以，设置激光的样式，然后设置它的“激光目标”属性为激光枪。激光枪的“env_laser 实体”属性也要填这个激光点实体的名称。",
            TipNeedOrigin,
            TipDefaultDirectionRightNoEditorRotation,
            f"如果你想让大炮更逼真，还可以模拟出射击后的地面振动效果。制作一个{get_entity_link('enc_shake')}实体，大炮的名称填它（声音点实体和地震点实体名称可以一样）即可。"
        ]
    },
    "func_trackautochange": {
        "tags": [],
        "short_description": "自动火车的立体变轨平台",
        "full_description": f"用于制作火车自动立体变轨平台的固体实体。可控制火车做上下、旋转的变轨（半条命1里有很多这种变轨系统），只能用于玩家不能控制的{get_entity_link('func_tracktrain')}实体，要玩家控制的变轨可使用{get_entity_link('func_trackchange')}。实体默认停在“第一路径”的位置。**待补充：具体的用法还不太清楚，欢迎使用过它的朋友补充。**",
        "tips": [
            TipMustTrigger,
            TipNeedOrigin,
        ]
    },
    "func_trackchange": {
        "tags": [],
        "short_description": "玩家控制火车的立体变轨平台",
        "full_description": f"用于制作玩家控制火车的自动立体变轨平台的固体实体。可控制火车做上下、旋转的变轨（半条命1里有很多这种变轨系统），只能用于玩家控制的{get_entity_link('func_tracktrain')}实体，要玩家不能控制的变轨可使用{get_entity_link('func_trackautochange')}。实体默认停在“第一路径”的位置。**待补充：具体的用法还不太清楚，欢迎使用过它的朋友补充。**",
        "tips": [
            TipMustTrigger,
            TipNeedOrigin,
        ]
    },
    "func_tracktrain": {
        "tags": [],
        "short_description": "火车",
        "full_description": f"用于火车的固体实体。火车按固定轨道行驶，可以是自动驾驶的，也可以玩家控制。如果需要玩家控制，则使用{get_entity_link('func_traincontrols')}指定控制区域。玩家控制时，在控制区域内按E开始控制火车，W加速，S减速/倒车。",
        "tips": [
            TipMustTrigger,
            TipNeedOrigin,
            TipWorkWithPath,
            "朝左放置：实体默认头朝向X轴反方向（即俯视图向左侧），在制作时确保车头方向也是这样。然后游戏中火车的朝向是自动决定的（从当前路径点指向下一个路径点）。",
            "放在任意位置：火车会出现在设置的路径点处，与你在编辑器里放的位置无关，你可以放在任意位置上。",
        ]
    },
    "func_train": {
        "tags": [],
        "short_description": "移动平台",
        "full_description": f"用于制作移动平台的固体实体。移动平台会在指定的路径上移动，可以用来制作电梯、载人平台、移动的障碍物等等物体。",
        "tips": [
            TipMustTrigger,
            TipNeedOrigin,
            TipWorkWithPath,
        ]
    },
    "func_traincontrols": {
        "tags": [],
        "short_description": "火车控制区域",
        "full_description": f"用于指定火车控制区域的固体实体。玩家在区域内按E可以控制目标火车。",
        "tips": [
            "火车控制区域会自动跟着火车一起移动，用它框住火车的驾驶范围即可。",
        ]
    },
     "func_vehicle": {
        "tags": [],
        "short_description": "载具",
        "full_description": f"用于制作载具的固体实体。玩家可以控制载具前后左右移动，用于制作汽车、飞机等。",
        "tips": [
            TipMustTrigger,
            TipNeedOrigin,
            TipWorkWithPath,
            f"朝左放置：实体默认头朝向X轴反方向（即俯视图向左侧），在制作时确保载具的朝向也是这样。然后进入游戏里，载具的朝向有两种方法控制：\n\n1. 调整实体角度属性。但这会有一个bug，这个属性只在第一回合生效，之后的回合，载具会回到初始位置，但是朝向却保留了上回合结束的状态...特别是如果载具上回合停在斜坡上，这回合刚开始载具就是歪的，不建议使用。\n2. 制作两个{get_entity_link('path_track')}路径点A和B，路径点A的“下一个路径点”属性填B的名称，然后载具的“路径点”填A的名字，这样每回合开始载具会回到路径点A，头朝向路径点B。",
        ]
    },
    "func_vehiclecontrols": {
        "tags": [],
        "short_description": "载具控制区域",
        "full_description": f"用于指定载具控制区域的固体实体。玩家在区域内按E可以控制目标载具。",
        "tips": [
            "载具控制区域会自动跟着载具一起移动，用它框住载具的驾驶范围即可。",
        ]
    },
    "func_vip_safetyzone": {
        "tags": ["游戏模式"],
        "short_description": "VIP逃脱区域",
        "full_description": "用于指定VIP逃脱区域的固体实体。",
        "tips": [
            "注意，放置这个实体会改变游戏模式，CT出生会有一个人变成VIP，VIP持有一把USP和一把匕首，有200点护甲，不能购买、捡起或使用其他武器，VIP到达逃脱区域后CT胜利，VIP死亡或倒计时结束后T获胜。"
        ]
    },
    "func_wall": {
        "tags": [],
        "short_description": "普通实体",
        "full_description": "和普通的固体类似的固体实体。表现基本和固体相同，但可以实现一些实体的效果，比如半透明。",
        "tips": [
            "X-man天书：当你用的是+A开头的动画纹理（需要引发才能改变的纹理）给该固体贴图的时候，那么他的引发结果就是改变纹理！除此以外这个实体的名称是没有任何意义的。"
        ]
    },
    "func_wall_toggle": {
        "tags": [],
        "short_description": "切换出现消失的实体",
        "full_description": f"用于制作可切换出现消失物体的固体实体。被引发时会在出现/消失之间切换，出现时和{get_entity_link('func_wall')}没有区别，消失后看不见也碰不着。",
        "tips": []
    },
    "func_water": {
        "tags": [],
        "short_description": "水",
        "full_description": f"用于制作水等液体的固体实体。玩家进入液体会变成游泳状态，在液体下呆太久会窒息开始掉血，离开液体后这部分血量会慢慢恢复。液体只有上表面可见，下表面和侧面都是透明的。这个实体包含了很多和{get_entity_link('func_door')}相同的属性，功能也是相同的。",
        "tips": []
    },
    "func_weaponcheck": {
        "tags": [],
        "short_description": "检查携带武器",
        "full_description": f"用于实现携带武器检查的固体实体。玩家在范围内时会检查其携带的武器是否符合要求，然后引发对应的目标。",
        "tips": [],
        "alerts": [
            AlertOnlyOnce
        ]
    },
    "game_counter": {
        "tags": [],
        "short_description": "计数器",
        "full_description": f"用于实现计数器的点实体。本实体每次被引发，内置的计数值都会+1，当达到设定的限定值后，本实体会引发目标。如果设置“引发后复位”，引发目标后计数值会恢复到初始值，能重新开始计数，反复使用。",
        "tips": [
            f"本实体能传输引发者的信息，这一点优于{get_entity_link('trigger_relay')}点实体，可以用它做{get_entity_link('game_text')}、{get_entity_link('env_fade')}等的中继。",
            f"你可以用{get_entity_link('game_counter_set')}直接设置本实体当前的计数值。",
        ],
    },
    "game_counter_set": {
        "tags": [],
        "short_description": "设置计数器的值",
        "full_description": f"用于设置计数器的点实体。目标是{get_entity_link('game_counter')}，能直接设置它的计数值。",
        "tips": [],
    },
    "game_end": {
        "tags": [],
        "short_description": "结束游戏",
        "full_description": f"用于结束游戏的点实体。被引发后会让游戏结束。",
        "tips": [],
    },
    "game_player_equip": {
        "tags": [],
        "short_description": "初始武器/分发武器",
        "full_description": f"用于发枪的点实体。默认会在回合开始时对所有玩家自动引发，也可以被手动引发，引发后给引发者发枪械、弹药、匕首、医疗包和盔甲等装备。",
        "tips": [],
        "alerts": [
            f"地图中使用该实体后，无论有没有勾选“只能引发”，玩家不会再发默认武器了（CT是匕首+USP，T是匕首+Glock18）。如果没有勾选“只能引发”，每回合开始玩家会得到这个实体指定的装备（上局的装备依旧保留）；而如果勾选了“只能引发”，因为不再发默认武器，如果玩家是新加入的、或者上回合死亡了，玩家只会变空手，什么武器都没有。建议使用这个实体时配合{get_entity_link('player_weaponstrip')}，每回合开始先剥夺武器，然后发固定的枪，这样能保证每回合开始的枪都一样。",
            "发的武器不能太多，不然可能导致地图崩溃闪退。",
        ]
    },
    "game_player_hurt": {
        "tags": [],
        "short_description": "伤害/治疗",
        "full_description": f"用于造成伤害/治疗的点实体。引发后会对引发者造成伤害，或者加血。",
        "tips": [],
    },
    "game_score": {
        "tags": [],
        "short_description": "加分、减分",
        "full_description": f"用于给玩家加分、减分的点实体。指计分板里的分数。",
        "tips": [],
    },
    "game_team_master": {
        "tags": [],
        "short_description": "（废弃）确认玩家队伍",
        "full_description": f"用于确认玩家队伍的点实体，**但因为BUG无法正常使用**。与此相关的game_team_set点实体也无法正常使用。",
        "tips": [],
        "alerts": ["因为存在BUG已废弃，本实体不能正确辨别玩家队伍，不能正常使用。"],
    },
    "game_text": {
        "tags": [],
        "short_description": "显示文本",
        "full_description": f"用于显示文本的点实体。文本直接显示在屏幕HUD上。",
        "tips": [
            TipMustTrigger,
        ],
        "alerts": [
            f"如果没有勾选了“对所有玩家”，注意玩家引发时要正确传递引发者属性（比如不能用{get_entity_link('trigger_relay')}做中继），否则游戏会立刻卡死并闪退。"
        ],
    },
    "game_zone_player": {
        "tags": [],
        "short_description": "判断玩家所在区域",
        "full_description": f"用于判断玩家所在区域的固体实体。根据不同的条件执行不同的功能，详情看属性。",
        "tips": [],
    },
    "gibshooter": {
        "tags": [],
        "short_description": "喷射肢体碎片",
        "full_description": f"用于喷射肢体碎片的点实体。",
        "tips": [],
    },
    "hostage_entity": {
        "tags": [],
        "short_description": "人质",
        "full_description": f"用于放置人质的点实体。就是解救人质模式里的人质。",
        "tips": [],
    },
    "info_bomb_target": {
        "tags": [],
        "short_description": "人质",
        "full_description": f"用于放置人质的点实体。就是解救人质模式里的人质。",
        "tips": [
            f"不建议使用，炸弹放置范围不好控制，推荐使用{get_entity_link('func_bomb_target')}"
        ],
    },
    "info_bomb_target": {
        "tags": ["游戏模式"],
        "short_description": "炸弹（C4）放置区域（不推荐使用）",
        "full_description": "用于指定炸弹（C4）放置区域的点实体，点实体周围距离256（也可能是128）单位以内的范围变成炸弹安置区域。",
        "tips": [
            f"不建议使用，炸弹放置范围不好控制，推荐使用{get_entity_link('func_bomb_target')}。",
            "注意，放置这个实体会改变游戏模式，T出生会有一个人带有C4，在指定地点安放C4，CT要阻止T放置C4，或拆卸C4。"
        ]
    },
    "info_hostage_rescue": {
        "tags": [],
        "short_description": "人质获救区域（不推荐使用）",
        "full_description": "用于指定人质获救区域的点实体，点实体周围距离256（也可能是128）单位以内的范围变成人质获救区域。人质进入该区域后会获救并消失。",
        "tips": [
            "注意，放置这个实体会改变游戏模式，所有人质获救后，CT获胜，否则倒计时结束后T获胜。"
        ],
    },
    "info_map_parameters": {
        "tags": [],
        "short_description": "地图设置（购买限制、C4爆炸范围）",
        "full_description": "用于修改一些地图设置的点实体。只有两个可以修改的设置，一个是限制能否购买武器，另一个是设置C4爆炸范围。",
    },
    "info_null": {
        "tags": [],
        "short_description": "聚光灯目标",
        "full_description": f"专用做{get_entity_link('light_spot')}聚光灯的目标，设置后聚光灯就会朝向本实体照射。",
    },
    "info_player_deathmatch": {
        "tags": [],
        "short_description": "土匪（T）出生点",
        "full_description": f"用于指定土匪（T）的点实体。放在哪里玩家就会出生在哪里，注意不要卡在墙里或地下，否则玩家出生也会卡住。",
    },
    "info_player_start": {
        "tags": [],
        "short_description": "警察（CT）出生点",
        "full_description": f"用于指定警察（CT）的点实体。放在哪里玩家就会出生在哪里，注意不要卡在墙里或地下，否则玩家出生也会卡住。",
    },
    "info_target": {
        "tags": [],
        "short_description": "闪电/激光目标",
        "full_description": f"专用做{get_entity_link('env_beam')}闪电和{get_entity_link('env_laser')}激光的起点、终点。",
    },
    "info_teleport_destination": {
        "tags": [],
        "short_description": "传送终点",
        "full_description": f"专用做{get_entity_link('trigger_teleport')}传送区的目标。本实体的中心对应的是传送后玩家的脚底，所以可以放在贴合地面的位置。",
    },
    "info_texlights": {
        "tags": [],
        "short_description": "发光纹理设置",
        "full_description": f"和lights.rad发光纹理设置文件的功能相同，给这个纹理添加键值来设置编译时的发光纹理，添加键值的方法类似{get_entity_link('multi_manager')}。\n\n添加的格式为\n\n```\nkey: 纹理名称\nvalue: R G B 亮度\n```\n\n比如你希望mylight1纹理发红色的亮度为1000的光，则添加一个叫做```mylight1```的键，值为```255 0 0 1000```",
    },
    "info_vip_start": {
        "tags": [],
        "short_description": "VIP出生点",
        "full_description": f"用于指定VIP的点实体。放在哪里玩家就会出生在哪里，注意不要卡在墙里或地下，否则玩家出生也会卡住。",
    },
    "infodecal": {
        "tags": [],
        "short_description": "印花纹理",
        "full_description": f"用于制作印花纹理的点实体。一般不直接用它，而是用hammer的印花纹理工具制作，否则很难控制它贴的效果。印花纹理能制作贴在墙上的额外图标（比如C4爆炸点的叉、墙上的AB点标记、血迹等等。",
    },
    "item_airtank": {
        "tags": [],
        "short_description": "氧气罐",
        "full_description": f"用于放置氧气罐的点实体。一般放在水下，靠近后可以补充氧气（重置缺氧计时），攻击后会爆炸然后产生类似闪光弹爆炸的效果（玩家屏幕全白一段时间）。",
        "tips": [],
        "alerts": [
            "被破坏后会永远消失，除非重新载入地图。"
        ],
    },
    "item_antidote": {
        "tags": [],
        "short_description": "解毒药",
        "full_description": f"用于生成解毒药的点实体。会在放置的位置生成一瓶解毒药，能终止玩家受到的瓦斯、毒的持续伤害。",
        "tips": [
            "被拾取后过一段时间（30秒）会重新生成。"
        ],
    },
    "item_assaultsuit": {
        "tags": [],
        "short_description": "护甲（带头盔）",
        "full_description": f"用于生成护甲（带头盔）的点实体。会在放置的位置生成一个护甲（带头盔），玩家接触可以拾起或补满护甲。",
        "tips": [
            "被拾取后过一段时间（30秒）会重新生成。"
        ],
    },
    "item_kevlar": {
        "tags": [],
        "short_description": "护甲（不带头盔）",
        "full_description": f"用于生成护甲（不带头盔）的点实体。会在放置的位置生成一个护甲（不带头盔），玩家接触可以拾起或补满护甲。",
        "tips": [
            "被拾取后过一段时间（30秒）会重新生成。"
        ],
    },
    "item_battery": {
        "tags": [],
        "short_description": "护甲补充包",
        "full_description": f"用于生成护甲补充包的点实体。实际对应了半条命的电池，捡起能补充15点护甲。",
        "tips": [
            "被拾取后过一段时间（30秒）会重新生成。"
        ],
    },
    "item_healthkit": {
        "tags": [],
        "short_description": "补血包",
        "full_description": f"用于生成补血包的点实体。捡起能补充30点HP。",
        "tips": [
            "被拾取后过一段时间（30秒）会重新生成。"
        ],
    },
    "item_longjump": {
        "tags": [],
        "short_description": "长跳包",
        "full_description": f"用于生成长跳包的点实体。这里的长跳不是KZ的长跳，是类似喷气背包的功能，按住Ctrl然后跳可以向前弹射，但是注意，长跳包只在老版的CS里能用，最新版（Steam）的CS不再能使用了，捡起来也不能进行长跳。",
        "tips": [
            "被拾取后过一段时间（30秒）会重新生成。"
        ],
        "alerts": [
            "长跳包只在老版的CS里能用，最新版（Steam）的CS不再能使用了，捡起来也不能进行长跳。"
        ],
    },
    "item_security": {
        "tags": [],
        "short_description": "通行卡",
        "full_description": f"用于生成通行卡的点实体。通行卡并没有特殊的作用。",
        "tips": [
            "被拾取后过一段时间（30秒）会重新生成。"
        ],
    },
    "item_thighpack": {
        "tags": [],
        "short_description": "拆弹器",
        "full_description": f"用于生成拆弹器的点实体。CT可以捡起来使用。",
        "tips": [
            "被拾取后过一段时间（30秒）会重新生成。"
        ],
        "alerts": [
            "只在第一回合出现，此后的回合不再出现。"
        ],
    },
    "light": {
        "tags": [],
        "short_description": "点光源",
        "full_description": f"用于放置点光源的点实体。点光源会照亮它附近的物体，常用在室内照明上，可以用其他实体控制它开关。",
        "tips": [],
    },
    "light_environment": {
        "tags": [],
        "short_description": "环境光源",
        "full_description": f"用于指定环境光源的点实体。环境光源用来模拟太阳、月亮，是覆盖整个地图的平行光，整个地图放置一个即可。",
        "tips": [],
    },
    "light_spot": {
        "tags": [],
        "short_description": "聚光光源",
        "full_description": f"用于制作聚光光源的点实体。类似手电筒、台灯、路灯那样聚光灯/探照灯，朝着一个固定方向、一定角度内照明。",
        "tips": [
            f"你可设置它的目标为{get_entity_link('info_null')}或者{get_entity_link('info_target')}，这样他就会指向目标的位置。或者单纯用实体角度来控制方向（虽然很不直观）。"
        ],
    },
    "momentary_door": {
        "tags": [],
        "short_description": "连续的推拉门",
        "full_description": f"用于制作连续的推拉门的固体实体。和{get_entity_link('func_door')}类似，但它不是只有打开和关闭两种状态，而是由阀门控制逐渐打开关闭（阀门拧一点就开一点，要一直拧才会逐渐完全打开）。只能由{get_entity_link('momentary_rot_button')}引发。",
        "tips": [],
    },
    "momentary_rot_button": {
        "tags": [],
        "short_description": "连续阀门开关",
        "full_description": f"用于制作连续阀门开关的固体实体。配合{get_entity_link('momentary_door')}使用，玩家要对它按住E来转动阀门，缓慢打开{get_entity_link('momentary_door')}。",
        "tips": [],
    },
    "monster_scientist": {
        "tags": [],
        "short_description": "人质（冗余，不建议使用）",
        "full_description": f"用于放置人质的点实体。就是解救人质模式里的人质。和{get_entity_link('hostage_entity')}的唯一区别如下：\n\n?> 以下内容摘自天书\n\n这个实体和hostage_entity在cs里的作用是一样的，唯一的区别是：当cs地图使用于shalf-life游戏时，hostage_entity放置将会在游戏时存在，而hostage_entity将不会存在。（哈，谁在乎！！！）",
        "tips": [],
    },
    "multi_manager": {
        "tags": [],
        "short_description": "多目标定时引发器",
        "full_description": f"用于多目标定时的点实体。你可以给它设置多个目标和引发前延时。添加目标的方法和一般的实体不同，你要在界面上关闭优化模式，点击添加，然后键值（名称）填目标名称，变量（值）就是引发前延迟，就能添加一个引发目标。\n\n下图所示的multi_manager被引发后，会立刻引发target1，0.1秒后引发target2，1秒后引发target3。![multi_manager_example](../../images/multi_manager_example.png)",
        "tips": [],
        "alerts": [
            "本实体最多能设置16个目标"
        ]
    },
    "multisource": {
        "tags": [],
        "short_description": "全局状态读取实体（状态锁/多源控制器）",
        "full_description": f"本实体的使用比较特殊，它的主要作用有两个：制作被锁定的物体、实现多个实体共同引发才生效的功能。\n\n本实体有两种状态：开和关，默认是处于关的状态的。下面介绍两个作用的实现思路：\n\n---\n### 制作被锁定的物体：被锁住的门\n\n玩家在接触被锁住的门时能听到“锁住的声音”对应的音效，且门不会打开\n\n1. 制作一个{get_entity_link('env_global')}，名称叫```unlock```，“设置全局状态实体”填```door_lock_state```，引发模式填```开```。这个实体被引发时会把叫做```door_lock_state```的全局状态设为“开启”。\n2. 制作一个{get_entity_link('multisource')}，名称叫```lock```，“读取全局状态实体”填```door_lock_state```。这个实体会读取叫做```door_lock```的全局状态，只有为“开启”时才能使用。\n3. 制作一扇门，属主填```lock```。\n\n这样完成后，这扇门是否锁着归{get_entity_link('multisource')}管，而{get_entity_link('multisource')}会去查询```door_lock_state```状态是否为“开启”，引发{get_entity_link('env_global')}就能把```door_lock_state```状态设为“开启”，从而解锁门。\n\n---\n### 实现多个实体共同引发才生效的功能：两个开关同时按下才能打开的门。\n\n1. 制作一个门，名称叫```door```。\n2. 制作一个{get_entity_link('multisource')}，名称叫```both```，目标为```door```，其他不用填。\n3. 制作两个开关，目标都填```both```，复位前延时填2秒。\n\n这样玩家必须在2秒内同时按下两个按钮才能打开门",
        "tips": [],
    },
    "path_corner": {
        "tags": [],
        "short_description": "路径（常规）",
        "full_description": f"用于制作常规路径的点实体。在{get_entity_link('func_guntarget')}、{get_entity_link('func_train')}、{get_entity_link('trigger_camera')}等实体中会用到。",
        "tips": [],
    },
    "path_track": {
        "tags": [],
        "short_description": "路径（火车）",
        "full_description": f"用于制作火车路径的点实体。主要用在{get_entity_link('func_tracktrain')}实体上。",
        "tips": [],
    },
    "player_weaponstrip": {
        "tags": [],
        "short_description": "剥夺武器",
        "full_description": f"用于剥夺玩家的点实体。引发后移除玩家所有武器（包括匕首）。",
        "tips": [
            TipMustTrigger
        ],
    },
    "trigger_auto": {
        "tags": [],
        "short_description": "起始引发器",
        "full_description": f"用于在游戏开始时引发的点实体。只在地图载入后引发它的目标，仅此一次，此后不再有其他作用。",
        "tips": [],
    },
    "trigger_camera": {
        "tags": [],
        "short_description": "摄像机",
        "full_description": f"用于制作摄像机的点实体。它可以用来制作监控（比如仓库CT家车上的监控），另外进入游戏后选队伍的背景画面摄像位置也可以用这个实体指定（如果不用，默认是玩家出生点的画面）。",
        "tips": [],
    },
    "trigger_changetarget": {
        "tags": [],
        "short_description": "修改目标",
        "full_description": f"用于修改目标的点实体。能把其他实体的目标改成想要的目标。",
        "tips": [
            TipMustTrigger
        ],
        "alerts": [
            "本实体的目标必须是唯一的，也就是说不能同时改几个重名实体的目标，否则不会生效。"
        ]
    },
    "trigger_gravity": {
        "tags": [],
        "short_description": "修改重力",
        "full_description": f"用于修改重力的固体实体。规定一片区域，玩家进入这片区域后重力会发生变化，变化持续到再次被修改或者新回合开始。",
        "tips": [
            f"玩家离开区域重力是不会恢复的，可以在出口处放另一个{get_entity_link('trigger_gravity')}来恢复正常重力。"
        ],
    },
    "trigger_hurt": {
        "tags": [],
        "short_description": "区域伤害/治疗",
        "full_description": f"用于造成伤害/治疗的固体实体。规定一片区域，玩家在这片区域中时会持续受到伤害，伤害每隔0.5秒产生一次。",
        "tips": [],
    },
    "trigger_multiple": {
        "tags": [],
        "short_description": "区域引发（多次）",
        "full_description": f"用于区域引发（多次）的固体实体。规定一片区域，玩家进入区域后会引发目标，一段时间后复位，复位后玩家进入（或者一直呆在里面）可再次引发。",
        "tips": [],
    },
    "trigger_once": {
        "tags": [],
        "short_description": "区域引发（单次）",
        "full_description": f"用于区域引发（单次）的固体实体。规定一片区域，玩家进入区域后会引发目标，此后就再也不能引发了（直到重新载入地图）。",
        "tips": [],
    },
    "trigger_push": {
        "tags": [],
        "short_description": "区域推力",
        "full_description": f"用于实现推力的固体实体。规定一片区域，玩家进入区域后会受到推力，可模拟风的效果。",
        "tips": [],
    },
    "trigger_relay": {
        "tags": [],
        "short_description": "中继",
        "full_description": f"用于实现中继的点实体。做为引发的中继，方便管理引发的流程，一般是给没有“引发前延时”的实体增加延迟，或者没有“引发方式”的实体补充引发方式。",
        "tips": [],
        "alerts": [
            f"本实体不会传递引发者的信息，这意味着当你用{get_entity_link('game_text')}、{get_entity_link('env_fade')}等类似实体，而且没有选“对所有玩家”时，你不能用这个实体做中继，否则会导致游戏奔溃闪退。"
        ]
    },
    "trigger_teleport": {
        "tags": [],
        "short_description": "区域传送",
        "full_description": f"用于实现传送的固体实体。规定一片区域，玩家进入区域后会传送到目标位置。",
        "tips": [
            "多个玩家都在传送时，传送完后可能重叠在一起卡住。你可以把终点放在空中，这样传送过去会落到地方避免卡住，另外天花板不能太低，否则卡住后按跳跃也不能解除卡住了。"
        ],
    },
    "weapon_c4": {
        "tags": [],
        "short_description": "放置C4",
        "full_description": f"用于放置C4的点实体。会放置一个已经启动的C4。",
        "tips": [
            "如果没有设置名称，则回合开始会自动放置。否则就是引发后放置。"
        ],
        "alerts": [
            AlertOnlyOnce
        ]
    },
}

RELATED_ENTITYES = [
    ['env_laser', 'env_beam'],
    ['env_glow', 'env_sprite'],
    ['env_rain', 'env_snow'],
    ['func_healthcharger', 'func_recharge'],
    ['func_plat', 'func_platrot'],
    ['func_button', 'func_guntarget', 'button_target', 'func_rot_button'],
    ['func_trackautochange', 'func_trackchange'],
    ['func_escapezone', 'func_hostage_rescue', 'func_bomb_target', 'func_vip_safetyzone', 'info_bomb_target', 'info_hostage_rescue'],
    ['light', 'light_environment', 'light_spot'],
    ['path_corner', 'path_track'],
]

def gen_related_entity_tip(entities):
    if type(entities) == str:
        entities = [entities]

    text = "相关实体 "
    for entity in entities:
        text += f"{get_entity_link(entity)}：{ENTITIY_INFO[entity]['short_description']}；"
    return text

# generate related link tip
for relation in RELATED_ENTITYES:
    for entity in relation:
        others = relation.copy()
        others.remove(entity)
        ENTITIY_INFO[entity]['tips'].insert(0, gen_related_entity_tip(others))

PROPERTY_INFO = {
    "targetname": {
        "description": "实体的名称，用于被其他实体引发，可参考：[引发机制](wiki/trigger)",
    },
    "target": {
        "description": "目标实体的名称，用于引发其他实体，可参考：[引发机制](wiki/trigger)",
        "func_guntarget": InfoPathOnlyCorner,
        "func_tank": f"依旧是引发目标，不过机枪是发射一次就引发一次，这里一般填{get_entity_link('ambient_generic')}点实体的名称，用来制作机枪发射音效。",
        "func_tracktrain": f"火车的起始位置，填{get_entity_link('path_track')}的名称",
        "func_train": InfoPathOnlyCorner,
        "func_traincontrols": "填要控制的火车名称。",
        "func_vehiclecontrols": "填要控制的载具名称。",
        "light_spot": f"可设置为{get_entity_link('info_null')}或者{get_entity_link('info_target')}，这样他就会指向目标的位置。",
        "path_corner": f"下一个路径点的名称。",
        "path_track": f"下一个路径点的名称。",
        "trigger_camera": f"填{get_entity_link('info_target')}的名称，摄像机会看向指定的实体。",
        "trigger_teleport": f"填{get_entity_link('info_teleport_destination')}的名称。",
    },
    "message": {
        "ambient_generic": "声音文件路径，声音放入sound文件夹内，路径格式类似 ```myMap/mySound.wav```，注意前面没有 ```sound/```",
        "env_message": "?> 摘自天书\n\n设置你需要显示的文本。不能随意写。 \n\n设置方法：\n1. 进入你的cstrike或valve目录，里面各有一个名为titles.txt的文本文件，可以调用的文本都在这里面。\n2. 打开随便一个titles.txt文件，看内容。我举个例子，引用：\n```\nGame_required_votes\n{\nRequired number of votes for a new map = %s\n}\n```\n\n里面都是这样的格式，上面的“Game_required_votes”是文本信息标题，下面的“{”和“}”之间的文本就是屏幕上会显示的文本内容了。你要做的，就是把标题填到这个键值里面。这个例子里面，需要填的就是“Game_required_votes”了，这样，当玩家在游戏里引发实体的时候，屏幕上将会显示：Required number of votes for a new map = %s了。",
        "game_text": "要显示的文本，支持中文（老的编译器可能会出问题，如果中文无法编译，尝试用V大最新的编译器），用\\n表示换行。",
    },
    "angles": {
        "description": "旋转角度",
        "armoury_entity": "旋转角度。可以在hammer中旋转，能直观地看到结果，无需用本属性"
    },
    "rendermode": {
        "description": "常用的有三个。普通：平时正常的样式；固体：配合{开头的纹理实现透明（如梯子）；发光：配合黑底的纹理实现半透明（如光柱）；",
        "env_glow": "对这个实体，一般选择“发光”",
    },
    "model": {
        "description": "模型文件路径，" + InfoModelPath,
        "cycler_sprite": "模型/图标文件路径。" + InfoModelPath + InfoSpritePath,
        "env_sprite": "图标文件路径。" + InfoSpritePath,
        "armoury_entity": None,
        "hostage_entity": None,
        "info_player_deathmatch": None,
        "info_player_start": None,
        "info_vip_start": None,
        "monster_scientist": None,
    },
    "LightningStart": {
        "description": f"闪电起点的实体名称，一般使用{get_entity_link('info_target')}",
    },
    "LightningEnd": {
        "description": f"闪电终点的实体名称，一般使用{get_entity_link('info_target')}",
    },
    "Radius": {
        "description": "闪电半径（长度），没有指定闪电终点时会使用这个值。" + TipDefaultDirectionRight,
    },
    "NoiseAmplitude": {
        "description": "越大弯折越多，=0则是直线",
    },
    "globalstate": {
        "env_global": f"全局状态的名称，全局状态是一个能跨地图传输的信息，它用一个字符串标识，每个全局状态有开和关两种状态。比如你填入```my_state```，引发模式选开，那么引发这个实体就会把叫做```my_state```的全局状态设置为开，这个```my_state```为开还能在下一张地图内读取。配合{get_entity_link('multisource')}实体使用，它能读取全局状态来实现一些功能。",
        "multisource": f"全局状态的名称，全局状态是一个能跨地图传输的信息，它用一个字符串标识，每个全局状态有开和关两种状态。比如你填入```my_state```，引发模式选开，那么引发这个实体就会把叫做```my_state```的全局状态设置为开，这个```my_state```为开还能在下一张地图内读取。配合{get_entity_link('env_global')}实体使用，它能设置全局状态。",
    },
    "triggermode": {
        "description": f"这个是一个选项，让你选择一种模式。当你这个实体被其他实体引发的时候，他将处于什么状态。 \n- 关：当这个实体被引发时这个实体将处于“关”的状态，无论被引发几次。而不会把“全局设置”的数据传给{get_entity_link('multisource')}实体\n- 开：当这个实体被引发时这个实体将处于“开”的状态，无论被引发几次。会把“全局设置”的数据传给{get_entity_link('multisource')}实体\n- 锁定：当这个实体被引发时这个实体将在“开”和“关”的状态间轮回。处于什么状态看你引发的次数而定，就像现实中的灯，引发一次是开，再来就关，再来又开...如此循环。根据自己的状态决定是否把“全局设置”的数据传给{get_entity_link('multisource')}实体，“开”就传，“关”就不传\n-死亡：这个是和hl游戏里的怪物实体（monster类实体）有关系的。cs里用不上。",
    },
    "initialstate": {
        "description": "选项。设定这个实体最原始的状态。也就是刚载入地图时的这个实体自身所处的状态。",
    },
    "count": {
        "armoury_entity": "武器的数量，仅第一回合有效。以后的回合始终只有一把。"
    },
    "scale": {
        "env_glow": "图标缩放比例，渲染模式必须设置为“附加”才有效果。",
        "env_sprite": "图标缩放比例，渲染模式必须设置为“附加”才有效果。"
    },
    "LaserTarget": {
        "description": f"激光终点的实体名称，一般使用{get_entity_link('info_target')}",
    },
    "m_iGibs": {
        "description": "喷射总数量，喷完就不再喷了",
    },
    "shootmodel": {
        "description": "模型/图标文件路径。" + InfoModelPath + InfoSpritePath,
    },
    "killtarget": {
        "description": "删除指定的实体，刷新不会恢复删除的实体，只有重新载入地图才能恢复。",
    },
    "health": {
        "func_breakable": "耐久度越高，打破物体需要造成的伤害越高。数值可类比HP，如100耐久度的墙需要两次重刀打破。",
        "func_guntarget": "枪靶的“血量”，“血量”耗尽后才会停下并引发目标。设置为0表示一旦被攻击立刻停下并引发目标。",
        "func_pushable": "如果勾选了[可打碎]()标记，这里可以设置耐久度。",
        "func_rot_button": "如果设置不是空而且大于0，则开关不再能按E引发，而是变成用武器攻击引发，这个值的大小对应了耐久度。",
        "game_counter": "计数的限定值，达到这个值后会引发目标。",
    },
    "explodemagnitude": {
        "func_breakable": "如果设置了大于0，则它破碎的同时会爆炸，会对玩家造成伤害。",
        "func_pushable": "如果勾选了[可打碎]()标记，这里可以设置爆炸范围，如果大于0，则它破碎的同时会爆炸，会对玩家造成伤害。",
    },
    "delay": {
        "description": "将要引发目标时，不再是立刻引发，而是延迟一段时间再引发。单位为秒，精确到0.1秒。",
        "gibshooter": "喷射的间隔时间，填0则是同时喷出。",
    },
    "material": {
        "func_breakable": "不同材质破碎后产生的碎片不同，刀划在上面的音效也不同。",
    },
    "gibmodel": {
        "func_breakable": "指定自定义的碎片模型，指定后会替换生成的碎片。",
    },
    "master": {
        "description": f"填写{get_entity_link('multisource')}的名称，详见{get_entity_link('multisource')}",
    },
    "lip": {
        "func_button": "默认情况下，开关引发后会移动一段距离，距离和开关的大小对应。比如一个厚度是10单位的开关，我们把它贴在墙上，移动方向设置为朝着墙，按下开关后它会移动10单位，刚好嵌进墙里面。而这个露出的尺寸可以让它不完全嵌进去，比如设置为2单位后，开关会露出2单位，实际只移动了8单位。",
        "func_door": "默认情况下，推拉门引发后会移动一段距离，距离和门的大小对应。比如一面墙上有一扇宽120单位的推拉门，开门时它会移动120单位，刚好嵌进墙里面。而这个露出的尺寸可以让它不完全嵌进去，比如设置为10单位后，开关会露出10单位，实际只移动了110单位。",
    },
    "speed": {
        "description": "速度，单位/秒",
        "func_vehicle": f"其实指能达到的最大速度",
        "path_track": f"火车经过后这个路径点时改变火车的速度，设为0表示不改变速度。",
        "trigger_push": None,
    },
    "wait": {
        "func_door": "多久后门自动关闭，单位是秒",
        "func_door_rotating": "多久后门自动关闭，单位是秒",
        "trigger_multiple": "单位是秒",
    },
    "dmg": {
        "func_door": "被门夹到时造成的伤害大小。",
        "func_door_rotating": "被门夹到时造成的伤害大小。",
        "func_pendulum": "被碰到时造成的伤害大小。",
        "func_rotating": "被夹到时造成的伤害大小。",
        "func_tracktrain": "被撞到时造成的伤害大小。",
        "func_train": "被夹到时造成的伤害大小。",
        "func_vehicle": "被撞到时造成的伤害大小。",
        "game_player_hurt": "造成的伤害大小。填负数则是加多少血。",
        "trigger_hurt": "每秒造成的伤害大小。填负数则是每秒加多少血。",
    },
    "distance": {
        "func_door_rotating": "转门旋转的角度。",
    },
    "modifier": {
        "func_friction": "0表示没有摩檫力，100是正常的摩檫力。",
    },
    "avelocity": {
        "func_train": "实体最初的转动，配合路径使用。"
    },
    "m_flSpread": {
        "func_mortar_field": "越小闪光弹投掷得越准。"
    },
    "m_iCount": {
        "func_mortar_field": "投弹几次。"
    },
    "m_fControl": {
        "func_mortar_field": "?> 以下内容摘自天书\n\n- 随机：就是炸弹随机乱扔，谁吃到谁倒霉。\n- 引发者：谁引发这个实体炸弹就扔谁\n- 桌面控制：当选中这个选项时，下面的健值：“x控制实体”和“y控制实体”才会起作用。我尝试解释一下意思：就是相当余你有一张这个实体笼罩区域的地图放在桌面上，用x控制者和y控制者在地图上定义一个点，然后按按钮来引发这个实体，那么闪光弹就会在你对应点的地图的实际位置上落下。"
    },
    "m_iszXController": {
        "func_mortar_field": f"目标时桌面控制时才有效。填写{get_entity_link('momentary_rot_button')}固体实体的名称。"
    },
    "m_iszYController": {
        "func_mortar_field": f"目标时桌面控制时才有效。填写{get_entity_link('momentary_rot_button')}固体实体的名称。"
    },
    "damp": {
        "func_pendulum": "为0时它会永远摆动下去。设置阻力后摆动幅度逐渐减少直到停止。"
    },
    "height": {
        "func_plat": "即电梯移动的高度。",
        "func_platrot": "即电梯移动的高度。",
        "func_trackautochange": "变轨平台移动的高度。",
        "func_trackchange": "变轨平台移动的高度。",
        "func_vehicle": "默认情况下，载具的轴心出现在指定路径点的位置，这时有可能车轮陷在地下，调高这个数值来整体抬高载具。**待补充：利用好这个属性可以制作飞机等飞在天上的载具，但具体怎么做不清楚，如果有朋友制作过，欢迎补充。**",
    },
    "rotation": {
        "func_platrot": "整个上升过程里电梯旋转多少度。",
        "func_trackautochange": "变轨平台旋转的角度。",
        "func_trackchange": "变轨平台旋转的角度。",
    },
    "size": {
        "func_pushable": "?> 以下内容摘自X-man天书\n\n选定实体外壳的大小。对于这个选项我是这么理解的，举一个例子：我们造一个长宽高为64的箱子，在游戏里他表面上除了可以推动外，和别的箱子没有区别。其实不是，cs引擎默认情况下是把他作为一个“点”处理的（就是我们不改选项的情况下）。有的玩家有这样的设想：把他4个角用东西垫着，让他在游戏里悬空，让玩家可以从下面经过....然而到了却游戏发现他在地上，就大叫：怎么这东西搁不住啊？他搁不住是因为他默认是一个“点”嘛！！如果你不搁中心，当然会掉下来。"
    },
    "buoyancy": {
        "func_pushable": "因为它能浮在水面上，这里可以设置它在水中的浮力大小。"
    },
    "changetarget": {
        "func_rot_button": f"修改目标实体的目标。类似{get_entity_link('trigger_changetarget')}的作用。"
    },
    "fanfriction": {
        "func_rotating": "设置后，关闭时不是立刻关闭，而是有个减速的过程"
    },
    "yawrange": {
        "description": "单位是角度，只能在这个角度范围内转动"
    },
    "pitchrange": {
        "description": "单位是角度，只能在这个角度范围内转动"
    },
    "barrel": {
        "description": "和另外两个枪口坐标配合使用，指定枪口相对于轴心的偏移量。子弹会从枪口位置射出，枪焰图标也会生成在这里。因为枪口默认是朝着X轴正方向（俯视图向右），一般只设置barrel即可。"
    },
    "barrely": {
        "description": "和另外两个枪口坐标配合使用，指定枪口相对于轴心的偏移量。子弹会从枪口位置射出，枪焰图标也会生成在这里。因为枪口默认是朝着X轴正方向（俯视图向右），一般只设置barrel即可。"
    },
    "barrelz": {
        "description": "和另外两个枪口坐标配合使用，指定枪口相对于轴心的偏移量。子弹会从枪口位置射出，枪焰图标也会生成在这里。因为枪口默认是朝着X轴正方向（俯视图向右），一般只设置barrel即可。"
    },
    "spritesmoke": {
        "description": "枪口生成的烟雾图标"
    },
    "spriteflash": {
        "description": "枪口生成的火花图标"
    },
    "persistence": {
        "description": "看不见目标后会停止射击，设置这个值能让它火力压制一段时间后再停止射击。"
    },
    "toptrack": {
        "description": f"火车变轨前{get_entity_link('path_track')}路径点的名称。"
    },
    "bottomtrack": {
        "description": f"火车变轨后{get_entity_link('path_track')}路径点的名称。"
    },
    "startspeed": {
        "description": f"游戏一开始时的速度，会保持直到{get_entity_link('path_track')}或者玩家改变了速度。"
    },
    "bank": {
        "description": f"转弯时最大倾斜角度，可以类比摩托车转弯压弯的效果。"
    },
    "wheels": {
        "description": f"轮子的间距，会影响转弯时的效果，一般来说设置成火车的宽度即可。"
    },
    "frags": {
        "game_counter": f"计数的初始值，一般使用默认的0。",
        "game_counter_set": f"要设置为的计数值。",
    },
    "x": {
        "game_text": f"文本的水平位置，0（最左）~1（最右），填-1表示居中。",
    },
    "y": {
        "game_text": f"文本的垂直位置，0（最上）~1（最下），填-1表示居中。",
    },
    "channel": {
        "game_text": f"同一频道的文本，新文本在显示时会挤掉老文本，所以妥善设置，避免在同一时间显示相同频道的文本。",
    },
    "incount": {
        "game_zone_player": f"填{get_entity_link('game_counter')}的名称，会设置它的计数值为在区域内玩家的数量。",
    },
    "outcount": {
        "game_zone_player": f"填{get_entity_link('game_counter')}的名称，会设置它的计数值为在区域外玩家的数量。",
    },
    "m_flVelocity": {
        "gibshooter": f"喷射出的初始速度。",
    },
    "m_flVariance": {
        "gibshooter": f"喷射方向的分散程度，越大方向越分散。",
    },
    "_light": {
        "description": f"指定光源的颜色和亮度，格式是```R G B I```，对应红绿蓝（0~255）和亮度。"
    },
    "pattern": {
        "light": InfoLightPattern,
        "light_environment": InfoLightPattern,
        "light_spot": InfoLightPattern,
    },
    "_diffuse_light": {
        "light_environment": "用来模拟天空的映出的颜色（一般是蓝色），一般情况下默认值即可。",
    },
    "pitch": {
        "light_environment": "太阳/月亮的倾斜角，默认-90是垂直朝下（类似正午），建议设置在-30~-60之间（上午、下午）。",
    },
    "_cone": {
        "light_spot": "类比手电筒，中间的强光区域角度范围。",
    },
    "_cone2": {
        "light_spot": "类比手电筒，外围的弱光区域角度范围，要大于强光角度范围（两者相减就是弱光的实际范围）。",
    },
    "returnspeed": {
        "momentary_rot_button": "如果勾选了“自动回转”，当玩家松开E时，开关会慢慢自动回位，这个值就是回位的速度。",
    },
    "altpath": {
        "path_track": "当本实体被引发时，下一个路径会在“下一个路径点”和“第二路径点”之间切换，可以实现火车变轨。",
    },
    "moveto": {
        "trigger_camera": f"相机可以像{get_entity_link('func_train')}那样在路径点上运动，这里填路径点的名称。",
    },
    "m_iszNewTarget": {
        "trigger_changetarget": f"指定新的目标，比如这个实体的“目标”填```button1```，“新目标”填```door2```，引发后```button1```的“目标”就会变成```door2```。",
    },
    "detonatedelay": {
        "weapon_c4": f"C4爆炸倒计时时间，单位是秒。",
    },
}

FLAG_INFO = {
    "随机方向": {
        "description": "喷血的方向变成随机，会向四面八方。",
    },
    "血流": {
        "description": "喷血的效果更可怕、喷血的规模更大。",
    },
    "从引发者身上喷出": {
        "description": "如果是玩家引发，则从玩家身上喷出。不会造成伤害。",
    },
    "设为初始状态": {
        "description": "勾选后，当地图被重复载入时，无论前次你离开地图时这个实体的状态是什么，他将恢复到“初始状态设定”里设定的状态。",
    },
    "开始时打开": {
        "button_target": "反转+A纹理的状态。TODO:补充",
        "func_door": "勾选后，门在开局时是打开的而非关闭的。",
        "func_door_rotating": "勾选后，门在开局时是打开的而非关闭的。"
    },
    "反向渐变": {
        "env_fade": "勾选后，会从全屏纯色慢慢过渡到正常画面，相当于反转的渐变"
    },
    "调制模式": {
        "env_fade": "勾选后，画面不会是纯色，而是纯色和正常画面的混合。比如可以设置颜色为绿色（0 255 0），勾选这个标记后，看到的画面类似夜视仪"
    },
    "只对引发者有效": {
        "env_fade": "勾选后，引发时只对引发的玩家生效。而默认情况下是对所有玩家生效。"
    },
    "不移动": {
        "func_button": "勾选后，开关引发后不再移动。"
    },
    "锁定": {
        "func_button": "勾选后，开关变成按一下开、再按一下关的模式。默认开关不只是打开→一段时间后复位→打开...，勾选按后会变成打开→关闭→打开..."
    },
    "冒火花": {
        "func_button": "勾选后，开关引发时会生成一次火花，用来模拟坏掉的开关。"
    },
    "通过接触引发": {
        "func_button": "勾选后，按E不再能引发开关，改为玩家触碰来引发开关。"
    },
    "不推动": {
        "func_conveyor": "勾选后，传送带不会带动玩家。"
    },
    "不自动关闭": {
        "func_door": "勾选后，门不会自动关闭，变成引发一次开，再引发一次关的模式。",
        "func_door_rotating": "勾选后，门不会自动关闭，变成引发一次开，再引发一次关的模式。"
    },
    "按E键打开": {
        "func_door": "勾选后，对着门按E可以开门，而不再能触碰开门。",
        "func_door_rotating": "勾选后，对着门按E可以开门，而不再能触碰开门。",
    },
    "反向": {
        "func_door_rotating": "勾选后，门开的方向会和正常相反。默认情况下，玩家开门时，门会背向玩家打开，如果勾选了这个选项，则会变成朝向玩家打开。另外门被引发打开时，会固定朝着一个方向开，勾选这个能让它固定朝另一个方向开。"
    },
    "单方向": {
        "func_door_rotating": "勾选后，门永远只朝一个方向打开。"
    },
    "绕X轴旋转": {
        "func_door_rotating": "勾选后，门以X轴为转轴旋转。默认情况下门是绕Z轴旋转的，看起来就是普通的转门。勾选这个选项后转轴会改变，可以用来制作特殊的旋转效果（比如笔记本电脑翻盖那样的旋转）",
        "description": "勾选后，变成以X轴为转轴旋转。默认情况下是绕Z轴旋转的。"
    },
    "绕Y轴旋转": {
        "func_door_rotating": "勾选后，门以Y轴为转轴旋转。默认情况下门是绕Z轴旋转的，看起来就是普通的转门。勾选这个选项后转轴会改变，可以用来制作特殊的旋转效果（比如笔记本电脑翻盖那样的旋转）",
        "description": "勾选后，变成以X轴为转轴旋转。默认情况下是绕Z轴旋转的。"
    },
    "关闭时复位": {
        "func_pendulum": "勾选后，受到阻力最后停止时，它会复位到最开始的位置上。"
    },
    "可破碎[不复位]": {
        "func_pushable": "勾选后，变得可以打碎，被引发也会破碎，但是破碎后新回合不会复原。"
    },
    "先连接第二路径": {
        "func_trackautochange": "勾选后，初始状态平台在第二路径，而非默认的第一路径。"
    },
    "只旋转": {
        "func_trackautochange": "勾选后，变轨平台只旋转，不会升高降低。",
        "func_trackchange": "勾选后，变轨平台只旋转，不会升高降低。",
    },
    "不能控制": {
        "func_tracktrain": "勾选后，火车不能被玩家控制。",
        "func_vehicle": "勾选后，载具不能被玩家控制。",
    },
    "不能后退": {
        "func_tracktrain": "勾选后，火车不能倒车了。",
    },
    "引发后复位": {
        "game_counter": "勾选后，达到限定值引发目标的同时，会恢复计数到初始值，让实体能反复引发。",
    },
    "引发后删除": {
        "description": "勾选后，实体引发其目标后会删除自己，此后都不能使用了（刷新回合依旧不能使用，只有重新载入地图）。",
    },
    "只能引发": {
        "game_player_equip": "勾选后，回合开始时不会自动引发，只能手动引发。但回合开始的默认武器依旧会消失。",
    },
    "允许负分": {
        "game_score": "默认玩家评分最低为0，勾选后，减分时可以减到负。",
    },
    "队友计分": {
        "game_score": "默认是对引发的单个玩家计分，勾选后，变成对玩家所属队伍全员计分。",
    },
    "对所有玩家": {
        "game_text": "勾选后，引发时对游戏里所有玩家显示文本。",
    },
    "感应(作为转门)": {
        "momentary_rot_button": "?> 摘自天书\n\n这是一个很有意思的标记。不知道怎么解释，只好举一个例子了： \n\n制作2个2个momentary_rot_button实体，让他们一起指向同一个momentary_door实体，在其中一个里选上这个标记时，我们用另一个开门时，这个会自动同步做和另外一个momentary_rot_button一样的运动！！！甚至你不给他们指定momentary_door实体也可以。",
    },
    "自动回转": {
        "momentary_rot_button": "勾选后，玩家松开E时阀门开关会自动回转归位。",
    },
    "多线程": {
        "multi_manager": "勾选后，multi_manager能在还没结束前再次引发，而且可以引发自己了（可以用来做定时引发器，比如每隔1秒引发一次），如果不勾选则结束前的重复引发是无效的。比如multi_manager设置了10秒后引发其他实体，此时我们先引发multi_manager，在5秒后在引发了一次multi_manager，如果不勾选这个标记，第二次引发不会起作用，其他实体只会在第10秒被引发这一次；而如果勾选了，第二次引发会另开一个线程，其他实体会在第10秒被引发一次，15秒又引发一次。",
    },
    "到达后暂停移动": {
        "path_corner": "勾选后，实体到达这个路径点后会暂停，再次引发实体后才会继续移动。",
    },
    "传送到此路径点": {
        "path_corner": "勾选后，实体会直接传送到这个路径点，而非慢慢移动过来。",
    },
    "反向第二路径点": {
        "path_corner": "勾选后，“下一个路径点”和“第二路径点”的设置对换，最初的路径点变成“第二路径点”，而非原来的“下一个路径点”。",
    },
    "禁用控制": {
        "path_corner": "勾选后，火车到达这个路径点后抛锚，不再能使用。",
    },
    "开始于引发者": {
        "trigger_camera": "勾选后，初始摄像机视角和玩家相同，与自己的设置无关。",
    },
    "跟踪引发者": {
        "trigger_camera": "勾选后，摄像机焦点会跟随引发者移动。",
    },
    "冻结引发者": {
        "trigger_camera": "勾选后，在使用摄像机时不能移动。",
    },
}