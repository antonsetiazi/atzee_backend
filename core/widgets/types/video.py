# core/widgets/types/video.py

from core.ui.schema.field import Field

def video_fields():
    return [
        Field(
            key="config.video_url",
            label="Video URL",
            type="text",
            required=True,
        ),
        Field(
            key="config.autoplay",
            label="Autoplay",
            type="boolean",
            default=False,
        ),
    ]

