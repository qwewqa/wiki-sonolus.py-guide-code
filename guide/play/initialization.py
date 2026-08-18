from sonolus.script.archetype import PlayArchetype

from guide.lib import archetype_names
from guide.lib.buckets import init_buckets
from guide.lib.layout import init_layout
from guide.lib.note import init_life, init_score
from guide.lib.options import Options
from guide.lib.ui import init_ui
from guide.play.input_manager import InputManager
from guide.play.note import Note


class Initialization(PlayArchetype):
    name = archetype_names.INITIALIZATION

    def spawn_order(self) -> float:
        return -10

    def preprocess(self):
        init_buckets()
        init_score()
        init_life(Note)
        init_ui()
        init_layout(Options.note_size)

    def update_sequential(self):
        InputManager.spawn()
        self.despawn = True
