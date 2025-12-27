from __future__ import annotations
import functools
from typing import List, Dict, Set
from dataclasses import dataclass
from Options import Toggle, OptionSet, Choice, NamedRange
from ..game import Game
from ..game_objective_template import GameObjectiveTemplate
from ..enums import KeymastersKeepGamePlatforms

@dataclass
class BitsBopsArchipelagoOptions:
    Bits_Bops_Perfects: BitsBopsPerfects

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
                weight=10,
            ),
        ]

        if self.perfects:
            templates.extend([
                GameObjectiveTemplate(
                    label="Get Perfect in SONG",
                    data={
                        "SONG": (self.songs, 1),
                    },
                    # it very much is, BUT its its own yaml option thus it can only appear if you explicitly turned it on
                    is_time_consuming=False,
                    is_difficult=False,
                    weight=1,
                ),
            ])

        return templates

    @property
    def perfects(self) -> bool:
        return bool(self.archipelago_options.Bits_Bops_Perfects.value)

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
    """
    display_name = "Bits & Bops Perfects enabled"