"""Day 007: Lists Tuples

Reference solution for the 100 Days of Machine Learning learning plan.
Scheduled date in folder: 2026-08-10. This file is populated now; it does not
assert that this work was completed on the scheduled date.
"""

scores = [72, 88, 91, 88, 67, 72]
# dict.fromkeys preserves first-seen order while removing duplicates.
unique_scores = list(dict.fromkeys(scores))
print("Unique scores:", unique_scores)
print("First three:", scores[:3])
print("Last two:", scores[-2:])

coordinates = (28.6139, 77.2090)  # tuple: fixed latitude and longitude
latitude, longitude = coordinates
print("Latitude:", latitude, "Longitude:", longitude)
