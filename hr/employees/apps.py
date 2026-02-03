from django.apps import AppConfig


class EmployeesConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "hr.employees"
    label = "hr_employees"

    def ready(self):    
        from core.entities.registry import register_entity
        from .entities.employee_list import EmployeeListEntity
        from .entities.employee_create import EmployeesCreateEntity

        register_entity(EmployeeListEntity())
        register_entity(EmployeesCreateEntity())