from __future__ import annotations

from sonolus.script.globals import level_memory
from sonolus.script.record import Record
from sonolus.script.runtime import time


@level_memory
class PhaseState:
    start_time: float
    previous_frame_time: float


class PhaseTime(Record):
    current: float
    previous: float

    def first(self, duration: float) -> PhaseRange:
        return PhaseRange(phase=self, start=0, end=duration)

    def crossed(self, timing: float) -> bool:
        return self.previous < timing <= self.current


class PhaseRange(Record):
    phase: PhaseTime
    start: float
    end: float

    @property
    def elapsed(self) -> float:
        return self.phase.current - self.start

    @property
    def is_done(self) -> bool:
        return self.phase.current >= self.end

    def next(self, duration: float) -> PhaseRange:
        return PhaseRange(phase=self.phase, start=self.end, end=self.end + duration)

    def __bool__(self) -> bool:
        return self.start <= self.phase.current < self.end


def current_phase_time() -> PhaseTime:
    return PhaseTime(
        current=time() - PhaseState.start_time,
        previous=PhaseState.previous_frame_time - PhaseState.start_time,
    )


def reset_phase():
    PhaseState.start_time = time()
    PhaseState.previous_frame_time = time()


def finish_frame():
    PhaseState.previous_frame_time = time()


def navigate():
    reset_phase()
