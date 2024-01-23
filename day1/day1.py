"""
takes a string and returns the 'string' sum of the first and last digit
"""
def string_scanner(string):
    # defining the digits
    first_digit = None
    last_digit = None

    for char in string:
        if char.isdigit():
            # saving the first digit
            if not first_digit:
                first_digit = char
            # saving the last digit
            last_digit = char
    return first_digit + last_digit

def main():
    # reading the input file
    with open('input.txt', 'r') as file:
        input = file.readlines()

    sum = 0
    for string in input:
        sum += int(string_scanner(string))

    print(sum)

if __name__ == '__main__':
    main()
