ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

n = len(ages)
if n % 2 == 0:
    median_age = (ages[n//2 - 1] + ages[n//2]) / 2
else:
    median_age = ages[n//2]
print(f"Median age: {median_age}")