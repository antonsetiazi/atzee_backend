# accounting/selectors/receivable_selectors.py

from accounting.models import ReceivableInvoice


def get_recent_receivable_invoices(*, tenant, limit=5):
    invoices = (
        ReceivableInvoice.objects.filter(tenant=tenant)
        .select_related("customer")
        .order_by("-invoice_date")[:limit]
    )

    results = []

    for invoice in invoices:
        results.append(
            {
                "id": str(invoice.id),
                "customer": invoice.customer.name,
                "invoice": invoice.invoice_number,
                "amount": f"Rp {invoice.total_amount:,.0f}".replace(",", "."),
                "status": invoice.status.title(),
            }
        )

    return results
