from dataclasses import dataclass

@dataclass
class BurnoutItem:
    ap_id: int
    name: str
    addr_check: int = None   

medals_races_list = [
    # Silver Lake
    BurnoutItem(21051000, "Silver Lake - Race (USA)",               0x0051BE86),
    BurnoutItem(21051001, "Silver Lake - Compact GP (USA)",         0x0051BE8F),
    BurnoutItem(21051002, "Silver Lake - Eliminator (USA)",         0x0051BE92),
    BurnoutItem(21051003, "Silver Lake - Special Event (USA)",      0x0051BEA2),

    # Lakeside Getaway
    BurnoutItem(21051004, "Lakeside Getaway - Face-Off 1 (USA)",    0x0051BE90),
    BurnoutItem(21051005, "Lakeside Getaway - Race (USA)",          0x0051BE96),
    BurnoutItem(21051006, "Lakeside Getaway - Face-Off 2 (USA)",    0x0051BE9B),
    BurnoutItem(21051007, "Lakeside Getaway - Special Event (USA)", 0x0051BECD),

    # Waterfront
    BurnoutItem(21051008, "Waterfront - Burning Lap (USA)",         0x0051BE88),
    BurnoutItem(21051009, "Waterfront - Face-Off (USA)",            0x0051BE8C),
    BurnoutItem(21051010, "Waterfront - Muscle GP (USA)",           0x0051BE9C),
    BurnoutItem(21051011, "Waterfront - Preview Lap (USA)",         0x0051BECB),

    # Mountain Parkway
    BurnoutItem(21051012, "Mountain Parkway - Face-Off 1 (USA)",    0x0051BE99),
    BurnoutItem(21051013, "Mountain Parkway - Road Rage (USA)",     0x0051BE9A),
    BurnoutItem(21051014, "Mountain Parkway - Face-Off 2 (USA)",    0x0051BE9D),
    BurnoutItem(21051015, "Mountain Parkway - Special Event (USA)", 0x0051BEB7),

    # Kings Of The Road
    BurnoutItem(21051016, "Kings Of The Road - Face-Off (USA)",     0x0051BE8E),
    BurnoutItem(21051017, "Kings Of The Road - Race (USA)",         0x0051BE98),
    BurnoutItem(21051018, "Kings Of The Road - Gold Medal GP (USA)",0x0051BECE),

    # Downtown
    BurnoutItem(21051019, "Downtown - Preview Lap 1 (USA)",         0x0051BE87),
    BurnoutItem(21051020, "Downtown - Road Rage 1 (USA)",           0x0051BE89),
    BurnoutItem(21051021, "Downtown - Race 1 (USA)",                0x0051BE8A),
    BurnoutItem(21051022, "Downtown - Race 2 (USA)",                0x0051BE91),
    BurnoutItem(21051023, "Downtown - Road Rage 2 (USA)",           0x0051BE94),
    BurnoutItem(21051024, "Downtown - Preview Lap 2 (USA)",         0x0051BEBE),

    # Winter City
    BurnoutItem(21051025, "Winter City - Race (Europe)",            0x0051BE9E),
    BurnoutItem(21051026, "Winter City - Special Event (Europe)",   0x0051BEA4),
    BurnoutItem(21051027, "Winter City - Eliminator (Europe)",      0x0051BEA9),

    # Frozen Peak
    BurnoutItem(21051028, "Frozen Peak - Face-Off 1 (Europe)",      0x0051BEA8),
    BurnoutItem(21051029, "Frozen Peak - Face-Off 2 (Europe)",      0x0051BEBC),

    # Alpine
    BurnoutItem(21051030, "Alpine - Special Event (Europe)",        0x0051BE93),
    BurnoutItem(21051031, "Alpine - Road Rage (Europe)",            0x0051BEA0),
    BurnoutItem(21051032, "Alpine - Race (Europe)",                 0x0051BEA1),
    BurnoutItem(21051033, "Alpine - Face-Off (Europe)",             0x0051BEB4),

    # Continental Run
    BurnoutItem(21051034, "Continental Run - Face-Off 1 (Europe)",   0x0051BEAB),
    BurnoutItem(21051035, "Continental Run - Race 1 (Europe)",        0x0051BEB2),
    BurnoutItem(21051036, "Continental Run - Race 2 (Europe)",        0x0051BEB8),
    BurnoutItem(21051037, "Continental Run - Special Event (Europe)", 0x0051BEB9),
    BurnoutItem(21051038, "Continental Run - Face-Off 2 (Europe)",    0x0051BEBA),

    # Alpine Expressway
    BurnoutItem(21051039, "Alpine Expressway - Sports GP (Europe)", 0x0051BEBB),
    BurnoutItem(21051040, "Alpine Expressway - Race (Europe)",      0x0051BEA3),

    # Riviera
    BurnoutItem(21051041, "Riviera - Road Rage 1 (Europe)",         0x0051BEA5),
    BurnoutItem(21051042, "Riviera - Burning Lap (Europe)",         0x0051BEAC),
    BurnoutItem(21051043, "Riviera - Eliminator (Europe)",          0x0051BEB1),
    BurnoutItem(21051044, "Riviera - Road Rage 2 (Europe)",         0x0051BEB3),

    # Coastal Dream
    BurnoutItem(21051045, "Coastal Dream - Preview Lap (Europe)",   0x0051BE95),
    BurnoutItem(21051046, "Coastal Dream - Race (Europe)",          0x0051BEAE),
    BurnoutItem(21051047, "Coastal Dream - Road Rage 1 (Europe)",   0x0051BEB5),
    BurnoutItem(21051048, "Coastal Dream - Road Rage 2 (Europe)",   0x0051BEB6),

    # Vineyard
    BurnoutItem(21051049, "Vineyard - Special Event (Europe)",      0x0051BE8B),
    BurnoutItem(21051050, "Vineyard - Road Rage 1 (Europe)",        0x0051BE9F),
    BurnoutItem(21051051, "Vineyard - Face-Off (Europe)",           0x0051BEA7),
    BurnoutItem(21051052, "Vineyard - Coupe GP (Europe)",           0x0051BEAA),
    BurnoutItem(21051053, "Vineyard - Road Rage 2 (Europe)",        0x0051BEAD),
    BurnoutItem(21051054, "Vineyard - Eliminator (Europe)",         0x0051BEAF),

    # Island Paradise
    BurnoutItem(21051055, "Island Paradise - Special Event (Far East)", 0x0051BEA6),
    BurnoutItem(21051056, "Island Paradise - Race (Far East)",          0x0051BEC0),
    BurnoutItem(21051057, "Island Paradise - Face-Off (Far East)",      0x0051BEC3),
    BurnoutItem(21051058, "Island Paradise - Eliminator (Far East)",    0x0051BEC5),

    # Tropical Drive
    BurnoutItem(21051059, "Tropical Drive - Preview Lap (Far East)", 0x0051BEB0),
    BurnoutItem(21051060, "Tropical Drive - Race 1 (Far East)",      0x0051BEC6),
    BurnoutItem(21051061, "Tropical Drive - Race 2 (Far East)",      0x0051BEC7),
    BurnoutItem(21051062, "Tropical Drive - Road Rage (Far East)",   0x0051BEC8),
    BurnoutItem(21051063, "Tropical Drive - Super GP (Far East)",    0x0051BECC),

    # Golden City
    BurnoutItem(21051064, "Golden City - Special Event (Far East)", 0x0051BE97),
    BurnoutItem(21051065, "Golden City - Road Rage (Far East)",     0x0051BEBD),
    BurnoutItem(21051066, "Golden City - Race (Far East)",          0x0051BEC1),
    BurnoutItem(21051067, "Golden City - Face-Off (Far East)",      0x0051BEC9),

    # Dockside
    BurnoutItem(21051068, "Dockside - Special Event (Far East)",    0x0051BE8D),
    BurnoutItem(21051069, "Dockside - Eliminator (Far East)",       0x0051BEBF),
    BurnoutItem(21051070, "Dockside - Road Rage 1 (Far East)",      0x0051BEC2),
    BurnoutItem(21051071, "Dockside - Face-Off (Far East)",         0x0051BEC4),
    BurnoutItem(21051072, "Dockside - Road Rage 2 (Far East)",      0x0051BECA),
]

