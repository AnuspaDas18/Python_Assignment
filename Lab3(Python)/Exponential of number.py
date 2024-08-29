def calculate_exponential(base, exp):
    result = 1
    for _ in range(exp):
        result *= base
    return result

# Example usage:
base = int(input("Enter the base number: "))
exp = int(input("Enter the exponent: "))
print(f"{base} raised to the power of {exp} is {calculate_exponential(base, exp)}")
