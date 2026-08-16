from sonolus.script.archetype import PlayArchetype
from sonolus.script.debug import debug_log
from sonolus.script.runtime import time

from guide.lib import archetype_names
from guide.play.initialization import Initialization


class Stage(PlayArchetype):
    name = archetype_names.STAGE

    def spawn_order(self) -> int:
        return -9

    def should_spawn(self) -> bool:
        return Initialization.at(0).is_despawned

    def update_parallel(self):
        debug_log(time())
