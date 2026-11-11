"""Day 009: File Handling

Reference solution for the 100 Days of Machine Learning learning plan.
Scheduled date in folder: 2026-08-12. This file is populated now; it does not
assert that this work was completed on the scheduled date.
"""

import csv
from pathlib import Path

file_path = Path("students.csv")
records = [
    {"name": "Asha", "score": 91},
    {"name": "Kabir", "score": 84},
    {"name": "Mira", "score": 96},
]
with file_path.open("w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=["name", "score"])
    writer.writeheader()
    writer.writerows(records)

with file_path.open(encoding="utf-8", newline="") as file:
    for row in csv.DictReader(file):
        print(row["name"], int(row["score"]))
