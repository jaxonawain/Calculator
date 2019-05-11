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

#Parse the equation into a ["value","operator","value"] format for evaluation. Parenthesis should be glued to the value. (IE: (-1-1) == ['(-1','-','1)']. The evaluator can look for an index of either 0 or -1 and find that
#the value is ( or ) and determine that that needs to be evaluated first. The evaluation should strip the parenthesis, and return the value, and run the renewed equation through the evaluator till only 1 value exists.
def parse_equation(user_input):
    equation = []
    temp_list = []

    if user_input[0] in ['-','(']:
        if user_input[0] == '(' and user_input[1] == '-':
            temp_list.extend(user_input[:1])
        else:
            temp_list.extend(user_input[0])

        for c in user_input[1:]:
            if c not in operators and c in possible_mid_char:
                temp_list.extend(c)

            elif c in operators:
                temp_str = ''.join(temp_list)
                equation.append(temp_str)
                equation.append(c)
                temp_list = []
        if temp_list:
            temp_str = ''.join(temp_list)
            equation.append(temp_str)
    elif user_input[0] != '-':
        for c in user_input:
            if c not in operators and c in possible_mid_char:
                temp_list.extend(c)
            elif c in operators:
                temp_str = ''.join(temp_list)
                equation.append(temp_str)
                equation.append(c)
                temp_list = []
        if temp_list:
            temp_str = ''.join(temp_list)
            equation.append(temp_str)
    return (equation)


try_again = True
while try_again:

    values = input('Waiting for input: ')
    valid_values = (test_values(values))
    print(parse_equation(valid_values))