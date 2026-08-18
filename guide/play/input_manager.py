from sonolus.script.archetype import PlayArchetype
from sonolus.script.array import Dim
from sonolus.script.containers import VarArray
from sonolus.script.globals import level_memory
from sonolus.script.runtime import Touch

from guide.lib import archetype_names

used_touch_ids = level_memory(VarArray[int, Dim[16]])


def touch_is_used(touch: Touch):
    return touch.id in used_touch_ids


def mark_touch_used(touch: Touch):
    used_touch_ids.set_add(touch.id)


class InputManager(PlayArchetype):
    name = archetype_names.INPUT_MANAGER

    def touch(self):
        used_touch_ids.clear()
