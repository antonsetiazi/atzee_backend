# accounting/journals/ui/pages/_base_general_journal_list.py

from core.ui.schema.page import Page
from core.ui.schema.block import TableBlock, TableColumn
from core.ui.schema.action import Action


def build_general_journal_list_page(
    *,
    key: str,
    domain: str,
    path: str,
    data_source: str,
    permissions: list[str],
    create_path: str,
):
    return Page(
        key=key,
        entity="journals",
        domain=domain,
        path=path,
        title="General Journals",
        permissions=permissions,
        data_source=data_source,
        blocks=[
            TableBlock(
                data_key="items",
                search_mode="server",
                columns=[
                    TableColumn(key="journal_number", label="Journal No"),
                    TableColumn(key="journal_date", label="Date"),
                    TableColumn(key="description", label="Description"),
                    TableColumn(key="status", label="Status"),
                ],
                actions=[],
                top_actions=[
                    Action(
                        type="navigate",
                        label="Create Journal",
                        to=create_path,
                        permission="accounting.journals.add",
                    )
                ],
            )
        ],
    )
