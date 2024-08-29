def segment_display(n):
    segments = [" _ ", "| |", "|_|"]
    for i in range(n):
        print(segments[0])
        print(segments[1])
        print(segments[2])

# Example usage:
n = int(input("Enter the number of lines: "))
segment_display(n)
