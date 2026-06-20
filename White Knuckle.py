from __future__ import annotations
from calendar import different_locale
import functools
import math
from typing import List, Dict, Set
from dataclasses import dataclass
from Options import Toggle, OptionSet, Choice, NamedRange, Range
from ..game import Game
from ..game_objective_template import GameObjectiveTemplate
from ..enums import KeymastersKeepGamePlatforms

@dataclass
class WhiteKnuckleArchipelagoOptions:
    ChosenAreas : WhiteKnuckleAreasEnabled
    MinClimbHeight : WhiteKnuckleMinHeight 
    MaxClimbHeight : WhiteKnuckleMaxHeight
    MinRoaches : WhiteKnuckleMinRoaches 
    MaxRoaches : WhiteKnuckleMaxRoaches
    MinScrap : WhiteKnuckleMinScrapCount
    MaxScrap : WhiteKnuckleMaxScrapCount
    AnyMapFrequency : WhiteKnuckleAnyMapFrequency

class WhiteKnuckle(Game):
    name = "White Knuckle"
    platform = KeymastersKeepGamePlatforms.PC
    is_adult_only_or_unrated = False 
    options_cls = WhiteKnuckleArchipelagoOptions
    def optional_game_constraint_templates(self) -> List[GameObjectiveTemplate]:
        return list()

    def game_objective_templates(self) -> List[GameObjectiveTemplate]:
        templates: List[GameObjectiveTemplate] = [
            GameObjectiveTemplate(
                label="Climb METERS0 meters in INFINITEMAP",
                data={
                    "METERS": (self.ClimbingHeights, 1),
                    "INFINITEMAP": (self.ChosenInfiniteMaps, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=20,
            ),
            GameObjectiveTemplate(
                label="Climb METERS0 meters in Any map",
                data={
                    "METERS": (self.ClimbingHeights, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=2 * self.archipelago_options.AnyMapFrequency.value,
            ),
            GameObjectiveTemplate(
                label="Deposit ROACHES roaches in INFINITEMAP",
                data={
                    "ROACHES": (self.RoachAmounts, 1),
                    "INFINITEMAP": (self.ChosenInfiniteMaps, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=10,
            ),
            GameObjectiveTemplate(
                label="Deposit ROACHES roaches in Any map",
                data={
                    "ROACHES": (self.RoachAmounts, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=self.archipelago_options.AnyMapFrequency.value,
            ),
            GameObjectiveTemplate(
                label="Scrap ROACHES worth of non-roach items roaches in INFINITEMAP",
                data={
                    "ROACHES": (self.ScrapAmounts, 1),
                    "INFINITEMAP": (self.Maps_NoChimney, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=10,
            ),
            GameObjectiveTemplate(
                label="Scrap ROACHES worth of non-roach items roaches in Any map",
                data={
                    "ROACHES": (self.ScrapAmounts, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=self.archipelago_options.AnyMapFrequency.value,
            ),]

        return templates
    
    @property
    def TrueMinClimbHeight(self) -> int:
        return math.floor (self.archipelago_options.MinClimbHeight.value / 50)
    
    @property
    def TrueMaxClimbHeight(self) -> int:
        return math.floor (self.archipelago_options.MaxClimbHeight.value / 50)

    @property
    def ClimbingHeights(self) -> range:
        if self.TrueMaxClimbHeight < self.TrueMinClimbHeight:
            raise OptionError("White Knuckle: Minimum climbing distance is higher tham maximum climbing distance")
        ClimbingHeights = range(self.archipelago_options.MinClimbHeight.value, self.archipelago_options.MaxClimbHeight.value + 1)
        return ClimbingHeights

    @property
    def RoachAmounts(self) -> range:
        if self.TrueMaxClimbHeight < self.TrueMinClimbHeight:
            raise OptionError("White Knuckle: Minimum Roaches deposited is higher tham maximum Roaches deposited")
        RoachAmounts = range(self.archipelago_options.MinRoaches.value, self.archipelago_options.MaxRoaches.value + 1)
        return RoachAmounts

    @property
    def ScrapAmounts(self) -> range:
        if self.TrueMaxClimbHeight < self.TrueMinClimbHeight:
            raise OptionError("White Knuckle: Minimum items scrapped is higher tham maximum items Scrapped")
        ScrapAmounts = range(self.archipelago_options.MinScrap.value, self.archipelago_options.MaxScrap.value + 1)
        return ScrapAmounts

    @property
    def ChosenInfiniteMaps(self) -> List[str]:
        return sorted(self.archipelago_options.ChosenAreas.value)
    
    @property
    def Maps_NoChimney(self) -> List[str]:
        Maps: List[str] = self.ChosenInfiniteMaps[:]

        if "Chimney" in Maps:
            Maps.remove("Chimney")

        return Maps

# Archipelago Options
class WhiteKnuckleAreasEnabled(OptionSet):
    """
    Indicates which areas you might be asked to climb
    Valid keys are:
    - Campaign
    - Chimney
    - Endless Silos
    - Endless Pipeworks
    - Endless Habitation
    - Endless Abyss
    - Endless Underworks
    - Endless Substructure
    - Endless Superstructure
    """

    display_name = "White Knuckle Areas"
    valid_keys = [
        "Campaign",
        "Chimney",
        "Endless Silos",
        "Endless Pipeworks",
        "Endless Habitation",
        "Endless Abyss",
        "Endless Underworks",
        "Endless Substructure",
        "Endless Superstructure",
        ]
    default = valid_keys
    
class WhiteKnuckleMinHeight(Range):
    """
    The minimum height you will be asked to climb in 1 session
    end result gets multiplied by 10
    """
    range_start = 10
    range_end = 199
    default = 25
class WhiteKnuckleMaxHeight(Range):
    """
    ^ same as above
    except the maximum
    """
    range_start = 11
    range_end = 200
    default = 50
    
class WhiteKnuckleMinRoaches(Range):
    """
    The minimum Roaches you will be asked to deposit in 1 session
    """
    range_start = 1
    range_end = 99
    default = 10
class WhiteKnuckleMaxRoaches(Range):
    """
    ^ same as above
    except the maximum
    """
    range_start = 2
    range_end = 100
    default = 20
    
class WhiteKnuckleMinScrapCount(Range):
    """
    The minimum Roaches worth of items you will be asked to scrap in 1 session
    recommended to not count the golden nugget for these challenges
    """
    range_start = 1
    range_end = 99
    default = 5
class WhiteKnuckleMaxScrapCount(Range):
    """
    ^ same as above
    except the maximum
    """
    range_start = 2
    range_end = 100
    default = 10

class WhiteKnuckleAnyMapFrequency(Range):
    """
    specifies how often the challenge doesnt specify the map
    useful if you want to do long runs
    multiplies the weight for the challenge by this amount /10
    """
    range_start = 0
    range_end = 100
    default = 20