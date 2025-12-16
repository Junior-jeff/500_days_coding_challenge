#!/usr/bin/env python3

# 1. Grade Evaluator with Weighted Scores 
# Prompt the user for test, assignment, and exam scores. Each is weighted: test (20%), assignment (30%), exam (50%).  
# - Cast inputs to float.  
# - Compute final score using arithmetic. 
# - Use if statements to assign grades:  
#  - A (≥70), B (60–69), C (50–59), F (<50)  
# - Print result with formatted message.

# Prompt user for scores
test_score = float(input("Enter your Test score (out of 100): "))
assignment_score = float(input("Enter your Assignment score (out of 100): "))
exam_score = float(input("Enter your Exam score (out of 100): "))

# Calculate weighted total
final_score = (0.2 * test_score) + (0.3 * assignment_score) + (0.5 * exam_score)

# Determine grade
if final_score >= 70:
    grade = "A"
elif final_score >= 60:
    grade = "B"
elif final_score >= 50:
    grade = "C"
else:
    grade = "F"

# Print result
print(f"Final Score: {final_score:.2f}")
print(f"Grade: {grade}")

