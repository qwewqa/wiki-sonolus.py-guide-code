from sonolus.script.archetype import WatchArchetype
from sonolus.script.quad import Rect

from guide.lib import archetype_names
from guide.lib.layout import Config
from guide.lib.skin import Skin


class WatchStage(WatchArchetype):
    name = archetype_names.STAGE

    def spawn_time(self) -> float:
        return -999999

    def despawn_time(self) -> float:
        return 999999

    def update_parallel(self):
        layout = Rect(
            l=Config.judge_line_l,
            r=Config.judge_line_r,
            t=1 - Config.note_radius / 4,
            b=1 + Config.note_radius / 4,
        )
        Skin.judge_line.draw(layout, z=(0,), a=1)
