from math import floor

from sonolus.script.archetype import PreviewArchetype, callback
from sonolus.script.printing import PrintColor, PrintFormat
from sonolus.script.quad import Rect
from sonolus.script.runtime import ScrollDirection, canvas, screen
from sonolus.script.timing import beat_to_time
from sonolus.script.vec import Vec2

from guide.lib import archetype_names
from guide.lib.skin import Skin
from guide.preview.chart import (
    PANEL_HEIGHT,
    PANEL_WIDTH,
    Chart,
    draw_line,
    panel_count,
    print_at_time,
)


class PreviewStage(PreviewArchetype):
    name = archetype_names.STAGE

    @callback(order=1)
    def preprocess(self):
        canvas().scroll_direction = ScrollDirection.LEFT_TO_RIGHT
        canvas().size = panel_count() * PANEL_WIDTH * screen().h / 20

    def render(self):
        self.render_panels()
        self.render_beats()
        self.print_times()
        self.print_measures()

    def render_panels(self):
        for i in range(panel_count()):
            x = i * PANEL_WIDTH

            middle = Rect(l=-1.5, r=1.5, b=0, t=PANEL_HEIGHT).translate(Vec2(x, 0))
            left_border = Rect(l=-1.75, r=-1.5, b=0, t=PANEL_HEIGHT).translate(
                Vec2(x, 0)
            )
            right_border = Rect(l=1.5, r=1.75, b=0, t=PANEL_HEIGHT).translate(
                Vec2(x, 0)
            )

            Skin.stage_middle.draw(middle, z=0)
            Skin.stage_left_border.draw(left_border, z=0)
            Skin.stage_right_border.draw(right_border, z=0)

    def render_beats(self):
        for beat in range(floor(Chart.beats) + 1):
            draw_line(Skin.beat_line, beat, order=0, a=0.25 if beat % 4 == 0 else 0.125)

    def print_times(self):
        for time in range(1, floor(Chart.duration) + 1):
            print_at_time(
                time,
                time,
                fmt=PrintFormat.TIME,
                decimal_places=0,
                color=PrintColor.NEUTRAL,
                side="left",
            )

    def print_measures(self):
        for beat in range(4, floor(Chart.beats) + 1, 4):
            print_at_time(
                beat / 4 + 1,
                beat_to_time(beat),
                fmt=PrintFormat.MEASURE_COUNT,
                decimal_places=0,
                color=PrintColor.NEUTRAL,
                side="right",
            )
