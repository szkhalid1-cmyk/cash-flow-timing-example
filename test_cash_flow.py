import unittest
from decimal import Decimal
from cash_flow import forecast


class CashFlowTests(unittest.TestCase):
    def test_collection_delay_creates_temporary_shortfall(self):
        payments = [110000, 125000, 85000, 100000]
        base = forecast(100000, [90000, 95000, 120000, 105000], payments, 60000)
        delayed = forecast(100000, [90000, 35000, 120000, 165000], payments, 60000)
        self.assertEqual([r["closing"] for r in base], [80000, 50000, 85000, 90000])
        self.assertEqual([r["closing"] for r in delayed], [80000, -10000, 25000, 90000])
        self.assertEqual(base[1]["reserve_gap"], 10000)
        self.assertEqual(delayed[1]["reserve_gap"], 70000)
        self.assertEqual(delayed[2]["opening"], delayed[1]["closing"])

    def test_financing_timing_and_decimal_precision(self):
        rows = forecast("0.10", ["0.20", 0], ["0.30", 1], financing=[0, "1.25"])
        self.assertEqual(rows[0]["closing"], Decimal("0.00"))
        self.assertEqual(rows[1]["closing"], Decimal("0.25"))
        self.assertEqual(rows[0]["reserve_gap"], 0)

    def test_invalid_inputs_stop_instead_of_hiding_errors(self):
        for args in [(0, [], []), (0, [1], [1, 2]), (0, [-1], [1]),
                     (0, ["NaN"], [0]), (0, ["Infinity"], [0]),
                     (0, [1], [1], -1), (0, [1], [1], 0, [1, 2])]:
            with self.subTest(args=args), self.assertRaises(ValueError):
                forecast(*args)


if __name__ == "__main__":
    unittest.main()
