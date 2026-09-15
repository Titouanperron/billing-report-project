"""Baseline calculation tests independent of local configuration."""

from decimal import Decimal

from billing_app.report import build_summary


def test_totals_for_two_invoices():
    rows = [
        {"amount": Decimal("120.10"), "paid": Decimal("80.10")},
        {"amount": Decimal("180.20"), "paid": Decimal("110.20")},
    ]
    assert build_summary(rows) == {
        "rows": 2,
        "total_billed": Decimal("300.30"),
        "total_paid": Decimal("190.30"),
    }


def test_unpaid_invoice():
    rows = [{"amount": Decimal("75.50"), "paid": Decimal("0.00")}]
    assert build_summary(rows) == {
        "rows": 1,
        "total_billed": Decimal("75.50"),
        "total_paid": Decimal("0.00"),
    }


def test_empty_dataset():
    assert build_summary([]) == {
        "rows": 0,
        "total_billed": Decimal("0.00"),
        "total_paid": Decimal("0.00"),
    }
