import math

def cosine_series(x, n):
    cosine = 0
    sign = 1
    for i in range(n):
        term = sign * (x ** (2 * i)) / math.factorial(2 * i)
        cosine += term
        sign = -sign
    return cosine

# Example usage:
x = float(input("Enter the value of x: "))
n = int(input("Enter the number of terms: "))
print(f"cos({x}) = {cosine_series(x, n)}")
