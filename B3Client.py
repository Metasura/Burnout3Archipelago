import asyncio
import sys
import threading
import time
from asyncio import run_coroutine_threadsafe
import ModuleUpdate
ModuleUpdate.update()
from Utils import  init_logging
from CommonClient import CommonContext, server_loop, gui_enabled, ClientCommandProcessor, logger, get_base_parser

try:
    from .pine import Pine
except ImportError:
    logger.error("PINE missing."); sys.exit(1)

from .items import ALL_ITEMS_BY_ID
from .locations import ALL_MEDALS_LIST, ALL_OTHERS_LIST, ALL_RACE_LIST, ALL_CRASH_LIST 

ALL_GOLD_IDS = {event.ap_id * 10 + 3 for event in ALL_MEDALS_LIST}
ALL_RACE_GOLD_IDS = {event.ap_id * 10 + 3 for event in ALL_RACE_LIST}
ALL_CRASH_GOLD_IDS = {event.ap_id * 10 + 3 for event in ALL_CRASH_LIST}

VAL_UNLOCKED = 0x01
VAL_LOCKED = 0x00
VAL_BRONZE, VAL_SILVER, VAL_GOLD = 0x01, 0x02, 0x03

class BT3CommandProcessor(ClientCommandProcessor):
    pass

class PS2Context(CommonContext):

    command_processor = BT3CommandProcessor

    def __init__(self, server_address, password):
        super().__init__(server_address, password)
        self.game = "Burnout 3"
        self.items_handling = 0b111
        self.pine = Pine()
        self.connected_to_pcsx2 = False
        self.keep_running = True
        self.last_deathlink = 0
        self.required_golds = 173
        self.gamemode = 0
        self.medal_type = 2
        self.victory_ids = set()

    def on_package(self, cmd: str, args: dict):
        super().on_package(cmd, args)
        if cmd == "Connected":
            if "slot_data" in args:
                slot_data = args["slot_data"]

                if "gameplay_mode" in slot_data and "req_golds" in slot_data:
                    self.gamemode = slot_data["gameplay_mode"]
                    self.required_golds = slot_data["req_golds"]
                    self.medal_type = slot_data.get("req_medal_type", 2)
                    offset = self.medal_type + 1

                    source_list = ALL_MEDALS_LIST
                    if self.gamemode == 1: source_list = ALL_RACE_LIST
                    elif self.gamemode == 2: source_list = ALL_CRASH_LIST

                    self.victory_ids = {event.ap_id * 10 + offset for event in source_list}

                    medal_name = ["Bronze", "Silver", "Gold"][self.medal_type]

                    mode_str = ""
                    if self.gamemode == 1: mode_str = "Race "
                    elif self.gamemode == 2: mode_str = "Crash "

                    logger.info(f"Goal : Obtain {self.required_golds} {mode_str}{medal_name} Medals.")


    def run_gui(self):
        from kvui import GameManager

        class PS2Manager(GameManager):
            logging_pairs = [("Client", "Archipelago")]
            base_title = "Archipelago Burnout 3 Client"

        self.ui = PS2Manager(self)
        self.ui_task = asyncio.create_task(self.ui.async_run(), name="ui")
    
    async def server_auth(self, password_requested: bool = False):
        if password_requested and not self.password:
            await super().server_auth(password_requested)
            return
        
        await self.get_username()
        await self.send_connect()

    async def get_username(self):
        if not self.auth:
            self.auth = self.username
            if not self.auth:
                logger.info('Enter slot name:')
                self.auth = await self.console_input()

    def event_invalid_slot(self):
        raise Exception('Invalid Slot; please verify that you have connected to the correct world.')

def try_connect_pine(ctx: PS2Context):
    if not ctx.connected_to_pcsx2:
        try:
            ctx.pine.read_int8(0x0051BFF7)
            if not ctx.connected_to_pcsx2:
                logger.info("[PINE] Connected to PCSX2 !")
                ctx.connected_to_pcsx2 = True
            return True
        except Exception:
            if ctx.connected_to_pcsx2:
                logger.warning("[PINE] Connexion lost...")
                ctx.connected_to_pcsx2 = False
            return False
    return True

