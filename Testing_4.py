data = ['1','-','(1','+','2)','+','(1','+','2)']

operators = ['+', '/', '*', '-']


def operate(start, stop, operation):
    if operation == '-':
        return start - stop
    elif operation == '+':
        return start + stop
    elif operators == '*':
        return start * stop
    elif operators == '/':
        return start / stop

temp = []
result = 0

def evaluate(data):
    for obj  in data:
        start = 0
        stop = 0
        if '(' in obj:
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
            print(data)


    print(temp)
    return(temp)

while len(evaluate(data)) > 5:
    evaluate(evaluate(data))