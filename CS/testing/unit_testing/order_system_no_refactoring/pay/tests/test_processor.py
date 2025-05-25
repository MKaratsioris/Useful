import pytest
from pay.processor import PaymentProcessor

API_KEY: str = "6cfb67f3-6281-4031-b893-ea85db0dce20"
VALID_CARD_NUMBER: str = "1249190007575069"
INVALID_CARD_NUMBER: str = f"{int(VALID_CARD_NUMBER) - 1}"


def test_invalid_api_key() -> None:
    with pytest.raises(ValueError, match="Invalid API key"):
        payment_processor = PaymentProcessor("")
        payment_processor.charge(VALID_CARD_NUMBER, 12, 2094, 100)


def test_card_number_valid_date():
    payment_processor = PaymentProcessor(API_KEY)
    assert payment_processor.validate_card(VALID_CARD_NUMBER, 12, 2094)


def test_card_number_invalid_date():
    payment_processor = PaymentProcessor(API_KEY)
    assert not payment_processor.validate_card(VALID_CARD_NUMBER, 12, 1900)


def test_card_number_invalid_luhn():
    payment_processor = PaymentProcessor(API_KEY)
    assert not payment_processor.luhn_checksum(INVALID_CARD_NUMBER)


def test_card_number_valid_luhn():
    payment_processor = PaymentProcessor(API_KEY)
    assert payment_processor.luhn_checksum(VALID_CARD_NUMBER)


def test_charge_card_valid():
    payment_processor = PaymentProcessor(API_KEY)
    payment_processor.charge(VALID_CARD_NUMBER, 12, 2094, 100)


def test_charge_card_invalid():
    with pytest.raises(ValueError):
        payment_processor = PaymentProcessor(API_KEY)
        payment_processor.charge(INVALID_CARD_NUMBER, 12, 2094, 100)