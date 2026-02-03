# hr/employees/ui/pages/employee_list.py
from core.ui.schema.page import Page
from core.ui.schema.block import TableBlock, TableColumn
from core.ui.schema.action import Action


UI_PAGES = Page(
    key="employees.list",
    entity="employees",
    domain="hr",
    title="Employees",
    permissions=["hr.employees.view"],
    blocks=[
        TableBlock(
            data_source="/entities/hr/employees.list/query/",
            search_mode="client",
            columns=[
                TableColumn(key="employee_code", label="Code"),
                TableColumn(key="full_name", label="Name"),
                TableColumn(key="email", label="Email"),
                TableColumn(key="phone", label="Phone"),
                TableColumn(key="job_title", label="Job Title"),
                TableColumn(key="join_date", label="Join Date"),
            ],
            actions=[
                Action(
                    type="navigate",
                    label="Edit",
                    to="/hr/employees/{id}/edit",
                    permission="hr.employees.update"
                ),
                Action(
                    type="delete",
                    label="Delete",
                    permission="hr.employees.delete",
                    confirm={
                        "title": "Delete Employee",
                        "message": "Are you sure you want to delete this employee?",
                        "level": "danger",
                    },
                    endpoint="/hr/employees/{id}/"
                ),
            ],
            top_actions=[
                Action(
                    type="navigate",
                    label="Create Employee",
                    to="/hr/employees/create",
                    permission="hr.employees.add"
                )
            ],
        )
    ]
)
