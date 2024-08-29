def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def count_primes(arr):
    return sum(1 for num in arr if is_prime(num))

# Example usage:
arr = [2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Number of primes in the array:", count_primes(arr))
