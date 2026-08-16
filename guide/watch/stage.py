from sonolus.script.archetype import WatchArchetype
from sonolus.script.debug import debug_log
from sonolus.script.runtime import time

from guide.lib import archetype_names


class WatchStage(WatchArchetype):
    name = archetype_names.STAGE

    def spawn_time(self) -> float:
        return -999999

    def despawn_time(self) -> float:
        return 999999

    def update_parallel(self):
        debug_log(time())
