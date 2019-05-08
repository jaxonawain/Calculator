import string

operators = ['+', '/', '*', '-']


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


def evaluate(equation):
    print(equation)
    running_equation = []
    temp = []
    for obj in equation:
        if obj in operators:
            if obj == '-':
                result = int(equation[(equation.index(obj) - 1)]) - int(equation[(equation.index(obj) + 1)])
                result_str = str(result)
                running_equation.append(result_str)
                if len(running_equation) != 1:
                    running_equation.extend(equation[(equation.index(obj) + 2):])

    while len(running_equation) > 1:
        evaluate(running_equation)

    return running_equation


print(evaluate(parse_equation('1-2-1')))