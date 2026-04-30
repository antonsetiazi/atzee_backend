# # core/widgets/ui/pages/_base_widget_list.py

# from core.ui.schema.page import Page
# from core.ui.schema.block import TableBlock, TableColumn, ActionBlock
# from core.ui.schema.action import Action

# from core.enum.permissions import CorePermission

# def build_widget_list_page(
#     *,
#     key: str,
#     domain: str,
#     path: str,
#     title_page: str,
#     subtitle_page: str,
#     data_source: str,
#     permissions: list[str],
#     create_label: str,
#     create_path: str,
#     edit_path: str,
#     search_mode: str,
#     delete_endpoint: str,
# ):
#     columns = [
#         # 🔗 identity
#         TableColumn(key="id", label="ID"),

#         # 🎯 widget info
#         TableColumn(key="type", label="Type"),
#         TableColumn(key="title", label="Title"),

#         # 📍 placement
#         TableColumn(key="position", label="Position"),

#         # 🎯 targeting
#         TableColumn(key="target_roles", label="Roles"),
#         TableColumn(key="target_apps", label="Apps"),

#         # ⏱️ schedule
#         TableColumn(
#             key="starts_at",
#             label="Start",
#             format="datetime",
#         ),
#         TableColumn(
#             key="ends_at",
#             label="End",
#             format="datetime",
#         ),

#         # 🔐 status
#         TableColumn(
#             key="is_active",
#             label="Active",
#             align="center",
#         ),

#         # 🔢 order
#         TableColumn(
#             key="order",
#             label="Order",
#             align="center",
#         ),
#     ]

#     return Page(
#         key=key,
#         entity="widgets",
#         domain=domain,
#         path=path,
#         title=title_page,
#         subtitle=subtitle_page,
#         permissions=permissions,
#         data_source=data_source,
#         blocks=[
#             TableBlock(
#                 title="UI Widgets",
#                 data_key="items",
#                 search_mode=search_mode,
#                 columns=columns,
#                 detail_as_state=False,
#                 actions=[
#                     Action(
#                         type="navigate",
#                         label="Edit",
#                         icon="edit",
#                         to=edit_path,
#                         permission=CorePermission.ADMIN_WIDGETS_EDIT,
#                     ),
#                     Action(
#                         type="delete",
#                         label="Delete",
#                         icon="delete",
#                         permission="core.widgets.delete",
#                         endpoint=delete_endpoint,
#                         confirm={
#                             "title": "Delete Widget",
#                             "message": "Are you sure you want to delete this widget?",
#                             "level": "danger",
#                         },
#                     ),
#                 ],
#             ),

#             ActionBlock(
#                 title="",
#                 justify="center",
#                 align="center",

#                 actions=[
#                     Action(
#                         type="navigate",
#                         label=create_label,
#                         icon="plus",
#                         to=create_path,
#                         permission=CorePermission.ADMIN_WIDGETS_CREATE,
#                     )
#                 ],
#             ),
#         ],
#     )