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
    Bits_Bops_16_Difficulty: BitsBops16Difficulty
    Bits_Bops_33_Difficulty: BitsBops33Difficulty
    Bits_Bops_45_Difficulty: BitsBops45Difficulty
    Bits_Bops_78_Difficulty: BitsBops78Difficulty
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
        templates: List[GameObjectiveTemplate] = self.SongTemplates

        if self.Clock_Enabled:
            templates.extend([
                GameObjectiveTemplate(
                    label="Survive SCORE seconds in the Clock infinite Minigame in one shot",
                    data={
                        "SCORE": (self.Clock_Scores, 1),
                    },
                    is_time_consuming=False,
                    is_difficult=False,
                    weight=self.DifferentSpeedsEnabled,
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
                    weight=self.DifferentSpeedsEnabled,
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
                    weight=self.DifferentSpeedsEnabled,
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
                    weight=self.DifferentSpeedsEnabled,
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
                    weight=self.DifferentSpeedsEnabled,
                ),
            ])
        
        return templates
    
    @property
    def SongTemplates(self) -> List[GameObjectiveTemplate]:
        SongTemplates: List[GameObjectiveTemplate] = [];
        
        if not self.EnabledDiff16 and self.EnabledDiff33 and not self.EnabledDiff45 and not self.EnabledDiff78:
            SongTemplates.extend([
                GameObjectiveTemplate(
                    label="Get at least RESULT in SONG",
                    data={
                        "RESULT": (self.Scores33, 1),
                        "SONG": (self.songs, 1),
                    },
                is_time_consuming=False,
                is_difficult=False,
                weight=20,
            ),
        ])
        elif self.EnabledDiff33:
            SongTemplates.extend([
                GameObjectiveTemplate(
                    label="Get at least RESULT in SONG at speed 33",
                    data={
                        "RESULT": (self.Scores33, 1),
                        "SONG": (self.songs, 1),
                    },
                is_time_consuming=False,
                is_difficult=False,
                weight=20,
            ),
        ])

        if self.EnabledDiff16:
            SongTemplates.extend([
                GameObjectiveTemplate(
                    label="Get at least RESULT in SONG at speed 16",
                    data={
                        "RESULT": (self.Scores16, 1),
                        "SONG": (self.songs, 1),
                    },
                is_time_consuming=False,
                is_difficult=False,
                weight=20,
            ),
        ])

        if self.EnabledDiff45:
            SongTemplates.extend([
                GameObjectiveTemplate(
                    label="Get at least RESULT in SONG at speed 45",
                    data={
                        "RESULT": (self.Scores45, 1),
                        "SONG": (self.songs, 1),
                    },
                is_time_consuming=False,
                is_difficult=False,
                weight=20,
            ),
        ])

        if self.EnabledDiff78:
            SongTemplates.extend([
                GameObjectiveTemplate(
                    label="Get at least RESULT in SONG at speed 78",
                    data={
                        "RESULT": (self.Scores78, 1),
                        "SONG": (self.songs, 1),
                    },
                is_time_consuming=False,
                is_difficult=False,
                weight=20,
            ),
        ])
        
        return SongTemplates


    @property
    def Infinite_games(self) -> List[str]:
        return sorted(self.archipelago_options.Bits_Bops_Infinite_games.value)

    # this feels very cursed, no clue how to make it less cursed lmao
    # i miss c#
    @functools.cached_property
    def Cool(self) -> list[str]:
        return [
            "COOL",
        ]
    @functools.cached_property
    def Amazing(self) -> list[str]:
        return [
            "AMAZING",
        ]
    @functools.cached_property
    def Perfect(self) -> list[str]:
        return [
            "PERFECT",
        ]
    
    @property
    def EnabledDiff16(self) -> bool:
        return bool(self.archipelago_options.Bits_Bops_16_Difficulty.value != 0)
    @property
    def Scores16(self) -> list[str]:
        Scores16 = self.Cool[:]
        if (self.archipelago_options.Bits_Bops_16_Difficulty.value > 1):
            Scores16.extend(self.Amazing)
        if (self.archipelago_options.Bits_Bops_16_Difficulty.value > 2):
            Scores16.extend(self.Perfect)
        return Scores16
    
    @property
    def EnabledDiff33(self) -> bool:
        return bool(self.archipelago_options.Bits_Bops_33_Difficulty.value != 0)
    @property
    def Scores33(self) -> list[str]:
        Scores33 = self.Cool[:]
        if (self.archipelago_options.Bits_Bops_33_Difficulty.value > 1):
            Scores33.extend(self.Amazing)
        if (self.archipelago_options.Bits_Bops_33_Difficulty.value > 2):
            Scores33.extend(self.Perfect)
        return Scores33
    
    @property
    def EnabledDiff45(self) -> bool:
        return bool(self.archipelago_options.Bits_Bops_45_Difficulty.value != 0)
    @property
    def Scores45(self) -> list[str]:
        Scores45 = self.Cool[:]
        if (self.archipelago_options.Bits_Bops_45_Difficulty.value > 1):
            Scores45.extend(self.Amazing)
        if (self.archipelago_options.Bits_Bops_45_Difficulty.value > 2):
            Scores45.extend(self.Perfect)
        return Scores45
    
    @property
    def EnabledDiff78(self) -> bool:
        return bool(self.archipelago_options.Bits_Bops_78_Difficulty.value != 0)
    @property
    def Scores78(self) -> list[str]:
        Scores78 = self.Cool[:]
        if (self.archipelago_options.Bits_Bops_78_Difficulty.value > 1):
            Scores78.extend(self.Amazing)
        if (self.archipelago_options.Bits_Bops_78_Difficulty.value > 2):
            Scores78.extend(self.Perfect)
        return Scores78

    @property
    def DifferentSpeedsEnabled(self) -> int:
        DifferentSpeedsEnabled = 0
        if (self.EnabledDiff16):
            DifferentSpeedsEnabled = DifferentSpeedsEnabled + 1
        if (self.EnabledDiff33):
            DifferentSpeedsEnabled = DifferentSpeedsEnabled + 1
        if (self.EnabledDiff45):
            DifferentSpeedsEnabled = DifferentSpeedsEnabled + 1
        if (self.EnabledDiff78):
            DifferentSpeedsEnabled = DifferentSpeedsEnabled + 1
        return (DifferentSpeedsEnabled)

    @property
    def Clock_Enabled(self) -> bool:
        return "Clock" in self.Infinite_games
    
    @property
    def Symphony_Enabled(self) -> bool:
        return "Symphony" in self.Infinite_games
    
    @property
    def Race_Enabled(self) -> bool:
        return "Three Legged Race" in self.Infinite_games
    
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
# dont you love stealing code from eav
class BitsBops16Difficulty(Choice):
    """ 
    Defines the maximum rating the 16 speed will ask of you
    to switch speeds:
    - go to the record player
    - play the record of the song you want to play
    - switch the speed of the record to the desired speed
    - load into the minigame
    """
    display_name = "Difficulty"
    option_Disabled = 0
    option_Cool = 1
    option_Amazing = 2
    option_Perfect = 3
    default = 0

class BitsBops33Difficulty(Choice):
    """ 
    Defines the maximum rating the 33 speed will ask of you
    33 speed is normal speed
    """
    display_name = "Difficulty"
    option_Disabled = 0
    option_Cool = 1
    option_Amazing = 2
    option_Perfect = 3
    default = 2

class BitsBops45Difficulty(Choice):
    """ 
    Defines the maximum rating the 45 speed will ask of you
    to switch speeds:
    - go to the record player
    - play the record of the song you want to play
    - switch the speed of the record to the desired speed
    - load into the minigame
    """
    display_name = "Difficulty"
    option_Disabled = 0
    option_Cool = 1
    option_Amazing = 2
    option_Perfect = 3
    default = 0

class BitsBops78Difficulty(Choice):
    """ 
    Defines the maximum rating the 78 speed will ask of you
    to switch speeds:
    - go to the record player
    - play the record of the song you want to play
    - switch the speed of the record to the desired speed
    - load into the minigame
    """
    display_name = "Difficulty"
    option_Disabled = 0
    option_Cool = 1
    option_Amazing = 2
    option_Perfect = 3
    default = 0
    
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