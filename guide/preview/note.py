from sonolus.script.archetype import PreviewArchetype, StandardImport
from sonolus.script.quad import Rect
from sonolus.script.timing import beat_to_time
from sonolus.script.vec import Vec2

from guide.lib import archetype_names
from guide.lib.options import Options
from guide.lib.skin import Skin
from guide.preview.chart import HEIGHT_SCALE, Chart, pos_at_time


class PreviewNote(PreviewArchetype):
    name = archetype_names.NOTE

    beat: StandardImport.BEAT

    def preprocess(self):
        Chart.beats = max(Chart.beats, self.beat)
        Chart.duration = max(Chart.duration, beat_to_time(self.beat))

    def render(self):
        time = beat_to_time(self.beat)
        position = pos_at_time(time)

        layout = Rect.from_center(
            position,
            Vec2(2 * Options.note_size, 2 * Options.note_size * HEIGHT_SCALE),
        )
        Skin.note.draw(layout, z=(2, -time))
