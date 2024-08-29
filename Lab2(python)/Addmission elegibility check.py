def check_eligibility(math, physics, chemistry):
    total = math + physics + chemistry
    if (math >= 60 and physics >= 50 and chemistry >= 40 and total >= 200) or (math + physics >= 150):
        return True
    return False

# Example usage:
n = int(input("Enter the number of students: "))
eligible_students = []

for i in range(n):
    print(f"\nEnter marks for student {i + 1}:")
    math = int(input("Mathematics: "))
    physics = int(input("Physics: "))
    chemistry = int(input("Chemistry: "))
    
    if check_eligibility(math, physics, chemistry):
        eligible_students.append(i + 1)

if eligible_students:
    print("\nEligible students:", eligible_students)
else:
    print("\nNo students are eligible.")
