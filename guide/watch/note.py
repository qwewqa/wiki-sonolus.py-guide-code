from sonolus.script.archetype import StandardImport, WatchArchetype, entity_data
from sonolus.script.bucket import Judgment
from sonolus.script.interval import Interval
from sonolus.script.quad import Rect
from sonolus.script.runtime import is_replay, is_skip, scaled_time
from sonolus.script.timing import beat_to_bpm, beat_to_time, time_to_scaled_time
from sonolus.script.vec import Vec2

from guide.lib import archetype_names
from guide.lib.buckets import Buckets
from guide.lib.effect import Effects
from guide.lib.layout import Config
from guide.lib.particle import Particles
from guide.lib.skin import Skin


class WatchNote(WatchArchetype):
    name = archetype_names.NOTE
    is_scored = True

    beat: StandardImport.BEAT
    judgment: StandardImport.JUDGMENT
    accuracy: StandardImport.ACCURACY

    target_time: float = entity_data()
    visual_time: Interval = entity_data()

    def preprocess(self):
        self.target_time = beat_to_time(self.beat)
        self.visual_time.end = time_to_scaled_time(self.target_time)
        self.visual_time.start = self.visual_time.end - 120 / beat_to_bpm(self.beat)

        self.result.target_time = self.target_time

        if is_replay():
            hit_time = self.target_time + self.accuracy
        else:
            hit_time = self.target_time
            self.judgment = Judgment.PERFECT
            self.accuracy = 0

        match self.judgment:
            case Judgment.PERFECT:
                Effects.perfect.schedule(hit_time, 0.02)
            case Judgment.GREAT:
                Effects.great.schedule(hit_time, 0.02)
            case Judgment.GOOD:
                Effects.good.schedule(hit_time, 0.02)

        self.result.bucket @= Buckets.note
        self.result.bucket_value = self.accuracy * 1000

    def spawn_time(self) -> float:
        return self.visual_time.start

    def despawn_time(self) -> float:
        if is_replay():
            return time_to_scaled_time(self.target_time + self.accuracy)
        return self.visual_time.end

    def update_parallel(self):
        y = self.visual_time.unlerp(scaled_time())

        layout = Rect.from_center(
            Vec2(0, y),
            Vec2(2 * Config.note_radius, -2 * Config.note_radius),
        )

        Skin.note.draw(layout, z=(1, -self.target_time))

    def terminate(self):
        if is_skip():
            return

        if is_replay() and self.judgment == Judgment.MISS:
            return

        particle_layout = Rect.from_center(
            Vec2(0, 1),
            Vec2(4 * Config.note_radius, -4 * Config.note_radius),
        )

        Particles.note.spawn(particle_layout, duration=0.3)
