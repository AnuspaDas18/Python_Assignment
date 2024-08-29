sentence = input("Enter a sentence: ")
letters = sum(c.isalpha() for c in sentence)
digits = sum(c.isdigit() for c in sentence)

print("LETTERS", letters)
print("DIGITS", digits)
