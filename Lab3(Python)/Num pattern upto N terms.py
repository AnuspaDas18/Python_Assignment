def number_pattern(n):
    num = 1
    arr = [[0 for _ in range(n)] for _ in range(n)]
    top, bottom, left, right = 0, n-1, 0, n-1
    direction = 0

    while top <= bottom and left <= right:
        if direction == 0:
            for i in range(left, right+1):
                arr[top][i] = num
                num += 1
            top += 1
        elif direction == 1:
            for i in range(top, bottom+1):
                arr[i][right] = num
                num += 1
            right -= 1
        elif direction == 2:
            for i in range(right, left-1, -1):
                arr[bottom][i] = num
                num += 1
            bottom -= 1
        elif direction == 3:
            for i in range(bottom, top-1, -1):
                arr[i][left] = num
                num += 1
            left += 1
        direction = (direction + 1) % 4

    for row in arr:
        print(" ".join(map(str, row)))

# Example usage:
n = int(input("Enter the value of N: "))
number_pattern(n)
