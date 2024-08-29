text = "India is my motherland. I love my country. Capital of India is New Delhi."
substring = "country"

# Calculate the length of the string
length_of_string = len(text)

# Find the substring 'country'
substring_index = text.find(substring)

# Count the occurrences of each word
from collections import Counter
word_counts = Counter(text.split())

print("Length of the string:", length_of_string)
print("Index of substring 'country':", substring_index)
print("Word counts:", word_counts)
