# config/urls.py

"""
URL configuration for atzee_backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),

    # --- Core ---
    path("api/auth/", include("core.users.auth.urls")),
    path("api/tenants/", include("core.tenants.urls")),
    path("api/roles/", include("core.roles.urls")),
    path("api/permissions/", include("core.permissions.urls")),
    path("api/ui/", include("core.ui.urls")),
    path("api/entities/", include("core.entities.urls")),
    path("api/dashboard/", include("core.dashboard.urls")),
    path("api/settings/", include("core.settings.urls")),
    path("api/notifications/", include("core.notifications.urls")),
    path("lookups/", include("core.lookups.urls")),

    # --- Business ---
    path("api/business/", include("business.customers.urls")),
    path("api/business/", include("business.products.urls")),
    path("api/business/", include("business.inventory.urls")),
    path("api/business/", include("business.partners.urls")),
    path("api/business/", include("business.transactions.urls")),
    path("api/business/", include("business.documents.urls")),
    path("api/business/", include("business.payments.urls")),

    # --- Accounting ---
    path("api/accounting/", include("accounting.chart_of_accounts.urls")),
    path("api/accounting/", include("accounting.journals.urls")),
    path("api/accounting/", include("accounting.financial_reports.urls")),

    # --- HR ---
    path("api/hr/", include("hr.employees.urls")),
    path("api/hr/", include("hr.attendance.urls")),

    # --- Verticals ---
    path("api/verticals/apotek/", include("verticals.apotek.api.urls")),
]
