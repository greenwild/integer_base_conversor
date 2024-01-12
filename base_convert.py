

# a practice for python to convert different base integers
number_input = int(input('input the number,integers only: '))
base_input = int(input('input the base of input number: '))
base_output = int(input('input the base of the output number:'))


def decimal_conversion(number_input, base_input):
    number_input = str(number_input)
    decimal_result = 0
    power = 0
    for digit in reversed(number_input):
        decimal_result += int(digit) * (base_input ** power)
        power += 1

    return decimal_result


if base_input != 10:
    number_input = decimal_conversion(number_input, base_input)
print(number_input)


def base_conversion(number_input, base_output):

    quotient = number_input/base_output
    output = []
    while quotient != 0:

        quotient = number_input // base_output
        remain = number_input % base_output
        output.insert(0, remain)
        number_input = quotient
    return output


result = base_conversion(number_input, base_output)
# convert to string to output
print("Output in base", base_output, "is:", ''.join(map(str, result)))

# output_str = ''
# for number in result:
#     output_str = output_str+str(number)
# print("Output in base", base_output, "is:", output_str)