medals_crashes_list = [
    # Silver Lake
    BurnoutItem(21052000, "Silver Lake - Trailer Trash (USA)",      0x0051BECF),
    BurnoutItem(21052001, "Silver Lake - Shut Up and Jump (USA)",   0x0051BED4),
    BurnoutItem(21052002, "Silver Lake - Showdown (USA)",           0x0051BEE3),
    BurnoutItem(21052003, "Silver Lake - Ticket to Collide (USA)",  0x0051BEE6),
    BurnoutItem(21052004, "Silver Lake - 3 Ways to Fly (USA)",      0x0051BEF8),
    BurnoutItem(21052005, "Silver Lake - Bridge Too Far (USA)",     0x0051BEFB),
    BurnoutItem(21052006, "Silver Lake - Out of Control (USA)",     0x0051BF0B),
    BurnoutItem(21052007, "Silver Lake - Fear Factor (USA)",        0x0051BF0E),
    BurnoutItem(21052008, "Silver Lake - Pick Up the Pieces (USA)", 0x0051BF1F),

    # Waterfront
    BurnoutItem(21052009, "Waterfront - Marina Mayhem (USA)",       0x0051BED1),
    BurnoutItem(21052010, "Waterfront - Twister (USA)",             0x0051BED2),
    BurnoutItem(21052011, "Waterfront - Leap of Faith (USA)",       0x0051BEE4),
    BurnoutItem(21052012, "Waterfront - Danger Zone (USA)",         0x0051BEE8),
    BurnoutItem(21052013, "Waterfront - Bay-side Blitz (USA)",      0x0051BEF9),
    BurnoutItem(21052014, "Waterfront - Falling Down (USA)",        0x0051BF0D),
    BurnoutItem(21052015, "Waterfront - T-Boned (USA)",             0x0051BF0F),
    BurnoutItem(21052016, "Waterfront - Sunshine Smash (USA)",      0x0051BF10),
    BurnoutItem(21052017, "Waterfront - Look then Leap (USA)",      0x0051BF23),
    BurnoutItem(21052018, "Waterfront - Tram-Pulled (USA)",         0x0051BF24),

    # Downtown
    BurnoutItem(21052019, "Downtown - Cross Traffic (USA)",         0x0051BED0),
    BurnoutItem(21052020, "Downtown - Demolition (USA)",            0x0051BED3),
    BurnoutItem(21052021, "Downtown - Dead End (USA)",              0x0051BEE5),
    BurnoutItem(21052022, "Downtown - Wrecks City (USA)",           0x0051BEE7),
    BurnoutItem(21052023, "Downtown - Hate to be Late (USA)",       0x0051BEF7),
    BurnoutItem(21052024, "Downtown - Hold Tight (USA)",            0x0051BEFA),
    BurnoutItem(21052025, "Downtown - Traffic Jammed (USA)",        0x0051BEFC),
    BurnoutItem(21052026, "Downtown - Bus Blockade (USA)",          0x0051BF0C),
    BurnoutItem(21052027, "Downtown - Grid Locked (USA)",           0x0051BF20),
    BurnoutItem(21052028, "Downtown - Air Rage (USA)",              0x0051BF21),
    BurnoutItem(21052029, "Downtown - Hit and Run (USA)",           0x0051BF22),

    # Winter City
    BurnoutItem(21052030, "Winter City - Slip and Slide (Europe)",    0x0051BED5),
    BurnoutItem(21052031, "Winter City - Pump Up the Tram (Europe)",  0x0051BED9),
    BurnoutItem(21052032, "Winter City - Corner Chaos (Europe)",      0x0051BEDB),
    BurnoutItem(21052033, "Winter City - Riverside Wreck (Europe)",   0x0051BEEA),
    BurnoutItem(21052034, "Winter City - Snow Joke (Europe)",         0x0051BEEF),
    BurnoutItem(21052035, "Winter City - Market Crash (Europe)",      0x0051BF00),
    BurnoutItem(21052036, "Winter City - Winter Wipe-out (Europe)",   0x0051BF01),
    BurnoutItem(21052037, "Winter City - Crash Landing (Europe)",     0x0051BF12),
    BurnoutItem(21052038, "Winter City - Run for the Bus (Europe)",   0x0051BF17),
    BurnoutItem(21052039, "Winter City - On Rampage (Europe)",        0x0051BF25),
    BurnoutItem(21052040, "Winter City - Cool for Crash (Europe)",    0x0051BF29),

    # Alpine
    BurnoutItem(21052041, "Alpine - Roadblock (Europe)",            0x0051BED7),
    BurnoutItem(21052042, "Alpine - Don't Look Down (Europe)",      0x0051BEEC),
    BurnoutItem(21052043, "Alpine - Chilly Crash (Europe)",         0x0051BEF0),
    BurnoutItem(21052044, "Alpine - Exact Change (Europe)",         0x0051BEFD),
    BurnoutItem(21052045, "Alpine - Lanes Lunacy (Europe)",         0x0051BF04),
    BurnoutItem(21052046, "Alpine - Snow Plough (Europe)",          0x0051BF11),
    BurnoutItem(21052047, "Alpine - Corkscrewed (Europe)",          0x0051BF18),
    BurnoutItem(21052048, "Alpine - Jump the Toll (Europe)",        0x0051BF26),
    BurnoutItem(21052049, "Alpine - Highway to Hell (Europe)",      0x0051BF2C),

    # Riviera
    BurnoutItem(21052050, "Riviera - Grand Slam (Europe)",          0x0051BED6),
    BurnoutItem(21052051, "Riviera - Get Bent (Europe)",            0x0051BEDA),
    BurnoutItem(21052052, "Riviera - Riviera Rampage (Europe)",     0x0051BEE9),
    BurnoutItem(21052053, "Riviera - Spin the Wheel (Europe)",      0x0051BEED),
    BurnoutItem(21052054, "Riviera - Cliff Hanger (Europe)",        0x0051BEFF),
    BurnoutItem(21052055, "Riviera - High Roller (Europe)",         0x0051BF02),
    BurnoutItem(21052056, "Riviera - Break the Bank (Europe)",      0x0051BF13),
    BurnoutItem(21052057, "Riviera - Go for Broke (Europe)",        0x0051BF15),
    BurnoutItem(21052058, "Riviera - Jumping Jam (Europe)",         0x0051BF27),
    BurnoutItem(21052059, "Riviera - Ship Wrecked (Europe)",        0x0051BF2A),

    # Vineyard
    BurnoutItem(21052060, "Vineyard - Grapes of Wrath (Europe)",    0x0051BED8),
    BurnoutItem(21052061, "Vineyard - Jack Knife City (Europe)",    0x0051BEDC),
    BurnoutItem(21052062, "Vineyard - Grape Fear (Europe)",         0x0051BEEB),
    BurnoutItem(21052063, "Vineyard - Field of Screams (Europe)",   0x0051BEEE),
    BurnoutItem(21052064, "Vineyard - Country Chaos (Europe)",      0x0051BEFE),
    BurnoutItem(21052065, "Vineyard - Haul A$$ (Europe)",           0x0051BF03),
    BurnoutItem(21052066, "Vineyard - Bale Out (Europe)",           0x0051BF14),
    BurnoutItem(21052067, "Vineyard - Medieval Mash (Europe)",      0x0051BF16),
    BurnoutItem(21052068, "Vineyard - Crash au Van (Europe)",       0x0051BF28),
    BurnoutItem(21052069, "Vineyard - Gate Crasher (Europe)",       0x0051BF2B),

    # Island Paradise
    BurnoutItem(21052070, "Island Paradise - Paradise Peril (Far East)",  0x0051BEDE),
    BurnoutItem(21052071, "Island Paradise - Ruined Holiday (Far East)",  0x0051BEE0),
    BurnoutItem(21052072, "Island Paradise - Tropical Storm (Far East)",  0x0051BEF3),
    BurnoutItem(21052073, "Island Paradise - Drive Angry (Far East)",     0x0051BEF6),
    BurnoutItem(21052074, "Island Paradise - Jungle Rumble (Far East)",   0x0051BF06),
    BurnoutItem(21052075, "Island Paradise - Airstrike (Far East)",       0x0051BF08),
    BurnoutItem(21052076, "Island Paradise - Steel Tsunami (Far East)",   0x0051BF1B),
    BurnoutItem(21052077, "Island Paradise - Uphill Struggle (Far East)", 0x0051BF1D),
    BurnoutItem(21052078, "Island Paradise - Tourist Trap (Far East)",    0x0051BF2F),
    BurnoutItem(21052079, "Island Paradise - Pure Scores (Far East)",     0x0051BF30),
    BurnoutItem(21052080, "Island Paradise - Lost Luggage (Far East)",    0x0051BF31),

    # Golden City
    BurnoutItem(21052081, "Golden City - Neon Nightmare (Far East)",    0x0051BEDD),
    BurnoutItem(21052082, "Golden City - Tuk Down (Far East)",          0x0051BEE1),
    BurnoutItem(21052083, "Golden City - Handle with Care (Far East)",  0x0051BEE2),
    BurnoutItem(21052084, "Golden City - Turn & Burn (Far East)",       0x0051BEF1),
    BurnoutItem(21052085, "Golden City - Crossing Crush (Far East)",    0x0051BEF4),
    BurnoutItem(21052086, "Golden City - Freeway Thunder (Far East)",   0x0051BEF5),
    BurnoutItem(21052087, "Golden City - Road to Ruin (Far East)",      0x0051BF05),
    BurnoutItem(21052088, "Golden City - Trash Smash (Far East)",       0x0051BF09),
    BurnoutItem(21052089, "Golden City - Heavy Hitter (Far East)",      0x0051BF1A),
    BurnoutItem(21052090, "Golden City - Eastern Block (Far East)",     0x0051BF1E),
    BurnoutItem(21052091, "Golden City - Crash Fu (Far East)",          0x0051BF2D),

    # Dockside
    BurnoutItem(21052092, "Dockside - Rock the Dock (Far East)",    0x0051BEDF),
    BurnoutItem(21052093, "Dockside - Exit the Dragon (Far East)",  0x0051BEF2),
    BurnoutItem(21052094, "Dockside - Reiko-chet (Far East)",       0x0051BF07),
    BurnoutItem(21052095, "Dockside - Whirlwind (Far East)",        0x0051BF0A),
    BurnoutItem(21052096, "Dockside - Look Both Ways (Far East)",   0x0051BF19),
    BurnoutItem(21052097, "Dockside - Buckle Up (Far East)",        0x0051BF1C),
    BurnoutItem(21052098, "Dockside - The Crate Escape (Far East)", 0x0051BF2E),
    BurnoutItem(21052099, "Dockside - Crashed Out (Far East)",      0x0051BF32),
]

