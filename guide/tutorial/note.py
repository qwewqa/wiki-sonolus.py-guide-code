from math import pi

from sonolus.script.interval import remap, remap_clamped
from sonolus.script.quad import Rect
from sonolus.script.runtime import runtime_ui, skin_transform
from sonolus.script.vec import Vec2

from guide.lib.effect import Effects
from guide.lib.layout import Config
from guide.lib.particle import Particles
from guide.lib.skin import Skin
from guide.tutorial.instructions import InstructionIcons, Instructions
from guide.tutorial.navigate import PhaseTime

INTRO_DURATION = 1
FALL_DURATION = 2
FROZEN_DURATION = 4
PAUSE_DURATION = 1


def draw_note(y: float, scale: float = 1, alpha: float = 1):
    size = 2 * Config.note_radius * scale
    layout = Rect.from_center(Vec2(0, y), Vec2(size, -size))
    Skin.note.draw(layout, z=(1,), a=alpha)


def draw_intro(elapsed: float):
    alpha = remap_clamped(0.75 * INTRO_DURATION, INTRO_DURATION, 1, 0, elapsed)
    draw_note(0.5, scale=2, alpha=alpha)


def draw_fall(elapsed: float):
    y = remap(0, FALL_DURATION, 0, 1, elapsed)
    draw_note(y)


def draw_frozen(elapsed: float):
    Instructions.tap.show()
    draw_note(1)

    cycle = elapsed % 1
    angle = remap_clamped(0.25, 0.75, pi / 6, pi / 3, cycle)
    alpha = remap_clamped(0.5, 0.25, 0, 1, abs(cycle - 0.5))

    config = runtime_ui().instruction_config
    judgment_position = skin_transform().transform_vec(Vec2(0, 1))
    position = Vec2(0, -1).rotate(pi / 3) * (0.25 * config.scale) + judgment_position

    InstructionIcons.hand.paint(
        position=Vec2(0, 1).rotate(angle) * (0.25 * config.scale) + position,
        size=0.25 * config.scale,
        rotation=(180 * angle) / pi,
        z=0,
        a=alpha * config.alpha,
    )


def play_note_hit_effects():
    layout = Rect.from_center(
        Vec2(0, 1),
        Vec2(4 * Config.note_radius, -4 * Config.note_radius),
    )
    Effects.perfect.play()
    Particles.note.spawn(layout, duration=0.3)


def tap_phase(phase_time: PhaseTime) -> bool:
    intro = phase_time.first(INTRO_DURATION)
    fall = intro.next(FALL_DURATION)
    frozen = fall.next(FROZEN_DURATION)
    hit_time = frozen.end
    pause = frozen.next(PAUSE_DURATION)

    if intro:
        draw_intro(intro.elapsed)
    if fall:
        draw_fall(fall.elapsed)
    if frozen:
        draw_frozen(frozen.elapsed)
    if phase_time.crossed(hit_time):
        play_note_hit_effects()

    return pause.is_done
