"""Educational weekly cash roll-forward; hypothetical inputs, no external services."""
from decimal import Decimal, InvalidOperation


def amount(value):
    try:
        number = Decimal(str(value))
    except InvalidOperation as error:
        raise ValueError("Amounts must be finite numbers") from error
    if not number.is_finite():
        raise ValueError("Amounts must be finite numbers")
    return number


def forecast(opening_cash, receipts, payments, reserve=0, financing=None):
    """Use positive receipts/payments; financing is signed net external cash flow.

    Breaches are tested at week-end only. No automatic borrowing is assumed.
    Equality to the reserve is not a breach. Negative cash is reported, not floored.
    """
    receipts, payments = list(receipts), list(payments)
    if not receipts or len(receipts) != len(payments):
        raise ValueError("Receipts and payments need matching, nonempty horizons")
    financing = [0] * len(receipts) if financing is None else list(financing)
    if len(financing) != len(receipts):
        raise ValueError("Financing must match the forecast horizon")
    cash, floor = amount(opening_cash), amount(reserve)
    if floor < 0:
        raise ValueError("Reserve must be nonnegative")
    rows = []
    for week, (received, paid, funded) in enumerate(zip(receipts, payments, financing), 1):
        received, paid, funded = map(amount, (received, paid, funded))
        if min(received, paid) < 0:
            raise ValueError("Use positive receipts and payments")
        closing = cash + received - paid + funded
        rows.append(dict(week=week, opening=cash, receipts=received, payments=paid,
                         financing=funded, closing=closing,
                         reserve_gap=max(floor - closing, Decimal(0))))
        cash = closing
    return rows


if __name__ == "__main__":
    base_receipts = [90_000, 95_000, 120_000, 105_000] + [100_000] * 9
    payments = [110_000, 125_000, 85_000, 100_000] + [100_000] * 9
    delayed = base_receipts.copy()
    delayed[1] -= 60_000
    delayed[3] += 60_000
    for label, receipts in (("BASE", base_receipts), ("COLLECTION DELAY", delayed)):
        rows = forecast(100_000, receipts, payments, reserve=60_000)
        first_breach = next((r["week"] for r in rows if r["reserve_gap"] > 0), None)
        first_negative = next((r["week"] for r in rows if r["closing"] < 0), None)
        print(label, "first reserve breach:", first_breach,
              "first negative week:", first_negative,
              "lowest week-end cash:", min(r["closing"] for r in rows))
        for r in rows:
            print(r["week"], r["opening"], r["receipts"], r["payments"], r["closing"])
