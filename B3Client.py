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
    def _cmd_showmedals(self):
        """Show medal progression."""
        
        if not self.ctx.server_task:
            logger.info("You are not connected to the server.")
            return

        if not hasattr(self.ctx, 'victory_ids') or not self.ctx.victory_ids:
            logger.info("Goal not defined ! Please wait until sync is done.")
            return

        server_checked_set = set(self.ctx.checked_locations)
        obtained = len(server_checked_set.intersection(self.ctx.victory_ids))
        
        required = getattr(self.ctx, 'required_golds', 173)
        
        medal_names = ["Bronze", "Silver", "Gold"]
        medal_str = medal_names[self.ctx.medal_type] if hasattr(self.ctx, 'medal_type') else "Gold"
        
        mode_str = ""
        if getattr(self.ctx, 'gamemode', 0) == 1: mode_str = " (Races only)"
        elif getattr(self.ctx, 'gamemode', 0) == 2: mode_str = " (Crashs only)"

        logger.info("--- Progress ---")
        logger.info(f"{medal_str} medals obained : {obtained} / {required}{mode_str}")
        
        if obtained <= required:
            logger.info(f"You still need {required - obtained} medals.")
        else:
            pass
       
    
    def _cmd_deathlink(self):
        """Enable or disable DeathLinks."""
        self.ctx.death_link_enabled = not getattr(self.ctx, "death_link_enabled", False)
        
        if self.ctx.death_link_enabled:
            self.ctx.tags.add("DeathLink")
            logger.info("DeathLink enabled !")
        else:
            self.ctx.tags.discard("DeathLink")
            logger.info("DeathLink disabled !")
            
        run_coroutine_threadsafe(
            self.ctx.send_msgs([{"cmd": "ConnectUpdate", "tags": list(self.ctx.tags)}]),
            self.ctx.loop
        )

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

                self.death_link_enabled = bool(slot_data.get("death_link", 0))

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
                
                
                if getattr(self, "death_link_enabled", False):
                    self.tags.add("DeathLink")
                    from asyncio import run_coroutine_threadsafe
                    run_coroutine_threadsafe(
                        self.send_msgs([{"cmd": "ConnectUpdate", "tags": list(self.tags)}]),
                        self.loop
                    )
                
        elif cmd == "Bounced":
            tags = args.get("tags", [])
            if "DeathLink" in tags:
                self.on_deathlink(args.get("data", {}))
    
    def on_deathlink(self, data: dict):
        if not getattr(self, "death_link_enabled", False):
            return

        source = data.get("source", "An other player")

        if source == self.username:
            return
    
        try:
            self.pine.write_int8(0x00197000, 1)
        except Exception as e:
            logger.error(f"PINE ERROR : {e}")

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

def update_dynamic_values(ctx: PS2Context):
    if not ctx.connected_to_pcsx2:
        return

    try:
        in_game = ctx.pine.read_int8(0x01D6E204)
        if in_game != 0:
            return

        cursor_pos = ctx.pine.read_int8(0x01E895E8)
        if cursor_pos != 0:
            return

        etat_serveur = "CONNECTED" if ctx.server_task else "DISCONNECTED"
        
        server_checked_set = set(ctx.checked_locations)
        obtained = len(server_checked_set.intersection(ctx.victory_ids)) if ctx.victory_ids else 0
        required = getattr(ctx, 'required_golds', 173)
        val_obtained = f"{obtained}/{required}"
        
        medal_names = ["BRONZE", "SILVER", "GOLD"] 
        current_medal_idx = getattr(ctx, 'medal_type', 2) 
        val_medal = medal_names[current_medal_idx] if current_medal_idx < len(medal_names) else "GOLD"
        mode_value = getattr(ctx, 'gameplay_mode', 0)
        
        if mode_value == 1:
            gamemode = 'RACE'
        elif mode_value == 2:
            gamemode = 'CRASH'
        else:
            gamemode = 'ALL MEDALS'
        
        
        deathlink_status = "ON" if 'DeathLink' in ctx.tags else "OFF"

        def write_utf16(address, text):
            bytes_to_write = (text + '\0').encode('utf-16le')
            for i, b in enumerate(bytes_to_write):
                ctx.pine.write_int8(address + i, b)

        write_utf16(0x01E94F4C, etat_serveur)    
        write_utf16(0x01E94F6C, val_obtained)    
        write_utf16(0x01E94F8C, val_medal)       
        write_utf16(0x01E94FAC, gamemode)        
        write_utf16(0x01E94FCC, deathlink_status)

    except Exception:
        pass     

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
            new_checks.append(loc_bronze); 
            
        if medal_val >= VAL_SILVER and loc_silver not in ctx.locations_checked:
            new_checks.append(loc_silver); 
            
        if medal_val >= VAL_GOLD and loc_gold not in ctx.locations_checked:
            new_checks.append(loc_gold); 
    
    for other in ALL_OTHERS_LIST:
        try:
            other_val = ctx.pine.read_int8(other.addr_check)
        except: continue

        if other_val == 0x00: continue

        if other_val >= VAL_UNLOCKED and other.ap_id not in ctx.locations_checked:
            new_checks.append(other.ap_id)

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
    
    checked_targets = set(ctx.checked_locations).intersection(ctx.victory_ids)
    
    if len(checked_targets) >= ctx.required_golds:
        logger.info(f"Victory ! {len(checked_targets)} medals obtained (Req: {ctx.required_golds})")
        from NetUtils import ClientStatus
        run_coroutine_threadsafe(
            ctx.send_msgs([{"cmd": "StatusUpdate", "status": ClientStatus.CLIENT_GOAL}]),
            ctx.loop
        )
        ctx.finished_game = True


def check_death(ctx: PS2Context):
    if not getattr(ctx, "death_link_enabled", False):
        return
        
    try:
        is_crashing = ctx.pine.read_int8(0x0064EC9A) 
    except Exception:
        return

    if is_crashing == 1 and getattr(ctx, "last_crash_state", 0) == 0:
        
        current_time = time.time()
        if current_time - getattr(ctx, "last_deathlink_time", 0) > 5.0:
            
            message = {
                "time": current_time,
                "cause": "crashed.",
                "source": ctx.username,
            }
            
            from asyncio import run_coroutine_threadsafe
            run_coroutine_threadsafe(
                ctx.send_msgs([{"cmd": "Bounce", "tags": ["DeathLink"], "data": message}]),
                ctx.loop
            )
            
            ctx.last_deathlink_time = current_time
            
    ctx.last_crash_state = is_crashing


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
            check_death(ctx)
            update_dynamic_values(ctx)
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