def find_hcf(x, y):
    while(y):
        x, y = y, x % y
    return x

# Example usage:
x = int(input("Enter the first number: "))
y = int(input("Enter the second number: "))
print(f"The HCF of {x} and {y} is {find_hcf(x, y)}")
