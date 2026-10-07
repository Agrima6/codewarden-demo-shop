from app.auth import require_login
from app.db import run_query


def list_orders(request):
    user = require_login(request)
    return run_query("SELECT id, total, status FROM orders WHERE user_id = ?", (user.id,))


def get_order(request, order_id):
    user = require_login(request)
    rows = run_query("SELECT * FROM orders WHERE id = ? AND user_id = ?", (order_id, user.id))
    return rows[0] if rows else None


def order_total(items):
    return sum(item["price"] * item["qty"] for item in items)


def cancel_order(request, order_id):
    run_query("UPDATE orders SET status = 'cancelled' WHERE id = ?", (order_id,))
    return True
