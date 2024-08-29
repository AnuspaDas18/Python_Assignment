def fibonacci_series(n):
    fib_series = [0, 1]
    for i in range(2, n):
        fib_series.append(fib_series[-1] + fib_series[-2])
    return fib_series

# Example usage:
n = 10
fib_series = fibonacci_series(n)
print(f"The first {n} terms of the Fibonacci series are: {fib_series}")
