# verticals/pesantren/enum/permissions.py

from enum import Enum

class PesantrenPermission(str, Enum):

    OWNER_DASHBOARD_VIEW = "pesantren.owner.dashboard.view"
    MUDHIR_DASHBOARD_VIEW = "pesantren.mudhir.dashboard.view"
    USTADZ_DASHBOARD_VIEW = "pesantren.ustadz.dashboard.view"
    MUSYRIF_DASHBOARD_VIEW = "pesantren.musyrif.dashboard.view"
    STAFF_ADMIN_DASHBOARD_VIEW = "pesantren.staff.admin.dashboard.view"
    BENDAHARA_DASHBOARD_VIEW = "pesantren.bendahara.dashboard.view"
    WALI_DASHBOARD_VIEW = "pesantren.wali.dashboard.view"
    SANTRI_DASHBOARD_VIEW = "pesantren.santri.dashboard.view"


    def __str__(self):
        return self.value