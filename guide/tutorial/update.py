from sonolus.script.instruction import clear_instruction

from guide.tutorial.navigate import current_phase_time, finish_frame, reset_phase
from guide.tutorial.note import tap_phase
from guide.tutorial.stage import draw_stage


def update():
    clear_instruction()
    draw_stage()
    if tap_phase(current_phase_time()):
        reset_phase()
    finish_frame()
