from sonolus.script.globals import level_data
from sonolus.script.runtime import screen, set_particle_transform, set_skin_transform
from sonolus.script.transform import Transform2d
from sonolus.script.vec import Vec2


@level_data
class Config:
    judge_line_l: float
    judge_line_r: float
    note_radius: float


def init_layout(note_size: float):
    note_radius = 0.2 * note_size
    judge_line_y = -0.6

    t = screen().t + note_radius
    b = judge_line_y
    h = t - b

    Config.judge_line_l = screen().l / h
    Config.judge_line_r = screen().r / h

    Config.note_radius = note_radius / h

    transform = Transform2d.new().scale(Vec2(h, -h)).translate(Vec2(0, t))

    set_skin_transform(transform)
    set_particle_transform(transform)
