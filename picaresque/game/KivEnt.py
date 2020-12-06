class GameWorldMixin():
    def __init__(self):
        self.init_game = None
        self._worlds = None
        self.gameworld = None

    def add_world(self, world_name, **kwargs):
        self._worlds[world_name] = GameWorld(world_name, **kwargs)
        self.gameworld.init_gameworld([], callback=self.init_game)

class GameWorld():
    def __init__(self, world_name, screen_manager="gamescreenmanager", world_size=100 * 1024,
                 entity_block_size=128, system_count=8):
        self.name = world_name
        self.screen_manager = screen_manager
        self.world_size = world_size
        self.entity_block_size = entity_block_size
        self.system_count = system_count
        self.zones = {}
        self._states = {}

    def add_zone(self, zone, size):
        self.zones[zone] = size

    def _create_gameworld_str(self):
        gw_str = f"\tgameworld: {self.name}\n"
        gw_str += "\tGameWorld:\n"
        gw_str += f"\t\tid: {self.name}\n"
        gw_str += f"\t\tgamescreenmanager: {self.screen_manager}\n"
        gw_str += f"\t\tsize_of_gameworld: {self.world_size}\n"
        gw_str += f"\t\tsize_of_entity_block: {self.entity_block_size}\n"
        gw_str += f"\t\tsystem_count: {self.system_count}\n"
        gw_str += f"\t\tzones: {str(self.zones)}\n"
        gw_str += f"\tGameScreenManager:\n"
        gw_str += f"\t\tid: {self.screen_manager}\n"
        gw_str += "\t\tsize: root.size\n"
        gw_str += "\t\tpos: root.pos\n"
        gw_str += f"\t\tgameworld: {self.name}\n"
        gw_str += "\t\tGameScreen:\n"
        gw_str += '\t\t\tname: "main"\n'
        return gw_str

    def _make_state_dict(self, state_name="main", screenmanager_screen="main", systems_added=[], systems_removed=[],
                   systems_paused=[], systems_unpaused=[], **kwargs):
        return kwargs

    def get_state(self):
        pass