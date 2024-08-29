input_string = input("Enter a string: ")
words = input_string.split()
longest_word = max(words, key=len)
print("Longest word:", longest_word, "with length", len(longest_word))
