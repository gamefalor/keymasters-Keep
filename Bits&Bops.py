from __future__ import annotations
import functools
from typing import List, Dict, Set
from dataclasses import dataclass
from Options import Toggle, OptionSet, Choice, NamedRange, Range
from ..game import Game
from ..game_objective_template import GameObjectiveTemplate
from ..enums import KeymastersKeepGamePlatforms

@dataclass
class BitsBopsArchipelagoOptions:
    Bits_Bops_Perfects: BitsBopsPerfects
    Bits_Bops_Infinite_games: BitsBopsInfiniteGameSelection
    Bits_Bops_Min_Clock: BitsBopsClockMinScore
    Bits_Bops_Max_Clock: BitsBopsClockMaxScore
    Bits_Bops_Min_Race: BitsBopsRaceMinScore
    Bits_Bops_Max_Race: BitsBopsRaceMaxScore
    Bits_Bops_Min_Smith: BitsBopsBlacksmithMinScore
    Bits_Bops_Max_Smith: BitsBopsBlacksmithMaxScore


class BitsBopsGame(Game):
    name = "Bits & Bops"
    platform = KeymastersKeepGamePlatforms.PC
    is_adult_only_or_unrated = False 
    options_cls = BitsBopsArchipelagoOptions
    def optional_game_constraint_templates(self) -> List[GameObjectiveTemplate]:
        return list()

    def game_objective_templates(self) -> List[GameObjectiveTemplate]:
        templates: List[GameObjectiveTemplate] = [
            GameObjectiveTemplate(
                label="Get at least RESULT in SONG",
                data={
                    "RESULT": (self.results, 1),
                    "SONG": (self.songs, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=20,
            ),
        ]

        if self.perfects:
            templates.extend([
                GameObjectiveTemplate(
                    label="Get Perfect in SONG",
                    data={
                        "SONG": (self.songs, 1),
                    },
                    is_time_consuming=False,
                    is_difficult=True,
                    weight=2,
                ),
            ])

        if self.Clock_Enabled:
            templates.extend([
                GameObjectiveTemplate(
                    label="Survive SCORE seconds in the Clock infinite Minigame in one shot",
                    data={
                        "SCORE": (self.Clock_Scores, 1),
                    },
                    is_time_consuming=False,
                    is_difficult=False,
                    weight=1,
                ),
            ])

        if self.Symphony_Enabled:
            templates.extend([
                GameObjectiveTemplate(
                    label="Complete any song in the Symphony minigame",
                    data={
                    },
                    is_time_consuming=False,
                    is_difficult=False,
                    weight=1,
                ),
            ])

        if self.Race_Enabled:
            templates.extend([
                GameObjectiveTemplate(
                    label="Walk SCORE steps in the Three-Legged race infinite minigame in one shot",
                    data={
                        "SCORE": (self.Race_Scores, 1),
                    },
                    is_time_consuming=False,
                    is_difficult=False,
                    weight=1,
                ),
            ])

        if self.Blacksmith_Enabled:
            templates.extend([
                GameObjectiveTemplate(
                    label="Forge SCORE items in the BlackSmith infinite minigame in one shot",
                    data={
                        "SCORE": (self.Blacksmith_Scores, 1),
                    },
                    is_time_consuming=False,
                    is_difficult=False,
                    weight=1,
                ),
            ])

        if self.Encore_Enabled:
            templates.extend([
                GameObjectiveTemplate(
                    label="Get The curtains to open in the Encore minigame",
                    data={
                    },
                    is_time_consuming=False,
                    is_difficult=False,
                    weight=1,
                ),
            ])

        return templates

    @property
    def perfects(self) -> bool:
        return bool(self.archipelago_options.Bits_Bops_Perfects.value)
    
    @property
    def Infinite_games(self) -> List[str]:
        return sorted(self.archipelago_options.Bits_Bops_Infinite_games.value)

    @property
    def Clock_Enabled(self) -> bool:
        return "Clock" in self.Infinite_games
    
    @property
    def Symphony_Enabled(self) -> bool:
        return "Symphony" in self.Infinite_games
    
    @property
    def Race_Enabled(self) -> bool:
        return "Race" in self.Infinite_games
    
    @property
    def Blacksmith_Enabled(self) -> bool:
        return "Blacksmith" in self.Infinite_games
    
    @property
    def Encore_Enabled(self) -> bool:
        return "Encore" in self.Infinite_games

    def Clock_Scores(self) -> range:
        if self.archipelago_options.Bits_Bops_Max_Clock.value < self.archipelago_options.Bits_Bops_Min_Clock.value:
            raise OptionError("BITS&BOPS: Clock Max goal cannot be lower than the Min")
        return range(int(self.archipelago_options.Bits_Bops_Min_Clock.value),int(self.archipelago_options.Bits_Bops_Max_Clock.value) +1)

    def Race_Scores(self) -> range:
        if self.archipelago_options.Bits_Bops_Max_Race.value < self.archipelago_options.Bits_Bops_Min_Race.value:
            raise OptionError("BITS&BOPS: Race Max goal cannot be lower than the Min")
        return range(int(self.archipelago_options.Bits_Bops_Min_Race.value),int(self.archipelago_options.Bits_Bops_Max_Race.value) +1)

    def Blacksmith_Scores(self) -> range:
        if self.archipelago_options.Bits_Bops_Max_Smith.value < self.archipelago_options.Bits_Bops_Min_Smith.value:
            raise OptionError("BITS&BOPS: Blacksmith Max goal cannot be lower than the Min")
        return range(int(self.archipelago_options.Bits_Bops_Min_Smith.value),int(self.archipelago_options.Bits_Bops_Max_Smith.value) +1)

    @staticmethod
    def results() -> List[str]:
        return [
            "COOL",
            "AMAZING",
        ]

    @staticmethod
    def songs() -> List[str]:
        return [
            "Flipper Snapper",
            "Sweet Tooth",
            "Rock, Paper, Showdown!",
            "Pantry Parade",
            "Jungle Mixtape",
            "B-BOT & THE FLY GIRLS",
            "flow worms",
            "Meet & Tweet",
            "STEADY BEARS",
            "Sky Mixtape",
            "POP UP KITCHEN",
            "FIREWORK FESTIVAL",
            "HAMMER TIME!",
            "MOLECANO",
            "OCEAN MIXTAPE",
            "PRESIDENT BIRD",
            "SNAKEDOWN",
            "Octeaparty",
            "Globe Trotters",
            "FIRE MIXTAPE",
            "FINAL MIXTAPE",
        ]

# Archipelago Options
class BitsBopsPerfects(Toggle):
    """
    If you want the Bits & Bops perfects to be a possible requirement.
    Doesnt do anything if the implementation is not allowed to bring difficult requirements
    """
    display_name = "Bits & Bops Perfects enabled"
class BitsBopsInfiniteGameSelection(OptionSet):
    """
    Which of the *5* infinite games to include
    Valid Keys:
    - Clock
    - Symphony
    - Three Legged Race (might eventually change name)
    - Blacksmith
    - Encore (might eventually change name)
    """

    display_name = "Bits and Bops Infinite Game Selection"
    valid_keys = [
        "Clock",
        "Symphony",
        "Three Legged Race",
        "Blacksmith",
        "Encore",
    ]
    default = [
        "Clock",
        "Three Legged Race",
        "Blacksmith",
    ]
class BitsBopsClockMinScore(Range):
    """
    The Minimum Score the Clock minigame will ask of you in seconds
    """
    range_start = 1
    range_end = 299
    default = 10
class BitsBopsClockMaxScore(Range):
    """
    The maximum Score the Clock minigame will ask of you in seconds
    """
    range_start = 2
    range_end = 300
    default = 20
class BitsBopsRaceMinScore(Range):
    """
    The Minimum Score the Three-Legged Race minigame will ask of you in steps
    """
    range_start = 1
    range_end = 999
    default = 25
class BitsBopsRaceMaxScore(Range):
    """
    The Maximum Score the Three-Legged Race minigame will ask of you in steps
    """
    range_start = 2
    range_end = 1000
    default = 50
class BitsBopsBlacksmithMinScore(Range):
    """
    The Minimum Score the Blacksmith minigame will ask of you in items
    """
    range_start = 1
    range_end = 49
    default = 5
class BitsBopsBlacksmithMaxScore(Range):
    """
    The Minimum Score the Blacksmith minigame will ask of you in items
    """
    range_start = 2
    range_end = 50
    default = 10