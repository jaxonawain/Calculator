import string

#Set Operators list
operators = ['+', '/', '*', '-']

#Set - or ( as possible first characters
possible_first_char = ['-','(']

#set () as valid characters
possible_mid_char = ['(',')','-']

#Append 0-9 to the possible characters list
for item in string.digits:
    possible_first_char.append(item)
    possible_mid_char.append(item)

#Tests user input to ensure it's valid
def test_values(user_input):

#Create buffer for character segments and an empty string to house final value
    valid_entry = []
    valid_return_values = ""
    for character in user_input:
        if user_input[0] not in possible_first_char:
            print("Invalid first character, exiting")
            exit()

        elif user_input[-1] not in possible_mid_char:
            print('Invalid Entry. Exiting')
            exit()

        elif character in operators and user_input[(user_input.index(character) + 1)] in operators[:3]:
            print('Cannot have two operators back to back, exiting.')
            exit()

        valid_entry.extend(character)
        valid_return_values = ''.join(valid_entry)
    return valid_return_values

#Parse the equation into a ["value","operator","value"] format for evaluation. opbuffer is a buffer used to store sequences of non-integer type characters. intbuffer stores floats.
#The buffers store values until a nonvalid value type occurs. Then it condenses the buffer, and appends that result to the equation.
def parse_equation(user_input):
    equation = []
    intbuffer = []
    opbuffer = []
    for c in user_input:
        if c in string.digits:
            if opbuffer:
                value = ''.join(opbuffer)
                equation.append(value)
                opbuffer = []
            intbuffer.extend(c)
        else:
            if intbuffer:
                value = ''.join(intbuffer)
                equation.append(float(value))
                intbuffer = []
            opbuffer.extend(c)
    if opbuffer:
        value = ''.join(opbuffer)
        equation.append(value)

    if intbuffer:
        value = ''.join(intbuffer)
        equation.append(float(value))
    print(equation)

try_again = True
while try_again:

    values = input('Waiting for input: ')
    valid_values = (test_values(values))
    print(f"To pass this value through the evaluator: {parse_equation(valid_values)}")


