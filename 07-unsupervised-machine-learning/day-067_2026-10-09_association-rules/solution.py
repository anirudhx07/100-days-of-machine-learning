"""Day 067: Association Rules

Reference solution for the 100 Days of Machine Learning learning plan.
Scheduled date in folder: 2026-10-09. This file is populated now; it does not
assert that this work was completed on the scheduled date.
"""

from itertools import combinations

transactions = [
    {"bread", "milk"}, {"bread", "diapers", "beer", "eggs"},
    {"milk", "diapers", "beer", "cola"}, {"bread", "milk", "diapers", "beer"},
    {"bread", "milk", "diapers", "cola"},
]
itemsets = sorted(set().union(*transactions))
def support(items):
    return sum(items.issubset(t) for t in transactions) / len(transactions)

for pair in combinations(itemsets, 2):
    pair_set = set(pair)
    sup = support(pair_set)
    if sup == 0:
        continue
    for a in pair:
        b = pair_set - {a}
        confidence = sup / support({a})
        lift = confidence / support(b)
        print(f"{a} -> {next(iter(b))}: support={sup:.2f}, confidence={confidence:.2f}, lift={lift:.2f}")
