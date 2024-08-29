def count_digits(n):
    return len(str(abs(n)))

# Example usage:
n = int(input("Enter an integer: "))
print(f"The number of digits in {n} is {count_digits(n)}")
