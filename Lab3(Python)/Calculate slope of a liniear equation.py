def calculate_slope(x1, y1, x2, y2):
    if x1 == x2:
        return 'Infinity'  # Vertical line
    else:
        return (y2 - y1) / (x2 - x1)

# Example usage:
print(calculate_slope(2, 3, 5, 11))  # Output: 2.6666666666666665
