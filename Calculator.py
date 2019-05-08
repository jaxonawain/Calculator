import string
operators = ['+', '/', '*', '-']
possible_first_char = ['-']
for item in string.digits:
    possible_first_char.append(item)


def test_values(user_input):
    i = 0
    operator_index = -1
    valid_entry = []
    valid_return_values = ""
    for character in user_input:
        operator_index += 1

        if user_input[0] not in possible_first_char:
            print("Invalid first character, exiting")
            exit()
        elif user_input[-1] not in string.digits:
            print('Invalid Entry. Exiting')
            exit()

        elif character in operators and user_input[(user_input.index(character) + 1)] in operators[:3]:
            print('Cannot have two operators back to back, exiting.')
            exit()
        valid_entry.extend(character)
        valid_return_values = ''.join(valid_entry)
    return valid_return_values


def parse_equation(user_input):
    equation = []
    temp_list = []
    temp_str = None
    if user_input[0] == '-':
        temp_list.extend('-')
        for c in user_input[1:]:
            if c not in operators and c in string.digits:
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
            if c not in operators and c in string.digits:
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