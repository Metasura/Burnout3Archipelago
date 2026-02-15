from dataclasses import dataclass

@dataclass
class BurnoutItem:
    ap_id: int
    name: str
    addr_unlock: int = None  
      

cars_list = [
    # Compact Class
    BurnoutItem(21053000,"Compact Type 1", 0x051BFA0),
    BurnoutItem(21053001,"Compact Type 2", 0x051BFA1),
    BurnoutItem(21053002,"Compact Type 3", 0x051BFA2),
    BurnoutItem(21053003,"Tuned Compact", 0x051BFA3),
    BurnoutItem(21053004,"Modified Compact", 0x051BFA4),
    BurnoutItem(21053005,"Custom Compact", 0x051BFA5),
    BurnoutItem(21053006,"Assassin Compact", 0x051BFA6),
    BurnoutItem(21053007,"Compact Protoype", 0x051BFA7),
    BurnoutItem(21053008,"Compact DX", 0x051BFA8),
    BurnoutItem(21053009,"Dominator Compact", 0x051BFA9),

    # Muscle Class
    BurnoutItem(21053010,"Muscle Type 1", 0x051BFAA),
    BurnoutItem(21053011,"Muscle Type 2", 0x051BFAB),
    BurnoutItem(21053012,"Muscle Type 3", 0x051BFAC),
    BurnoutItem(21053013,"Tuned Muscle", 0x051BFAD),
    BurnoutItem(21053014,"Modified Muscle", 0x051BFAE),
    BurnoutItem(21053015,"Custom Muscle", 0x051BFAF),
    BurnoutItem(21053016,"Assassin Muscle", 0x051BFB0),
    BurnoutItem(21053017,"Muscle Protoype", 0x051BFB1),
    BurnoutItem(21053018,"Muscle DX", 0x051BFB2),
    BurnoutItem(21053019,"Dominator Muscle", 0x051BFB3),

    # Coupe Class
    BurnoutItem(21053020,"Coupe Type 1", 0x051BFB4),
    BurnoutItem(21053021,"Coupe Type 2", 0x051BFB5),
    BurnoutItem(21053022,"Coupe Type 3", 0x051BFB6),
    BurnoutItem(21053023,"Tuned Coupe", 0x051BFB7),
    BurnoutItem(21053024,"Modified Coupe", 0x051BFB8),
    BurnoutItem(21053025,"Custom Coupe", 0x051BFB9),
    BurnoutItem(21053026,"Assassin Coupe", 0x051BFBA),
    BurnoutItem(21053027,"Coupe Protoype", 0x051BFBB),
    BurnoutItem(21053028,"Coupe DX", 0x051BFBC),
    BurnoutItem(21053029,"Dominator Coupe", 0x051BFBD),

    # Sports Class
    BurnoutItem(21053030,"Sports Type 1", 0x051BFBE),
    BurnoutItem(21053031,"Sports Type 2", 0x051BFBF),
    BurnoutItem(21053032,"Sports Type 3", 0x051BFC0),
    BurnoutItem(21053033,"Tuned Sports", 0x051BFC1),
    BurnoutItem(21053034,"Modified Sports", 0x051BFC2),
    BurnoutItem(21053035,"Custom Sports", 0x051BFC3),
    BurnoutItem(21053036,"Assassin Sports", 0x051BFC4),
    BurnoutItem(21053037,"Sports Protoype", 0x051BFC5),
    BurnoutItem(21053038,"Sports DX", 0x051BFC6),
    BurnoutItem(21053039,"Dominator Sports", 0x051BFC7),

    # Super Class 
    BurnoutItem(21053040,"Super Type 1", 0x051BFC8),
    BurnoutItem(21053041,"Super Type 2", 0x051BFC9),
    BurnoutItem(21053042,"Super Type 3", 0x051BFCA),
    BurnoutItem(21053043,"Tuned Super", 0x051BFCB),
    BurnoutItem(21053044,"Modified Super", 0x051BFCC),
    BurnoutItem(21053045,"Custom Super", 0x051BFCD),
    BurnoutItem(21053046,"Assassin Super", 0x051BFCE),
    BurnoutItem(21053047,"Super Protoype", 0x051BFCF),
    BurnoutItem(21053048,"Super DX", 0x051BFD0),
    BurnoutItem(21053049,"Dominator Super", 0x051BFD1),

    # Special Class
    BurnoutItem(21053050,"Oval Racer Special", 0x051BFD2),
    BurnoutItem(21053051,"Custom Coupe Ultimate", 0x051BFD3),
    BurnoutItem(21053052,"Euro Circuit Racer", 0x051BFD4),
    BurnoutItem(21053053,"Classic Hotrod", 0x051BFD5),
    BurnoutItem(21053054,"US Circuit Racer", 0x051BFD7),
    BurnoutItem(21053055,"World Circuit Racer", 0x051BFD8),

    # Crash Class 
    BurnoutItem(21053056,"Heavy Pick-Up", 0x051BFD9),
    BurnoutItem(21053057,"4WD Racer", 0x051BFDA),
    BurnoutItem(21053058,"SUV Deluxe", 0x051BFDB),
    BurnoutItem(21053059,"4WD Heavy Duty", 0x051BFDC),
    BurnoutItem(21053060,"B-Team Van", 0x051BFDD),
    BurnoutItem(21053061,"Delivery Truck", 0x051BFDE),
    BurnoutItem(21053062,"Tractor Cab", 0x051BFDF),
    BurnoutItem(21053063,"Longnose Cab", 0x051BFE0),
    BurnoutItem(21053064,"City Bus", 0x051BFE1),
    BurnoutItem(21053065,"Trash Truck", 0x051BFE2),
    BurnoutItem(21053066,"Fire Truck", 0x051BFD6),
]

