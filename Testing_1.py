import string

operators = ['+', '/', '*', '-']
possible_first_char = ['-']

for item in string.digits:
    possible_first_char.append(item)
temp_space = []
instance = 0


def evaluate(values_to_eval):
    seq_val_temp = []
    seq_val_str = ""
    equation = []

    seq_val_temp.append(values_to_eval[0])

    for c in values_to_eval:
        print(values_to_eval.index(c))
        if c not in operators:
            seq_val_temp.extend(c)
            seq_val_str = ''.join(seq_val_temp)
        if c in operators:
            equation.append(seq_val_str)
            equation.append(c)
            seq_val_temp.clear()
            seq_val_str = None

    equation.append(seq_val_str)
    length = len(equation)

    parenthesis = '('
    exponent = '^'
    addition = '+'
    subtraction = '-'
    multiplication = '*'
    division = '/'
    for item in equation:
        if item == addition or subtraction:
            if item == addition:
                temp_space = []
                result = int(equation[(equation.index(item) - 1)]) + int(equation[(equation.index(item) + 1)])
                result_str = str(result)
                temp_space.append(result_str)
                temp_space.extend(equation[(equation.index(item) + 2):])
                temp_str = ''.join(temp_space)
                while len(temp_space) > 0:
                    evaluate(temp_str)
                    exit()

            elif item == subtraction:
                temp_space = []
                result = int(equation[(equation.index(item) - 1)]) - int(equation[(equation.index(item) + 1)])
                result_str = str(result)
                temp_space.append(result_str)
                temp_space.extend(equation[(equation.index(item) + 2):])
                temp_str = ''.join(temp_space)
                while len(temp_space) > 0:
                    evaluate(temp_str)
                    print(temp_str)
                    exit()

        if item == multiplication or division:
            if item == multiplication:
                temp_space = []
                print(equation)
                result = int(equation[(equation.index(item) - 1)]) * int(equation[(equation.index(item) + 1)])
                result_str = str(result)
                temp_space.append(result_str)
                temp_space.extend(equation[(equation.index(item) + 2):])
                temp_str = ''.join(temp_space)
                while len(temp_space) > 0:
                    evaluate(temp_str)
                    print(temp_str)
                    exit()



testing = evaluate('-3-3-3-3')


print(testing)