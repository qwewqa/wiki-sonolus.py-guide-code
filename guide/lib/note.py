from sonolus.script.runtime import level_life, level_score


def init_score():
    level_score().update(
        perfect_multiplier=1,
        great_multiplier=0.75,
        good_multiplier=0.5,
        consecutive_great_multiplier=0.01,
        consecutive_great_step=10,
        consecutive_great_cap=50,
    )


def init_life(note_class):
    note_class.archetype_life.update(
        perfect_increment=10,
        miss_increment=-100,
    )

    level_life().update(
        consecutive_perfect_increment=50,
        consecutive_perfect_step=10,
    )
