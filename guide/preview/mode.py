from sonolus.script.engine import PreviewMode

from guide.lib.skin import Skin
from guide.preview.initialization import PreviewInitialization

preview_mode = PreviewMode(
    archetypes=[PreviewInitialization],
    skin=Skin,
)
