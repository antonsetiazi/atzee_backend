from core.widgets.ui.pages._base_widget_form import build_widget_form_page
from core.ui.schema.field import Field


UI_PAGES = build_widget_form_page(
    key="widgets.videos.edit",
    domain="core",
    path="/widgets/videos/:id/edit",
    title_page="Videos",
    submit_to="/widgets/{id}/",
    method="PATCH",
    permissions=["core.widgets.update"],
    title="Edit Video",
    redirect_page="/widgets/videos",
    widget_type="video",
    extra_fields=[
        Field(key="id", label="Widget ID", type="hidden"),
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
    ],
)