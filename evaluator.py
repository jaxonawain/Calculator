import string
# Set data to evaluate. This will be passed to through the parser.
data = ['(-1','-','1)','-','1',')']

# Set valid operators and create an operator function

def operate(start, operation, stop):
    if operation == '-':
        return start - stop
    elif operation == '+':
        return start + stop
    elif operation == '*':
        return start * stop
    elif operation == '/':
        return start / stop
# Set valid values. Note that - is also an operator, unfckingfortunately


valid_values = ['(',')','-']
for digit in string.digits:
    valid_values.extend(digit)

# List to define possible begin parenthesis options.
paren = ['(','-']


result = 0


def evaluate(data):
    for obj in data:
        print(data.index(value))
        if obj[0] == '(':
            print('shit')
            if obj[1] == '-':
                start = int(obj[2:]) * -1
                stop = int(data[data.index(obj) + 2])
                operator = data[data.index(obj) + 1]
                op_result = operate(start,operator, stop)
                print(stop)

                if (data[data.index(obj) + 4])[-1] == ')':
                    print('fu')


evaluate(data)