import string
# Set data to evaluate. This will be passed to through the parser.
data = ['-(-1','-','1)','-','1']

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
    start = 0
    stop = 0
    for obj in data:
        buffer = []
        print(obj)
        if '-' == obj[0] and '(' == obj[1] and '-' == obj[2]:
            start = int(obj[3:]) * -1
            print(start)
            for item in data:
                if ')' in item:
                    print('stop')


evaluate(data)