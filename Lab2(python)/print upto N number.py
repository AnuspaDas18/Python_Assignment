def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

def factorial_series(n):
    return [factorial(i) for i in range(1, n+1)]

# Example usage:
terms = factorial_series(6)
print("Factorial series up to 6 terms:", terms)
