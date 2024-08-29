input_string = input("Enter a string: ")
vowels = "aeiouAEIOU"
no_vowels_string = ''.join([char for char in input_string if char not in vowels])
print("String without vowels:", no_vowels_string)
