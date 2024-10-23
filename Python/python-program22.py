def decimal_to_binary(decimal):
    if decimal == 0:
        return '0'
    
    binary = ''
    while decimal > 0:
        remainder = decimal % 2
        binary = str(remainder) + binary
        decimal = decimal // 2
    
    return binary

decimal_number = int(input("Enter decimal"))
binary_representation = decimal_to_binary(decimal_number)
print(f"The binary representation of {decimal_number} is {binary_representation}")
