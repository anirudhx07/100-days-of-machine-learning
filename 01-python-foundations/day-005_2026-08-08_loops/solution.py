"""Day 005: Loops

Reference solution for the 100 Days of Machine Learning learning plan.
Scheduled date in folder: 2026-08-08. This file is populated now; it does not
assert that this work was completed on the scheduled date.
"""

numbers = [12, 7, 19, 4, 8]
total = 0
for value in numbers:
    total += value
print("Total:", total)
print("Average:", total / len(numbers))

countdown = 3
while countdown > 0:
    print(countdown)
    countdown -= 1
print("Go!")
