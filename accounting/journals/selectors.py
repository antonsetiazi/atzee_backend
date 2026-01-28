from django.db.models import QuerySet
from accounting.journals.models import Journal
from core.tenants.models import Tenant
from accounting.journals.constants import JournalStatus


def get_journal_queryset(*, tenant: Tenant) -> QuerySet[Journal]:
    return Journal.objects.filter(
        tenant=tenant,
        is_deleted=False
    )


def get_journal_by_id(
    *, 
    tenant: Tenant, 
    journal_id: int
) -> Journal | None:
    try:
        return get_journal_queryset(tenant=tenant).get(id=journal_id)
    except Journal.DoesNotExist:
        return None
    

def get_posted_journals(*, tenant: Tenant) -> QuerySet[Journal]:
    return get_journal_queryset(tenant=tenant).filter(
        status=JournalStatus.POSTED
    )