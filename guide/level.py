from sonolus.script.level import Level, LevelData

from guide.play.initialization import Initialization
from guide.play.stage import Stage

level = Level(
    name="guide_level",
    title="Sonolus.py Guide Level",
    bgm=None,
    data=LevelData(
        bgm_offset=0,
        entities=[Initialization(), Stage()],
    ),
)


def load_levels():
    yield level
