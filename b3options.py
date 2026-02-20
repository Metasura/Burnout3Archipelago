from dataclasses import dataclass
from Options import Choice, PerGameCommonOptions, Toggle, Range

class GameplayMode(Choice):
     
    display_name = "Gameplay Mode"
    option_all_medals = 0
    option_race_medals = 1
    option_crash_medals = 2
    default = 0

class RequiredMedalType(Choice):
    display_name = "Required Medal Type"
    option_bronze = 0
    option_silver = 1
    option_gold = 2
    default = 2

class GeneratedEvents(Range):
    range_start = 1
    range_end = 173
    default = 173
    display_name = "Generated Events Count"

class RequiredMedals(Range):
    range_start = 1
    range_end = 173
    default = 173
    display_name = "Required Medals Count"

class EnableSignatures(Toggle):
    display_name = "Enable Signature Takedowns"

class EnableHeadlines(Toggle):
    display_name = "Enable Crash Headlines"


@dataclass
class Burnout3Options(PerGameCommonOptions):
    gameplay_mode: GameplayMode
    medal_type: RequiredMedalType
    generated_events: GeneratedEvents
    required_medals: RequiredMedals
    enable_signatures: EnableSignatures
    enable_headlines: EnableHeadlines
    