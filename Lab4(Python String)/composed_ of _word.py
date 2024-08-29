sentence = input("Enter a sentence: ")
words = sentence.split()
digit_words = [word for word in words if word.isdigit()]
print(digit_words)
