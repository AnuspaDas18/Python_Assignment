lines = []
while True:
    line = input("Enter a line (or just press Enter to finish): ")
    if line:
        lines.append(line.upper())
    else:
        break

for line in lines:
    print(line)
