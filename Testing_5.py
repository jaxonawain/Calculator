import string
# Set data to evaluate. This will be passed to through the parser.
data = ['(','-1','-','1',')']

# Set valid operators and create an operator function

def operate(start, operation, stop):
    if operation == '-':
        return int(start) - int(stop)
    elif operation == '+':
        return start + stop
    elif operation == '*':
        return start * stop
    elif operation == '/':
        return start / stop
# Set valid values. Note that - is also an operater. FFuckk me.


valid_values = ['(',')','-']
for digit in string.digits:
    valid_values.extend(digit)

# List to define possible begin parenthesis options.
paren = ['(','-']


result = 0


def evaluate(data):
    buffer = []
    for obj in data:
        if '(' in obj:
            start = data[data.index(obj) + 1]
            operator = data[data.index(obj) + 2]
            stop = data[data.index(obj) + 3]
            result = operate(start,operator,stop)
            if data.index(obj) > 1
                buffer.append(data[:data.index(obj)])
                buffer.append(result)





evaluate(data)