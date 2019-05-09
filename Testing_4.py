import string

operators = ['+', '/', '*', '-']



def evaluate(equation):
    running_equation = []
    temp = []
    for obj in equation:
        if obj in operators:
            if obj == '-' or obj == '+':
                if obj == '-':
                    print(equation)
                    result = int(equation[(equation.index(obj) - 1)]) - int(equation[(equation.index(obj) + 1)])
                    result_str = str(result)
                    running_equation.append(result_str)


                if obj == '+':
                    print(equation)
                    result = int(equation[(equation.index(obj) - 1)]) + int(equation[(equation.index(obj) + 1)])
                    result_str = str(result)
                    running_equation.append(result_str)
                    equation.pop(equation.index(obj) - 1)
                    equation.pop(equation.index(obj) + 1)
                    equation.pop(equation.index(obj))




        if len(running_equation) != 1:
            evaluate(running_equation)

        if len(running_equation) == 1:
            print(running_equation)



values = ['1','+','2','-','20']
evaluate(values)