races_list = [
    # Silver Lake
    BurnoutItem(21051000, "Silver Lake - Race (USA)",               0x0051BFF7),
    BurnoutItem(21051001, "Silver Lake - Compact GP (USA)",         0x0051C000),
    BurnoutItem(21051002, "Silver Lake - Eliminator (USA)",         0x0051C003),
    BurnoutItem(21051003, "Silver Lake - Special Event (USA)",      0x0051C013),

    # Lakeside Getaway
    BurnoutItem(21051004, "Lakeside Getaway - Face-Off 1 (USA)",    0x0051C001),
    BurnoutItem(21051005, "Lakeside Getaway - Race (USA)",          0x0051C007),
    BurnoutItem(21051006, "Lakeside Getaway - Face-Off 2 (USA)",    0x0051C00C),
    BurnoutItem(21051007, "Lakeside Getaway - Special Event (USA)", 0x0051C03E),

    # Waterfront
    BurnoutItem(21051008, "Waterfront - Burning Lap (USA)",         0x0051BFF9),
    BurnoutItem(21051009, "Waterfront - Face-Off (USA)",            0x0051BFFD),
    BurnoutItem(21051010, "Waterfront - Muscle GP (USA)",           0x0051C00D),
    BurnoutItem(21051011, "Waterfront - Preview Lap (USA)",         0x0051C03C),

    # Mountain Parkway
    BurnoutItem(21051012, "Mountain Parkway - Face-Off 1 (USA)",    0x0051C00A),
    BurnoutItem(21051013, "Mountain Parkway - Road Rage (USA)",     0x0051C00B),
    BurnoutItem(21051014, "Mountain Parkway - Face-Off 2 (USA)",    0x0051C00E),
    BurnoutItem(21051015, "Mountain Parkway - Special Event (USA)", 0x0051C028),

    # Kings Of The Road
    BurnoutItem(21051016, "Kings Of The Road - Face-Off (USA)",     0x0051BFFF),
    BurnoutItem(21051017, "Kings Of The Road - Race (USA)",         0x0051C009),
    BurnoutItem(21051018, "Kings Of The Road - Gold Medal GP (USA)",0x0051C03F),

    # Downtown
    BurnoutItem(21051019, "Downtown - Preview Lap 1 (USA)",         0x0051BFF8),
    BurnoutItem(21051020, "Downtown - Road Rage 1 (USA)",           0x0051BFFA),
    BurnoutItem(21051021, "Downtown - Race 1 (USA)",                0x0051BFFB),
    BurnoutItem(21051022, "Downtown - Race 2 (USA)",                0x0051C002),
    BurnoutItem(21051023, "Downtown - Road Rage 2 (USA)",           0x0051C005),
    BurnoutItem(21051024, "Downtown - Preview Lap 2 (USA)",         0x0051C02F),

    # Winter City
    BurnoutItem(21051025, "Winter City - Race (Europe)",            0x0051C00F),
    BurnoutItem(21051026, "Winter City - Special Event (Europe)",   0x0051C015),
    BurnoutItem(21051027, "Winter City - Eliminator (Europe)",      0x0051C01A),

    # Frozen Peak
    BurnoutItem(21051028, "Frozen Peak - Face-Off 1 (Europe)",      0x0051C019),
    BurnoutItem(21051029, "Frozen Peak - Face-Off 2 (Europe)",      0x0051C02D),

    # Alpine
    BurnoutItem(21051030, "Alpine - Special Event (Europe)",        0x0051C004),
    BurnoutItem(21051031, "Alpine - Road Rage (Europe)",            0x0051C011),
    BurnoutItem(21051032, "Alpine - Race (Europe)",                 0x0051C010),
    BurnoutItem(21051033, "Alpine - Face-Off (Europe)",             0x0051C025),

    # Continental Run
    BurnoutItem(21051034, "Continental Run - Face-Off 1 (Europe)",   0x0051C01C),
    BurnoutItem(21051035, "Continental Run - Race 1 (Europe)",        0x0051C023),
    BurnoutItem(21051036, "Continental Run - Race 2 (Europe)",        0x0051C029),
    BurnoutItem(21051037, "Continental Run - Special Event (Europe)", 0x0051C02A),
    BurnoutItem(21051038, "Continental Run - Face-Off 2 (Europe)",    0x0051C02B),

    # Alpine Expressway
    BurnoutItem(21051039, "Alpine Expressway - Sports GP (Europe)", 0x0051C02C),
    BurnoutItem(21051040, "Alpine Expressway - Race (Europe)",      0x0051C014),

    # Riviera
    BurnoutItem(21051041, "Riviera - Road Rage 1 (Europe)",         0x0051C016),
    BurnoutItem(21051042, "Riviera - Burning Lap (Europe)",         0x0051C01D),
    BurnoutItem(21051043, "Riviera - Eliminator (Europe)",          0x0051C022),
    BurnoutItem(21051044, "Riviera - Road Rage 2 (Europe)",         0x0051C024),

    # Coastal Dream
    BurnoutItem(21051045, "Coastal Dream - Preview Lap (Europe)",   0x0051C006),
    BurnoutItem(21051046, "Coastal Dream - Race (Europe)",          0x0051C01F),
    BurnoutItem(21051047, "Coastal Dream - Road Rage 1 (Europe)",   0x0051C026),
    BurnoutItem(21051048, "Coastal Dream - Road Rage 2 (Europe)",   0x0051C027),

    # Vineyard
    BurnoutItem(21051049, "Vineyard - Special Event (Europe)",      0x0051BFFC),
    BurnoutItem(21051050, "Vineyard - Road Rage 1 (Europe)",        0x0051C010),
    BurnoutItem(21051051, "Vineyard - Face-Off (Europe)",           0x0051C018),
    BurnoutItem(21051052, "Vineyard - Coupe GP (Europe)",           0x0051C01B),
    BurnoutItem(21051053, "Vineyard - Road Rage 2 (Europe)",        0x0051C01E),
    BurnoutItem(21051054, "Vineyard - Eliminator (Europe)",         0x0051C020),

    # Island Paradise
    BurnoutItem(21051055, "Island Paradise - Special Event (Far East)", 0x0051C017),
    BurnoutItem(21051056, "Island Paradise - Race (Far East)",          0x0051C031),
    BurnoutItem(21051057, "Island Paradise - Face-Off (Far East)",      0x0051C034),
    BurnoutItem(21051058, "Island Paradise - Eliminator (Far East)",    0x0051C036),

    # Tropical Drive
    BurnoutItem(21051059, "Tropical Drive - Preview Lap (Far East)", 0x0051C021),
    BurnoutItem(21051060, "Tropical Drive - Race 1 (Far East)",      0x0051C037),
    BurnoutItem(21051061, "Tropical Drive - Race 2 (Far East)",      0x0051C038),
    BurnoutItem(21051062, "Tropical Drive - Road Rage (Far East)",   0x0051C039),
    BurnoutItem(21051063, "Tropical Drive - Super GP (Far East)",    0x0051C03D),

    # Golden City
    BurnoutItem(21051064, "Golden City - Special Event (Far East)", 0x0051C008),
    BurnoutItem(21051065, "Golden City - Road Rage (Far East)",     0x0051C02E),
    BurnoutItem(21051066, "Golden City - Race (Far East)",          0x0051C032),
    BurnoutItem(21051067, "Golden City - Face-Off (Far East)",      0x0051C03A),

    # Dockside
    BurnoutItem(21051068, "Dockside - Special Event (Far East)",    0x0051BFFE),
    BurnoutItem(21051069, "Dockside - Eliminator (Far East)",       0x0051C030),
    BurnoutItem(21051070, "Dockside - Road Rage 1 (Far East)",      0x0051C033),
    BurnoutItem(21051071, "Dockside - Face-Off (Far East)",         0x0051C035),
    BurnoutItem(21051072, "Dockside - Road Rage 2 (Far East)",      0x0051C03B),
]

