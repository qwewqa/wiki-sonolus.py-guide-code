from sonolus.script.level import BpmChange, Level, LevelData, TimescaleChange

from guide.chart import BPMS, NOTE_BEATS, TIMESCALES
from guide.play.initialization import Initialization
from guide.play.note import Note
from guide.play.stage import Stage

guide_level = Level(
    name="guide",
    title="Patience",
    artists="More Plastic & VinDon",
    author="ntsu",
    description=(
        "Song: More Plastic & VinDon - Patience\n"
        "Music provided by NoCopyrightSounds\n"
        "Free Download/Stream: http://NCS.io/Patience\n"
        "Watch: https://youtu.be/Lxf65uhlR6s"
    ),
    cover="levels/patience/cover.jpg",
    bgm="levels/patience/bgm.mp3",
    data=LevelData(
        bgm_offset=0,
        entities=[
            Initialization(),
            Stage(),
            *(BpmChange(beat=beat, bpm=bpm) for beat, bpm in BPMS),
            *(
                TimescaleChange(beat=beat, timescale=timescale)
                for beat, timescale in TIMESCALES
            ),
            *(Note(beat=beat) for beat in NOTE_BEATS),
        ],
    ),
)


def load_levels():
    yield guide_level
