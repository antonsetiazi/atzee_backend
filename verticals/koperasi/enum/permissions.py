# verticals/koperasi/enum/permissions.py

from enum import Enum

class KoperasiPermission(str, Enum):

    KETUA_DASHBOARD_VIEW = "koperasi.ketua.dashboard.view"
    BENDAHARA_DASHBOARD_VIEW = "koperasi.bendahara.dashboard.view"
    PENGAWAS_DASHBOARD_VIEW = "koperasi.pengawas.dashboard.view"
    STAFF_DASHBOARD_VIEW = "koperasi.staff.dashboard.view"
    MEMBER_DASHBOARD_VIEW = "koperasi.member.dashboard.view"


    def __str__(self):
        return self.value