#!/usr/bin/env python3

# Vowel Extractor & Counter*
# - Prompt user for a sentence.
# - Use string methods and indexing to find and count vowels.
# - While loop repeats until a sentence with at least 5 vowels is entered.
# - Use conditional expressions to report if each vowel is found.
# - Use format specifiers to show final results clearly

vowels = "aeiou"

while True:
    sentence = input("Enter a sentence: ").lower()
    found_vowels = [c for c in sentence if c in vowels]
    
    if len(found_vowels) >= 5:
        break
    else:
        print("Please enter a sentence with at least 5 vowels.\n")

print("\nVowel Analysis Complete")
print("-" * 30)
for v in vowels:
    count = sentence.count(v)
    status = "Found" if count > 0 else "Not Found"
    print("Vowel {:>2} : {:>2} time(s) — {:<10}".format(v.upper(), count, status))

print("-" * 30)
print("Total vowels: {:>2}".format(len(found_vowels)))