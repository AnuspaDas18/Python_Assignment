import math

def find_roots(a, b, c):
    discriminant = b**2 - 4*a*c
    if discriminant > 0:
        root1 = (-b + math.sqrt(discriminant)) / (2 * a)
        root2 = (-b - math.sqrt(discriminant)) / (2 * a)
        return root1, root2
    elif discriminant == 0:
        root = -b / (2 * a)
        return root, None
    else:
        real_part = -b / (2 * a)
        imaginary_part = math.sqrt(-discriminant) / (2 * a)
        return complex(real_part, imaginary_part), complex(real_part, -imaginary_part)

# Example usage:
a, b, c = 1, -3, 2
roots = find_roots(a, b, c)
if roots[1] is None:
    print(f"The equation has one real root: {roots[0]}")
elif isinstance(roots[0], complex):
    print(f"The equation has two complex roots: {roots[0]} and {roots[1]}")
else:
    print(f"The equation has two real roots: {roots[0]} and {roots[1]}")
