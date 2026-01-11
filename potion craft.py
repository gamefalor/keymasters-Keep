from __future__ import annotations
import functools
from typing import List, Dict, Set
from dataclasses import dataclass
from Options import Toggle, OptionSet
from ..game import Game
from ..game_objective_template import GameObjectiveTemplate
from ..enums import KeymastersKeepGamePlatforms

@dataclass
class PotionCraftArchipelagoOptions:
    Potion_Bases: PotionBases
    Objective_Types: ObjectiveTypes
    Enable_Hard_Water: PotionCraftWaterBaseDifficulty


class PotionCraft(Game):
    name = "PotionCraft"
    platform = KeymastersKeepGamePlatforms.PC
    is_adult_only_or_unrated = False 
    options_cls = PotionCraftArchipelagoOptions
    def optional_game_constraint_templates(self) -> List[GameObjectiveTemplate]:
        return list()

    def game_objective_templates(self) -> List[GameObjectiveTemplate]:
        templates: List[GameObjectiveTemplate] = [
            GameObjectiveTemplate(
                label="Complete a day",
                data={ },
                is_time_consuming=False,
                is_difficult=False,
                weight=self.Enabled_Trials_Num,
            ),
        ]

        if self.Enable_BWater & self.Enable_PAAA:
            templates.extend([
                GameObjectiveTemplate(
                    label="[Water Base] Create a strong potion of WATEREFFECT.",
                    data={
                        "WATEREFFECT": (self.Water_Effects, 1),
                    },
                    is_time_consuming=False,
                    is_difficult=False,
                    weight=49,
                ),
            ])

        if self.Enable_BOil & self.Enable_PAAA:
            templates.extend([
                GameObjectiveTemplate(
                    label="[Oil Base] Create a strong potion of OILEFFECT.",
                    data={
                        "OILEFFECT": (self.Oil_Effects, 1),
                    },
                    is_time_consuming=False,
                    is_difficult=False,
                    weight=49,
                ),
            ])

        if self.Enable_BWine & self.Enable_PAAA:
            templates.extend([
                GameObjectiveTemplate(
                    label="[Wine Base] Create a strong potion of WINEEFFECT.",
                    data={
                        "WINEEFFECT": (self.Wine_effects, 1),
                    },
                    is_time_consuming=False,
                    is_difficult=False,
                    weight=49,
                ),
            ])

        if self.Enable_BWater & self.Enable_PA:
            templates.extend([
                GameObjectiveTemplate(
                    label="[Water Base] Create a Weak potion of WATEREFFECT.",
                    data={
                        "WATEREFFECT": (self.Water_Effects, 1),
                    },
                    is_time_consuming=False,
                    is_difficult=False,
                    weight=49,
                ),
            ])

        if self.Enable_BOil & self.Enable_PA:
            templates.extend([
                GameObjectiveTemplate(
                    label="[Oil Base] Create a Weak potion of OILEFFECT.",
                    data={
                        "OILEFFECT": (self.Oil_Effects, 1),
                    },
                    is_time_consuming=False,
                    is_difficult=False,
                    weight=49,
                ),
            ])

        if self.Enable_BWine & self.Enable_PA:
            templates.extend([
                GameObjectiveTemplate(
                    label="[Wine Base] Create a weak potion of WINEEFFECT.",
                    data={
                        "WINEEFFECT": (self.Wine_effects, 1),
                    },
                    is_time_consuming=False,
                    is_difficult=False,
                    weight=49,
                ),
            ])
            
        if self.Enable_BWater & self.Enable_PAABBC:
            templates.extend([
                GameObjectiveTemplate(
                    label="[Water Base] Create a potion with the effects: WATEREFFECT at Medium, Medium and Weak Strength Respectively.",
                    data={
                        "WATEREFFECT": (self.Water_Effects, 3),
                    },
                    is_time_consuming=False,
                    is_difficult=False,
                    weight=49,
                ),
            ])

        if self.Enable_BOil & self.Enable_PAABBC:
            templates.extend([
                GameObjectiveTemplate(
                    label="[Oil Base] Create a potion with the effects: OILEFFECT Medium, Medium and Weak Strength Respectively.",
                    data={
                        "OILEFFECT": (self.Oil_Effects, 3),
                    },
                    is_time_consuming=False,
                    is_difficult=False,
                    weight=49,
                ),
            ])

        if self.Enable_BWine & self.Enable_PAABBC:
            templates.extend([
                GameObjectiveTemplate(
                    label="[Wine Base] Create a potion with the effects: WINEEFFECT Medium, Medium and Weak Strength Respectively.",
                    data={
                        "WINEEFFECT": (self.Wine_effects, 3),
                    },
                    is_time_consuming=False,
                    is_difficult=False,
                    weight=49,
                ),
            ])

        if self.Enable_BWater & self.Enable_PAAABB:
            templates.extend([
                GameObjectiveTemplate(
                    label="[Water Base] Create a potion with the effects: WATEREFFECT at strong and medium effectiveness respectively.",
                    data={
                        "WATEREFFECT": (self.Water_Effects, 2),
                    },
                    is_time_consuming=False,
                    is_difficult=False,
                    weight=49,
                ),
            ])

        if self.Enable_BOil & self.Enable_PAAABB:
            templates.extend([
                GameObjectiveTemplate(
                    label="[Oil Base] Create a potion with the effects: OILEFFECT at strong and medium effectiveness respectively.",
                    data={
                        "OILEFFECT": (self.Oil_Effects, 2),
                    },
                    is_time_consuming=False,
                    is_difficult=False,
                    weight=49,
                ),
            ])

        if self.Enable_BWine & self.Enable_PAAABB:
            templates.extend([
                GameObjectiveTemplate(
                    label="[Wine Base] Create a potion with the effects: WINEEFFECT at strong and medium effectiveness respectively.",
                    data={
                        "WINEEFFECT": (self.Wine_effects, 2),
                    },
                    is_time_consuming=False,
                    is_difficult=False,
                    weight=49,
                ),
            ])

        if self.Enable_BWater & self.Enable_PAAABC:
            templates.extend([
                GameObjectiveTemplate(
                    label="[Water Base] Create a potion with the effects: WATEREFFECT at strong weak and weak effectiveness respectively.",
                    data={
                        "WATEREFFECT": (self.Water_Effects, 3),
                    },
                    is_time_consuming=False,
                    is_difficult=False,
                    weight=49,
                ),
            ])

        if self.Enable_BOil & self.Enable_PAAABC:
            templates.extend([
                GameObjectiveTemplate(
                    label="[Oil Base] Create a potion with the effects: OILEFFECT at strong weak and weak effectiveness respectively.",
                    data={
                        "OILEFFECT": (self.Oil_Effects, 3),
                    },
                    is_time_consuming=False,
                    is_difficult=False,
                    weight=49,
                ),
            ])

        if self.Enable_BWine & self.Enable_PAAABC:
            templates.extend([
                GameObjectiveTemplate(
                    label="[Wine Base] Create a potion with the effects: WINEEFFECT at strong weak and weak effectiveness respectively.",
                    data={
                        "WINEEFFECT": (self.Wine_effects, 3),
                    },
                    is_time_consuming=False,
                    is_difficult=False,
                    weight=49,
                ),
            ])

        if self.Enable_BWater & self.Enable_PABCDE:
            templates.extend([
                GameObjectiveTemplate(
                    label="[Water Base] Create a potion with the effects: WATEREFFECT.",
                    data={
                        "WATEREFFECT": (self.Water_Effects, 5),
                    },
                    is_time_consuming=False,
                    is_difficult=False,
                    weight=49,
                ),
            ])

        if self.Enable_BOil & self.Enable_PABCDE:
            templates.extend([
                GameObjectiveTemplate(
                    label="[Oil Base] Create a potion with the effects: OILEFFECT.",
                    data={
                        "OILEFFECT": (self.Oil_Effects, 5),
                    },
                    is_time_consuming=False,
                    is_difficult=False,
                    weight=49,
                ),
            ])

        if self.Enable_BWine & self.Enable_PABCDE:
            templates.extend([
                GameObjectiveTemplate(
                    label="[Wine Base] Create a potion with the effects: WINEEFFECT.",
                    data={
                        "WINEEFFECT": (self.Wine_effects, 5),
                    },
                    is_time_consuming=False,
                    is_difficult=False,
                    weight=49,
                ),
            ])

        if self.Enable_BWater & self.Enable_PAAAR1:
            templates.extend([
                GameObjectiveTemplate(
                    label="[Water Base] Create a strong potion of WATEREFFECT while WATERRESTRICTION.",
                    data={
                        "WATEREFFECT": (self.Water_Effects, 1),
                        "WATERRESTRICTION": (self.Water_Restrictions, 1),
                    },
                    is_time_consuming=False,
                    is_difficult=False,
                    weight=49,
                ),
            ])

        if self.Enable_BOil & self.Enable_PAAAR1:
            templates.extend([
                GameObjectiveTemplate(
                    label="[Oil Base] Create a strong potion of OILEFFECT while OILRESTRICTION.",
                    data={
                        "OILEFFECT": (self.Oil_Effects, 1),
                        "OILRESTRICTION": (self.Oil_Restrictions, 1),
                    },
                    is_time_consuming=False,
                    is_difficult=False,
                    weight=49,
                ),
            ])

        if self.Enable_BWine & self.Enable_PAAAR1:
            templates.extend([
                GameObjectiveTemplate(
                    label="[Wine Base] Create a strong potion of WINEEFFECT while WINERESTRICTION.",
                    data={
                        "WINEEFFECT": (self.Wine_effects, 1),
                        "WINERESTRICTION": (self.Wine_Restrictions, 1),
                    },
                    is_time_consuming=False,
                    is_difficult=False,
                    weight=49,
                ),
            ])

        if self.Enable_BWater & self.Enable_PAR1:
            templates.extend([
                GameObjectiveTemplate(
                    label="[Water Base] Create a Weak potion of WATEREFFECT while WATERRESTRICTION.",
                    data={
                        "WATEREFFECT": (self.Water_Effects, 1),
                        "WATERRESTRICTION": (self.Water_Restrictions, 1),
                    },
                    is_time_consuming=False,
                    is_difficult=False,
                    weight=49,
                ),
            ])

        if self.Enable_BOil & self.Enable_PAR1:
            templates.extend([
                GameObjectiveTemplate(
                    label="[Oil Base] Create a Weak potion of OILEFFECT while OILRESTRICTION.",
                    data={
                        "OILEFFECT": (self.Oil_Effects, 1),
                        "OILRESTRICTION": (self.Oil_Restrictions, 1),
                    },
                    is_time_consuming=False,
                    is_difficult=False,
                    weight=49,
                ),
            ])

        if self.Enable_BWine & self.Enable_PAR1:
            templates.extend([
                GameObjectiveTemplate(
                    label="[Wine Base] Create a weak potion of WINEEFFECT while WINERESTRICTION.",
                    data={
                        "WINEEFFECT": (self.Wine_effects, 1),
                        "WINERESTRICTION": (self.Wine_Restrictions, 1),
                    },
                    is_time_consuming=False,
                    is_difficult=False,
                    weight=49,
                ),
            ])
            
        if self.Enable_BWater & self.Enable_PAABBCR1:
            templates.extend([
                GameObjectiveTemplate(
                    label="[Water Base] Create a potion with the effects: WATEREFFECT at Medium, Medium and Weak Strength Respectively while WATERRESTRICTION.",
                    data={
                        "WATEREFFECT": (self.Water_Effects, 3),
                        "WATERRESTRICTION": (self.Water_Restrictions, 1),
                    },
                    is_time_consuming=False,
                    is_difficult=False,
                    weight=49,
                ),
            ])

        if self.Enable_BOil & self.Enable_PAABBCR1:
            templates.extend([
                GameObjectiveTemplate(
                    label="[Oil Base] Create a potion with the effects: OILEFFECT Medium, Medium and Weak Strength Respectively while OILRESTRICTION.",
                    data={
                        "OILEFFECT": (self.Oil_Effects, 3),
                        "OILRESTRICTION": (self.Oil_Restrictions, 1),
                    },
                    is_time_consuming=False,
                    is_difficult=False,
                    weight=49,
                ),
            ])

        if self.Enable_BWine & self.Enable_PAABBCR1:
            templates.extend([
                GameObjectiveTemplate(
                    label="[Wine Base] Create a potion with the effects: WINEEFFECT Medium, Medium and Weak Strength Respectively while WINERESTRICTION.",
                    data={
                        "WINEEFFECT": (self.Wine_effects, 3),
                        "WINERESTRICTION": (self.Wine_Restrictions, 1),
                    },
                    is_time_consuming=False,
                    is_difficult=False,
                    weight=49,
                ),
            ])

        if self.Enable_BWater & self.Enable_PAAABBR1:
            templates.extend([
                GameObjectiveTemplate(
                    label="[Water Base] Create a potion with the effects: WATEREFFECT at strong and medium effectiveness respectively while WATERRESTRICTION.",
                    data={
                        "WATEREFFECT": (self.Water_Effects, 2),
                        "WATERRESTRICTION": (self.Water_Restrictions, 1),
                    },
                    is_time_consuming=False,
                    is_difficult=False,
                    weight=49,
                ),
            ])

        if self.Enable_BOil & self.Enable_PAAABBR1:
            templates.extend([
                GameObjectiveTemplate(
                    label="[Oil Base] Create a potion with the effects: OILEFFECT at strong and medium effectiveness respectively while OILRESTRICTION.",
                    data={
                        "OILEFFECT": (self.Oil_Effects, 2),
                        "OILRESTRICTION": (self.Oil_Restrictions, 1),
                    },
                    is_time_consuming=False,
                    is_difficult=False,
                    weight=49,
                ),
            ])

        if self.Enable_BWine & self.Enable_PAAABBR1:
            templates.extend([
                GameObjectiveTemplate(
                    label="[Wine Base] Create a potion with the effects: WINEEFFECT at strong and medium effectiveness respectively while WINERESTRICTION.",
                    data={
                        "WINEEFFECT": (self.Wine_effects, 2),
                        "WINERESTRICTION": (self.Wine_Restrictions, 1),
                    },
                    is_time_consuming=False,
                    is_difficult=False,
                    weight=49,
                ),
            ])

        if self.Enable_BWater & self.Enable_PAAABCR1:
            templates.extend([
                GameObjectiveTemplate(
                    label="[Water Base] Create a potion with the effects: WATEREFFECT at strong weak and weak effectiveness respectively while WATERRESTRICTION.",
                    data={
                        "WATEREFFECT": (self.Water_Effects, 3),
                        "WATERRESTRICTION": (self.Water_Restrictions, 1),
                    },
                    is_time_consuming=False,
                    is_difficult=False,
                    weight=49,
                ),
            ])

        if self.Enable_BOil & self.Enable_PAAABCR1:
            templates.extend([
                GameObjectiveTemplate(
                    label="[Oil Base] Create a potion with the effects: OILEFFECT at strong weak and weak effectiveness respectively while OILRESTRICTION.",
                    data={
                        "OILEFFECT": (self.Oil_Effects, 3),
                        "OILRESTRICTION": (self.Oil_Restrictions, 1),
                    },
                    is_time_consuming=False,
                    is_difficult=False,
                    weight=49,
                ),
            ])

        if self.Enable_BWine & self.Enable_PAAABCR1:
            templates.extend([
                GameObjectiveTemplate(
                    label="[Wine Base] Create a potion with the effects: WINEEFFECT at strong weak and weak effectiveness respectively while WINERESTRICTION.",
                    data={
                        "WINEEFFECT": (self.Wine_effects, 3),
                        "WINERESTRICTION": (self.Wine_Restrictions, 1),
                    },
                    is_time_consuming=False,
                    is_difficult=False,
                    weight=49,
                ),
            ])

        if self.Enable_BWater & self.Enable_PABCDER1:
            templates.extend([
                GameObjectiveTemplate(
                    label="[Water Base] Create a potion with the effects: WATEREFFECT while WATERRESTRICTION.",
                    data={
                        "WATEREFFECT": (self.Water_Effects, 5),
                        "WATERRESTRICTION": (self.Water_Restrictions, 1),
                    },
                    is_time_consuming=False,
                    is_difficult=False,
                    weight=49,
                ),
            ])

        if self.Enable_BOil & self.Enable_PABCDER1:
            templates.extend([
                GameObjectiveTemplate(
                    label="[Oil Base] Create a potion with the effects: OILEFFECT while OILRESTRICTION.",
                    data={
                        "OILEFFECT": (self.Oil_Effects, 5),
                        "OILRESTRICTION": (self.Oil_Restrictions, 1),
                    },
                    is_time_consuming=False,
                    is_difficult=False,
                    weight=49,
                ),
            ])

        if self.Enable_BWine & self.Enable_PABCDER1:
            templates.extend([
                GameObjectiveTemplate(
                    label="[Wine Base] Create a potion with the effects: WINEEFFECT while WINERESTRICTION.",
                    data={
                        "WINEEFFECT": (self.Wine_effects, 5),
                        "WINERESTRICTION": (self.Wine_Restrictions, 1),
                    },
                    is_time_consuming=False,
                    is_difficult=False,
                    weight=49,
                ),
            ])

        if self.Enable_BWater & self.Enable_PAAAR2:
            templates.extend([
                GameObjectiveTemplate(
                    label="[Water Base] Create a strong potion of WATEREFFECT while WATERRESTRICTION.",
                    data={
                        "WATEREFFECT": (self.Water_Effects, 1),
                        "WATERRESTRICTION": (self.Water_Restrictions, 2),
                    },
                    is_time_consuming=False,
                    is_difficult=True,
                    weight=49,
                ),
            ])

        if self.Enable_BOil & self.Enable_PAAAR2:
            templates.extend([
                GameObjectiveTemplate(
                    label="[Oil Base] Create a strong potion of OILEFFECT while OILRESTRICTION.",
                    data={
                        "OILEFFECT": (self.Oil_Effects, 1),
                        "OILRESTRICTION": (self.Oil_Restrictions, 2),
                    },
                    is_time_consuming=False,
                    is_difficult=True,
                    weight=49,
                ),
            ])

        if self.Enable_BWine & self.Enable_PAAAR2:
            templates.extend([
                GameObjectiveTemplate(
                    label="[Wine Base] Create a strong potion of WINEEFFECT while WINERESTRICTION.",
                    data={
                        "WINEEFFECT": (self.Wine_effects, 1),
                        "WINERESTRICTION": (self.Wine_Restrictions, 2),
                    },
                    is_time_consuming=False,
                    is_difficult=True,
                    weight=49,
                ),
            ])

        if self.Enable_BWater & self.Enable_PAR2:
            templates.extend([
                GameObjectiveTemplate(
                    label="[Water Base] Create a Weak potion of WATEREFFECT while WATERRESTRICTION.",
                    data={
                        "WATEREFFECT": (self.Water_Effects, 1),
                        "WATERRESTRICTION": (self.Water_Restrictions, 2),
                    },
                    is_time_consuming=False,
                    is_difficult=True,
                    weight=49,
                ),
            ])

        if self.Enable_BOil & self.Enable_PAR2:
            templates.extend([
                GameObjectiveTemplate(
                    label="[Oil Base] Create a Weak potion of OILEFFECT while OILRESTRICTION.",
                    data={
                        "OILEFFECT": (self.Oil_Effects, 1),
                        "OILRESTRICTION": (self.Oil_Restrictions, 2),
                    },
                    is_time_consuming=False,
                    is_difficult=True,
                    weight=49,
                ),
            ])

        if self.Enable_BWine & self.Enable_PAR2:
            templates.extend([
                GameObjectiveTemplate(
                    label="[Wine Base] Create a weak potion of WINEEFFECT while WINERESTRICTION.",
                    data={
                        "WINEEFFECT": (self.Wine_effects, 1),
                        "WINERESTRICTION": (self.Wine_Restrictions, 2),
                    },
                    is_time_consuming=False,
                    is_difficult=True,
                    weight=49,
                ),
            ])
            
        if self.Enable_BWater & self.Enable_PAABBCR2:
            templates.extend([
                GameObjectiveTemplate(
                    label="[Water Base] Create a potion with the effects: WATEREFFECT at Medium, Medium and Weak Strength Respectively while WATERRESTRICTION.",
                    data={
                        "WATEREFFECT": (self.Water_Effects, 3),
                        "WATERRESTRICTION": (self.Water_Restrictions, 2),
                    },
                    is_time_consuming=False,
                    is_difficult=True,
                    weight=49,
                ),
            ])

        if self.Enable_BOil & self.Enable_PAABBCR2:
            templates.extend([
                GameObjectiveTemplate(
                    label="[Oil Base] Create a potion with the effects: OILEFFECT Medium, Medium and Weak Strength Respectively while OILRESTRICTION.",
                    data={
                        "OILEFFECT": (self.Oil_Effects, 3),
                        "OILRESTRICTION": (self.Oil_Restrictions, 2),
                    },
                    is_time_consuming=False,
                    is_difficult=True,
                    weight=49,
                ),
            ])

        if self.Enable_BWine & self.Enable_PAABBCR2:
            templates.extend([
                GameObjectiveTemplate(
                    label="[Wine Base] Create a potion with the effects: WINEEFFECT Medium, Medium and Weak Strength Respectively while WINERESTRICTION.",
                    data={
                        "WINEEFFECT": (self.Wine_effects, 3),
                        "WINERESTRICTION": (self.Wine_Restrictions, 2),
                    },
                    is_time_consuming=False,
                    is_difficult=True,
                    weight=49,
                ),
            ])

        if self.Enable_BWater & self.Enable_PAAABBR2:
            templates.extend([
                GameObjectiveTemplate(
                    label="[Water Base] Create a potion with the effects: WATEREFFECT at strong and medium effectiveness respectively while WATERRESTRICTION.",
                    data={
                        "WATEREFFECT": (self.Water_Effects, 2),
                        "WATERRESTRICTION": (self.Water_Restrictions, 2),
                    },
                    is_time_consuming=False,
                    is_difficult=True,
                    weight=49,
                ),
            ])

        if self.Enable_BOil & self.Enable_PAAABBR2:
            templates.extend([
                GameObjectiveTemplate(
                    label="[Oil Base] Create a potion with the effects: OILEFFECT at strong and medium effectiveness respectively while OILRESTRICTION.",
                    data={
                        "OILEFFECT": (self.Oil_Effects, 2),
                        "OILRESTRICTION": (self.Oil_Restrictions, 2),
                    },
                    is_time_consuming=False,
                    is_difficult=True,
                    weight=49,
                ),
            ])

        if self.Enable_BWine & self.Enable_PAAABBR2:
            templates.extend([
                GameObjectiveTemplate(
                    label="[Wine Base] Create a potion with the effects: WINEEFFECT at strong and medium effectiveness respectively while WINERESTRICTION.",
                    data={
                        "WINEEFFECT": (self.Wine_effects, 2),
                        "WINERESTRICTION": (self.Wine_Restrictions, 2),
                    },
                    is_time_consuming=False,
                    is_difficult=True,
                    weight=49,
                ),
            ])

        if self.Enable_BWater & self.Enable_PAAABCR2:
            templates.extend([
                GameObjectiveTemplate(
                    label="[Water Base] Create a potion with the effects: WATEREFFECT at strong weak and weak effectiveness respectively while WATERRESTRICTION.",
                    data={
                        "WATEREFFECT": (self.Water_Effects, 3),
                        "WATERRESTRICTION": (self.Water_Restrictions, 2),
                    },
                    is_time_consuming=False,
                    is_difficult=True,
                    weight=49,
                ),
            ])

        if self.Enable_BOil & self.Enable_PAAABCR2:
            templates.extend([
                GameObjectiveTemplate(
                    label="[Oil Base] Create a potion with the effects: OILEFFECT at strong weak and weak effectiveness respectively while OILRESTRICTION.",
                    data={
                        "OILEFFECT": (self.Oil_Effects, 3),
                        "OILRESTRICTION": (self.Oil_Restrictions, 2),
                    },
                    is_time_consuming=False,
                    is_difficult=True,
                    weight=49,
                ),
            ])

        if self.Enable_BWine & self.Enable_PAAABCR2:
            templates.extend([
                GameObjectiveTemplate(
                    label="[Wine Base] Create a potion with the effects: WINEEFFECT at strong weak and weak effectiveness respectively while WINERESTRICTION.",
                    data={
                        "WINEEFFECT": (self.Wine_effects, 3),
                        "WINERESTRICTION": (self.Wine_Restrictions, 2),
                    },
                    is_time_consuming=False,
                    is_difficult=True,
                    weight=49,
                ),
            ])

        if self.Enable_BWater & self.Enable_PABCDER2:
            templates.extend([
                GameObjectiveTemplate(
                    label="[Water Base] Create a potion with the effects: WATEREFFECT while WATERRESTRICTION.",
                    data={
                        "WATEREFFECT": (self.Water_Effects, 5),
                        "WATERRESTRICTION": (self.Water_Restrictions, 2),
                    },
                    is_time_consuming=False,
                    is_difficult=True,
                    weight=49,
                ),
            ])

        if self.Enable_BOil & self.Enable_PABCDER2:
            templates.extend([
                GameObjectiveTemplate(
                    label="[Oil Base] Create a potion with the effects: OILEFFECT while OILRESTRICTION.",
                    data={
                        "OILEFFECT": (self.Oil_Effects, 5),
                        "OILRESTRICTION": (self.Oil_Restrictions, 2),
                    },
                    is_time_consuming=False,
                    is_difficult=True,
                    weight=49,
                ),
            ])

        if self.Enable_BWine & self.Enable_PABCDER2:
            templates.extend([
                GameObjectiveTemplate(
                    label="[Wine Base] Create a potion with the effects: WINEEFFECT while WINERESTRICTION.",
                    data={
                        "WINEEFFECT": (self.Wine_effects, 5),
                        "WINERESTRICTION": (self.Wine_Restrictions, 2),
                    },
                    is_time_consuming=False,
                    is_difficult=True,
                    weight=49,
                ),
            ])
        return templates

    @property
    def bases(self) -> List[str]:
        return sorted(self.archipelago_options.Potion_Bases.value)
    
    @property
    def Objective_Types(self) -> List[str]:
        return sorted(self.archipelago_options.Objective_Types.value)

    @property
    def Hard_Water(self) -> bool:
        return bool(self.archipelago_options.Enable_Hard_Water.value)

    @property
    def Enabled_Trials_Num(self) -> int:
        Enabled_Trials_Num = len(self.bases) * len(self.Objective_Types)
        if Enabled_Trials_Num == 0:
            Enabled_Trials_Num = 1
        return Enabled_Trials_Num

    @property
    def Enable_BWater(self) -> bool:
        return "Water" in self.bases

    @property
    def Enable_BOil(self) -> bool:
        return "Oil" in self.bases

    @property
    def Enable_BWine(self) -> bool:
        return "Wine" in self.bases
    
    @property
    def Enable_PAAA(self) -> bool:
        return "Strong Potion" in self.Objective_Types
    
    @property
    def Enable_PA(self) -> bool:
        return "Weak Potion" in self.Objective_Types
    
    @property
    def Enable_PAABBC(self) -> bool:
        return "Dual Medium with Side Effect" in self.Objective_Types
    
    @property
    def Enable_PAAABB(self) -> bool:
        return "Strong with side effect" in self.Objective_Types
    
    @property
    def Enable_PAAABC(self) -> bool:
        return "Strong with two side effects" in self.Objective_Types
    
    @property
    def Enable_PABCDE(self) -> bool:
        return "Chaos" in self.Objective_Types
    
    @property
    def Enable_PAAAR1(self) -> bool:
        return "Strong Potion with 1 restriction" in self.Objective_Types
    
    @property
    def Enable_PAR1(self) -> bool:
        return "Weak Potion with 1 restriction" in self.Objective_Types
    
    @property
    def Enable_PAABBCR1(self) -> bool:
        return "Dual Medium with Side Effect with 1 restriction" in self.Objective_Types
    
    @property
    def Enable_PAAABBR1(self) -> bool:
        return "Strong with side effect with 1 restriction" in self.Objective_Types
    
    @property
    def Enable_PAAABCR1(self) -> bool:
        return "Strong with two side effects with 1 restriction" in self.Objective_Types
    
    @property
    def Enable_PABCDER1(self) -> bool:
        return "Chaos with 1 restriction" in self.Objective_Types
    
    @property
    def Enable_PAAAR2(self) -> bool:
        return "Strong Potion with 2 restrictions" in self.Objective_Types
    
    @property
    def Enable_PAR2(self) -> bool:
        return "Weak Potion with 2 restrictions" in self.Objective_Types
    
    @property
    def Enable_PAABBCR2(self) -> bool:
        return "Dual Medium with Side Effect with 2 restrictions" in self.Objective_Types
    
    @property
    def Enable_PAAABBR2(self) -> bool:
        return "Strong with side effect with 2 restrictions" in self.Objective_Types
    
    @property
    def Enable_PAAABCR2(self) -> bool:
        return "Strong with two side effects with 2 restrictions" in self.Objective_Types
    
    @property
    def Enable_PABCDER2(self) -> bool:
        return "Chaos with 2 restrictions" in self.Objective_Types
    
    @functools.cached_property
    def Easy_Water_Effects(self) -> List[str]:
        return [
            "Healing",
            "Poisoning",
            "Fire",
            "Frost",
            "Explosion",
            "Wild Growth",
            "Dexterity",
            "Swiftness",
            "Lightning",
            "Mana",
            "Stone Skin",
            "Sleep",
            "Light",
            "Charm",
            "Slowness",
            "Rage",
            "Magical Vision",
            "Acid",
            "Libido",
            "Invisibility",
            "Levitation",
            "Necromancy",
        ]

    @functools.cached_property
    def Hard_Water_Effects(self) -> List[str]:
        return [
            "Poison Protection",
            "Lightning Protection",
            "Fire Protection",
            "Frost Protection",
            "Gluing",
            "Slipperiness",
            "Stench",
            "Acid Protection",
            "Anti-Magic",
            "Shrinking",
            "Enlargement",
            "Rejuvenation",
            "Inspiration",
            "Fragrance",
            "Fear",
            "Hallucinations",
            "Luck",
            "Curse"
        ]

    def Water_Effects(self) -> List[str]:
        Water_Effects = self.Easy_Water_Effects[:]

        if self.Hard_Water:
            Water_Effects.extend(self.Hard_Water_Effects)

        return sorted(Water_Effects)

    @staticmethod
    def Oil_Effects() -> List[str]:
        return [
            "Fire Protection",
            "Frost Protection",
            "Lightning Protection",
            "Poison Protection",
            "Acid Protection",
            "Anti-Magic",
            "Slipperiness",
            "Gluing",
            "Stench",
            "Elargement",
            "Shrinking",
            "Rejuvenation",
            "Explosion",
            "Fire",
            "Healing",
            "Invisibility",
            "Lightning",
            "Light",
            "Poisoning",
            "Stone Skin",
            "Wild Growth",
        ]

    @staticmethod
    def Wine_effects() -> list[str]:
        return [
            "Fear",
            "Inspiration",
            "Luck",
            "Hallucinations",
            "Fragrance",
            "Curse",
            "Healing",
            "Frost",
            "Strength",
            "Swiftness",
            "Mana",
            "Dexterity",
            "Sleep",
            "Slowness",
            "Acid",
            "Libido",
            "Rage",
            "Charm",
            "Levitation",
            "Magical Vision",
            "Necromancy",
        ]

    @functools.cached_property
    def Base_Restrictions(self) -> list[str]:
        return [
            "collecting 50 singular books",
            "collecting 25 dual books",
            "collecting 10 triple books",
            "collecting 2 quadruple books",
            "collecting 1 quintuple books",
            "not Running into skulls",
            "not Stirring before putting all your ingredients in",
            "not using any plants",
            "not using any mushrooms",
            "only using 3 unique ingredients excluding the base",
            "using only the items sold by 1 instance of a merchant",
        ]

    @functools.cached_property
    def EXWater_Restrictions(self) -> list[str]:
        return [
            "not using any extra water",
            "Going through 3 whirlpools"
        ]

    @functools.cached_property
    def EXEasy_Water_Restrictions(self) -> list[str]:
        return [
            "Not using Any crystals",
            "Not using Any salts",
        ]

    @functools.cached_property
    def EXHard_Water_Restrictions(self) -> list[str]:
        return [
            'clicking the "Finish Potion" button at the edge of the map', 
        ]

    @functools.cached_property
    def EXOil_Restrictions(self) -> list[str]:
        return [
            "Not using Any crystals",
            "Not using Any salts",
            "Going through 3 whirlpools",
            "not using any extra oil",
            'clicking the "Finish Potion" button at the edge of the map',
            "not touching any swamps",
        ]

    @functools.cached_property
    def EXWine_Restrictions(self) -> list[str]:
        return [
            "not using any extra wine",
            'clicking the "Finish Potion" button at the edge of the map',
        ]

    def Water_Restrictions(self) -> List[str]:
        Water_Restrictions = self.Base_Restrictions[:]
        
        Water_Restrictions.extend(self.EXWater_Restrictions)
        if self.Hard_Water == False:
            Water_Restrictions.extend(self.EXEasy_Water_Restrictions)
        if self.Hard_Water:
            Water_Restrictions.extend(self.EXHard_Water_Restrictions)

        return sorted(Water_Restrictions)

    def Oil_Restrictions(self) -> List[str]:
        Oil_Restrictions = self.Base_Restrictions[:]
        Oil_Restrictions.extend(self.EXOil_Restrictions)
        return sorted(Oil_Restrictions)


    def Wine_Restrictions(self) -> List[str]:
        Wine_Restrictions = self.Base_Restrictions[:]
        Wine_Restrictions.extend(self.EXWine_Restrictions)
        return sorted(Wine_Restrictions)