signature_list = [
    BurnoutItem(21054000, "Gone Fishin'",         0x0051BF33),
    BurnoutItem(21054001, "Home Wrecker",         0x0051BF34),
    BurnoutItem(21054002, "Pillar Driller",       0x0051BF35),
    BurnoutItem(21054003, "Hit the Split",        0x0051BF36),
    BurnoutItem(21054004, "Tram Ram",             0x0051BF37),
    BurnoutItem(21054005, "Truck Torpedo",        0x0051BF38),
    BurnoutItem(21054006, "Euro Tram Ram",        0x0051BF39),
    BurnoutItem(21054007, "Snowed Under",         0x0051BF3A),
    BurnoutItem(21054008, "Avalanche!",           0x0051BF3B),
    BurnoutItem(21054009, "Paid the Price!",      0x0051BF3C),
    BurnoutItem(21054010, "Riviera Roustabout",   0x0051BF3D),
    BurnoutItem(21054011, "Berth Trauma",         0x0051BF3E),
    BurnoutItem(21054012, "Gate Crasher",         0x0051BF3F),
    BurnoutItem(21054013, "Grapes of Wrath",      0x0051BF40),
    BurnoutItem(21054014, "Market-Stalled",       0x0051BF41),
    BurnoutItem(21054015, "Tuk-Down",             0x0051BF42),
    BurnoutItem(21054016, "Tunnel of Shove",      0x0051BF43),
    BurnoutItem(21054017, "Ship Wreck",           0x0051BF44),
    BurnoutItem(21054018, "Rumble in the Jungle", 0x0051BF45),
    BurnoutItem(21054019, "Catch The Tour Bus",   0x0051BF46),
]

