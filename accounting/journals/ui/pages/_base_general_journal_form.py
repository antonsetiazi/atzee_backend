# accounting/journals/ui/pages/_base_general_journal_form.py

from core.ui.schema.page import Page
from core.ui.schema.block import FormBlock, TableBlock, TableColumn
from core.ui.schema.field import Field
from core.ui.schema.action import Action


def build_general_journal_form_page(
    *,
    key: str,
    domain: str,
    path: str,
    submit_to: str,
    method: str,
    permissions: list[str],
    title: str,
    redirect_page: str,
):
    return Page(
        key=key,
        entity="journals",
        domain=domain,
        path=path,
        title="General Journal",
        permissions=permissions,
        blocks=[
            FormBlock(
                submit_to=submit_to,
                method=method,
                title=title,
                description="Manual journal for adjustment, opening balance, or correction",
                redirect_to={"page": redirect_page},
                fields=[
                    Field(
                        key="journal_date",
                        label="Journal Date",
                        type="date",
                        required=True,
                    ),
                    Field(
                        key="description",
                        label="Description",
                        type="textarea",
                        placeholder="Adjustment / Opening balance / Correction",
                    ),
                ],
                actions=[
                    Action(type="submit", label="Save & Post"),
                    Action(
                        type="redirect",
                        label="Cancel",
                        to=redirect_page,
                    ),
                ],
                refresh_cache=["journals.list"],
            ),
            # TableBlock(
            #     title="Journal Lines",
            #     columns=[
            #         TableColumn(
            #             key="account",
            #             label="Account",
            #         ),
            #         TableColumn(
            #             key="debit",
            #             label="Debit",
            #         ),
            #         TableColumn(
            #             key="credit",
            #             label="Credit",
            #         ),
            #         TableColumn(
            #             key="memo",
            #             label="Memo",
            #         ),
            #     ],
            # ),
        ],
        # meta={
        #     "journal_type": "general",
        #     "is_manual": True,
        #     "advanced": True,
        # },
    )
