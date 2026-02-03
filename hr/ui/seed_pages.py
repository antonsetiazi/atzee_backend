# hr/ui/seed_pages.py

from hr.employees.ui.pages import UI_PAGES as EMPLOYEE_PAGES

UI_PAGES = [
    *EMPLOYEE_PAGES
]


# UI_PAGES = [
#     # =====================
#     # EMPLOYEES
#     # =====================
#     {
#         "key": "employees.list",
#         "domain": "hr",
#         "entity": "employees",
#         "title": "Employees",
#         "permissions": ["hr.employees.view"],
#         "blocks": [
#             {
#                 "type": "table",
#                 "data_source": "/api/hr/employees/",
#                 "columns": [
#                     {"key": "employee_id", "label": "ID"},
#                     {"key": "full_name", "label": "Full Name"},
#                     {"key": "department", "label": "Department"},
#                     {"key": "position", "label": "Position"},
#                     {"key": "is_active", "label": "Active"},
#                 ],
#             }
#         ],
#     },

#     # =====================
#     # ATTENDANCE
#     # =====================
#     {
#         "key": "attendance.list",
#         "domain": "hr",
#         "entity": "attendance",
#         "title": "Attendance",
#         "permissions": ["hr.attendance.view"],
#         "blocks": [
#             {
#                 "type": "table",
#                 "data_source": "/api/hr/attendance/",
#                 "columns": [
#                     {"key": "employee", "label": "Employee"},
#                     {"key": "date", "label": "Date"},
#                     {"key": "check_in", "label": "Check In"},
#                     {"key": "check_out", "label": "Check Out"},
#                     {"key": "status", "label": "Status"},
#                 ],
#             }
#         ],
#     },

#     # =====================
#     # PAYROLL
#     # =====================
#     {
#         "key": "payroll.list",
#         "domain": "hr",
#         "entity": "payroll",
#         "title": "Payroll",
#         "permissions": ["hr.payroll.view"],
#         "blocks": [
#             {
#                 "type": "table",
#                 "data_source": "/api/hr/payroll/",
#                 "columns": [
#                     {"key": "employee", "label": "Employee"},
#                     {"key": "period", "label": "Period"},
#                     {"key": "basic_salary", "label": "Basic Salary"},
#                     {"key": "allowances", "label": "Allowances"},
#                     {"key": "deductions", "label": "Deductions"},
#                     {"key": "net_salary", "label": "Net Salary"},
#                 ],
#             }
#         ],
#     },

#     # =====================
#     # ASSETS
#     # =====================
#     {
#         "key": "assets.list",
#         "domain": "hr",
#         "entity": "assets",
#         "title": "Assets",
#         "permissions": ["hr.assets.view"],
#         "blocks": [
#             {
#                 "type": "table",
#                 "data_source": "/api/hr/assets/",
#                 "columns": [
#                     {"key": "asset_id", "label": "Asset ID"},
#                     {"key": "name", "label": "Asset Name"},
#                     {"key": "category", "label": "Category"},
#                     {"key": "assigned_to", "label": "Assigned To"},
#                     {"key": "status", "label": "Status"},
#                 ],
#             }
#         ],
#     },
# ]
