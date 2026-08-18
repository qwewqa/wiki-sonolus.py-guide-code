from sonolus.script.archetype import (
    PreviewArchetype,
    StandardArchetypeName,
    StandardImport,
)
from sonolus.script.printing import PrintColor, PrintFormat
from sonolus.script.timing import beat_to_time

from guide.lib.skin import Skin
from guide.preview.chart import Chart, draw_line, print_at_time


class PreviewBpmChange(PreviewArchetype):
    name = StandardArchetypeName.BPM_CHANGE

    beat: StandardImport.BEAT
    bpm: StandardImport.BPM

    def preprocess(self):
        Chart.beats = max(Chart.beats, self.beat)
        Chart.duration = max(Chart.duration, beat_to_time(self.beat))

    def render(self):
        draw_line(Skin.bpm_change_line, self.beat, order=1, a=0.5)
        print_at_time(
            self.bpm,
            beat_to_time(self.beat),
            fmt=PrintFormat.BPM,
            color=PrintColor.PURPLE,
            side="right",
        )


class PreviewTimescaleChange(PreviewArchetype):
    name = StandardArchetypeName.TIMESCALE_CHANGE

    beat: StandardImport.BEAT
    timescale: StandardImport.TIMESCALE

    def preprocess(self):
        Chart.beats = max(Chart.beats, self.beat)
        Chart.duration = max(Chart.duration, beat_to_time(self.beat))

    def render(self):
        draw_line(Skin.timescale_change_line, self.beat, order=2, a=0.5)
        print_at_time(
            self.timescale,
            beat_to_time(self.beat),
            fmt=PrintFormat.TIMESCALE,
            color=PrintColor.YELLOW,
            side="left",
        )
