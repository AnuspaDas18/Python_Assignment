ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()
min_age = ages[0]
max_age = ages[-1]
print(f"Sorted ages: {ages}")
print(f"Min age: {min_age}, Max age: {max_age}")
ages.append(min_age)
ages.append(max_age)
range_age = max_age - min_age
print(f"Range of ages: {range_age}")