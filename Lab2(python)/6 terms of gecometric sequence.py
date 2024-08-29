def geometric_sequence(start, ratio, terms):
    sequence = [start * ratio**i for i in range(terms)]
    return sequence

# Example usage:
sequence = geometric_sequence(2, 3, 6)
print("First 6 terms of the geometric sequence:", sequence)
