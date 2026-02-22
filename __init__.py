from BaseClasses import Region, Location, Item, Entrance, Tutorial, ItemClassification
from worlds.AutoWorld import World, WebWorld
from worlds.LauncherComponents import Component, components, Type, icon_paths
from .b3options import Burnout3Options
from multiprocessing import Process

from .items import cars_list, races_list, crashes_list
from .locations import signature_list, headline_list, medals_races_list, medals_crashes_list

GAME_NAME = "Burnout 3"
BASE_ID = 21050000

OFFSET_FILLER = 5000 

RACE_EVENT_NAMES = [r.name for r in races_list]
CRASH_EVENT_NAMES = [c.name for c in crashes_list]
ALL_SIGNATURE_NAMES = [s.name for s in signature_list]
ALL_HEADLINE_NAMES = [h.name for h in headline_list]
ALL_EVENT_NAMES = RACE_EVENT_NAMES + CRASH_EVENT_NAMES + ALL_SIGNATURE_NAMES + ALL_HEADLINE_NAMES
ALL_CAR_NAMES = [c.name for c in cars_list]


CARS_BY_CLASS = {
    "Compact": ["Compact Type 1", "Compact Type 2", "Compact Type 3", "Tuned Compact", "Modified Compact", "Custom Compact", "Assassin Compact", "Compact Prototype", "Compact DX", "Dominator Compact"],
    "Muscle":  ["Muscle Type 1", "Muscle Type 2", "Muscle Type 3", "Tuned Muscle", "Modified Muscle", "Custom Muscle", "Assassin Muscle", "Muscle Prototype", "Muscle DX", "Dominator Muscle"],
    "Coupe":   ["Coupe Type 1", "Coupe Type 2", "Coupe Type 3", "Tuned Coupe", "Modified Coupe", "Custom Coupe", "Assassin Coupe", "Coupe Prototype", "Coupe DX", "Dominator Coupe"],
    "Sports":  ["Sports Type 1", "Sports Type 2", "Sports Type 3", "Tuned Sports", "Modified Sports", "Custom Sports", "Assassin Sports", "Sports Prototype", "Sports DX", "Dominator Sports"],
    "Super":   ["Super Type 1", "Super Type 2", "Super Type 3", "Tuned Super", "Modified Super", "Custom Super", "Assassin Super", "Super Prototype", "Super DX", "Dominator Super"],
    "Special": [] 
}

