string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")
are_anagrams = sorted(string1) == sorted(string2)
print("Are anagrams:", are_anagrams)
