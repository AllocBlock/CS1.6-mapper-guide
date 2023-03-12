# func_weaponcheck
[#固体实体](wiki/solid_entity)

用于实现携带武器检查的固体实体。玩家在范围内时会检查其携带的武器是否符合要求，然后引发对应的目标。

!> 本实体只能使用一次/一回合。引发一次后，或者到新的回合后，实体会失效。

## 属性 (property)
> **[注意!!只能使用一次或一回合]** *classname* = *空* | 字符串

> **名称** *targetname* = *空* | 字符串

实体的名称，用于被其他实体引发，可参考：[引发机制](wiki/trigger)

> **属主** *master* = *空* | 字符串

填写[multisource](wiki/entity/multisource)的名称，详见[multisource](wiki/entity/multisource)

> **检查成功时时引发的目标** *trigger_items* = *空* | 字符串

> **检查失败时引发的目标** *trigger_noitems* = *空* | 字符串

> **检查失败后重新检查延时** *trigger_noitems_delay* = *空* | 整数

> **任何武器都可以** *any_weapon* = *0* | 单选

- 否 = *0*
- 是 = *1*

> **需携带的武器1** *item1* = *空* | 单选

- 无 = *空*
- 刀 = *weapon_knife*
- Glock18 = *weapon_glock18*
- USP45 = *weapon_usp*
- P-228 = *weapon_p228*
- DesertEagle = *weapon_deagle*
- BerettaElites = *weapon_elite*
- Five-Seven = *weapon_fiveseven*
- BenelliM3 = *weapon_m3*
- BenelliXM1014 = *weapon_xm1014*
- Mac-10 = *weapon_mac10*
- TMP = *weapon_tmp*
- MP5/Navy = *weapon_mp5navy*
- UMP45 = *weapon_ump45*
- FNP90 = *weapon_p90*
- Galil = *weapon_galil*
- Famas = *weapon_famas*
- AK47 = *weapon_ak47*
- Scout = *weapon_scout*
- M4A1 = *weapon_m4a1*
- SG552 = *weapon_sg552*
- Aug = *weapon_aug*
- SG550 = *weapon_sg550*
- AWP = *weapon_awp*
- G3/SG-1 = *weapon_g3sg1*
- M249 = *weapon_m249*
- 防暴盾牌 = *weapon_shield*
- 闪光弹 = *weapon_flashbang*
- 高爆手榴弹 = *weapon_hegrenade*
- 烟雾弹 = *weapon_smokegrenade*
- C4炸弹 = *weapon_c4*

> **需携带的武器2** *item2* = *空* | 单选

- 无 = *空*
- 刀 = *weapon_knife*
- Glock18 = *weapon_glock18*
- USP45 = *weapon_usp*
- P-228 = *weapon_p228*
- DesertEagle = *weapon_deagle*
- BerettaElites = *weapon_elite*
- Five-Seven = *weapon_fiveseven*
- BenelliM3 = *weapon_m3*
- BenelliXM1014 = *weapon_xm1014*
- Mac-10 = *weapon_mac10*
- TMP = *weapon_tmp*
- MP5/Navy = *weapon_mp5navy*
- UMP45 = *weapon_ump45*
- FNP90 = *weapon_p90*
- Galil = *weapon_galil*
- Famas = *weapon_famas*
- AK47 = *weapon_ak47*
- Scout = *weapon_scout*
- M4A1 = *weapon_m4a1*
- SG552 = *weapon_sg552*
- Aug = *weapon_aug*
- SG550 = *weapon_sg550*
- AWP = *weapon_awp*
- G3/SG-1 = *weapon_g3sg1*
- M249 = *weapon_m249*
- 防暴盾牌 = *weapon_shield*
- 闪光弹 = *weapon_flashbang*
- 高爆手榴弹 = *weapon_hegrenade*
- 烟雾弹 = *weapon_smokegrenade*
- C4炸弹 = *weapon_c4*

> **需携带的武器3** *item3* = *空* | 单选

- 无 = *空*
- 刀 = *weapon_knife*
- Glock18 = *weapon_glock18*
- USP45 = *weapon_usp*
- P-228 = *weapon_p228*
- DesertEagle = *weapon_deagle*
- BerettaElites = *weapon_elite*
- Five-Seven = *weapon_fiveseven*
- BenelliM3 = *weapon_m3*
- BenelliXM1014 = *weapon_xm1014*
- Mac-10 = *weapon_mac10*
- TMP = *weapon_tmp*
- MP5/Navy = *weapon_mp5navy*
- UMP45 = *weapon_ump45*
- FNP90 = *weapon_p90*
- Galil = *weapon_galil*
- Famas = *weapon_famas*
- AK47 = *weapon_ak47*
- Scout = *weapon_scout*
- M4A1 = *weapon_m4a1*
- SG552 = *weapon_sg552*
- Aug = *weapon_aug*
- SG550 = *weapon_sg550*
- AWP = *weapon_awp*
- G3/SG-1 = *weapon_g3sg1*
- M249 = *weapon_m249*
- 防暴盾牌 = *weapon_shield*
- 闪光弹 = *weapon_flashbang*
- 高爆手榴弹 = *weapon_hegrenade*
- 烟雾弹 = *weapon_smokegrenade*
- C4炸弹 = *weapon_c4*

> **需携带的武器4** *item4* = *空* | 单选

- 无 = *空*
- 刀 = *weapon_knife*
- Glock18 = *weapon_glock18*
- USP45 = *weapon_usp*
- P-228 = *weapon_p228*
- DesertEagle = *weapon_deagle*
- BerettaElites = *weapon_elite*
- Five-Seven = *weapon_fiveseven*
- BenelliM3 = *weapon_m3*
- BenelliXM1014 = *weapon_xm1014*
- Mac-10 = *weapon_mac10*
- TMP = *weapon_tmp*
- MP5/Navy = *weapon_mp5navy*
- UMP45 = *weapon_ump45*
- FNP90 = *weapon_p90*
- Galil = *weapon_galil*
- Famas = *weapon_famas*
- AK47 = *weapon_ak47*
- Scout = *weapon_scout*
- M4A1 = *weapon_m4a1*
- SG552 = *weapon_sg552*
- Aug = *weapon_aug*
- SG550 = *weapon_sg550*
- AWP = *weapon_awp*
- G3/SG-1 = *weapon_g3sg1*
- M249 = *weapon_m249*
- 防暴盾牌 = *weapon_shield*
- 闪光弹 = *weapon_flashbang*
- 高爆手榴弹 = *weapon_hegrenade*
- 烟雾弹 = *weapon_smokegrenade*
- C4炸弹 = *weapon_c4*

> **需携带的武器5** *item5* = *空* | 单选

- 无 = *空*
- 刀 = *weapon_knife*
- Glock18 = *weapon_glock18*
- USP45 = *weapon_usp*
- P-228 = *weapon_p228*
- DesertEagle = *weapon_deagle*
- BerettaElites = *weapon_elite*
- Five-Seven = *weapon_fiveseven*
- BenelliM3 = *weapon_m3*
- BenelliXM1014 = *weapon_xm1014*
- Mac-10 = *weapon_mac10*
- TMP = *weapon_tmp*
- MP5/Navy = *weapon_mp5navy*
- UMP45 = *weapon_ump45*
- FNP90 = *weapon_p90*
- Galil = *weapon_galil*
- Famas = *weapon_famas*
- AK47 = *weapon_ak47*
- Scout = *weapon_scout*
- M4A1 = *weapon_m4a1*
- SG552 = *weapon_sg552*
- Aug = *weapon_aug*
- SG550 = *weapon_sg550*
- AWP = *weapon_awp*
- G3/SG-1 = *weapon_g3sg1*
- M249 = *weapon_m249*
- 防暴盾牌 = *weapon_shield*
- 闪光弹 = *weapon_flashbang*
- 高爆手榴弹 = *weapon_hegrenade*
- 烟雾弹 = *weapon_smokegrenade*
- C4炸弹 = *weapon_c4*

> **需携带的武器6** *item6* = *空* | 单选

- 无 = *空*
- 刀 = *weapon_knife*
- Glock18 = *weapon_glock18*
- USP45 = *weapon_usp*
- P-228 = *weapon_p228*
- DesertEagle = *weapon_deagle*
- BerettaElites = *weapon_elite*
- Five-Seven = *weapon_fiveseven*
- BenelliM3 = *weapon_m3*
- BenelliXM1014 = *weapon_xm1014*
- Mac-10 = *weapon_mac10*
- TMP = *weapon_tmp*
- MP5/Navy = *weapon_mp5navy*
- UMP45 = *weapon_ump45*
- FNP90 = *weapon_p90*
- Galil = *weapon_galil*
- Famas = *weapon_famas*
- AK47 = *weapon_ak47*
- Scout = *weapon_scout*
- M4A1 = *weapon_m4a1*
- SG552 = *weapon_sg552*
- Aug = *weapon_aug*
- SG550 = *weapon_sg550*
- AWP = *weapon_awp*
- G3/SG-1 = *weapon_g3sg1*
- M249 = *weapon_m249*
- 防暴盾牌 = *weapon_shield*
- 闪光弹 = *weapon_flashbang*
- 高爆手榴弹 = *weapon_hegrenade*
- 烟雾弹 = *weapon_smokegrenade*
- C4炸弹 = *weapon_c4*

> **需携带的武器7** *item7* = *空* | 单选

- 无 = *空*
- 刀 = *weapon_knife*
- Glock18 = *weapon_glock18*
- USP45 = *weapon_usp*
- P-228 = *weapon_p228*
- DesertEagle = *weapon_deagle*
- BerettaElites = *weapon_elite*
- Five-Seven = *weapon_fiveseven*
- BenelliM3 = *weapon_m3*
- BenelliXM1014 = *weapon_xm1014*
- Mac-10 = *weapon_mac10*
- TMP = *weapon_tmp*
- MP5/Navy = *weapon_mp5navy*
- UMP45 = *weapon_ump45*
- FNP90 = *weapon_p90*
- Galil = *weapon_galil*
- Famas = *weapon_famas*
- AK47 = *weapon_ak47*
- Scout = *weapon_scout*
- M4A1 = *weapon_m4a1*
- SG552 = *weapon_sg552*
- Aug = *weapon_aug*
- SG550 = *weapon_sg550*
- AWP = *weapon_awp*
- G3/SG-1 = *weapon_g3sg1*
- M249 = *weapon_m249*
- 防暴盾牌 = *weapon_shield*
- 闪光弹 = *weapon_flashbang*
- 高爆手榴弹 = *weapon_hegrenade*
- 烟雾弹 = *weapon_smokegrenade*
- C4炸弹 = *weapon_c4*

## 标记 (flag)
> **死亡模式中禁用** *= 2048*

