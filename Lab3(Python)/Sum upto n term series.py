def sum_series(n):
    sum = 0.0
    for i in range(1, n + 1):
        if i % 2 == 0:
            sum -= 1 / i
        else:
            sum += 1 / i
    return sum

# Example usage:
n = int(input("Enter the value of n: "))
print(f"The sum of the series up to {n} terms is {sum_series(n)}")
