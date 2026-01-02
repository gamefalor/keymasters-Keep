from __future__ import annotations
import functools
from typing import List, Dict, Set
from dataclasses import dataclass
from Options import Toggle, OptionSet, Choice, NamedRange, OptionList
from ..game import Game
from ..game_objective_template import GameObjectiveTemplate
from ..enums import KeymastersKeepGamePlatforms

@dataclass
class ArcaeaArchipelagoOptions:
    Arcaea_DLC_Owned: ArcaeaPacksOwned
    Arcaea_Individual_Song_Selection: ArcaeaIndividualDLCSongs
    Arcaea_Required_Grades: ArcaeaRequiredGrades
    Arcaea_Selected_Parners: ArcaeaPartners
    

class ArcaeaGame(Game):
    name = "Arcaea"
    platform = KeymastersKeepGamePlatforms.AND
    platforms_other = [
        KeymastersKeepGamePlatforms.IOS,
    ]
    is_adult_only_or_unrated = False 
    options_cls = ArcaeaArchipelagoOptions
    def optional_game_constraint_templates(self) -> List[GameObjectiveTemplate]:
        return list()

    def game_objective_templates(self) -> List[GameObjectiveTemplate]:
        templates: List[GameObjectiveTemplate] = [
            GameObjectiveTemplate(
                label="Clear SONGS in a row",
                data={
                    "SONGS": (self.songs, 4),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=1,
            ),

            GameObjectiveTemplate(
                label="Achieve GRADE on SONG",
                data={
                    "SONG": (self.songs, 1),
                    "GRADE": (self.grades, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=10,
            ),

            GameObjectiveTemplate(
                label="Clear SONG with PARTNER",
                data={
                    "SONG": (self.songs_without_last_variants, 1),
                    "PARTNER": (self.partners, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=2,
            ),
        ]

        return templates

    @property
    def dlc_owned(self) -> List[str]:
        return sorted(self.archipelago_options.Arcaea_DLC_Owned.value)

    def grades(self) -> List[str]:
        grades: List[str] = list(self.archipelago_options.Arcaea_Required_Grades.value)
        return sorted(grades)

    def partners(self) -> List[str]:
        partners: List[str] = list(self.archipelago_options.Arcaea_Selected_Parners.value)
        return sorted(partners)

    @property
    def has_dlc_Arcaea(self) -> bool:
        return "Arcaea" in self.dlc_owned

    @property
    def has_dlc_Liminal_Eclipse(self) -> bool:
        return "Liminal Eclipse" in self.dlc_owned

    @property
    def has_dlc_Lucent_Historia(self) -> bool:
        return "Lucent Historia" in self.dlc_owned

    @property
    def has_dlc_Absolute_Nihil(self) -> bool:
        return "Absolute Nihil" in self.dlc_owned

    @property
    def has_dlc_Lasting_Eden(self) -> bool:
        return "Lasting Eden" in self.dlc_owned

    @property
    def has_dlc_Lasting_Eden_Chapter_2(self) -> bool:
        return "Lasting Eden Chapter 2" in self.dlc_owned

    @property
    def has_dlc_Shifting_Veil(self) -> bool:
        return "Shifting Veil" in self.dlc_owned

    @property
    def has_dlc_Silent_Awnser(self) -> bool:
        return "Silent Awnser" in self.dlc_owned

    @property
    def has_dlc_Final_Verdict(self) -> bool:
        return "Final Verdict" in self.dlc_owned

    @property
    def has_dlc_Black_Fate(self) -> bool:
        return "Black Fate" in self.dlc_owned

    @property
    def has_dlc_Adverse_Prelude(self) -> bool:
        return "Adverse Prelude" in self.dlc_owned

    @property
    def has_dlc_Luminous_Sky(self) -> bool:
        return "Luminous Sky" in self.dlc_owned

    @property
    def has_dlc_Vicious_Labyrinth(self) -> bool:
        return "Vicious Labyrinth" in self.dlc_owned

    @property
    def has_dlc_Eternal_Core(self) -> bool:
        return "Eternal Core" in self.dlc_owned

    @property
    def has_dlc_Extant_Anima(self) -> bool:
        return "Extant Anima" in self.dlc_owned

    @property
    def has_dlc_Chapter_Experientia(self) -> bool:
        return "Chapter Experientia" in self.dlc_owned

    @property
    def has_dlc_Esoteric_Order(self) -> bool:
        return "Esoteric Order" in self.dlc_owned

    @property
    def has_dlc_Pale_Tapestry(self) -> bool:
        return "Pale Tapestry" in self.dlc_owned

    @property
    def has_dlc_Light_Of_Salvation(self) -> bool:
        return "Light Of Salvation" in self.dlc_owned

    @property
    def has_dlc_Divided_Heart(self) -> bool:
        return "Divided Heart" in self.dlc_owned

    @property
    def has_dlc_Ephemeral_Page(self) -> bool:
        return "Ephemeral Page" in self.dlc_owned

    @property
    def has_dlc_The_Journey_Onwards(self) -> bool:
        return "The Journey Onwards" in self.dlc_owned

    @property
    def has_dlc_Sunset_Radiance(self) -> bool:
        return "Sunset Radiance" in self.dlc_owned

    @property
    def has_dlc_Absolute_Reason(self) -> bool:
        return "Absolute Reason" in self.dlc_owned

    @property
    def has_dlc_Binary_Enfold(self) -> bool:
        return "Binary Enfold" in self.dlc_owned

    @property
    def has_dlc_Shared_Time(self) -> bool:
        return "Shared Time" in self.dlc_owned

    @property
    def has_dlc_Ambivalent_Vision(self) -> bool:
        return "Ambivalent Vision" in self.dlc_owned

    @property
    def has_dlc_Crimson_Solace(self) -> bool:
        return "Crimson Solace" in self.dlc_owned

    @property
    def has_dlc_Arcaea_Next_Stage(self) -> bool:
        return "Arcaea Next Stage" in self.dlc_owned

    @property
    def has_dlc_DJMAX(self) -> bool:
        return "DJMAX" in self.dlc_owned

    @property
    def has_dlc_DJMAX_Collab_2(self) -> bool:
        return "DJMAX Collab 2" in self.dlc_owned

    @property
    def has_dlc_UNDERTALE(self) -> bool:
        return "UNDERTALE" in self.dlc_owned

    @property
    def has_dlc_Rotaeno(self) -> bool:
        return "Rotaeno" in self.dlc_owned

    @property
    def has_dlc_Cytus_II(self) -> bool:
        return "Cytus II" in self.dlc_owned

    @property
    def has_dlc_Cytus_II_Collab_2(self) -> bool:
        return "Cytus II Collab 2" in self.dlc_owned

    @property
    def has_dlc_Muse_Dash(self) -> bool:
        return "Muse Dash" in self.dlc_owned

    @property
    def has_dlc_WACCA(self) -> bool:
        return "WACCA" in self.dlc_owned

    @property
    def has_dlc_WACCA_Collab_2(self) -> bool:
        return "WACCA Collab 2" in self.dlc_owned

    @property
    def has_dlc_maimai(self) -> bool:
        return "maimai" in self.dlc_owned

    @property
    def has_dlc_maimai_Collab_2(self) -> bool:
        return "maimai Collab 2" in self.dlc_owned

    @property
    def has_dlc_maimai_Collab_3(self) -> bool:
        return "maimai Collab 3" in self.dlc_owned

    @property
    def has_dlc_ONGEKI(self) -> bool:
        return "O.N.G.E.K.I." in self.dlc_owned

    @property
    def has_dlc_ONGEKI_Collab_2(self) -> bool:
        return "O.N.G.E.K.I. Collab 2" in self.dlc_owned

    @property
    def has_dlc_ONGEKI_Collab_3(self) -> bool:
        return "O.N.G.E.K.I. Collab 3" in self.dlc_owned

    @property
    def has_dlc_CHUNITHM(self) -> bool:
        return "CHUNITHM" in self.dlc_owned

    @property
    def has_dlc_CHUNITHM_Collab_2(self) -> bool:
        return "CHUNITHM Collab 2" in self.dlc_owned

    @property
    def has_dlc_CHUNITHM_Collab_3(self) -> bool:
        return "CHUNITHM Collab 3" in self.dlc_owned

    @property
    def has_dlc_CHUNITHM_Collab_4(self) -> bool:
        return "CHUNITHM Collab 4" in self.dlc_owned

    @property
    def has_dlc_Groove_Coaster(self) -> bool:
        return "Groove Coaster" in self.dlc_owned

    @property
    def has_dlc_Groove_Coaster_Collab_2(self) -> bool:
        return "Groove Coaster Collab 2" in self.dlc_owned

    @property
    def has_dlc_Tone_Sphere(self) -> bool:
        return "Tone Sphere" in self.dlc_owned

    @property
    def has_dlc_Lanota(self) -> bool:
        return "Lanota" in self.dlc_owned

    @property
    def has_dlc_Lanota_Collab_2(self) -> bool:
        return "Lanota Collab 2" in self.dlc_owned

    @property
    def has_dlc_Dynamix(self) -> bool:
        return "Dynamix" in self.dlc_owned


    @functools.cached_property
    def songs_pack_Arcaea(self) -> List[str]:
        return [
            "Dematerialized",
            "Fairytale",
            "Hidden Rainbows of Epicurus",
            "Sayonara Hatsukoi",
            "Vexaria",
            "Brand new world",
            "Clotho and the stargazer",
            "Dement ~after legend~",
            "Infinity Heaven",
            "inkar-usi",
            "Jingle",
            "Rise",
            "Suomi",
            "Altair (feat. *spiLa*",
            "Babaroque",
            "Bookmader (2D Version)",
            "Dandelion",
            "DDD",
            "Diode",
            "FreeF4ll",
            "Harutopia ~Utopia of Spring~",
            "Lucifer",
            "Oblivia",
            "One Last Drive",
            "Purgatorium",
            "Rabbit In The Black Room",
            "Reinvent",
            "san skia",
            "SATISFACTION",
            "Shades of Light in a Transcendent Realm",
            "Snow White",
            "world.execute(me);",
            "Avril -Flicka i krans-",
            "Chronostasis",
            "Dialnote",
            "Grimheart",
            "Senkyou",
            "Anökumene",
            "Blaster",
            "Cybernecia Catharsis",
            "Dancin' on a Cat's Paw",
            "Dreamin' Attraction!!",
            "GOODTEK (Arcaea Edit)",
            "Ignotus",
            "Illegal Paradise",
            "Kanagawa Cyber Culvert",
            "Lost Civilization",
            "LunarOrbit -believe in the Espebranch road-",
            "NULCTRL",
            "qualia -ideaesthesia-",
            "Red and Blue",
            "Redraw the Colorless World",
            "Remind the Souls (Short Version)",
            "ReviXy",
            "Rugie",
            "Sakura Fubuki",
            "Syro",
            "The Formula",
            "VectoR",
            "Monochrome Princess",
            "Nhelv",
            "SUPERNOVA",
            "Trap Crow",
            "Red and Blue and Green"
            "Ignotus Afterburn"
        ]

    @functools.cached_property
    def songs_pack_Liminal_Eclipse(self) -> List[str]:
        return [
            "Vainspire",
            "No Way Back",
            "Viola Illyria",
            "ANDORXOR",
            "Undying Macula",
        ]

    @functools.cached_property
    def songs_pack_Lucent_Historia(self) -> List[str]:
        return [
            "Renegade",
            "Rays of Remnant",
            "Swan Song",
            "Astral Quantization",
            "Breach of Faith",
            "Lament Rain",
            "Designant.",
        ]

    @functools.cached_property
    def songs_pack_Absolute_Nihil(self) -> List[str]:
        return [
            "Hypnotize",
            "In Vain",
            "Ashen 6oundary",
            "ALTER EGO",
            "Judgement",
        ]

    @functools.cached_property
    def songs_pack_Lasting_Eden(self) -> List[str]:
        return [
            "WAIT FOR DAWN",
            "Raven's Pride",
            "Rise of the World",
            "UNKNOWN LEVELS",
            "abstruse Dilemma",
        ]

    @functools.cached_property
    def songs_pack_Lasting_Eden_Chapter_2(self) -> List[str]:
        return [
            "Primeval Texture",
            "Technicolour",
            "Ego Eimi",
            "Logos",
            "Arghena",
        ]

    @functools.cached_property
    def songs_pack_Shifting_Veil(self) -> List[str]:
        return [
            "Transient Space",
            "Nameless Passion",
            "TeraVolt",
        ]

    @functools.cached_property
    def songs_pack_Silent_Awnser(self) -> List[str]:
        return [
            "Last",
            "Last | Moment",
            "Calima Karma",
            "Loveless Dress",
            "Last | Eternity",
        ]

    @functools.cached_property
    def songs_pack_Final_Verdict(self) -> List[str]:
        return [
            "Defection",
            "Infinite Strife,",
            "Arcana Eden",
            "Pentiment",
            "World Ender",
            "Testify",
        ]

    @functools.cached_property
    def songs_pack_Black_Fate(self) -> List[str]:
        return [
            "Equilibrium",
            "Antagonism",
            "Arcahv",
            "Lost Desire",
            "Dantalion",
            "Tempestissimo",
            "#1f1e33",
        ]

    @functools.cached_property
    def songs_pack_Adverse_Prelude(self) -> List[str]:
        return [
            "Saint or Sinner",
            "Vindication",
            "BLRINK",
            "Heavendoor",
            "Ringed Genesis",
        ]

    @functools.cached_property
    def songs_pack_Luminous_Sky(self) -> List[str]:
        return [
            "Maze No.9",
            "Sulfur",
            "The Message",
            "Ether Strike",
            "Halcyon",
            "Fracture Ray",
        ]

    @functools.cached_property
    def songs_pack_Vicious_Labyrinth(self) -> List[str]:
        return [
            "Iconoclast",
            "SOUNDWiTCH",
            "trappola bewitching",
            "Axium Crisis",
            "conflict",
            "Grievous Lady",
        ]

    @functools.cached_property
    def songs_pack_Eternal_Core(self) -> List[str]:
        return [
            "I've heard it said",
            "Lumia",
            "Relentless",
            "cry of viyella",
            "memoryfactory.lzh",
            "Solitairy Dream",
            "Essence of Twilight",
            "PRAGMATISM",
            "Sheriruth",
        ]

    @functools.cached_property
    def songs_pack_Extant_Anima(self) -> List[str]:
        return [
            "See the Lights!",
            "Dual Dependency",
            "Lilly",
            "Scarlet Lunar Empress",
            "Extradimensional Cosmic Phenomenon",
        ]

    @functools.cached_property
    def songs_pack_Chapter_Experientia(self) -> List[str]:
        return [
            "Factorder",
            "incomplete the one",
            "CHAOSBLAST",
            "Welcome, Queen of Fiction",
            "AlterGate",
        ]

    @functools.cached_property
    def songs_pack_Esoteric_Order(self) -> List[str]:
        return [
            "Paper Witch",
            "Crystal Gravity",
            "Far Away Light",
            "Löschen",
            "Seclusion",
            "AegleSeeker",
        ]

    @functools.cached_property
    def songs_pack_Pale_Tapestry(self) -> List[str]:
        return [
            "Coastal Highway",
            "ODYSSEIA",
            "Overwhelm",
        ]

    @functools.cached_property
    def songs_pack_Light_Of_Salvation(self) -> List[str]:
        return [
            "Small Cloud Sugar Candy",
            "AlterAle",
            "Divine Light of Myriad",
        ]

    @functools.cached_property
    def songs_pack_Divided_Heart(self) -> List[str]:
        return [
            "First Snow",
            "Blocked Library",
            "Blue Rose",
            "néo kósmo",
            "Lightning Screw",
        ]

    @functools.cached_property
    def songs_pack_Ephemeral_Page(self) -> List[str]:
        return [
            "Eccentric Tale",
            "Alice à la mode",
            "Alice's Suitcase",
            "Jump",
            "Felis",
        ]

    @functools.cached_property
    def songs_pack_The_Journey_Onwards(self) -> List[str]:
        return [
            "Beside You",
            "Heart jackin'",
            "To: Alice Liddell",
        ]

    @functools.cached_property
    def songs_pack_Sunset_Radiance(self) -> List[str]:
        return [
            "Tie me down gently",
            "Chelsea",
            "A Wandering Melody of Love",
            "AI[UE]OON",
            "Hotarubi no Yuki",
            "Valhalla:0",
        ]

    @functools.cached_property
    def songs_pack_Absolute_Reason(self) -> List[str]:
        return [
            "Antithese",
            "Black Territory",
            "Corruption",
            "Vicious Heroism",
            "Cyaegha",
        ]

    @functools.cached_property
    def songs_pack_Binary_Enfold(self) -> List[str]:
        return [
            "Silent Rush",
            "next to you",
            "Strongholds",
            "Memory Forest",
            "Singularity",
            "SINGULARITY VVVIP",
        ]

    @functools.cached_property
    def songs_pack_Shared_Time(self) -> List[str]:
        return [
            "Cosmica",
            "Ascent",
            "Live Fast Die Young",
        ]

    @functools.cached_property
    def songs_pack_Ambivalent_Vision(self) -> List[str]:
        return [
            "Blossoms",
            "Romance Wars",
            "Genesis",
            "Moonheart",
            "Lethaeus",
            "corps-sans-organes",
        ]

    @functools.cached_property
    def songs_pack_Crimson_Solace(self) -> List[str]:
        return [
            "Paradise",
            "Flashback",
            "Flyburg and Endroll",
            "Party Vinyl",
            "Nirv lucE",
            "GLORY : ROAD",
        ]

    @functools.cached_property
    def songs_pack_Arcaea_Next_Stage(self) -> List[str]:
        return [
            "INFINITE DIMENSION",
            "INCARNATOR",
            "MARENYX",
            "Zephyrlasting",
            "AZALEA",
            "CODE : Oblivion",
        ]

    @functools.cached_property
    def songs_pack_DJMAX(self) -> List[str]:
        return [
            "Ladymade Star",
            "U.A.D",
            "End of The Moonlight",
            "OBLIVION",
            "Nightmare",
        ]

    @functools.cached_property
    def songs_pack_DJMAX_Collab_2(self) -> List[str]:
        return [
            "I want You",
            "BlythE",
            "Syriana",
            "Liar",
            "We're All Gonna Die",
        ]

    @functools.cached_property
    def songs_pack_UNDERTALE(self) -> List[str]:
        return [
            "Heartache",
            "Death By Glamour",
            "Last Goodbye",
            "Your Best Nightmare",
            "MEGALOVANIA",
        ]

    @functools.cached_property
    def songs_pack_Rotaeno(self) -> List[str]:
        return [
            "Dual Doom Deathmatch",
            "Waltz for Lorelei",
            "Inverted World",
            "MVURBD",
            "Vulcanus",
                    ]

    @functools.cached_property
    def songs_pack_Cytus_II(self) -> List[str]:
        return [
            "Bullet Waiting For Me (James Landino remix)",
            "used to be",
            "Devillic Sphere",
            "Lucid Traveler",
            "CHAOS",
        ]

    @functools.cached_property
    def songs_pack_Cytus_II_Collab_2(self) -> List[str]:
        return [
            "syuten",
            "DRG",
            "99 Glooms",
            "Cytus II 2 10+ with the messed up name",
            "Magnolia",
        ]

    @functools.cached_property
    def songs_pack_Muse_Dash(self) -> List[str]:
        return [
            "Lights of Muse",
            "Final Step!",
            "Haze of Autumn",
            "Medusa",
        ]

    @functools.cached_property
    def songs_pack_WACCA(self) -> List[str]:
        return [
            "Quon (WACCA)",
            "Let you DIVE! (nitro rmx)",
            "With U",
            "Mazy Metroplex",
            "GENOCIDER",
        ]

    @functools.cached_property
    def songs_pack_WACCA_Collab_2(self) -> List[str]:
        return [
            "Stratoliner",
            "Ouvertüre",
            "eden",
            "XTREME",
            "Meta-Mysteria",
        ]

    @functools.cached_property
    def songs_pack_maimai(self) -> List[str]:
        return [
            "April Showers",
            "7thSense",
            "Oshama Scramble",
            "AMAZING MIGHTYYYY!!!!",
        ]

    @functools.cached_property
    def songs_pack_maimai_Collab_2(self) -> List[str]:
        return [
            "CYCLES",
            "MAXRAGE",
            "[X]",
            "TEmPTaTiON",
        ]

    @functools.cached_property
    def songs_pack_maimai_Collab_3(self) -> List[str]:
        return [
            "BREak! BREaK! BREak!",
            "Straight into the lights",
            "ViRTUS",
            "yomibito_shirazu",
        ]

    @functools.cached_property
    def songs_pack_ONGEKI(self) -> List[str]:
        return [
            "Lazy Addiction",
            "Dazzle hop",
            "Viyella's Tears",
            "w4",
        ]

    @functools.cached_property
    def songs_pack_ONGEKI_Collab_2(self) -> List[str]:
        return [
            "Heart",
            "Ai Drew",
            "FLUFFY FLASH",
            "Good bye, Merry-Go-Round",
        ]

    @functools.cached_property
    def songs_pack_ONGEKI_Collab_3(self) -> List[str]:
        return [
            "LiftOff",
            "Don't Fight The Music",
            "SUPER AMBULANCE",
            "And Revive The Melody",
        ]

    @functools.cached_property
    def songs_pack_CHUNITHM(self) -> List[str]:
        return [
            "Garakuta Doll Play",
            "Ikazuchi",
            "World Vanquisher",
        ]

    @functools.cached_property
    def songs_pack_CHUNITHM_Collab_2(self) -> List[str]:
        return [
            "Climax",
            "Last Celebration",
            "Misdeed -la bonté de Dieu et l'origine du mal-",
        ]

    @functools.cached_property
    def songs_pack_CHUNITHM_Collab_3(self) -> List[str]:
        return [
            "Cosmo Pop Fanclub",
            "IMPACT",
            "Genesis",
            "Trricksters!!",
            "Spider's Thread",
        ]

    @functools.cached_property
    def songs_pack_CHUNITHM_Collab_4(self) -> List[str]:
        return [
            "BlazinG AIR",
            "8-EM",
            "Ignition",
            "Aether Crest: Astral",
            "DA'AT -The First Seeker of Souls-",
        ]

    @functools.cached_property
    def songs_pack_Groove_Coaster(self) -> List[str]:
        return [
            "MERLIN",
            "OMAKENO Stroke",
            "DX Choseinou FUll Metal Shojo",
            "Got Hive of Ra",
            "Scarlet Lance",
            "ouroboros -twin stroke of the end-",
        ]

    @functools.cached_property
    def songs_pack_Groove_Coaster_Collab_2(self) -> List[str]:
        return [
            'Sign of "10.5km"',
            "10pt8ion",
            "Black MinD",
        ]

    @functools.cached_property
    def songs_pack_Tone_Sphere(self) -> List[str]:
        return [
            "Hall of Mirrors",
            "Hikari",
            "STAGER (ALL STAGER CLEAR)",
            "Linear Accelerator",
            "Tiferet",
        ]

    @functools.cached_property
    def songs_pack_Lanota(self) -> List[str]:
        return [
            "Dream goes on",
            "Journey",
            "Quon (lanota)",
            "Specta",
            "cyanine",
        ]

    @functools.cached_property
    def songs_pack_Lanota_Collab_2(self) -> List[str]:
        return [
            "Prism",
            "Protoflicker",
            "Stasis",
        ]

    @functools.cached_property
    def songs_pack_Dynamix(self) -> List[str]:
        return [
            "Moonlight of Sand Castle",
            "REconstruction",
            "Evoltex (poppi'n mix)",
            "Oracle",
            "aterlbus"
        ]

    def songs(self) -> List[str]:
        songs = []
        individual_selection = self.archipelago_options.Arcaea_Individual_Song_Selection.value

        if individual_selection:
            songs = list(individual_selection)
        
        if self.has_dlc_Arcaea:
            songs.extend(self.songs_pack_Arcaea)
        if self.has_dlc_Liminal_Eclipse:
            songs.extend(self.songs_pack_Liminal_Eclipse)
        if self.has_dlc_Lucent_Historia:
            songs.extend(self.songs_pack_Lucent_Historia)
        if self.has_dlc_Absolute_Nihil:
            songs.extend(self.songs_pack_Absolute_Nihil)
        if self.has_dlc_Lasting_Eden:
            songs.extend(self.songs_pack_Lasting_Eden)
        if self.has_dlc_Lasting_Eden_Chapter_2:
            songs.extend(self.songs_pack_Lasting_Eden_Chapter_2)
        if self.has_dlc_Shifting_Veil:
            songs.extend(self.songs_pack_Shifting_Veil)
        if self.has_dlc_Silent_Awnser:
            songs.extend(self.songs_pack_Silent_Awnser)
        if self.has_dlc_Final_Verdict:
            songs.extend(self.songs_pack_Final_Verdict)
        if self.has_dlc_Black_Fate:
            songs.extend(self.songs_pack_Black_Fate)
        if self.has_dlc_Adverse_Prelude:
            songs.extend(self.songs_pack_Adverse_Prelude)
        if self.has_dlc_Luminous_Sky:
            songs.extend(self.songs_pack_Luminous_Sky)
        if self.has_dlc_Vicious_Labyrinth:
            songs.extend(self.songs_pack_Vicious_Labyrinth)
        if self.has_dlc_Eternal_Core:
            songs.extend(self.songs_pack_Eternal_Core)
        if self.has_dlc_Extant_Anima:
            songs.extend(self.songs_pack_Extant_Anima)
        if self.has_dlc_Chapter_Experientia:
            songs.extend(self.songs_pack_Chapter_Experientia)
        if self.has_dlc_Esoteric_Order:
            songs.extend(self.songs_pack_Esoteric_Order)
        if self.has_dlc_Pale_Tapestry:
            songs.extend(self.songs_pack_Pale_Tapestry)
        if self.has_dlc_Light_Of_Salvation:
            songs.extend(self.songs_pack_Light_Of_Salvation)
        if self.has_dlc_Divided_Heart:
            songs.extend(self.songs_pack_Divided_Heart)
        if self.has_dlc_Ephemeral_Page:
            songs.extend(self.songs_pack_Ephemeral_Page)
        if self.has_dlc_The_Journey_Onwards:
            songs.extend(self.songs_pack_The_Journey_Onwards)
        if self.has_dlc_Sunset_Radiance:
            songs.extend(self.songs_pack_Sunset_Radiance)
        if self.has_dlc_Absolute_Reason:
            songs.extend(self.songs_pack_Absolute_Reason)
        if self.has_dlc_Binary_Enfold:
            songs.extend(self.songs_pack_Binary_Enfold)
        if self.has_dlc_Shared_Time:
            songs.extend(self.songs_pack_Shared_Time)
        if self.has_dlc_Ambivalent_Vision:
            songs.extend(self.songs_pack_Ambivalent_Vision)
        if self.has_dlc_Crimson_Solace:
            songs.extend(self.songs_pack_Crimson_Solace)
        if self.has_dlc_Arcaea_Next_Stage:
            songs.extend(self.songs_pack_Arcaea_Next_Stage)
        if self.has_dlc_DJMAX:
            songs.extend(self.songs_pack_DJMAX)
        if self.has_dlc_DJMAX_Collab_2:
            songs.extend(self.songs_pack_DJMAX_Collab_2)
        if self.has_dlc_UNDERTALE:
            songs.extend(self.songs_pack_UNDERTALE)
        if self.has_dlc_Rotaeno:
            songs.extend(self.songs_pack_Rotaeno)
        if self.has_dlc_Cytus_II:
            songs.extend(self.songs_pack_Cytus_II)
        if self.has_dlc_Cytus_II_Collab_2:
            songs.extend(self.songs_pack_Cytus_II_Collab_2)
        if self.has_dlc_Muse_Dash:
            songs.extend(self.songs_pack_Muse_Dash)
        if self.has_dlc_WACCA:
            songs.extend(self.songs_pack_WACCA)
        if self.has_dlc_WACCA_Collab_2:
            songs.extend(self.songs_pack_WACCA_Collab_2)
        if self.has_dlc_maimai:
            songs.extend(self.songs_pack_maimai)
        if self.has_dlc_maimai_Collab_2:
            songs.extend(self.songs_pack_maimai_Collab_2)
        if self.has_dlc_maimai_Collab_3:
            songs.extend(self.songs_pack_maimai_Collab_3)
        if self.has_dlc_ONGEKI:
            songs.extend(self.songs_pack_ONGEKI)
        if self.has_dlc_ONGEKI_Collab_2:
            songs.extend(self.songs_pack_ONGEKI_Collab_2)
        if self.has_dlc_ONGEKI_Collab_3:
            songs.extend(self.songs_pack_ONGEKI_Collab_3)
        if self.has_dlc_CHUNITHM:
            songs.extend(self.songs_pack_CHUNITHM)
        if self.has_dlc_CHUNITHM_Collab_2:
            songs.extend(self.songs_pack_CHUNITHM_Collab_2)
        if self.has_dlc_CHUNITHM_Collab_3:
            songs.extend(self.songs_pack_CHUNITHM_Collab_3)
        if self.has_dlc_CHUNITHM_Collab_4:
            songs.extend(self.songs_pack_CHUNITHM_Collab_4)
        if self.has_dlc_Groove_Coaster:
            songs.extend(self.songs_pack_Groove_Coaster)
        if self.has_dlc_Groove_Coaster_Collab_2:
            songs.extend(self.songs_pack_Groove_Coaster_Collab_2)
        if self.has_dlc_Tone_Sphere:
            songs.extend(self.songs_pack_Tone_Sphere)
        if self.has_dlc_Lanota:
            songs.extend(self.songs_pack_Lanota)
        if self.has_dlc_Lanota_Collab_2:
            songs.extend(self.songs_pack_Lanota_Collab_2)
        if self.has_dlc_Dynamix:
            songs.extend(self.songs_pack_Dynamix)

        return sorted(songs)
    
    def songs_without_last_variants(self) -> List[str]:
        songs_without_last_variants: List[str] = self.songs()[:]

        if "Last | Moment" in songs_without_last_variants:
            songs_without_last_variants.remove("Last | Moment")
        if "Last | Eternity" in songs_without_last_variants:
            songs_without_last_variants.remove("Last | Eternity")

        return songs_without_last_variants

# Archipelago Options
class ArcaeaPacksOwned(OptionSet):
    """
    Indicates which Arcaea packs you player own.
    World Extend, Extend Archive & Memory archive are not valid options due to buying the songs individually.
    BYDS with a different name that require multiple packs to unlock are not automatically added and you should look to the second option to add them
    Look in Arcaea.txt to get valid options
    """

    display_name = "Arcaea Packs Owned"
    valid_keys = [
        "Arcaea",
        "Liminal Eclipse",
        "Lucent Historia",
        "Absolute Nihil",
        "Lasting Eden",
        "Lasting Eden Chapter 2",
        "Shifting Veil",
        "Silent Awnser",
        "Final Verdict",
        "Black Fate",
        "Adverse Prelude",
        "Luminous Sky",
        "Vicious Labyrinth",
        "Eternal Core",
        "Extant Anima",
        "Chapter Experientia",
        "Esoteric Order",
        "Pale Tapestry",
        "Light Of Salvation",
        "Divided Heart",
        "Ephemeral Page",
        "The Journey Onwards",
        "Sunset Radiance",
        "Absolute Reason",
        "Binary Enfold",
        "Shared Time",
        "Ambivalent Vision",
        "Crimson Solace",
        "Arcaea Next Stage",
        "DJMAX",
        "DJMAX Collab 2",
        "UNDERTALE",
        "Rotaeno",
        "Cytus II",
        "Cytus II Collab 2",
        "Muse Dash",
        "WACCA",
        "WACCA Collab 2",
        "maimai",
        "maimai Collab 2",
        "maimai Collab 3",
        "O.N.G.E.K.I.",
        "O.N.G.E.K.I. Collab 2",
        "O.N.G.E.K.I. Collab 3",
        "CHUNITHM",
        "CHUNITHM Collab 2",
        "CHUNITHM Collab 3",
        "CHUNITHM Collab 4",
        "Groove Coaster",
        "Groove Coaster Collab 2",
        "Tone Sphere",
        "Lanota",
        "Lanota Collab 2",
        "Dynamix",
    ]

    default = [
        "Arcaea",
    ]

class ArcaeaIndividualDLCSongs(OptionSet):
    """
    Which Other songs not part of a pack youd like to add in.
    Accepts ANY input, meaning you can also use this to add in only parts of a pack.
    probably used for all World Extend, Memory Archive.
    Use this option to add in new songs because this will probably be outdated every so often
    Look in Arcaea.txt to get list of songs that would be included in here
    """

    display_name = "Arcaea Individual DLC Songs"
    default = [
        "Innocence",
    ]

class ArcaeaRequiredGrades(OptionList):
    """
    Grade that the trial might ask you for, will never ask for a specific difficulty
    available options are
    - EX+
    - EX
    - AA
    - A
    - B 
    - C 
    - D 
    - PM / Pure Memory
    - FR / Full Recall
    - HC / Hard Clear 
    - NC / Normal Clear 
    - EC / Easy Clear 
    Allows Duplicates
    """

    display_name = "Arcaea Required Grade"
    valid_keys = [
        "EX+",
        "EX",
        "AA",
        "A",
        "B",
        "C",
        "D",
        "PM",
        "Pure Memory",
        "FR",
        "Full Recall",
        "HC",
        "Hard Clear",
        "NC",
        "Normal Clear",
        "EC",
        "Easy Clear",
    ]

    default = [
        "AA",
        "AA",
        "AA",
        "NC",
    ]
class ArcaeaPartners(OptionList):
    """
    All partners the KMK might as you to do, usually nothing that affects the grading or mirror matters but they will still show up
    For list of partners look in Arcaea.txt
    Accepts any input
    """

    display_name = "Arcaea Partners"

    default = [
        "Hikari",
        "Tairitsu",
    ]