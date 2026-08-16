from sonolus.script.engine import TutorialMode

from guide.lib.effect import Effects
from guide.lib.particle import Particles
from guide.lib.skin import Skin
from guide.tutorial.instructions import InstructionIcons, Instructions
from guide.tutorial.navigate import navigate
from guide.tutorial.preprocess import preprocess
from guide.tutorial.update import update

tutorial_mode = TutorialMode(
    skin=Skin,
    effects=Effects,
    particles=Particles,
    instructions=Instructions,
    instruction_icons=InstructionIcons,
    preprocess=preprocess,
    navigate=navigate,
    update=update,
)
