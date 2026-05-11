# accounting/services/depreciation_batch_service.py

from accounting.models import FixedAsset
from accounting.services.depreciation_service import (
    DepreciationService,
)


class DepreciationBatchService:

    @staticmethod
    def run_monthly_depreciation(
        *,
        tenant,
        user,
        period_date,
    ):

        assets = FixedAsset.objects.filter(
            tenant=tenant,
            status="active",
            is_deleted=False,
        )

        success_count = 0

        failed = []

        for asset in assets:

            try:

                DepreciationService.run_asset_depreciation(
                    asset=asset,
                    period_date=period_date,
                    user=user,
                )

                success_count += 1

            except Exception as e:

                failed.append(
                    {
                        "asset_id": str(asset.id),
                        "asset_number": asset.asset_number,
                        "error": str(e),
                    }
                )

        return {
            "success": True,
            "processed": success_count,
            "failed_count": len(failed),
            "failed": failed,
        }
