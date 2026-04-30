
# from core.ui.registry import register_ui_module_pages
# from core.widgets.ui.pages._base_widget_form import build_widget_form_page
# from core.ui.schema.field import Field

# UI_PAGES = build_widget_form_page(
#     key="widgets.videos.create",
#     domain="core",
#     path="/widgets/videos/create",
#     title_page="Videos",
#     submit_to="/widgets/",
#     method="POST",
#     permissions=["core.widgets.add"],
#     title="Create Video",
#     redirect_page="/widgets/videos",
#     widget_type="video",
#     extra_fields=[
#         Field(
#             key="config.video_url",
#             label="Video URL",
#             type="text",
#             required=True,
#         ),
#         Field(
#             key="config.autoplay",
#             label="Autoplay",
#             type="boolean",
#             default=False,
#         ),
#     ],
# )

# register_ui_module_pages("core", UI_PAGES)