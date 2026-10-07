from app.orders import order_total


def test_order_total_sums_line_items():
    assert order_total([{"price": 5, "qty": 2}, {"price": 1, "qty": 3}]) == 13
