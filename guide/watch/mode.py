from sonolus.script.engine import WatchMode

from guide.lib.buckets import Buckets
from guide.lib.effect import Effects
from guide.lib.particle import Particles
from guide.lib.skin import Skin
from guide.watch.initialization import WatchInitialization
from guide.watch.stage import WatchStage
from guide.watch.update_spawn import update_spawn

watch_mode = WatchMode(
    archetypes=[WatchInitialization, WatchStage],
    skin=Skin,
    effects=Effects,
    particles=Particles,
    buckets=Buckets,
    update_spawn=update_spawn,
)
