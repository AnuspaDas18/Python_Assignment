def is_buzz_number(number):
    return number % 7 == 0 or str(number).endswith('7')

# Example usage:
number = 49
if is_buzz_number(number):
    print(f"{number} is a Buzz number.")
else:
    print(f"{number} is not a Buzz number.")