EVENT_CAR_CLASSES = {
    "Silver Lake - Race (USA)": "Compact",
    "Silver Lake - Compact GP (USA)": "Compact",
    "Silver Lake - Eliminator (USA)": "Muscle",
    "Silver Lake - Special Event (USA)": "Special",
    "Lakeside Getaway - Face-Off 1 (USA)": "Compact",
    "Lakeside Getaway - Race (USA)": "Muscle",
    "Lakeside Getaway - Face-Off 2 (USA)": "Muscle",
    "Lakeside Getaway - Special Event (USA)": "Special",
    "Waterfront - Burning Lap (USA)": "Special",
    "Waterfront - Face-Off (USA)": "Compact",
    "Waterfront - Muscle GP (USA)": "Muscle",
    "Waterfront - Preview Lap (USA)": "Special",
    "Mountain Parkway - Face-Off 1 (USA)": "Muscle",
    "Mountain Parkway - Road Rage (USA)": "Muscle",
    "Mountain Parkway - Face-Off 2 (USA)": "Muscle",
    "Mountain Parkway - Special Event (USA)": "Special",
    "Kings Of The Road - Face-Off (USA)": "Compact",
    "Kings Of The Road - Race (USA)": "Special",
    "Kings Of The Road - Gold Medal GP (USA)": "Special",
    "Downtown - Preview Lap 1 (USA)": "Special",
    "Downtown - Road Rage 1 (USA)": "Compact",
    "Downtown - Race 1 (USA)": "Special",
    "Downtown - Race 2 (USA)": "Muscle",
    "Downtown - Road Rage 2 (USA)": "Muscle",
    "Downtown - Preview Lap 2 (USA)": "Special",
    "Winter City - Race (Europe)": "Coupe",
    "Winter City - Special Event (Europe)": "Special",
    "Winter City - Eliminator (Europe)": "Coupe",
    "Frozen Peak - Face-Off 1 (Europe)": "Coupe",
    "Frozen Peak - Face-Off 2 (Europe)": "Sports",
    "Alpine - Special Event (Europe)": "Special",
    "Alpine - Road Rage (Europe)": "Coupe",
    "Alpine - Race (Europe)": "Special",
    "Alpine - Face-Off (Europe)": "Sports",
    "Continental Run - Face-Off 1 (Europe)": "Coupe",
    "Continental Run - Race 1 (Europe)": "Sports",
    "Continental Run - Race 2 (Europe)": "Special",
    "Continental Run - Special Event (Europe)": "Special",
    "Continental Run - Face-Off 2 (Europe)": "Sports",
    "Alpine Expressway - Sports GP (Europe)": "Sports",
    "Alpine Expressway - Race (Europe)": "Coupe",
    "Riviera - Road Rage 1 (Europe)": "Coupe",
    "Riviera - Burning Lap (Europe)": "Special",
    "Riviera - Eliminator (Europe)": "Sports",
    "Riviera - Road Rage 2 (Europe)": "Sports",
    "Coastal Dream - Preview Lap (Europe)": "Special",
    "Coastal Dream - Race (Europe)": "Sports",
    "Coastal Dream - Road Rage 1 (Europe)": "Sports",
    "Coastal Dream - Road Rage 2 (Europe)": "Sports",
    "Vineyard - Special Event (Europe)": "Special",
    "Vineyard - Road Rage 1 (Europe)": "Coupe",
    "Vineyard - Face-Off (Europe)": "Coupe",
    "Vineyard - Coupe GP (Europe)": "Coupe",
    "Vineyard - Road Rage 2 (Europe)": "Sports",
    "Vineyard - Eliminator (Europe)": "Sports",
    "Island Paradise - Special Event (Far East)": "Special",
    "Island Paradise - Race (Far East)": "Super",
    "Island Paradise - Face-Off (Far East)": "Super",
    "Island Paradise - Eliminator (Far East)": "Super",
    "Tropical Drive - Preview Lap (Far East)": "Special",
    "Tropical Drive - Race 1 (Far East)": "Super",
    "Tropical Drive - Race 2 (Far East)": "Super",
    "Tropical Drive - Road Rage (Far East)": "Super",
    "Tropical Drive - Super GP (Far East)": "Super",
    "Golden City - Special Event (Far East)": "Special",
    "Golden City - Road Rage (Far East)": "Super",
    "Golden City - Race (Far East)": "Super",
    "Golden City - Face-Off (Far East)": "Super",
    "Dockside - Special Event (Far East)": "Special",
    "Dockside - Eliminator (Far East)": "Super",
    "Dockside - Road Rage 1 (Far East)": "Super",
    "Dockside - Face-Off (Far East)": "Super",
    "Dockside - Road Rage 2 (Far East)": "Super",
}

