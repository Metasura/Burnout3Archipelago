from dataclasses import dataclass
from Options import Choice, PerGameCommonOptions, Toggle, Range

class GameplayMode(Choice):
     
    display_name = "Gameplay Mode"
    option_all_gold_medals = 0
    option_race_gold_medals = 1
    option_crash_gold_medals = 2
    default = 0

class EnableSignatures(Toggle):
    display_name = "Enable Signature Takedowns"

class EnableHeadlines(Toggle):
    display_name = "Enable Crash Headlines"

class RequiredMedals(Range):
    range_start = 1
    range_end = 173
    default = 173
    display_name = "Required Gold Medals"

    
@dataclass
class Burnout3Options(PerGameCommonOptions):
    gameplay_mode: GameplayMode
    enable_signatures: EnableSignatures
    enable_headlines: EnableHeadlines
    required_medals: RequiredMedals