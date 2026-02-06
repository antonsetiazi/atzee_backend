# business/employees/ui/pages/_base_employee_form.py

from core.ui.schema.page import Page
from core.ui.schema.block import FormBlock
from core.ui.schema.field import Field
from core.ui.schema.action import Action


def build_employee_form_page(
    *,
    key: str,
    domain: str,
    path: str,
    submit_to: str,
    method: str,
    permissions: list[str],
    title: str,
    redirect_page: str,
    extra_fields: list[Field] | None = None,
):
    fields = [
        Field(key="employee_code", label="Employee Code", type="text"),
        Field(key="full_name", label="Employee Name", type="text", required=True),
        Field(key="email", label="Email", type="email"),
        Field(key="phone", label="Phone", type="text"),
        Field(key="join_date", label="Join Date", type="date", required=True),
        Field(key="job_title", label="Job Title", type="text"),
        Field(key="notes", label="Notes", type="textarea"),
    ]

    if extra_fields:
        # extra_fields boleh:
        # - id (edit)
        # - vertical-specific fields
        fields = fields + extra_fields
    
    return Page(
        key=key,
        entity="employees",
        domain=domain,
        path=path,
        title="Employee",
        permissions=permissions,
        blocks=[
            FormBlock(
                submit_to=submit_to,
                method=method,
                title=title,
                description="Lengkapi data employee dengan benar",
                redirect_to={"page": redirect_page},
                fields=fields,
                actions=[
                    Action(type="submit", label="Save"),
                    Action(type="redirect", label="Cancel", to=path.rsplit("/", 2)[0],)
                ],
            )
        ],
    )
