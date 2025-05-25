from pay.order import LineItem, Order, OrderStatus


def test_empty_order_total() -> None:
    order = Order()
    assert order.total == 0


def test_order_total() -> None:
    order = Order()
    order.line_items.append(LineItem(name="Test", price=100))
    assert order.total == 100


def test_orders_total() -> None:
    order = Order()
    order.line_items.append(LineItem(name="Test", price=100))
    order.line_items.append(LineItem(name="Test", price=100))
    order.line_items.append(LineItem(name="Test", price=100))
    assert order.total == 300

def test_order_pay_status() -> None:
    order = Order()
    order.pay()
    assert order.status == OrderStatus.PAID