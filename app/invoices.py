from app.db import run_query


def get_invoice(request, invoice_id):
    rows = run_query("SELECT * FROM invoices WHERE id = ?", (invoice_id,))
    return rows[0] if rows else None