SIGNATURE_BY_RACE = {
    "Gone Fishin'": ["Silver Lake - Race (USA)", "Silver Lake - Compact GP (USA)", "Silver Lake - Eliminator (USA)", "Lakeside Getaway - Face-Off 1 (USA)", "Lakeside Getaway - Race (USA)", "Lakeside Getaway - Face-Off 2 (USA)", "Kings Of The Road - Face-Off (USA)", "Kings Of The Road - Race (USA)"], 
    "Home Wrecker": ["Silver Lake - Race (USA)", "Silver Lake - Compact GP (USA)", "Silver Lake - Eliminator (USA)", "Lakeside Getaway - Face-Off 1 (USA)", "Lakeside Getaway - Race (USA)", "Lakeside Getaway - Face-Off 2 (USA)"],
    "Pillar Driller": ["Downtown - Road Rage 1 (USA)", "Downtown - Race 1 (USA)", "Downtown - Race 2 (USA)", "Downtown - Road Rage 2 (USA)", "Kings Of The Road - Face-Off (USA)", "Kings Of The Road - Race (USA)", "Mountain Parkway - Face-Off 2 (USA)"],
    "Hit the Split": ["Downtown - Road Rage 1 (USA)", "Downtown - Race 1 (USA)", "Downtown - Race 2 (USA)", "Downtown - Road Rage 2 (USA)", "Mountain Parkway - Road Rage (USA)"],
    "Tram Ram": ["Waterfront - Face-Off (USA)", "Waterfront - Muscle GP (USA)", "Mountain Parkway - Face-Off 1 (USA)", "Mountain Parkway - Road Rage (USA)"],
    "Truck Torpedo": ["Downtown - Road Rage 1 (USA)", "Downtown - Race 1 (USA)", "Downtown - Race 2 (USA)", "Downtown - Road Rage 2 (USA)", "Waterfront - Face-Off (USA)", "Waterfront - Muscle GP (USA)", "Silver Lake - Race (USA)", "Silver Lake - Compact GP (USA)", "Silver Lake - Eliminator (USA)"],
    "Euro Tram Ram": ["Winter City - Race (Europe)", "Winter City - Eliminator (Europe)"],
    "Snowed Under": ["Winter City - Race (Europe)", "Winter City - Eliminator (Europe)", "Alpine - Road Rage (Europe)", "Alpine - Race (Europe)", "Alpine - Face-Off (Europe)"],
    "Avalanche!": ["Alpine - Road Rage (Europe)", "Alpine - Race (Europe)", "Alpine - Face-Off (Europe)", "Alpine Expressway - Sports GP (Europe)", "Alpine Expressway - Race (Europe)", "Frozen Peak - Face-Off 1 (Europe)", "Frozen Peak - Face-Off 2 (Europe)"],
    "Paid the Price!": ["Alpine - Road Rage (Europe)", "Alpine - Race (Europe)", "Alpine - Face-Off (Europe)", "Alpine Expressway - Sports GP (Europe)", "Alpine Expressway - Race (Europe)", "Frozen Peak - Face-Off 1 (Europe)", "Frozen Peak - Face-Off 2 (Europe)"],
    "Riviera Roustabout": ["Riviera - Road Rage 1 (Europe)", "Riviera - Eliminator (Europe)", "Riviera - Road Rage 2 (Europe)", "Coastal Dream - Race (Europe)", "Coastal Dream - Road Rage 1 (Europe)", "Coastal Dream - Road Rage 2 (Europe)", "Alpine Expressway - Sports GP (Europe)", "Alpine Expressway - Race (Europe)"],
    "Berth Trauma": ["Riviera - Road Rage 1 (Europe)", "Riviera - Eliminator (Europe)", "Riviera - Road Rage 2 (Europe)", "Coastal Dream - Race (Europe)", "Coastal Dream - Road Rage 1 (Europe)", "Coastal Dream - Road Rage 2 (Europe)"],
    "Gate Crasher": ["Vineyard - Road Rage 1 (Europe)", "Vineyard - Face-Off (Europe)", "Vineyard - Coupe GP (Europe)", "Vineyard - Road Rage 2 (Europe)", "Vineyard - Eliminator (Europe)", "Coastal Dream - Race (Europe)", "Coastal Dream - Road Rage 1 (Europe)", "Coastal Dream - Road Rage 2 (Europe)", "Continental Run - Face-Off 1 (Europe)", "Continental Run - Race 1 (Europe)", "Continental Run - Race 2 (Europe)", "Continental Run - Face-Off 2 (Europe)"],
    "Grapes of Wrath": ["Vineyard - Road Rage 1 (Europe)", "Vineyard - Face-Off (Europe)", "Vineyard - Coupe GP (Europe)", "Vineyard - Road Rage 2 (Europe)", "Vineyard - Eliminator (Europe)"],
    "Market-Stalled": ["Golden City - Road Rage (Far East)", "Golden City - Race (Far East)", "Golden City - Face-Off (Far East)", "Tropical Drive - Race 1 (Far East)", "Tropical Drive - Race 2 (Far East)", "Tropical Drive - Road Rage (Far East)", "Tropical Drive - Super GP (Far East)"],
    "Tuk-Down": ["Golden City - Road Rage (Far East)", "Golden City - Race (Far East)", "Golden City - Face-Off (Far East)", "Island Paradise - Race (Far East)", "Island Paradise - Face-Off (Far East)", "Island Paradise - Eliminator (Far East)", "Dockside - Eliminator (Far East)", "Dockside - Road Rage 1 (Far East)", "Dockside - Face-Off (Far East)", "Dockside - Road Rage 2 (Far East)"],
    "Tunnel of Shove":["Dockside - Eliminator (Far East)", "Dockside - Road Rage 1 (Far East)", "Dockside - Face-Off (Far East)", "Dockside - Road Rage 2 (Far East)"],
    "Ship Wreck":["Dockside - Eliminator (Far East)", "Dockside - Road Rage 1 (Far East)", "Dockside - Face-Off (Far East)", "Dockside - Road Rage 2 (Far East)"],
    "Rumble in the Jungle":["Island Paradise - Race (Far East)", "Island Paradise - Face-Off (Far East)", "Island Paradise - Eliminator (Far East)", "Tropical Drive - Race 1 (Far East)", "Tropical Drive - Race 2 (Far East)", "Tropical Drive - Road Rage (Far East)", "Tropical Drive - Super GP (Far East)"],
    "Catch The Tour Bus":["Island Paradise - Race (Far East)", "Island Paradise - Face-Off (Far East)", "Island Paradise - Eliminator (Far East)", "Tropical Drive - Race 1 (Far East)", "Tropical Drive - Race 2 (Far East)", "Tropical Drive - Road Rage (Far East)", "Tropical Drive - Super GP (Far East)"]
}

