from sonolus.script.archetype import (
    PlayArchetype,
    StandardImport,
    callback,
    entity_data,
    entity_memory,
)
from sonolus.script.bucket import Judgment
from sonolus.script.interval import Interval
from sonolus.script.quad import Rect
from sonolus.script.runtime import input_offset, scaled_time, time, touches
from sonolus.script.timing import beat_to_bpm, beat_to_time, time_to_scaled_time
from sonolus.script.vec import Vec2

from guide.lib import archetype_names
from guide.lib.buckets import Buckets, note_window
from guide.lib.effect import Effects
from guide.lib.layout import Config
from guide.lib.particle import Particles
from guide.lib.skin import Skin
from guide.play.input_manager import mark_touch_used, touch_is_used


class Note(PlayArchetype):
    name = archetype_names.NOTE
    is_scored = True

    beat: StandardImport.BEAT
    target_time: float = entity_data()
    visual_time: Interval = entity_data()
    spawn_time: float = entity_data()
    input_time: Interval = entity_memory()

    def preprocess(self):
        self.target_time = beat_to_time(self.beat)
        self.visual_time.end = time_to_scaled_time(self.target_time)
        self.visual_time.start = self.visual_time.end - 120 / beat_to_bpm(self.beat)
        self.spawn_time = self.visual_time.start

    def spawn_order(self) -> float:
        return self.spawn_time

    def should_spawn(self) -> bool:
        return scaled_time() >= self.spawn_time

    def initialize(self):
        self.input_time = note_window.good + self.target_time + input_offset()
        self.result.accuracy = note_window.good.end

    @callback(order=1)
    def touch(self):
        if time() not in self.input_time:
            return

        for touch in touches():
            if not touch.started or touch_is_used(touch):
                continue

            mark_touch_used(touch)

            self.result.judgment = note_window.judge(touch.start_time, self.target_time)
            self.result.accuracy = touch.start_time - self.target_time

            self.result.bucket @= Buckets.note
            self.result.bucket_value = self.result.accuracy * 1000

            match self.result.judgment:
                case Judgment.PERFECT:
                    Effects.perfect.play(0.02)
                case Judgment.GREAT:
                    Effects.great.play(0.02)
                case Judgment.GOOD:
                    Effects.good.play(0.02)

            layout = Rect.from_center(
                Vec2(0, 1),
                Vec2(4 * Config.note_radius, -4 * Config.note_radius),
            )

            Particles.note.spawn(layout, duration=0.3, loop=False)

            self.despawn = True
            return

    def update_parallel(self):
        if time() > self.input_time.end:
            self.despawn = True
        if self.despawn:
            return

        y = self.visual_time.unlerp(scaled_time())
        layout = Rect.from_center(
            Vec2(0, y), Vec2(2 * Config.note_radius, -2 * Config.note_radius)
        )
        Skin.note.draw(layout, z=(1, -self.target_time))
