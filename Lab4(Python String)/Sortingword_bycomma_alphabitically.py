words = input("Enter a comma-separated sequence of words: ")
word_list = words.split(',')
sorted_words = ','.join(sorted(word_list))
print("Sorted words:", sorted_words)