def check_locations(ctx, loop_count):
    if loop_count % 3 != 0: return
    new_checks = []
    for event in ALL_MEDALS_LIST:
        try:
            medal_val = ctx.pine.read_int8(event.addr_check)
        except: continue
        if medal_val == 0xFF: continue
        loc_bronze = event.ap_id * 10 + 1
        loc_silver = event.ap_id * 10 + 2
        loc_gold   = event.ap_id * 10 + 3
        if medal_val >= VAL_BRONZE and loc_bronze not in ctx.locations_checked:
            new_checks.append(loc_bronze); #logger.info(f"[CHECK] Bronze: {event.name}")
            
        if medal_val >= VAL_SILVER and loc_silver not in ctx.locations_checked:
            new_checks.append(loc_silver); #logger.info(f"[CHECK] Silver: {event.name}")
            
        if medal_val >= VAL_GOLD and loc_gold not in ctx.locations_checked:
            new_checks.append(loc_gold); #logger.info(f"[CHECK] Gold: {event.name}")
    
    for other in ALL_OTHERS_LIST:
        try:
            other_val = ctx.pine.read_int8(other.addr_check)
        except: continue

        if other_val == 0x00: continue

        if other_val >= VAL_UNLOCKED and other.ap_id not in ctx.locations_checked:
            new_checks.append(other.ap_id)
            #logger.info(f"[CHECK] Découverte : {other.name}")

    if new_checks:
        ctx.locations_checked.update(new_checks)
        if ctx.loop:
            run_coroutine_threadsafe(ctx.send_msgs([{"cmd": "LocationChecks", "locations": new_checks}]), ctx.loop)

def enforce_state(ctx, loop_count):
    if loop_count % 2 != 0: return
    received_ids = set()
    for item in ctx.items_received:
        received_ids.add(item.item)
    for ap_id, game_item in ALL_ITEMS_BY_ID.items():
        if game_item.addr_unlock is None:
            continue

        target_value = VAL_UNLOCKED if ap_id in received_ids else VAL_LOCKED

        try:
            current_val = ctx.pine.read_int8(game_item.addr_unlock)            
            if target_value == VAL_LOCKED:
                if current_val != VAL_LOCKED:
                    ctx.pine.write_int8(game_item.addr_unlock, VAL_LOCKED)          
            elif target_value == VAL_UNLOCKED:
                if current_val == VAL_LOCKED: 
                    ctx.pine.write_int8(game_item.addr_unlock, VAL_UNLOCKED)
                    #logger.info(f"[UNLOCK] {game_item.name} unlocked !")
        except Exception:
            pass

def check_victory(ctx):
    if ctx.finished_game:
        return
    
    checked_targets = ctx.locations_checked.intersection(ctx.victory_ids)
    
    if len(checked_targets) >= ctx.required_golds:
        logger.info(f"Victory ! {len(checked_targets)} medals obtained (Req: {ctx.required_golds})")
        from NetUtils import ClientStatus
        run_coroutine_threadsafe(
            ctx.send_msgs([{"cmd": "StatusUpdate", "status": ClientStatus.CLIENT_GOAL}]),
            ctx.loop
        )
        ctx.finished_game = True

def pine_thread_loop(ctx: PS2Context):
    logger.info("--- PINE Thread Started ---")
    loop_count = 0
    
    while ctx.keep_running:
        try:
            if not try_connect_pine(ctx):
                time.sleep(2)
                continue
        except Exception:
            time.sleep(2)
            continue
        if ctx.slot is not None:
            enforce_state(ctx, loop_count)
            check_locations(ctx, loop_count)
            if loop_count % 3 == 0:
                check_victory(ctx)
        if loop_count % 10 == 0 and ctx.slot is not None:
            pass

        loop_count += 1
        time.sleep(0.5)

    #logger.info("--- PINE Thread stopped ---")

async def async_main(args):
    init_logging("Burnout3Client", exception_logger="Client")
    ctx = PS2Context(args.connect, args.password)
    ctx.server_task = asyncio.create_task(server_loop(ctx), name="server loop")

    if args.username:
        ctx.auth = args.username
        ctx.username = args.username
    
    ctx.loop = asyncio.get_running_loop()
    pine_thread = threading.Thread(target=pine_thread_loop, args=(ctx,), daemon=True)
    pine_thread.start()

    if gui_enabled:
        ctx.run_gui()
        logger.info("GUI Launched")
        await ctx.ui_task 
    else:
        await ctx.server_task
    ctx.keep_running = False

def main(connect=None, password=None):
    parser = get_base_parser()
    parser.add_argument("username", nargs="?", help="Player Name")
    args = parser.parse_args()

    if connect: 
        args.connect = connect
    if password:
        args.password = password

    if sys.platform == 'win32':
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    
    try:
        asyncio.run(async_main(args))
    except KeyboardInterrupt:
        pass
    except Exception as e:
        print(f"Fatal Error : {e}")
        input("Press Enter to continue ...")

if __name__ == '__main__':
    main()