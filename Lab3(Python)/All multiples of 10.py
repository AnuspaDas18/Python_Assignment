def multiples_of_10(start, end):
    for i in range(start, end + 1):
        if i % 10 == 0:
            print(i, end=" ")

# Example usage:
start = int(input("Enter the start of the interval: "))
end = int(input("Enter the end of the interval: "))
print("Multiples of 10 between the given interval are: ")
multiples_of_10(start, end)
