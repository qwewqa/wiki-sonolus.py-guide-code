from sonolus.script.engine import PreviewMode

from guide.lib.skin import Skin
from guide.preview.bar_line import PreviewBpmChange, PreviewTimescaleChange
from guide.preview.initialization import PreviewInitialization
from guide.preview.note import PreviewNote
from guide.preview.stage import PreviewStage

preview_mode = PreviewMode(
    archetypes=[
        PreviewInitialization,
        PreviewStage,
        PreviewNote,
        PreviewBpmChange,
        PreviewTimescaleChange,
    ],
    skin=Skin,
)
