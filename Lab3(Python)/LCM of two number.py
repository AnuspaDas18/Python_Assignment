def find_lcm(x, y):
    lcm = (x * y) // find_lcm(x, y)
    return lcm

# Example usage:
x = int(input("Enter the first number: "))
y = int(input("Enter the second number: "))
print(f"The LCM of {x} and {y} is {find_lcm(x, y)}")