HEADLINE_BY_CRASH = {
    "Alpine Smash!": ["Alpine - Chilly Crash (Europe)", "Alpine - Corkscrewed (Europe)", "Alpine - Exact Change (Europe)", "Alpine - Highway to Hell (Europe)", "Alpine - Jump the Toll (Europe)", "Alpine - Lanes Lunacy (Europe)", "Alpine - Snow Plough (Europe)"],
    "Dockside Ridge Ruin!": ["Dockside - Buckle Up (Far East)", "Dockside - Crashed Out (Far East)", "Dockside - Look Both Ways (Far East)", "Dockside - Reiko-chet (Far East)", "Dockside - The Crate Escape (Far East)", "Dockside - Whirlwind (Far East)"],
    "Downtown Demolition!": ["Downtown - Air Rage (USA)", "Downtown - Bus Blockade (USA)", "Downtown - Dead End (USA)", "Downtown - Grid Locked (USA)", "Downtown - Hate to be Late (USA)", "Downtown - Hit and Run (USA)", "Downtown - Hold Tight (USA)", "Downtown - Traffic Jammed (USA)", "Downtown - Wrecks City (USA)"],
    "Golden City Madness!": ["Golden City - Crash Fu (Far East)", "Golden City - Crossing Crush (Far East)", "Golden City - Eastern Block (Far East)", "Golden City - Freeway Thunder (Far East)", "Golden City - Handle with Care (Far East)", "Golden City - Heavy Hitter (Far East)", "Golden City - Road to Ruin (Far East)", "Golden City - Trash Smash (Far East)", "Golden City - Turn & Burn (Far East)"],
    "Trouble in Paradise!": ["Island Paradise - Airstrike (Far East)", "Island Paradise - Drive Angry (Far East)", "Island Paradise - Jungle Rumble (Far East)", "Island Paradise - Lost Luggage (Far East)", "Island Paradise - Pure Scores (Far East)", "Island Paradise - Steel Tsunami (Far East)", "Island Paradise - Tourist Trap (Far East)", "Island Paradise - Tropical Storm (Far East)", "Island Paradise - Uphill Struggle (Far East)"],
    "Riviera Wreck!": ["Riviera - Break the Bank (Europe)", "Riviera - Cliff Hanger (Europe)", "Riviera - Go for Broke (Europe)", "Riviera - High Roller (Europe)", "Riviera - Jumping Jam (Europe)", "Riviera - Riviera Rampage (Europe)", "Riviera - Ship Wrecked (Europe)", "Riviera - Spin the Wheel (Europe)"],
    "Silver Lake Lunacy!": ["Silver Lake - 3 Ways to Fly (USA)", "Silver Lake - Bridge Too Far (USA)", "Silver Lake - Fear Factor (USA)", "Silver Lake - Out of Control (USA)", "Silver Lake - Pick Up the Pieces (USA)", "Silver Lake - Showdown (USA)", "Silver Lake - Ticket to Collide (USA)"],
    "Grape Harvests Crushed!": ["Vineyard - Bale Out (Europe)", "Vineyard - Country Chaos (Europe)", "Vineyard - Crash au Van (Europe)", "Vineyard - Field of Screams (Europe)", "Vineyard - Gate Crasher (Europe)", "Vineyard - Grape Fear (Europe)", "Vineyard - Haul A$$ (Europe)", "Vineyard - Medieval Mash (Europe)"],
    "Bayside Blitz!": ["Waterfront - Bay-side Blitz (USA)", "Waterfront - Danger Zone (USA)", "Waterfront - Falling Down (USA)", "Waterfront - Leap of Faith (USA)", "Waterfront - Look then Leap (USA)", "Waterfront - Sunshine Smash (USA)", "Waterfront - T-Boned (USA)", "Waterfront - Tram-Pulled (USA)"],
    "Winter City Frozen!": ["Winter City - Cool for Crash (Europe)", "Winter City - Corner Chaos (Europe)", "Winter City - Crash Landing (Europe)", "Winter City - Market Crash (Europe)", "Winter City - On Rampage (Europe)", "Winter City - Riverside Wreck (Europe)", "Winter City - Run for the Bus (Europe)", "Winter City - Snow Joke (Europe)", "Winter City - Winter Wipe-out (Europe)"]
}

