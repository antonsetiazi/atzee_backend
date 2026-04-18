# core/enum/permissions.py

from enum import Enum

class CorePermission(str, Enum):
    ACCOUNT_ADDRESS_CREATE = "core.account.address.create"
    ACCOUNT_ADDRESS_UPDATE = "core.account.address.update"

    ACCOUNT_PASSWORD_UPDATE = "core.account.password.update"

    ACCOUNT_PROFILE_VIEW = "core.account.profile.view"
    ACCOUNT_PROFILE_UPDATE = "core.account.profile.update"

    ACCOUNT_SETTINGS_VIEW = "core.account.settings.view"
    ACCOUNT_SETTINGS_UPDATE = "core.account.settings.update"

    CLASSIFICATIONS_TAGS_VIEW = "core.classifications.tags.view"

    DASHBOARD_VIEW = "core.dashboard.view"

    FILES_VIEW = "core.files.view"

    GEO_SPATIAL_VIEW = "core.geo.spatial.view"

    NOTIFICATION_VIEW = "core.notification.view"

    TAGS_VIEW = "core.tags.view"

    TIMEZONES_VIEW = "core.timezones.view"

    USER_WALLET_VIEW = "core.user.wallet.view"
    ADMIN_WALLET_WITHDRAWAL_VIEW = "core.admin.wallet.withdrawal.view"
    ADMIN_WALLET_WITHDRAWAL_APPROVE = "core.admin.wallet.withdrawal.approve"
    ADMIN_WALLET_TRANSACTIONS_VIEW = "core.admin.wallet.transactions.view"
    ADMIN_USERS_VIEW = "core.admin.users.view"
    ADMIN_WIDGETS_VIEW = "core.admin.widgets.view"
    CATEGORIES_VIEW = "core.categories.view"
    
    ADMIN_BANK_VIEW = "core.admin.bank.view"
    ADMIN_BANK_CREATE = "core.admin.bank.create"
    ADMIN_BANK_EDIT = "core.admin.bank.edit"


    def __str__(self):
        return self.value
