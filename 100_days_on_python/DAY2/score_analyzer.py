#!/usr/bin/env python3

# Student Score Analyzer*
# - Input comma-separated scores (as string), cast to integers.
# - Use a while loop to keep asking until all scores are valid (0–100).
# - Check if student passed (all scores ≥ 50) using logical ops.
# - Extract highest and lowest scores using indexing.
# - Use format specifiers and string methods to present results in styled output.

while True:
    raw_input_scores = input("Enter comma-separated scores (0–100): ")
    try:
        scores = [int(s.strip()) for s in raw_input_scores.split(",")]
        if all(0 <= score <= 100 for score in scores):
            break
        else:
            print("All scores must be between 0 and 100.\n")
    except ValueError:
        print("Please enter only valid integers separated by commas.\n")

passed = all(score >= 50 for score in scores)
highest = max(scores)
lowest = min(scores)

status = "PASSED" if passed else "FAILED"

print("\nStudent Score Report")
print("-" * 25)
print("Scores       : {}".format(", ".join(str(s) for s in scores)))
print("Highest Score: {:>3}".format(highest))
print("Lowest Score : {:>3}".format(lowest))
print("Status       : {}".format(status.center(10)))
