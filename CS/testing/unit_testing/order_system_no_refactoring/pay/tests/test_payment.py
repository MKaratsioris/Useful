import pytest
from pay.order import LineItem, Order
from pay.payment import pay_order
from pay.processor import PaymentProcessor
from pytest import MonkeyPatch

VALID_CARD_NUMBER: str = "1249190007575069"
INVALID_CARD_NUMBER: str = f"{int(VALID_CARD_NUMBER) - 1}"
MONTH: str = "12"
YEAR: str = "2094"


def test_pay_order(monkeypatch: MonkeyPatch):
    inputs = [VALID_CARD_NUMBER, MONTH, YEAR]
    monkeypatch.setattr("builtins.input", lambda _: inputs.pop(0))
    monkeypatch.setattr(PaymentProcessor, "_check_api_key", lambda _: True)
    order = Order()
    order.line_items.append(LineItem(name="Shoes", price=100_00, quantity=2))
    pay_order(order)


def test_pay_order_invalid(monkeypatch: MonkeyPatch):
    with pytest.raises(ValueError, match="Can't pay an order with total 0."):
        inputs = [INVALID_CARD_NUMBER, MONTH, YEAR]
        monkeypatch.setattr("builtins.input", lambda _: inputs.pop(0))
        monkeypatch.setattr(PaymentProcessor, "_check_api_key", lambda _: True)
        order = Order()
        pay_order(order)