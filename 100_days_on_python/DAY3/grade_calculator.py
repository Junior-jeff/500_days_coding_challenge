#!/usr/bin/env python3

# Student Gradebook Analyzer
# - Allows input of multiple student names and their scores across 3 subjects.
# - Stores data in a dictionary: {student_name: [score1, score2, score3]}
# - Validates that all scores are between 0–100.
# - Calculates average, highest and lowest scores using a for loop.
# - Prints a report using format specifiers.
# - Keeps asking until the user types 'done'.

gradebook = {}

while True:
    name = input("Enter student name (or type 'done' to finish): ").strip()
    if name.lower() == 'done':
        break

    scores_input = input("Enter 3 scores separated by commas (e.g. 75, 88, 92): ")
    scores = [s.strip() for s in scores_input.split(",")]

    if len(scores) != 3 or not all(score.isdigit() for score in scores):
        print("Please enter exactly 3 valid numbers.\n")
        continue

    scores = [int(score) for score in scores]

    if not all(0 <= s <= 100 for s in scores):
        print("Scores must be between 0 and 100.\n")
        continue

    gradebook[name] = scores
    print(f"{name}'s scores recorded!\n")

print("\nSTUDENT REPORT")
print("-" * 40)

for student, scores in gradebook.items():
    total = sum(scores)
    avg = total / 3
    high = max(scores)
    low = min(scores)

    print("Name    : {:<15}".format(student))
    print("Scores  : {}".format(", ".join(f"{s:>3}" for s in scores)))
    print("Average : {:>6.2f}".format(avg))
    print("Highest : {:>6}".format(high))
    print("Lowest  : {:>6}".format(low))
    print("-" * 40)