crashes_list = [
    # Silver Lake
    BurnoutItem(21052000, "Silver Lake - Trailer Trash (USA)",      0x0051C040),
    BurnoutItem(21052001, "Silver Lake - Shut Up and Jump (USA)",   0x0051C045),
    BurnoutItem(21052002, "Silver Lake - Showdown (USA)",           0x0051C054),
    BurnoutItem(21052003, "Silver Lake - Ticket to Collide (USA)",  0x0051C057),
    BurnoutItem(21052004, "Silver Lake - 3 Ways to Fly (USA)",      0x0051C069),
    BurnoutItem(21052005, "Silver Lake - Bridge Too Far (USA)",     0x0051C06C),
    BurnoutItem(21052006, "Silver Lake - Out of Control (USA)",     0x0051C07C),
    BurnoutItem(21052007, "Silver Lake - Fear Factor (USA)",        0x0051C07F),
    BurnoutItem(21052008, "Silver Lake - Pick Up the Pieces (USA)", 0x0051C090),

    # Waterfront
    BurnoutItem(21052009, "Waterfront - Marina Mayhem (USA)",       0x0051C042),
    BurnoutItem(21052010, "Waterfront - Twister (USA)",             0x0051C043),
    BurnoutItem(21052011, "Waterfront - Leap of Faith (USA)",       0x0051C055),
    BurnoutItem(21052012, "Waterfront - Danger Zone (USA)",         0x0051C059),
    BurnoutItem(21052013, "Waterfront - Bay-side Blitz (USA)",      0x0051C06A),
    BurnoutItem(21052014, "Waterfront - Falling Down (USA)",        0x0051C07E),
    BurnoutItem(21052015, "Waterfront - T-Boned (USA)",             0x0051C080),
    BurnoutItem(21052016, "Waterfront - Sunshine Smash (USA)",      0x0051C081),
    BurnoutItem(21052017, "Waterfront - Look then Leap (USA)",      0x0051C094),
    BurnoutItem(21052018, "Waterfront - Tram-Pulled (USA)",         0x0051C095),

    # Downtown
    BurnoutItem(21052019, "Downtown - Cross Traffic (USA)",         0x0051C041),
    BurnoutItem(21052020, "Downtown - Demolition (USA)",            0x0051C044),
    BurnoutItem(21052021, "Downtown - Dead End (USA)",              0x0051C056),
    BurnoutItem(21052022, "Downtown - Wrecks City (USA)",           0x0051C058),
    BurnoutItem(21052023, "Downtown - Hate to be Late (USA)",       0x0051C068),
    BurnoutItem(21052024, "Downtown - Hold Tight (USA)",            0x0051C06B),
    BurnoutItem(21052025, "Downtown - Traffic Jammed (USA)",        0x0051C06D),
    BurnoutItem(21052026, "Downtown - Bus Blockade (USA)",          0x0051C07D),
    BurnoutItem(21052027, "Downtown - Grid Locked (USA)",           0x0051C091),
    BurnoutItem(21052028, "Downtown - Air Rage (USA)",              0x0051C092),
    BurnoutItem(21052029, "Downtown - Hit and Run (USA)",           0x0051C093),

    # Winter City
    BurnoutItem(21052030, "Winter City - Slip and Slide (Europe)",    0x0051C046),
    BurnoutItem(21052031, "Winter City - Pump Up the Tram (Europe)",  0x0051C04A),
    BurnoutItem(21052032, "Winter City - Corner Chaos (Europe)",      0x0051C04C),
    BurnoutItem(21052033, "Winter City - Riverside Wreck (Europe)",   0x0051C05B),
    BurnoutItem(21052034, "Winter City - Snow Joke (Europe)",         0x0051C060),
    BurnoutItem(21052035, "Winter City - Market Crash (Europe)",      0x0051C071),
    BurnoutItem(21052036, "Winter City - Winter Wipe-out (Europe)",   0x0051C072),
    BurnoutItem(21052037, "Winter City - Crash Landing (Europe)",     0x0051C083),
    BurnoutItem(21052038, "Winter City - Run for the Bus (Europe)",   0x0051C088),
    BurnoutItem(21052039, "Winter City - On Rampage (Europe)",        0x0051C096),
    BurnoutItem(21052040, "Winter City - Cool for Crash (Europe)",    0x0051C09A),

    # Alpine
    BurnoutItem(21052041, "Alpine - Roadblock (Europe)",            0x0051C048),
    BurnoutItem(21052042, "Alpine - Don't Look Down (Europe)",      0x0051C05D),
    BurnoutItem(21052043, "Alpine - Chilly Crash (Europe)",         0x0051C061),
    BurnoutItem(21052044, "Alpine - Exact Change (Europe)",         0x0051C06E),
    BurnoutItem(21052045, "Alpine - Lanes Lunacy (Europe)",         0x0051C075),
    BurnoutItem(21052046, "Alpine - Snow Plough (Europe)",          0x0051C082),
    BurnoutItem(21052047, "Alpine - Corkscrewed (Europe)",          0x0051C089),
    BurnoutItem(21052048, "Alpine - Jump the Toll (Europe)",        0x0051C097),
    BurnoutItem(21052049, "Alpine - Highway to Hell (Europe)",      0x0051C09D),

    # Riviera
    BurnoutItem(21052050, "Riviera - Grand Slam (Europe)",          0x0051C047),
    BurnoutItem(21052051, "Riviera - Get Bent (Europe)",            0x0051C04B),
    BurnoutItem(21052052, "Riviera - Riviera Rampage (Europe)",     0x0051C05A),
    BurnoutItem(21052053, "Riviera - Spin the Wheel (Europe)",      0x0051C05E),
    BurnoutItem(21052054, "Riviera - Cliff Hanger (Europe)",        0x0051C070),
    BurnoutItem(21052055, "Riviera - High Roller (Europe)",         0x0051C073),
    BurnoutItem(21052056, "Riviera - Break the Bank (Europe)",      0x0051C084),
    BurnoutItem(21052057, "Riviera - Go for Broke (Europe)",        0x0051C086),
    BurnoutItem(21052058, "Riviera - Jumping Jam (Europe)",         0x0051C098),
    BurnoutItem(21052059, "Riviera - Ship Wrecked (Europe)",        0x0051C09B),

    # Vineyard
    BurnoutItem(21052060, "Vineyard - Grapes of Wrath (Europe)",    0x0051C049),
    BurnoutItem(21052061, "Vineyard - Jack Knife City (Europe)",    0x0051C04D),
    BurnoutItem(21052062, "Vineyard - Grape Fear (Europe)",         0x0051C05C),
    BurnoutItem(21052063, "Vineyard - Field of Screams (Europe)",   0x0051C05F),
    BurnoutItem(21052064, "Vineyard - Country Chaos (Europe)",      0x0051C06F),
    BurnoutItem(21052065, "Vineyard - Haul A$$ (Europe)",           0x0051C074),
    BurnoutItem(21052066, "Vineyard - Bale Out (Europe)",           0x0051C085),
    BurnoutItem(21052067, "Vineyard - Medieval Mash (Europe)",      0x0051C087),
    BurnoutItem(21052068, "Vineyard - Crash au Van (Europe)",       0x0051C099),
    BurnoutItem(21052069, "Vineyard - Gate Crasher (Europe)",       0x0051C09C),

    # Island Paradise
    BurnoutItem(21052070, "Island Paradise - Paradise Peril (Far East)",  0x0051C04F),
    BurnoutItem(21052071, "Island Paradise - Ruined Holiday (Far East)",  0x0051C051),
    BurnoutItem(21052072, "Island Paradise - Tropical Storm (Far East)",  0x0051C064),
    BurnoutItem(21052073, "Island Paradise - Drive Angry (Far East)",     0x0051C067),
    BurnoutItem(21052074, "Island Paradise - Jungle Rumble (Far East)",   0x0051C077),
    BurnoutItem(21052075, "Island Paradise - Airstrike (Far East)",       0x0051C079),
    BurnoutItem(21052076, "Island Paradise - Steel Tsunami (Far East)",   0x0051C08C),
    BurnoutItem(21052077, "Island Paradise - Uphill Struggle (Far East)", 0x0051C08E),
    BurnoutItem(21052078, "Island Paradise - Tourist Trap (Far East)",    0x0051C0A0),
    BurnoutItem(21052079, "Island Paradise - Pure Scores (Far East)",     0x0051C0A1),
    BurnoutItem(21052080, "Island Paradise - Lost Luggage (Far East)",    0x0051C0A2),

    # Golden City
    BurnoutItem(21052081, "Golden City - Neon Nightmare (Far East)",    0x0051C04E),
    BurnoutItem(21052082, "Golden City - Tuk Down (Far East)",          0x0051C052),
    BurnoutItem(21052083, "Golden City - Handle with Care (Far East)",  0x0051C053),
    BurnoutItem(21052084, "Golden City - Turn & Burn (Far East)",       0x0051C062),
    BurnoutItem(21052085, "Golden City - Crossing Crush (Far East)",    0x0051C065),
    BurnoutItem(21052086, "Golden City - Freeway Thunder (Far East)",   0x0051C066),
    BurnoutItem(21052087, "Golden City - Road to Ruin (Far East)",      0x0051C076),
    BurnoutItem(21052088, "Golden City - Trash Smash (Far East)",       0x0051C07A),
    BurnoutItem(21052089, "Golden City - Heavy Hitter (Far East)",      0x0051C08B),
    BurnoutItem(21052090, "Golden City - Eastern Block (Far East)",     0x0051C08F),
    BurnoutItem(21052091, "Golden City - Crash Fu (Far East)",          0x0051C09E),

    # Dockside
    BurnoutItem(21052092, "Dockside - Rock the Dock (Far East)",    0x0051C050),
    BurnoutItem(21052093, "Dockside - Exit the Dragon (Far East)",  0x0051C063),
    BurnoutItem(21052094, "Dockside - Reiko-chet (Far East)",       0x0051C078),
    BurnoutItem(21052095, "Dockside - Whirlwind (Far East)",        0x0051C07B),
    BurnoutItem(21052096, "Dockside - Look Both Ways (Far East)",   0x0051C08A),
    BurnoutItem(21052097, "Dockside - Buckle Up (Far East)",        0x0051C08D),
    BurnoutItem(21052098, "Dockside - The Crate Escape (Far East)", 0x0051C09F),
    BurnoutItem(21052099, "Dockside - Crashed Out (Far East)",      0x0051C0A3),
]

ALL_ITEMS_BY_ID = {}
for item in cars_list + races_list + crashes_list:
    ALL_ITEMS_BY_ID[item.ap_id] = item
