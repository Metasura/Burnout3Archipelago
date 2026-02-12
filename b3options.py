from dataclasses import dataclass
from Options import Choice, PerGameCommonOptions, Toggle, DefaultOnToggle

class GameplayMode(Choice):
     
    display_name = "Gameplay Mode"
    option_all_gold_medals = 0
    option_race_gold_medals = 1
    option_crash_gold_medals = 2
    default = 0

class EnableSignatures(DefaultOnToggle):
    display_name = "Enable Signature Takedowns"

class EnableHeadlines(DefaultOnToggle):
    display_name = "Enable Crash Headlines"

    
@dataclass
class Burnout3Options(PerGameCommonOptions):
    gameplay_mode: GameplayMode
    enable_signatures: EnableSignatures
    enable_headlines: EnableHeadlines