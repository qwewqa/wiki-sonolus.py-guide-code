from guide.lib.layout import init_layout
from guide.lib.ui import init_ui
from guide.tutorial.navigate import reset_phase


def preprocess():
    init_ui()
    init_layout(1)
    reset_phase()