def run_mapping():
    item_table = {}
    loc_table = {}
    
    all_medals = medals_races_list + medals_crashes_list
    
    for medals in all_medals:
        if "Face-Off" not in medals.name:
            loc_table[f"{medals.name} - Bronze"] = medals.ap_id * 10 + 1
            loc_table[f"{medals.name} - Silver"] = medals.ap_id * 10 + 2
            loc_table[f"{medals.name} - Gold"]   = medals.ap_id * 10 + 3
        else:
            loc_table[f"{medals.name} - Gold"]   = medals.ap_id * 10 + 3

    all_events = races_list + crashes_list

    for event in all_events:
        item_name = f"Unlock {event.name}"
        item_table[item_name] = event.ap_id

    for car in cars_list:
        item_table[car.name] = car.ap_id

    for signature in signature_list:
        loc_table[f"Signature Takedown - {signature.name}"] = signature.ap_id

    for headline in headline_list:
        loc_table[f"Crash Headline - {headline.name}"] = headline.ap_id

    item_table["Bonus Points"] = 21059999
        
    return item_table, loc_table

full_item_table, full_loc_table = run_mapping()

def run_client():
    from .B3Client import main
    p = Process(target=main)
    p.start()


components.append(Component("Burnout 3 Client", func=run_client, component_type=Type.CLIENT))


class Burnout3Web(WebWorld):
    theme = "ocean"

class Burnout3Item(Item):
    game = GAME_NAME

class Burnout3Location(Location):
    game = GAME_NAME

