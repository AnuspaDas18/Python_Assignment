def is_palindrome(n):
    return str(n) == str(n)[::-1]

# Example usage:
n = int(input("Enter a number: "))
if is_palindrome(n):
    print(f"{n} is a palindrome")
else:
    print(f"{n} is not a palindrome")
