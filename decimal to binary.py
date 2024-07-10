def decimal_to_binary(num):
    binary_digits = []
    abs_num = abs(num)
    if num == 0:
        return "0"
    while abs_num > 0:
        binary_digits.append(str(abs_num % 2))
        abs_num = abs_num // 2
    
    binary_digits.reverse()
    binary_string = ''.join(binary_digits)

    if num < 0:
        binary_string = '-' + binary_string
    
    return binary_string

print(decimal_to_binary(10))