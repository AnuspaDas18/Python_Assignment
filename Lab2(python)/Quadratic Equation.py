import math

def solve_quadratic(a, b, c):
    discriminant = b**2 - 4*a*c
    if discriminant >= 0:
        root1 = (-b + math.sqrt(discriminant)) / (2*a)
        root2 = (-b - math.sqrt(discriminant)) / (2*a)
        return root1, root2
    else:
        return "Complex Roots"

# Example usage:
roots = solve_quadratic(1, -7, 12)
print("Roots of the quadratic equation:", roots)
