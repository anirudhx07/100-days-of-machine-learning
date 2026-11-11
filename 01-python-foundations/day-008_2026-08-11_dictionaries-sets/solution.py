"""Day 008: Dictionaries Sets

Reference solution for the 100 Days of Machine Learning learning plan.
Scheduled date in folder: 2026-08-11. This file is populated now; it does not
assert that this work was completed on the scheduled date.
"""

sentence = "machine learning uses data and machine learning builds models"
frequency: dict[str, int] = {}
for word in sentence.split():
    frequency[word] = frequency.get(word, 0) + 1
print("Word counts:", frequency)
print("Unique words:", sorted(set(sentence.split())))

student = {"name": "Mira", "marks": [82, 91, 88]}
student["average"] = sum(student["marks"]) / len(student["marks"])
print(student)
