# verticals/pesantren/seeds/navigation.py

NAVIGATION_SEED = [

    # ========================================
    # DESKTOP SIDEBAR — OWNER (Level 100)
    # ========================================
    {
        "tenant_code": None,
        "role": "Owner",
        "type": "sidebar",
        "device": "desktop",
        "app": "pesantren",
        "items": [
            {"action_type": "page", "target": "pesantren.dashboard", "icon": "home", "route": "/pesantren/dashboard", "label": "Dashboard"},
            {"action_type": "page", "target": "pesantren.santri", "icon": "users", "route": "/pesantren/santri", "label": "Santri"},
            {"action_type": "page", "target": "pesantren.asrama", "icon": "building", "route": "/pesantren/asrama", "label": "Asrama"},
            {"action_type": "page", "target": "pesantren.akademik", "icon": "book-open", "route": "/pesantren/akademik", "label": "Akademik"},
            {"action_type": "page", "target": "pesantren.tahfidz", "icon": "book", "route": "/pesantren/tahfidz", "label": "Tahfidz"},
            {"action_type": "page", "target": "pesantren.keuangan", "icon": "credit-card", "route": "/pesantren/keuangan", "label": "Keuangan Santri"},
            {"action_type": "page", "target": "business.accounting", "icon": "bar-chart", "route": "/business/accounting", "label": "Accounting"},
            {"action_type": "page", "target": "pesantren.disiplin", "icon": "shield", "route": "/pesantren/disiplin", "label": "Disiplin & Izin"},
            {"action_type": "page", "target": "pesantren.donatur", "icon": "heart", "route": "/pesantren/donatur", "label": "Donatur & Wakaf"},
            {"action_type": "page", "target": "business.asset", "icon": "layers", "route": "/business/asset", "label": "Asset"},
            {"action_type": "page", "target": "core.users", "icon": "settings", "route": "/core/users", "label": "Users & Roles"},
        ],
    },

    # ========================================
    # DESKTOP SIDEBAR — MUDHIR (Level 90)
    # ========================================
    {
        "tenant_code": None,
        "role": "Mudhir",
        "type": "sidebar",
        "device": "desktop",
        "app": "pesantren",
        "items": [
            {"action_type": "page", "target": "pesantren.dashboard", "icon": "home", "route": "/pesantren/dashboard", "label": "Dashboard"},
            {"action_type": "page", "target": "pesantren.santri", "icon": "users", "route": "/pesantren/santri", "label": "Santri"},
            {"action_type": "page", "target": "pesantren.akademik", "icon": "book-open", "route": "/pesantren/akademik", "label": "Akademik"},
            {"action_type": "page", "target": "pesantren.tahfidz", "icon": "book", "route": "/pesantren/tahfidz", "label": "Tahfidz"},
            {"action_type": "page", "target": "pesantren.disiplin", "icon": "shield", "route": "/pesantren/disiplin", "label": "Disiplin & Izin"},
            {"action_type": "page", "target": "pesantren.reports", "icon": "bar-chart", "route": "/pesantren/reports", "label": "Reports"},
        ],
    },

    # ========================================
    # DESKTOP SIDEBAR — BENDAHARA (Level 80)
    # ========================================
    {
        "tenant_code": None,
        "role": "Bendahara",
        "type": "sidebar",
        "device": "desktop",
        "app": "pesantren",
        "items": [
            {"action_type": "page", "target": "pesantren.dashboard_keuangan", "icon": "activity", "route": "/pesantren/keuangan/dashboard", "label": "Dashboard Keuangan"},
            {"action_type": "page", "target": "pesantren.keuangan", "icon": "credit-card", "route": "/pesantren/keuangan", "label": "Tagihan & Pembayaran"},
            {"action_type": "page", "target": "business.accounting", "icon": "book-open", "route": "/business/accounting", "label": "Jurnal & Buku Kas"},
            {"action_type": "page", "target": "pesantren.donatur", "icon": "heart", "route": "/pesantren/donatur", "label": "Donasi & Wakaf"},
        ],
    },

    # ========================================
    # DESKTOP SIDEBAR — STAFF ADMIN (Level 70)
    # ========================================
    {
        "tenant_code": None,
        "role": "Staff Admin",
        "type": "sidebar",
        "device": "desktop",
        "app": "pesantren",
        "items": [
            {"action_type": "page", "target": "pesantren.santri", "icon": "users", "route": "/pesantren/santri", "label": "Data Santri"},
            {"action_type": "page", "target": "pesantren.pendaftaran", "icon": "user-plus", "route": "/pesantren/pendaftaran", "label": "Pendaftaran"},
            {"action_type": "page", "target": "pesantren.keuangan", "icon": "credit-card", "route": "/pesantren/keuangan", "label": "Keuangan Santri"},
            {"action_type": "page", "target": "pesantren.perizinan", "icon": "clock", "route": "/pesantren/perizinan", "label": "Perizinan"},
            {"action_type": "page", "target": "pesantren.documents", "icon": "file-text", "route": "/pesantren/documents", "label": "Dokumen"},
        ],
    },

    # ========================================
    # DESKTOP SIDEBAR — USTADZ (Level 60)
    # ========================================
    {
        "tenant_code": None,
        "role": "Ustadz",
        "type": "sidebar",
        "device": "desktop",
        "app": "pesantren",
        "items": [
            {"action_type": "page", "target": "pesantren.dashboard_mengajar", "icon": "home", "route": "/pesantren/mengajar/dashboard", "label": "Dashboard"},
            {"action_type": "page", "target": "pesantren.jadwal", "icon": "calendar", "route": "/pesantren/jadwal", "label": "Jadwal Mengajar"},
            {"action_type": "page", "target": "pesantren.absensi", "icon": "check-square", "route": "/pesantren/absensi", "label": "Absensi"},
            {"action_type": "page", "target": "pesantren.nilai", "icon": "edit-3", "route": "/pesantren/nilai", "label": "Input Nilai"},
            {"action_type": "page", "target": "pesantren.tahfidz", "icon": "book", "route": "/pesantren/tahfidz", "label": "Tahfidz"},
        ],
    },

    # ========================================
    # DESKTOP SIDEBAR — MUSYRIF (Level 60)
    # ========================================
    {
        "tenant_code": None,
        "role": "Musyrif",
        "type": "sidebar",
        "device": "desktop",
        "app": "pesantren",
        "items": [
            {"action_type": "page", "target": "pesantren.dashboard_asrama", "icon": "home", "route": "/pesantren/asrama/dashboard", "label": "Dashboard Asrama"},
            {"action_type": "page", "target": "pesantren.asrama_santri", "icon": "users", "route": "/pesantren/asrama/santri", "label": "Santri Asrama"},
            {"action_type": "page", "target": "pesantren.absensi_asrama", "icon": "check-square", "route": "/pesantren/asrama/absensi", "label": "Absensi Asrama"},
            {"action_type": "page", "target": "pesantren.disiplin", "icon": "shield", "route": "/pesantren/disiplin", "label": "Disiplin"},
            {"action_type": "page", "target": "pesantren.perizinan", "icon": "clock", "route": "/pesantren/perizinan", "label": "Perizinan"},
        ],
    },

    # ========================================
    # DESKTOP SIDEBAR — WALI SANTRI (Level 30)
    # ========================================
    {
        "tenant_code": None,
        "role": "Wali Santri",
        "type": "sidebar",
        "device": "desktop",
        "app": "pesantren",
        "items": [
            {"action_type": "page", "target": "pesantren.portal_dashboard", "icon": "home", "route": "/pesantren/portal/dashboard", "label": "Dashboard"},
            {"action_type": "page", "target": "pesantren.portal_nilai", "icon": "book-open", "route": "/pesantren/portal/nilai", "label": "Nilai"},
            {"action_type": "page", "target": "pesantren.portal_tahfidz", "icon": "book", "route": "/pesantren/portal/tahfidz", "label": "Tahfidz"},
            {"action_type": "page", "target": "pesantren.portal_keuangan", "icon": "credit-card", "route": "/pesantren/portal/keuangan", "label": "Tagihan & Pembayaran"},
            {"action_type": "page", "target": "pesantren.portal_perizinan", "icon": "clock", "route": "/pesantren/portal/perizinan", "label": "Ajukan Izin"},
        ],
    },

    # ========================================
    # DESKTOP SIDEBAR — SANTRI (Level 20)
    # ========================================
    {
        "tenant_code": None,
        "role": "Santri",
        "type": "sidebar",
        "device": "desktop",
        "app": "pesantren",
        "items": [
            {"action_type": "page", "target": "pesantren.santri_dashboard", "icon": "home", "route": "/pesantren/santri/dashboard", "label": "Dashboard"},
            {"action_type": "page", "target": "pesantren.santri_jadwal", "icon": "calendar", "route": "/pesantren/santri/jadwal", "label": "Jadwal"},
            {"action_type": "page", "target": "pesantren.santri_nilai", "icon": "book-open", "route": "/pesantren/santri/nilai", "label": "Nilai"},
            {"action_type": "page", "target": "pesantren.santri_tahfidz", "icon": "book", "route": "/pesantren/santri/tahfidz", "label": "Progres Hafalan"},
            {"action_type": "page", "target": "pesantren.santri_tabungan", "icon": "credit-card", "route": "/pesantren/santri/tabungan", "label": "Tabungan"},
            {"action_type": "page", "target": "pesantren.santri_perizinan", "icon": "clock", "route": "/pesantren/santri/perizinan", "label": "Ajukan Izin"},
        ],
    },

]