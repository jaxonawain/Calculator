import string
data = ['1','-','1']

operators = ['+', '/', '*', '-']

valid_values = ['(',')','-']
for digit in string.digits:
    valid_values.extend(digit)

print(valid_values)

paren = ['(','-']


temp = []
result = 0

def evaluate(data):
    for obj  in data:
        start = 0
        stop = 0
        if '(' in obj:
            first_two_char = [data[data.index(obj) + 1],data[data.index(obj) + 1]]
            if first_two_char in paren:
                print('fucking aaaa')
                start = data.index(obj)
                operator = data[start + 1]
                for obj in data:
                    if ')' in obj:
                        stop = data.index(obj)
                temp.extend(data[:start])
                start_num = int(data[start][1:])
                stop_num = int(data[stop][:-1])
                result = operate(start_num, stop_num, operator)
                temp.extend(str(result))
                data.pop(start)
                temp.extend(data[stop:])
                data.pop(data.index(operator))
                data.pop(stop)


    print(temp)
    return(temp)

while len(evaluate(data)) > 1:
    evaluate(evaluate(data))