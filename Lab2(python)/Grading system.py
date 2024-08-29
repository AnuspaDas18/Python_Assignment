def get_grade(percentage):
    if percentage >= 90:
        return "Grade A"
    elif percentage >= 80:
        return "Grade B"
    elif percentage >= 70:
        return "Grade C"
    elif percentage >= 60:
        return "Grade D"
    elif percentage >= 40:
        return "Grade E"
    else:
        return "Grade F"

# Example usage:
percentage = 85
grade = get_grade(percentage)
print(f"With {percentage}%: {grade}")
