# core/dashboard/registry.py

from .schema import DashboardWidget

DASHBOARD_REGISTRY = {
    "default": [
        DashboardWidget(
            key="total_users",
            type="stat",
            title="Total Users",
            source={
                "service": "dashboard.total_users"
            },
            size="sm",
            permission="core.users.view",
            meta={
                "format": "number",
                "suffix": "users",
            },
        ),
        DashboardWidget(
            key="active_users",
            type="stat",
            title="Active Users",
            source={
                "service": "dashboard.active_users"
            },
            size="sm",
            permission="core.users.view",
        ),
        DashboardWidget(
            key="total_products",
            type="stat",
            title="Total Products",
            source={
                "service": "dashboard.total_products"
            },
            size="sm",
            permission="business.products.view",
        ),
        DashboardWidget(
            key="users_growth",
            type="chart",
            title="User Growth",
            source={
                "service": "dashboard.users_growth_by_month"
            },
            size="lg",
            permission="core.users.view",
        ),
        DashboardWidget(
            key="recent_users",
            type="table",
            title="Recent Users",
            source={
                "service": "dashboard.recent_users",
                "params": {"limit": 5},
            },
            size="lg",
            permission="core.users.view",
        ),
    ],

    "business": [
        DashboardWidget(
            key="total_products",
            type="stat",
            title="Total Products",
            source={"service": "dashboard.total_products"},
            size="sm",
            permission="business.products.view",
        ),
        DashboardWidget(
            key="recent_users",
            type="table",
            title="Recent Users",
            source={
                "service": "dashboard.recent_users",
                "params": {"limit": 5},
            },
            size="lg",
            permission="core.users.view",
        ),
    ],

    "accounting": [
        DashboardWidget(
            key="users_growth",
            type="chart",
            title="User Growth",
            source={"service": "dashboard.users_growth_by_month"},
            size="lg",
            permission="core.users.view",
        ),
    ],

    "hrms": [
        DashboardWidget(
            key="active_users",
            type="stat",
            title="Active Employees",
            source={"service": "dashboard.active_users"},
            size="sm",
            permission="core.users.view",
        ),
        DashboardWidget(
            key="recent_users",
            type="table",
            title="New Employees",
            source={
                "service": "dashboard.recent_users",
                "params": {"limit": 10},
            },
            size="lg",
            permission="core.users.view",
        ),
    ],
}
