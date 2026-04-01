from __future__ import annotations
import functools
from typing import List, Dict, Set
from dataclasses import dataclass
from Options import Toggle, OptionList
from ..game import Game
from ..game_objective_template import GameObjectiveTemplate
from ..enums import KeymastersKeepGamePlatforms

@dataclass
class APBigWorldsOptions:
    AP_BigWorlds_Game_List: APBigWorldsGameList
    AP_BigWorlds_Goal_List: APBigWorldsGoalList
    AP_BigWorlds_Gimmick_Toggle: APBigWorldsGimmickToggle
    AP_BigWorlds_Gimmick_List: APBigWorldsGimmicks
    AP_BigWorlds_Safety: APBigWorldsIKnowWhatImDoing


class APBigWorlds(Game):
    name = "AP Big Worlds"
    platform = KeymastersKeepGamePlatforms.META
    is_adult_only_or_unrated = False 
    options_cls = APBigWorldsOptions
    def optional_game_constraint_templates(self) -> List[GameObjectiveTemplate]:
        templates = [
            GameObjectiveTemplate(
                label="Hint Cost: COST, RELEASECOLLECT, Goal: GOAL",
                data={
                    "COST": (self.hint_costs, 1),
                    "RELEASECOLLECT": (self.ReleaseCollect, 1),
                    "GOAL": (self.TrueGoalList, 1),
                },
                weight = 2,
            ),
            GameObjectiveTemplate(
                label="Hint Cost: COST, RELEASECOLLECT, Goal: get BINGOCOUNT bingos on a BINGOSIZE bingo board",
                data={
                    "COST": (self.hint_costs, 1),
                    "RELEASECOLLECT": (self.ReleaseCollect, 1),
                    "BINGOCOUNT": (self.BingosAmount, 1),
                    "BINGOSIZE": (self.BingoSize, 1),
                },
                weight = self.BingoCount * 2,
            ),
            GameObjectiveTemplate(
                label="Hint Cost: COST, RELEASECOLLECT, Goal: get a blackout on a BINGOSIZE bingo board",
                data={
                    "COST": (self.hint_costs, 1),
                    "RELEASECOLLECT": (self.ReleaseCollect, 1),
                    "BINGOSIZE": (self.BingoSize, 1),
                },
                weight = self.BingoBlackoutCount * 2,
            )]
        if self.Gimmick_Enabled:
            templates.extend([
                GameObjectiveTemplate(
                    label="Hint Cost: COST, RELEASECOLLECT, Goal: GOAL, gimmick: GIMMICK",
                    data={
                        "COST": (self.hint_costs, 1),
                        "RELEASECOLLECT": (self.ReleaseCollect, 1),
                        "GOAL": (self.TrueGoalList, 1),
                        "GIMMICK": (self.GimmickList, 1)
                    },
                    weight = 2,
                ),
                GameObjectiveTemplate(
                    label="Hint Cost: COST, RELEASECOLLECT, Goal: get BINGOCOUNT bingos on a BINGOSIZE bingo board",
                    data={
                        "COST": (self.hint_costs, 1),
                        "RELEASECOLLECT": (self.ReleaseCollect, 1),
                        "BINGOCOUNT": (self.BingosAmount, 1),
                        "BINGOSIZE": (self.BingoSize, 1),
                    },
                    weight = self.BingoCount * 1,
                ),
                GameObjectiveTemplate(
                    label="Hint Cost: COST, RELEASECOLLECT, Goal: get a blackout on a BINGOSIZE bingo board",
                    data={
                        "COST": (self.hint_costs, 1),
                        "RELEASECOLLECT": (self.ReleaseCollect, 1),
                        "BINGOSIZE": (self.BingoSize, 1),
                    },
                    weight = self.BingoBlackoutCount * 1,
                )
            ]),
        return templates

    def game_objective_templates(self) -> List[GameObjectiveTemplate]:
        templates: List[GameObjectiveTemplate] = [
            GameObjectiveTemplate(
                label="Add GAME to this keeps' world",
                data={
                    "GAME": (self.GameList, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight = 10,
            ),
        ]
        
        return templates

    @property
    def GameList(self) -> list[str]:
        return sorted (self.archipelago_options.AP_BigWorlds_Game_List.value)
    @functools.cached_property
    def GoalList(self) -> list[str]:
        return sorted (self.archipelago_options.AP_BigWorlds_Goal_List.value)
    @property
    def TrueGoalList(self) -> list[str]:
        StartingList = self.GoalList
        TrueGoalList = []
        for Goal in StartingList:
            if Goal != "Bingo" and Goal != "BingoBlackout":
                TrueGoalList.append(Goal)
        return TrueGoalList
    @property
    def BingoCount(self) -> int:
        BingoCount = 0
        for Goal in self.GoalList:
            if Goal == "Bingo":
                BingoCount += 1
        return BingoCount
    @property
    def BingoBlackoutCount(self) -> int:
        BingoBlackoutCount = 0
        for Goal in self.GoalList:
            if Goal == "BingoBlackout":
                BingoBlackoutCount += 1
        return BingoBlackoutCount
    @property
    def OtherGoalCount(self) -> int:
        OtherGoalCount = self.TrueGoalList.count

    @property
    def GimmickList(self) -> list[str]:
        return sorted (self.archipelago_options.AP_BigWorlds_Gimmick_List.value)

    @property
    def Gimmick_Enabled(self) -> bool:
        return self.archipelago_options.AP_BigWorlds_Gimmick_Toggle.value

    @staticmethod
    def hint_costs() -> List[int]:
        return list(range(0, 26)) + [100]
    
    @staticmethod
    def ReleaseCollect() -> List[str]:
        return [
            "Release: Off, Collect: Off",
            "Release: Off, Collect: Off",
            "Release: On, Collect: Off",
            "Release: On, Collect: Off",
            "Release: On, Collect: Off",
            "Release: On, Collect: Off",
            "Release: On, Collect: Off",
            "Release: On, Collect: Off",
            "Release: On, Collect: Off",
            "Release: On, Collect: On",
        ]
    
    @staticmethod
    def BingoSize() -> List[str]:
        return [
            "4x4",
            "5x5",
            "6x6",
            "7x7",
            "8x8",
            "9x9",
            "10x10",
        ]
    @staticmethod
    def BingosAmount() -> List[int]:
        return list(range(0, 11))

# Archipelago Options
# dont you love stealing code from eav
class APBigWorldsIKnowWhatImDoing(Toggle):
    """
    this setting does nothing, just here so you hopefully read this if you didnt read it already
    do not under any circumstances put this game in medley mode, it will break
    when playing this kmk, read the optional conditions, those are the world settings, you need those
    """

class APBigWorldsGameList(OptionList):
    """
    Which games will be in the pool
    """

    display_name = "APBigWorld Games"
    default = [
        "Adventure",
        "APQuest",
        "Aquaria",
        "Blasphemous",
        "Bomb Rush Cyberfunk",
        "Bumper Stickers",
        "Castlevania - Circle of the Moon",
        "Castlevania 64",
        "Celeste (Open World)",
        "ChecksFinder",
        "Choo-Choo Charles",
        "Civilization VI",
        "Dark Souls III",
        "DLCQuest",
        "Donkey Kong Country 3",
        "DOOM 1993",
        "Doom II",
        "Factorio",
        "Faxanadu",
        "Final Fantasy",
        "Final Fantasy Mystic Quest",
        "A Hat in Time",
        "Heretic",
        "Hollow Knight",
        "Hylics 2",
        "Inscryption",
        "Jak and Daxter: The Precursor Legacy",
        "Kingdom Hearts",
        "Kingdom Hearts 2",
        "Kirby's Dream Land 3",
        "Landstalker - The Treasures of King Nole",
        "The Legend of Zelda",
        "Lingo",
        "A Link to the Past",
        "Links Awakening DX",
        "Lufia II Ancient Cave",
        "Mario & Luigi Superstar Saga",
        "Mega Man 2",
        "MegaMan Battle Network 3",
        "Meritous",
        "The Messenger",
        "Muse Dash",
        "Noita",
        "Ocarina of Time",
        "Old School Runescape",
        "Overcooked! 2",
        "Paint",
        "Pokemon Emerald",
        "Pokemon Red and Blue",
        "Raft",
        "Risk of Rain 2",
        "Saving Princess",
        "Secret of Evermore",
        "shapez",
        "Shivers",
        "A Short Hike",
        "SMZ3",
        "Sonic Adventure 2 Battle",
        "Starcraft 2",
        "Stardew Valley",
        "Subnautica",
        "Sudoku",
        "Super Mario 64",
        "Super Mario Land 2",
        "Super Mario World",
        "Super Metroid",
        "Terraria",
        "Timespinner",
        "TUNIC",
        "Undertale",
        "VVVVVV",
        "Wargroove",
        "The Wind Waker",
        "The Witness",
        "Yacht Dice",
        "Yoshi's Island",
        "Yu-Gi-Oh! 2006",
        "Zillion",
    ]

class APBigWorldsGoalList(OptionList):
    """
    The goals a world might ask for you to do
    Special Keys:
    - Bingo: Will add all bingo sized up to 10x10 automatically and ask for bingo amounts
    - BingoBlackout: Same as above, but will ask for blackout instead
    """

    display_name = "APBigWorld Goals"
    default = [
        "Finish the multiworld",
        "Bingo",
        "BingoBlackout",
    ]

class APBigWorldsGimmickToggle(Toggle):
    """
    A master toggle for gimmicks appearing in worlds.
    """
    display_name = "APBigWorld Gimmicks Master Toggle"
class APBigWorldsGimmicks(OptionList):
    """
    Possible Gimmicks that might appear in a world
    """

    display_name = "APBigWorld Gimmicks"
    default = [
        "0% hints, Release Off, only hint what's needed to goal the games, and where possible only collect hinted checks",
        'Add priority_locations: "Everywhere" to one random yaml per 5 trials, round down',
        "Include 2 copies of a random yaml after they have been made",
        "Slotlock every second game",
    ]