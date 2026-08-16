from sonolus.script.engine import Engine, EngineData
from sonolus.script.project import Project

from guide.level import load_levels
from guide.lib.options import Options
from guide.lib.ui import ui_config
from guide.play.mode import play_mode
from guide.preview.mode import preview_mode
from guide.tutorial.mode import tutorial_mode
from guide.watch.mode import watch_mode

engine = Engine(
    name="guide",
    title="Sonolus.py Guide",
    skin="pixel",
    particle="pixel",
    background="vanilla",
    effect="8bit",
    data=EngineData(
        ui=ui_config,
        options=Options,
        play=play_mode,
        watch=watch_mode,
        preview=preview_mode,
        tutorial=tutorial_mode,
    ),
)

project = Project(
    engine=engine,
    levels=load_levels,
)