# Archipelago Options
class PotionBases(OptionSet):
    """
    Enabled Potion Bases
    """

    valid_keys = [
        "Water",
        "Oil",
        "Wine",
    ]
    default = valid_keys
class ObjectiveTypes(OptionSet):
    """
    Which objectivetypes to enable, completing a day will appear by default
    requires at least 1 base to be enabled
    Strong Potion = Create a Strong potion (AAA__)
    Weak Potion = Create a Weak potion (A____)
    Dual Medium with Side Effect = Create a potion with 2 medium effects and 1 weak one (AABBC)
    Strong with Side Effect = Create a Strong potion with 1 side effect (AAABB)
    Strong with two Side Effects = Create a Strong potion with 1 side effect (AAABC)
    Chaos = 5 different effects at once (ABCDE)
    all of these come with variants that have 1 restriction and have 2 restrictions, add in the ones that arent in the default by just typing "with 1 restriction" or "with 2 restrictions" to add them
    2 restrictions does nothing good if you dont have difficuly objectives enabled
    """

    valid_keys = [
        "Strong Potion",
        "Weak Potion",
        "Dual Medium with Side Effect",
        "Strong with side effect",
        "Strong with two side effects",
        "Chaos",
        "Strong Potion with 1 restriction",
        "Weak Potion with 1 restriction",
        "Dual Medium with Side Effect with 1 restriction",
        "Strong with side effect with 1 restriction",
        "Strong with two side effects with 1 restriction",
        "Chaos with 1 restriction",
        "Strong Potion with 2 restrictions",
        "Weak Potion with 2 restrictions",
        "Dual Medium with Side Effect with 2 restrictions",
        "Strong with side effect with 2 restrictions",
        "Strong with two side effects with 2 restrictions",
        "Chaos with 2 restrictions",
    ]
    default = [
        "Strong Potion",
        "Weak Potion",
        "Dual Medium with Side Effect",
        "Strong with side effect",
        "Strong with two side effects",
        "Chaos",
        "Strong Potion with 1 restriction",
        "Weak Potion with 1 restriction",
        "Dual Medium with Side Effect with 1 restriction",
        "Strong with side effect with 1 restriction",
        "Strong with two side effects with 1 restriction",
        "Strong Potion with 2 restrictions",
        "Weak Potion with 2 restrictions",
    ]
class PotionCraftWaterBaseDifficulty(Toggle):
    """
    Whether to include Potion Effects in the Outer Ring in the water base
    """

    display_name = "Potion Craft Water Base Difficulty"