headline_list = [
    BurnoutItem(21054020, "Bayside Blitz!",         0x0051BF47),
    BurnoutItem(21054021, "Downtown Demolition!",    0x0051BF48),
    BurnoutItem(21054022, "Silver Lake Lunacy!",     0x0051BF49),
    BurnoutItem(21054023, "Winter City Frozen!",     0x0051BF4A),
    BurnoutItem(21054024, "Alpine Smash!",           0x0051BF4B),
    BurnoutItem(21054025, "Riviera Wreck!",          0x0051BF4C),
    BurnoutItem(21054026, "Grape Harvests Crushed!", 0x0051BF4D),
    BurnoutItem(21054027, "Golden City Madness!",    0x0051BF4E),
    BurnoutItem(21054028, "Dockside Ridge Ruin!",    0x0051BF4F),
    BurnoutItem(21054029, "Trouble in Paradise!",    0x0051BF50),
]

ALL_MEDALS_LIST = [item for item in medals_races_list + medals_crashes_list if item.addr_check is not None]
ALL_RACE_LIST = [item for item in medals_races_list if item.addr_check is not None]
ALL_CRASH_LIST = [item for item in medals_crashes_list if item.addr_check is not None]
ALL_OTHERS_LIST = [item for item in signature_list + headline_list if item.addr_check is not None]