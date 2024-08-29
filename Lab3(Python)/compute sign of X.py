import math

def sine_series(x, n):
    sine = 0
    sign = 1
    for i in range(n):
        term = sign * (x ** (2 * i + 1)) / math.factorial(2 * i + 1)
        sine += term
        sign = -sign
    return sine

# Example usage:
x = float(input("Enter the value of x: "))
n = int(input("Enter the number of terms: "))
print(f"sin({x}) = {sine_series(x, n)}")
