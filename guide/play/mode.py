from sonolus.script.engine import PlayMode

from guide.lib.buckets import Buckets
from guide.lib.effect import Effects
from guide.lib.particle import Particles
from guide.lib.skin import Skin
from guide.play.initialization import Initialization
from guide.play.stage import Stage

play_mode = PlayMode(
    archetypes=[Initialization, Stage],
    skin=Skin,
    effects=Effects,
    particles=Particles,
    buckets=Buckets,
)