class Burnout3World(World):
    game = GAME_NAME
    web = Burnout3Web()

    options_dataclass = Burnout3Options
    options = Burnout3Options
    
    item_name_to_id = full_item_table
    location_name_to_id = full_loc_table

    def __init__(self, *args, **kwargs):
        super(Burnout3World, self).__init__(*args, **kwargs)
        self.actual_event_list = []
        self.medal_suffix = "Gold"

    def get_filler_item_name(self) -> str:
        return "Bonus Points"

    def get_active_events(self):
        mode = self.options.gameplay_mode.value
        if mode == 1: return RACE_EVENT_NAMES
        elif mode == 2: return CRASH_EVENT_NAMES
        else: return RACE_EVENT_NAMES + CRASH_EVENT_NAMES

    def generate_early(self):
        mode = self.options.gameplay_mode.value
        req_medals_count = self.options.required_medals.value
        gen_events_count = self.options.generated_events.value
        medal_type_opt = self.options.medal_type.value

        if medal_type_opt == 0: self.medal_suffix = "Bronze"
        elif medal_type_opt == 1: self.medal_suffix = "Silver"
        else: self.medal_suffix = "Gold"

        max_events_in_mode = 173
        if mode == 1: max_events_in_mode = 73
        elif mode == 2: max_events_in_mode = 100

        self.final_gen_count = min(gen_events_count, max_events_in_mode)
        self.final_req_count = min(req_medals_count, self.final_gen_count)

        if self.final_req_count != req_medals_count or self.final_gen_count != gen_events_count:
            import logging
            logging.info(f"[Burnout 3] Adjusted counts: Generated {self.final_gen_count} (requested {gen_events_count}), Required {self.final_req_count} (requested {req_medals_count})")

        full_pool = self.get_active_events()

        if len(full_pool) > self.final_gen_count:
            self.actual_event_list = self.multiworld.random.sample(full_pool, self.final_gen_count)
        else:
            self.actual_event_list = full_pool
        
        self.progression_cars = []
        for car_class, car_list in CARS_BY_CLASS.items():
            if car_class != "Special" and car_list:
                self.progression_cars.append(self.multiworld.random.choice(car_list))

    def create_regions(self):
        menu_region = Region("Menu", self.player, self.multiworld)
        self.multiworld.regions.append(menu_region)

        signatures_on = self.options.enable_signatures.value
        headlines_on = self.options.enable_headlines.value
        mode = self.options.gameplay_mode.value

        for name in ALL_EVENT_NAMES:
            if name in ALL_SIGNATURE_NAMES:
                if signatures_on and mode in [0, 1] :  
                    loc_name = f"Signature Takedown - {name}"
                    if loc_name in self.location_name_to_id:
                        loc = Burnout3Location(self.player, loc_name, self.location_name_to_id[loc_name], menu_region)
                        menu_region.locations.append(loc)
        
            elif name in ALL_HEADLINE_NAMES:
                if headlines_on and mode in [0, 2]: 
                    loc_name = f"Crash Headline - {name}"
                    if loc_name in self.location_name_to_id:
                        loc = Burnout3Location(self.player, loc_name, self.location_name_to_id[loc_name], menu_region)
                        menu_region.locations.append(loc)
            
        for name in self.actual_event_list:
            unlock_item = f"Unlock {name}"
            for type_name in ["Bronze", "Silver", "Gold"]:
                loc_name = f"{name} - {type_name}"
                if loc_name in self.location_name_to_id:
                    loc = Burnout3Location(self.player, loc_name, self.location_name_to_id[loc_name], menu_region)
                    loc.access_rule = lambda state, n=unlock_item: state.has(n, self.player)
                    menu_region.locations.append(loc)
        
        victory_loc = Burnout3Location(self.player, "Victory", None, menu_region)
        victory_loc.place_locked_item(self.create_item("Victory"))
        menu_region.locations.append(victory_loc)   
        menu_region.add_exits([])

    def create_items(self):
        item_pool = []
        precollected_items = self.multiworld.precollected_items[self.player]
        precollected_names = [item.name for item in precollected_items]
        mode = self.options.gameplay_mode.value
        active_events = self.actual_event_list

        has_valid_combo = False
        for item_name in precollected_names:
            if item_name.startswith("Unlock "):
                event_name = item_name.replace("Unlock ", "")
                required_class = EVENT_CAR_CLASSES.get(event_name)

                if required_class is None or required_class == "Special":
                    has_valid_combo = True
                    break

                allowed_cars = CARS_BY_CLASS.get(required_class, [])
                for car in allowed_cars:
                    if car in precollected_names:
                        has_valid_combo = True
                        break
            if has_valid_combo: break

        if not has_valid_combo:
            
            
            available_special = [e for e in active_events if e in RACE_EVENT_NAMES and EVENT_CAR_CLASSES.get(e) == "Special" and "GP" not in e]
            available_races = [e for e in active_events if e in RACE_EVENT_NAMES and EVENT_CAR_CLASSES.get(e) != "Special" and "GP" not in e]
            available_crashes = [e for e in active_events if e in CRASH_EVENT_NAMES]
            
            events_to_unlock = []

            def get_safe_start(preferred_list, fallback_list):
                if preferred_list:
                    return self.multiworld.random.choice(preferred_list)
                elif fallback_list:
                    return self.multiworld.random.choice(fallback_list)
                else:
                    return self.multiworld.random.choice(active_events)

            if mode == 1:
                r1 = get_safe_start(available_races, [e for e in active_events if e in RACE_EVENT_NAMES])
                races_sans_r1 = [e for e in available_races if e != r1]
                r2 = get_safe_start(races_sans_r1, [e for e in active_events if e in RACE_EVENT_NAMES and e != r1])
                events_to_unlock = [r1, r2]
            
            elif mode == 2: 
                c1 = get_safe_start(available_crashes, [e for e in active_events if e in CRASH_EVENT_NAMES])
                crash_sans_c1 = [e for e in available_crashes if e != c1]
                c2 = get_safe_start(crash_sans_c1, [e for e in active_events if e in CRASH_EVENT_NAMES and e != c1])
                events_to_unlock = [c1, c2]
            
            else:
                r = get_safe_start(available_races, [e for e in active_events if e in RACE_EVENT_NAMES])
                c = get_safe_start(available_crashes, [e for e in active_events if e in CRASH_EVENT_NAMES])
                events_to_unlock = [r, c]

            for event_name in events_to_unlock:
                unlock_item_name = f"Unlock {event_name}"
                if unlock_item_name not in precollected_names:
                    item_evt = self.create_item(unlock_item_name)
                    self.multiworld.push_precollected(item_evt)
                    precollected_names.append(unlock_item_name)
                    
                required_class = EVENT_CAR_CLASSES.get(event_name)
                
                if required_class and required_class != "Special":
                    possible_cars = CARS_BY_CLASS.get(required_class, [])
                    if possible_cars:
                        has_class_car = any(c in precollected_names for c in possible_cars)
                        
                        if not has_class_car:
                            start_car = self.multiworld.random.choice(possible_cars)
                            item_car = self.create_item(start_car)
                            self.multiworld.push_precollected(item_car)
                            precollected_names.append(start_car)

        for name in active_events:
            full_name = f"Unlock {name}"
            if full_name not in precollected_names:
                item_pool.append(self.create_item(full_name))

        if mode in [0, 1]:
            cars_to_add = [name for name in ALL_CAR_NAMES if name not in precollected_names]
            prog_cars = [c for c in cars_to_add if hasattr(self, "progression_cars") and c in self.progression_cars]
            useful_cars = [c for c in cars_to_add if c not in prog_cars]

            for car in prog_cars:
                item_pool.append(self.create_item(car))

            for name in ALL_CAR_NAMES:
                if name not in precollected_names:
                    item_pool.append(self.create_item(name))

            unfilled_locs = len(self.multiworld.get_unfilled_locations(self.player))
            space_left = unfilled_locs - len(item_pool)

            self.multiworld.random.shuffle(useful_cars)
            for car in useful_cars:
                if space_left > 0:
                    item_pool.append(self.create_item(car))
                    space_left -= 1
        
        unfilled_locs = len(self.multiworld.get_unfilled_locations(self.player))
        needed = unfilled_locs - len(item_pool)        

        if needed > 0:
            for _ in range(needed):
                item_pool.append(self.create_item(self.get_filler_item_name()))
        
        self.multiworld.itempool += item_pool
    
    def fill_slot_data(self):
        req_sigs = self.options.enable_signatures.value if hasattr(self.options, 'enable_signatures') else False
        req_heads = self.options.enable_headlines.value if hasattr(self.options, 'enable_headlines') else False

        return {
            "gameplay_mode": self.options.gameplay_mode.value,
            "req_golds": self.final_req_count,
            "req_medal_type": self.options.medal_type.value, 
            "req_sigs": req_sigs,
            "req_heads": req_heads
        }

    def create_item(self, name: str) -> Item:
        if name not in self.item_name_to_id:
            return self.create_item("Bonus Points")

        item_id = self.item_name_to_id[name]
        player = self.player
        mode = self.options.gameplay_mode.value

        if name.startswith("Unlock "):
            event_name = name.replace("Unlock ", "")
            
            if mode == 1:
                if event_name in RACE_EVENT_NAMES:
                    classification = ItemClassification.progression
                else:
                    classification = ItemClassification.useful
                    
            elif mode == 2: 
                if event_name in CRASH_EVENT_NAMES:
                    classification = ItemClassification.progression
                else:
                    classification = ItemClassification.useful
            
            else:
                classification = ItemClassification.progression
        
        elif name in ALL_CAR_NAMES:

            if hasattr(self, "progression_cars") and name in self.progression_cars:
                classification = ItemClassification.progression
            else:
                classification = ItemClassification.useful
        
        elif name == "Bonus Points":
            classification = ItemClassification.filler
        else:
            classification = ItemClassification.filler

        return Burnout3Item(name, classification, item_id, player)


    def set_rules(self):
        def has_car_class(state, car_class):
            if not car_class or car_class == "Special": 
                return True
            
            allowed_cars = CARS_BY_CLASS.get(car_class, [])
            if not allowed_cars: 
                return True 
            
            return any(state.has(car, self.player) for car in allowed_cars)

        def can_access_event(state, event_name):
            if not state.has(f"Unlock {event_name}", self.player):
                return False
            
            required_class = EVENT_CAR_CLASSES.get(event_name)
            return has_car_class(state, required_class)

        for event_name in self.actual_event_list:
            def event_rule(state, e_name=event_name): 
                return can_access_event(state, e_name)

            for medal in ["Bronze", "Silver", "Gold"]:
                loc_name = f"{event_name} - {medal}"
                try:
                    loc = self.multiworld.get_location(loc_name, self.player)
                    loc.access_rule = event_rule
                except KeyError:
                    pass
        
        signatures_on = self.options.enable_signatures.value
        headlines_on = self.options.enable_headlines.value

        if signatures_on:
            for signature_name, allowed_events in SIGNATURE_BY_RACE.items():
                loc_name = f"Signature Takedown - {signature_name}"
                try:
                    loc = self.multiworld.get_location(loc_name, self.player)
                    loc.access_rule = lambda state, evts=allowed_events: any(can_access_event(state, evt) for evt in evts)
                except KeyError:
                    pass

        if headlines_on: 
            for headline_name, allowed_events in HEADLINE_BY_CRASH.items():
                loc_name = f"Crash Headline - {headline_name}"
                try:
                    loc = self.multiworld.get_location(loc_name, self.player)
                    loc.access_rule = lambda state, evts=allowed_events: any(can_access_event(state, evt) for evt in evts)
                except KeyError:
                    pass

        def victory_rule(state):
            for name in self.actual_event_list:
                if name in ALL_SIGNATURE_NAMES or name in ALL_HEADLINE_NAMES:
                    continue
                
                loc_name = f"{name} - {self.medal_suffix}"
                try:
                    loc = self.multiworld.get_location(loc_name, self.player)
                    if not loc.can_reach(state):
                        return False
                except KeyError:
                    continue
            return True

        self.multiworld.completion_condition[self.player] = victory_rule