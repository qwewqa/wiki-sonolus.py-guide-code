from sonolus.script.archetype import PlayArchetype, callback
from sonolus.script.quad import Rect
from sonolus.script.runtime import touches

from guide.lib import archetype_names
from guide.lib.effect import Effects
from guide.lib.layout import Config
from guide.lib.skin import Skin
from guide.play.initialization import Initialization
from guide.play.input_manager import touch_is_used


class Stage(PlayArchetype):
    name = archetype_names.STAGE

    def spawn_order(self) -> int:
        return -9

    def should_spawn(self) -> bool:
        return Initialization.at(0).is_despawned

    @callback(order=2)
    def touch(self):
        for touch in touches():
            if not touch.started:
                continue
            if touch_is_used(touch):
                continue

            Effects.stage.play(0.02)
            return

    def update_parallel(self):
        layout = Rect(
            l=Config.judge_line_l,
            r=Config.judge_line_r,
            t=1 - Config.note_radius / 4,
            b=1 + Config.note_radius / 4,
        )
        Skin.judge_line.draw(layout, z=0, a=1 if len(touches()) else 0.5)
