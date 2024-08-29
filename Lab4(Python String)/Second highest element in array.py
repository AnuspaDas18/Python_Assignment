def find_second_highest(arr):
    first, second = float('-inf'), float('-inf')
    for num in arr:
        if num > first:
            first, second = num, first
        elif first > num > second:
            second = num
    return second

# Example usage:
arr = [10, 20, 4, 45, 99]
second_highest = find_second_highest(arr)
print("Second highest element:", second_highest)
