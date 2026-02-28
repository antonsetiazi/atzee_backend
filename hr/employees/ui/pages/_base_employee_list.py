# hr/employees/ui/pages/_base_employee_list.py

from core.ui.schema.page import Page
from core.ui.schema.block import TableBlock, TableColumn
from core.ui.schema.action import Action


def build_employee_list_page(
    *,
    key: str,
    domain: str,
    path: str,
    data_source: str,
    permissions: list[str],
    create_path: str,
    edit_path: str,
    search_mode: str,
    delete_endpoint: str,
    extra_columns: list[TableColumn] | None = None,
):
    columns = [
        TableColumn(key="employee_code", label="Code"),
        TableColumn(key="full_name", label="Name"),
        TableColumn(key="email", label="Email"),
        TableColumn(key="phone", label="Phone"),
        TableColumn(key="job_title", label="Job Title"),
        TableColumn(key="join_date", label="Join Date"),
    ]

    if extra_columns:
        columns.extend(extra_columns)

    return Page(
        key=key,
        entity="employees",
        domain=domain,
        path=path,
        title="Employees",
        permissions=permissions,
        data_source=data_source,
        blocks=[
            TableBlock(
                data_key="items",
                search_mode=search_mode,
                columns=columns,
                detail_as_state=False,
                actions=[
                    Action(
                        type="navigate",
                        label="Edit",
                        icon="edit",
                        to=edit_path,
                        permission="hr.employees.update"
                    ),
                    Action(
                        type="delete",
                        label="Delete",
                        icon="delete",
                        permission="hr.employees.delete",
                        confirm={
                            "title": "Delete Employee",
                            "message": "Are you sure you want to delete this employee?",
                            "level": "danger",
                        },
                        endpoint=delete_endpoint
                    ),
                ],
                top_actions=[
                    Action(
                        type="navigate",
                        label="Create Employee",
                        to=create_path,
                        permission="hr.employees.add"
                    )
                ],
            )
        ]
    )
