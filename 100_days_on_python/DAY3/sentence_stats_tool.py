#!/usr/bin/env python3

# Sentence Stats Tool
# - Ask user to enter a sentence.
# - Analyze:
# - Total characters
# - Number of words
# - Count of each vowel
# - Unique letters used (set)
# - Use indexing to extract specific characters (e.g., first letter of each word).
# - Display all results in a clean, formatted summary.

vowels = "aeiou"

while True:
    sentence = input("Enter a sentence: ").strip()
    if sentence:
        break
    print("Sentence cannot be empty.\n")

# Clean for analysis
cleaned = sentence.lower()

# Count total characters (excluding spaces)
total_chars = len(sentence.replace(" ", ""))

# Word split
words = sentence.split()
num_words = len(words)

# Vowel counts
vowel_counts = {v: cleaned.count(v) for v in vowels}

# Unique letters
letters_only = [c for c in cleaned if c.isalpha()]
unique_letters = set(letters_only)

# First letters of each word
first_letters = [word[0] for word in words]

# Output
print("\nSENTENCE ANALYSIS")
print("-" * 30)
print("Original Sentence : {}".format(sentence))
print("Total Characters  : {}".format(total_chars))
print("Number of Words   : {}".format(num_words))
print("Vowel Counts      : {}".format(", ".join(f"{v.upper()}={c}" for v, c in vowel_counts.items())))
print("Unique Letters    : {}".format(", ".join(sorted(unique_letters))))
print("First Letters     : {}".format(", ".join(first_letters)))

