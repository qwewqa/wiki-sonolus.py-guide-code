from sonolus.script.bucket import Bucket, JudgmentWindow, bucket, bucket_sprite, buckets
from sonolus.script.interval import Interval
from sonolus.script.text import StandardText

from guide.lib.skin import Skin


@buckets
class Buckets:
    note: Bucket = bucket(
        sprites=[
            bucket_sprite(
                sprite=Skin.note,
                x=0,
                y=0,
                w=2,
                h=2,
                rotation=0,
            ),
        ],
        unit=StandardText.MILLISECOND_UNIT,
    )


note_window = JudgmentWindow(
    perfect=Interval(-0.05, 0.05),
    great=Interval(-0.1, 0.1),
    good=Interval(-0.2, 0.2),
)


def init_buckets():
    Buckets.note.window @= note_window * 1000
