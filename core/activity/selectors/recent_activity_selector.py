# core/activity/selectors/recent_activity_selector.py

from django.utils.timesince import timesince

from core.activity.models import Activity


def get_recent_activities(
    *,
    tenant,
    limit=10,
):
    recent_activities = (
        Activity.objects.filter(
            tenant=tenant,
            is_deleted=False,
        )
        .select_related("actor", "created_by")
        .order_by("-created_at")[:limit]
    )

    results = []

    for item in recent_activities:

        # =========================================
        # ACTIVITY TYPE MAPPING
        # =========================================
        activity_type = "journal"

        if "invoice" in item.event:
            activity_type = "invoice"

        elif "payment" in item.event:
            activity_type = "payment"

        elif "asset" in item.event:
            activity_type = "asset"

        elif "cash" in item.event:
            activity_type = "cashflow"

        # =========================================
        # HUMAN TIME
        # =========================================
        human_time = f"{timesince(item.created_at)} ago"

        results.append(
            {
                "id": str(item.id),
                "title": item.title,
                "description": item.description,
                "time": human_time,
                "type": activity_type,
            }
        )

    return results
