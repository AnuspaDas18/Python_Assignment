def print_pattern(n):
    for i in range(1, n + 1):
        print(" " * (n - i) + "/\\" + " " * (2 * (i - 1)) + "/\\")
    for i in range(n):
        print(" " * i + "\\" + "_" * (2 * (n - i) - 1) + "/")

# Example usage:
n = int(input("Enter the value of N: "))
print_pattern(n)
