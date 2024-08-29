import math

def is_krishnamurthy_number(n):
    return sum(math.factorial(int(digit)) for digit in str(n)) == n

# Example usage:
number = 145
if is_krishnamurthy_number(number):
    print(f"{number} is a Krishnamurthy number.")
else:
    print(f"{number} is not a Krishnamurthy number.")
