"""Read fictional billing records and print a small report."""

import csv
import sys
from decimal import Decimal

from billing_app.config import PROJECT_ROOT, validate_config


def load_rows(path):
    """Read invoices and convert monetary values to exact decimals."""
    with path.open(encoding="utf-8", newline="") as csv_file:
        rows = list(csv.DictReader(csv_file))
    for row in rows:
        row["amount"] = Decimal(row["amount"])
        row["paid"] = Decimal(row["paid"])
    return rows


def build_summary(rows):
    """Count invoices and sum billed and paid amounts in EUR."""
    return {
        "rows": len(rows),
        "total_billed": sum((row["amount"] for row in rows), Decimal("0.00")),
        "total_paid": sum((row["paid"] for row in rows), Decimal("0.00")),
    }


def print_report(summary):
    """Display the calculation separately from the calculation logic."""
    print("Billing Report")
    print("--------------")
    print(f"Rows: {summary['rows']}")
    print(f"Total billed (EUR): {summary['total_billed']:.2f}")
    print(f"Total paid (EUR): {summary['total_paid']:.2f}")


def main():
    try:
        validate_config()
        rows = load_rows(PROJECT_ROOT / "data" / "billing.csv")
    except (ValueError, OSError) as error:
        print(f"Error: {error}", file=sys.stderr)
        return 1
    print_report(build_summary(rows))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
