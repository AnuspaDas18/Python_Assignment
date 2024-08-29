def power(x, n):
    if n == 0:
        return 1
    else:
        return x * power(x, n-1)

# Example usage:
result = power(2, 3)
print("2 to the power of 3:", result)
