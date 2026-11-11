"""Day 006: Functions

Reference solution for the 100 Days of Machine Learning learning plan.
Scheduled date in folder: 2026-08-09. This file is populated now; it does not
assert that this work was completed on the scheduled date.
"""

def second_largest(values: list[int]) -> int:
    unique_values = sorted(set(values), reverse=True)
    if len(unique_values) < 2:
        raise ValueError("at least two distinct values are required")
    return unique_values[1]

def celsius_to_fahrenheit(celsius: float) -> float:
    return celsius * 9 / 5 + 32

print("Second largest:", second_largest([4, 9, 2, 9, 7]))
print("25°C in Fahrenheit:", celsius_to_fahrenheit(25))
