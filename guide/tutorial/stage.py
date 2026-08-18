from sonolus.script.quad import Rect

from guide.lib.layout import Config
from guide.lib.skin import Skin


def draw_stage():
    layout = Rect(
        l=Config.judge_line_l,
        r=Config.judge_line_r,
        t=1 - Config.note_radius / 4,
        b=1 + Config.note_radius / 4,
    )
    Skin.judge_line.draw(layout, z=0, a=1)
