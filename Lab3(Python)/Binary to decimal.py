def binary_to_decimal(binary):
    return int(binary, 2)

def decimal_to_binary(decimal):
    return bin(decimal).replace("0b", "")

# Example usage:
binary = input("Enter a binary number: ")
print(f"Binary {binary} to decimal is {binary_to_decimal(binary)}")

decimal = int(input("Enter a decimal number: "))
print(f"Decimal {decimal} to binary is {decimal_to_binary(decimal)}")
