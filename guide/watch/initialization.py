from sonolus.script.archetype import WatchArchetype

from guide.lib import archetype_names
from guide.lib.buckets import init_buckets
from guide.lib.layout import init_layout
from guide.lib.note import init_life, init_score
from guide.lib.options import Options
from guide.lib.ui import init_ui
from guide.watch.note import WatchNote


class WatchInitialization(WatchArchetype):
    name = archetype_names.INITIALIZATION

    def preprocess(self):
        init_buckets()
        init_score()
        init_life(WatchNote)
        init_ui()
        init_layout(Options.note_size)
