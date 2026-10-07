from app.auth import require_login
from app.db import run_query


def refund_status(request, order_id):
    require_login(request)
    return run_query("SELECT status FROM refunds WHERE order_id = ?", order_id)
