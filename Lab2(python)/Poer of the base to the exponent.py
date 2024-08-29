def custom_power(base, exponent):
    result = 1
    for _ in range(exponent):
        result *= base
    return result

# Example usage:
result = custom_power(2, 3)
print("2 to the power of 3:", result)
