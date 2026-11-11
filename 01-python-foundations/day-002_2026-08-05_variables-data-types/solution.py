"""Day 002: Variables Data Types

Reference solution for the 100 Days of Machine Learning learning plan.
Scheduled date in folder: 2026-08-05. This file is populated now; it does not
assert that this work was completed on the scheduled date.
"""

student_name = "Aarav"
semester = 3
cgpa = 8.42
is_enrolled = True

profile = {"name": student_name, "semester": semester, "cgpa": cgpa, "enrolled": is_enrolled}
for key, value in profile.items():
    print(f"{key}: {value!r} ({type(value).__name__})")

# Explicit conversion: input() always returns text.
credits_text = "24"
credits = int(credits_text)
print("Credits next semester:", credits + 2)
