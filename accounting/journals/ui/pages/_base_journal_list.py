from core.ui.schema.page import Page
from core.ui.schema.block import TableBlock, TableColumn
from core.ui.schema.action import Action


def build_journal_list_page(
    *,
    key: str,
    domain: str,
    path: str,
    data_source: str,
    create_path: str,
    permissions: list[str],
    detail_path: str,
):
    columns = [
        TableColumn(key="journal_number", label="Journal No"),
        TableColumn(key="journal_date", label="Date"),
        TableColumn(key="journal_type", label="Type"),
        TableColumn(key="status", label="Status"),
        TableColumn(key="description", label="Description"),
        TableColumn(key="total_debit", label="Debit"),
        TableColumn(key="total_credit", label="Credit"),
    ]

    return Page(
        key=key,
        entity="journals",
        domain=domain,
        path=path,
        title="Journals",
        permissions=permissions,
        blocks=[
            TableBlock(
                data_source=data_source,
                search_mode="server",
                columns=columns,
                detail_as_state=False,
                actions=[
                    Action(
                        type="navigate",
                        label="View",
                        icon="eye",
                        to=detail_path,
                        permission="accounting.journals.view",
                    ),
                ],
                top_actions=[
                    Action(
                        type="navigate",
                        label="Create General Journal",
                        to=create_path,
                        permission="accounting.journals.add"
                    )
                ],
            )
        ],
    )
