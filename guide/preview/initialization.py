from sonolus.script.archetype import PreviewArchetype
from sonolus.script.runtime import screen, set_skin_transform
from sonolus.script.transform import Transform2d
from sonolus.script.vec import Vec2

from guide.lib import archetype_names
from guide.lib.ui import init_ui
from guide.preview.chart import PANEL_HEIGHT, PANEL_WIDTH


class PreviewInitialization(PreviewArchetype):
    name = archetype_names.INITIALIZATION

    def preprocess(self):
        init_ui()

        transform = (
            Transform2d.new()
            .translate(Vec2(PANEL_WIDTH / 2, 0))
            .scale(Vec2(screen().h / 20, screen().h / PANEL_HEIGHT))
            .translate(screen().bl)
        )
        set_skin_transform(transform)
