# # core/widgets/ui/pages/widget_edit.py

# from core.ui.registry import register_ui_module_pages
# from core.ui.schema.field import Field
# from core.widgets.ui.pages._base_widget_form import (
#     build_widget_form_page,
# )

# UI_PAGES = build_widget_form_page(
#     key="widgets.edit",
#     domain="core",
#     path="/settings/widgets/:id/edit",
#     title_page="Widget",
#     submit_to="/widgets/{id}/",
#     method="PATCH",
#     permissions=["core.widgets.update"],
#     title="Edit Widget",
#     redirect_page="/settings/widgets",
#     widget_type="",
#     extra_fields=[
#         Field(key="id", label="Widget ID", type="hidden"),
#     ],
# )

# register_ui_module_pages("core", UI_PAGES)
