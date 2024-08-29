def reverse_number(number):
    reversed_number = int(str(number)[::-1])
    return reversed_number

# Example usage:
number = 12345
reversed_number = reverse_number(number)
print(f"The reverse of {number} is {reversed_number}.")
