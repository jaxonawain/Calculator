import string

try_again = True
while try_again:

    user_input = input('Waiting for input: ')

    i = 0
    operator_index = -1
    operators = ['+','/','*']


    for character in user_input:
        operator_index += 1

        if user_input[0] in operators:
            print("Invalid first character")

        elif character in operators and user_input[(user_input.index(character) - 1)] in operators:
            print('Cannot have two operators back to back')

        elif character in operators or character == '-':
            if user_input[(operator_index) - 1] or user_input[(operator_index) + 1] not in string.digits:
                print('Needs to be a number')
                print(string.digits)
            else:
                 if operator_index == "+":
                     print(user_input[(operator_index - 1)] + user_input[(opera1tor_index + 1)])