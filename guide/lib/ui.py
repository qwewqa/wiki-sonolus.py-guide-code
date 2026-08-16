from sonolus.script.runtime import HorizontalAlign, runtime_ui, safe_area
from sonolus.script.ui import UiConfig
from sonolus.script.vec import Vec2

ui_config = UiConfig()


def init_ui():
    ui = runtime_ui()
    ui.menu.update(
        anchor=safe_area().tl + Vec2(0.05, -0.05),
        pivot=Vec2(0, 1),
        dimensions=Vec2(0.15, 0.15) * ui.menu_config.scale,
        rotation=0,
        alpha=ui.menu_config.alpha,
        horizontal_align=HorizontalAlign.CENTER,
        background=True,
    )
