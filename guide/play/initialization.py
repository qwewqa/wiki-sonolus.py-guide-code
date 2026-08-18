from sonolus.script.archetype import PlayArchetype

from guide.lib import archetype_names
from guide.lib.ui import init_ui


class Initialization(PlayArchetype):
    name = archetype_names.INITIALIZATION

    def spawn_order(self) -> float:
        return -10

    def preprocess(self):
        init_ui()

    def update_sequential(self):
        self.despawn = True
