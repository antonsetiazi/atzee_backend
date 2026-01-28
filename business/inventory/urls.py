from django.urls import path, include
from rest_framework.routers import DefaultRouter

from business.inventory.views import (
    WarehouseViewSet,
    StockViewSet,
    StockMovementViewSet,
    StockActionViewSet,
)


router = DefaultRouter()
router.register(r"warehouses", WarehouseViewSet, basename="warehouse")
router.register(r"stock", StockViewSet, basename="stock")
router.register(r"movements", StockMovementViewSet, basename="stock-movement")


stock_action = StockActionViewSet.as_view({
    "post": "stock_in"
})

stock_out_action = StockActionViewSet.as_view({
    "post": "stock_out"
})

stock_adjust_action = StockActionViewSet.as_view({
    "post": "adjust"
})


urlpatterns = [
    path("", include(router.urls)),
    path("actions/stock-in/", stock_action, name="stock-in"),
    path("actions/stock-out/", stock_out_action, name="stock-out"),
    path("actions/adjust/", stock_adjust_action, name="stock-adjust"),
]


"""
Warehouse
| Method | Endpoint                    |
| ------ | --------------------------- |
| GET    | /inventory/warehouses/      |
| GET    | /inventory/warehouses/{id}/ |

Stock (Saldo)
| Method | Endpoint                         |
| ------ | -------------------------------- |
| GET    | /inventory/stock/?warehouse_id=1 |

Stock Ledger
| Method | Endpoint                                                  |
| ------ | --------------------------------------------------------- |
| GET    | /inventory/movements/?product_id=1                        |
| GET    | /inventory/movements/?warehouse_id=1                      |
| GET    | /inventory/movements/?reference_type=SALE&reference_id=10 |

Stock Actions
| Method | Endpoint                      |
| ------ | ----------------------------- |
| POST   | /inventory/actions/stock-in/  |
| POST   | /inventory/actions/stock-out/ |
| POST   | /inventory/actions/adjust/    |

"""