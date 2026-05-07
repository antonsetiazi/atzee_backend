# accounting/enum/permissions.py

from enum import Enum

class AccountingPermission(str, Enum):

    ACCOUNT_LIST_SELECT = "accounting.account.list.select"
    JOURNAL_CREATE = "accounting.journal.create"
    JOURNAL_VIEW = "accounting.journal.view"
    ACCOUNT_VIEW = "accounting.account.view"

    ADMIN_ACCOUNT_VIEW = "accounting.admin.account.view"
    ADMIN_ACCOUNT_CREATE = "accounting.admin.account.create"
    ADMIN_ACCOUNT_EDIT = "accounting.admin.account.edit"
    ADMIN_ACCOUNT_DELETE = "accounting.admin.account.delete"
    ADMIN_ACCOUNT_DETAIL = "accounting.admin.account.detail"

    ADMIN_REPORT_VIEW = "accounting.admin.report.view"


    def __str__(self):
        return self.value
