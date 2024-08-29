def swap_numbers(a, b):
    a, b = b, a
    return a, b

# Example usage:
x, y = 5, 10
x, y = swap_numbers(x, y)
print("After swapping:", x, y)
