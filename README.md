# Cash flow timing: a 13-week worked example

A small, transparent Python example showing why a profitable business can have a cash shortage when customer collections slip. All figures are hypothetical USD amounts. No client workbooks, client data, credentials or proprietary engagements are included.

## The decision the example exposes

Opening cash is $100,000 and management's operating reserve is $60,000. The first four weeks contain the following cash movements; weeks 5–13 each have $100,000 receipts and $100,000 payments solely to complete the illustrative horizon.

| Week | Base receipts | Payments | Base closing cash | Closing cash with collection delay |
| --- | ---: | ---: | ---: | ---: |
| 1 | 90,000 | 110,000 | 80,000 | 80,000 |
| 2 | 95,000 | 125,000 | 50,000 | -10,000 |
| 3 | 120,000 | 85,000 | 85,000 | 25,000 |
| 4 | 105,000 | 100,000 | 90,000 | 90,000 |

The downside moves $60,000 of receipts from week 2 to week 4. Total receipts are unchanged, but week 2 becomes negative. The base case already breaches the $60,000 reserve by $10,000. In the downside, the same reserve gap is $70,000: $60,000 desired reserve minus negative $10,000 cash.

A reserve breach and negative cash answer different questions. Neither is a forecast of insolvency or a recommendation to borrow. A financing decision also needs actual payment dates, committed facilities, covenants, restrictions and management actions.

## Run locally

Python 3, standard library only. No package installation, login, network request or file upload is required.

```sh
python cash_flow.py
python -m unittest -v
```

The function accepts positive receipts/payments and signed net financing. It preserves negative cash balances, rejects nonfinite inputs and mismatched horizons, and uses Decimal arithmetic. Financing is kept separate from operating receipts; it is not a balancing plug.

## Model review checks illustrated

- Every week's opening cash equals the preceding closing cash.
- Closing cash equals opening cash + receipts - payments + net financing.
- A receipt delayed within the horizon changes timing, not cumulative receipts.
- Reserve gaps are measured against a documented management assumption.
- Cash exactly equal to the reserve is not a breach.
- Missing or invalid inputs must not silently become a clean forecast.

This deliberately small example does not contain invoice aging, intraday liquidity, tax logic, interest calculations, restricted cash, currency translation, bank reconciliation or a live accounting connection. Use a company-specific model and professional review for an actual business decision. Weekly closing cash can hide a cash shortage within the week.

## Author and further explanation

Shahzaib Khalid — Independent Financial Modeling & Valuation Consultant, Lahore, Pakistan.

Read the [13-week cash flow forecasting guide](https://www.shahzaibkhalidfinance.com/13-week-cash-flow-forecast-guide/) for the modeling structure and management checks. The [independent model review checklist](https://www.shahzaibkhalidfinance.com/financial-model-review-checklist/) explains related technical checks.

This is educational consulting material, not regulated audit or assurance, investment advice, a financing offer or a client case study.
