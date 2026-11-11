"""Day 003: Operators

Reference solution for the 100 Days of Machine Learning learning plan.
Scheduled date in folder: 2026-08-06. This file is populated now; it does not
assert that this work was completed on the scheduled date.
"""

price = 799.0
discount_percent = 15
tax_percent = 18

discounted = price * (1 - discount_percent / 100)
final_price = discounted * (1 + tax_percent / 100)
print(f"Original: ₹{price:.2f}")
print(f"Final after discount and tax: ₹{final_price:.2f}")

quantity = 2
print("Bulk order:", quantity >= 2 and final_price > 500)
