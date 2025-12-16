#!/usr/bin/env python3

# 5. BMI Calculator with Age Advice*  
# Ask user for weight (kg), height (m), and age.  
# - Cast appropriately.  
# - Calculate BMI = weight / (height²)  
# - Use if statements to give feedback:  
#  - Underweight (<18.5), Normal (18.5–24.9), Overweight (25–29.9), Obese (≥30)  
# - Add age advice: if under 18, recommend medical check before interpreting.

weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in meters: "))
age = int(input("Enter your age: "))

# Calculate BMI
bmi = weight / (height ** 2)

# Feedback based on BMI calculation
if bmi < 18.5:
    status = "Underweight"
elif 18.5 <= bmi < 25:
    status = "Normal"
elif 25 <= bmi < 30:
    status = "Overweight"
else:
    status = "Obese"

# Display results
print(f"Your BMI is {bmi:.2f} — {status}.")

# Age advice
if age < 18:
    print("Note: Since you're under 18, consult a doctor for accurate BMI interpretation.")
