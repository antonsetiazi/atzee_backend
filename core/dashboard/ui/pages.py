from core.ui.schema.page import Page
from core.ui.schema.block import StatBlock, ChartBlock, ShortcutBlock, ShortcutItem
# from core.ui.schema.action import Action

UI_PAGES = [
    Page(
        key="core.dashboard",
        entity="dashboard",
        domain="core",
        path="/dashboard",
        title="Dashboard",
        permissions="core.dashboard.view",
        blocks=[
            ShortcutBlock(
                # title="Quick Actions",
                items=[
                    ShortcutItem(key="customers", label="Customers", icon="user-check", to="/business/customers"),
                    ShortcutItem(key="products", label="Products", icon="box", to="/business/products"),
                    ShortcutItem(key="sales", label="Sales", icon="shopping-cart", to="/business/sales"),
                    ShortcutItem(key="reports", label="Reports", icon="chart-line", to="/business/reports"),
                    ShortcutItem(key="partners", label="Partners", icon="user-check", to="/business/partners"),
                ]
            ),
            StatBlock(
                key="total_customers",
                title="Total Customers",
                value=120,
                size="sm",
            ),
            StatBlock(
                key="active_orders",
                title="Active Orders",
                value=35,
                size="sm",
            ),
            ChartBlock(
                key="sales_chart",
                title="Sales This Month",
                value={
                    "labels": ["Week 1", "Week 2", "Week 3", "Week 4"],
                    "datasets": [
                        {"label": "Revenue", "data": [5000, 7000, 6500, 8000]}
                    ],
                },
                size="lg",
            ),
            StatBlock(
                key="active_orders",
                title="Active Orders",
                value=45,
                size="sm",
            ),
            # ChartBlock(
            #     key="purchase_chart",
            #     title="Purchase This Month",
            #     value={
            #         "labels": ["Week 1", "Week 2", "Week 3", "Week 4"],
            #         "datasets": [
            #             {"label": "Revenue", "data": [5000, 7000, 6500, 8000]}
            #         ],
            #     },
            #     size="lg",
            # ),
        ],
    ),
]