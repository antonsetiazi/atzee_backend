# hr/employees/ui/pages/employee_create.py
from core.ui.schema.page import Page
from core.ui.schema.block import FormBlock
from core.ui.schema.field import Field
from core.ui.schema.action import Action

UI_PAGES = Page(
    key="employees.create",
    entity="employees",
    domain="hr",
    title="Employee",
    permissions=["hr.employees.add"],
    blocks=[
        FormBlock(
            submit_to="/hr/employees/",
            method="POST",
            title="Create Employee",
            description="Lengkapi data employee dengan benar",
            fields=[
                # Field(
                #     key="user_id", 
                #     label="User", 
                #     type="select", 
                #     data_source={
                #         "type": "entity",
                #         "domain": "core",
                #         "entity": "users.list",
                #         "query": {
                #             "fields": ["id", "full_name", "email"],
                #         },
                #         "map": {
                #             "value": "id",
                #             "label": "{full_name} ({email})"
                #         }
                #     },
                #     required=True
                # ),
                Field(key="employee_code", label="Employee Code", type="text"),
                Field(key="full_name", label="Employee Name", type="text", required=True),
                Field(key="email", label="Email", type="email"),
                Field(key="phone", label="Phone", type="text"),
                Field(key="join_date", label="Join Date", type="date", required=True),
                Field(key="job_title", label="Job Title", type="text"),
                Field(key="notes", label="Notes", type="textarea"),
            ],
            actions=[
                Action(type="submit", label="Save"),
                Action(type="redirect", label="Cancel", to="/hr/employees")
            ]
        )
    ],
)
