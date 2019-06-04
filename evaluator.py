import string

# Set data to evaluate. This will be passed to through the parser.
data2 = ['-(-', 1.0, '+', 1.0, '+', 1.0, '+', 1.0, ')-', 1.0, '@']
data3 = ['@', '-(-', 1.0, '+', 1.0, '+', 1.0, '+', 1.0, ')-(-', 1.0, '+', 1.0, '+', 1.0, '+', 1.0, ')', '@']
data4 = ['@', '-(-', 1.0, '+', 1.0, '+', 1.0, '+', 1.0, ')-(-', 1.0, '+', 1.0, '+', 1.0, '+', 1.0, ')-(-', 1.0, '-',
         1.0, ')', '@']
data = ['@', '(', 1.0, '+', 1.0, '+', 1.0, '+', 1.0, ')+(', 1.0, '-', 2.0, '+', 1.0, '+', 1.0, ')-(', 1.0, '+', 1.0,
        ')+(-', 1.0, '-', 1.0, ')', '@']


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


valid_values = ['(', ')', '-']
for digit in string.digits:
    valid_values.extend(digit)




def parse_parens(data):
    end_paren = [')', ')-', ')-(-', ')+(-', ')-(', ')+(']
    buffer = []
    for obj in data:
        if obj == '-(-' and data[data.index(obj) - 1] == '@':
            data[data.index(obj) + 1] = data[data.index(obj) + 1] * -1
            data.insert(data.index(obj), '-(')
            data.pop(data.index(obj))
            print(data)
            parse_parens(data)

        elif obj == '-(-' and data[data.index(obj) - 1] != '@':
            data.insert(data.index(obj), '-')
            data.insert(data.index(obj), '(-')
            data.pop(data.index(obj))
            print(data)
            parse_parens(data)

        elif obj == '+(-' and data[data.index(obj) - 1] != '@':
            data.insert(data.index(obj), '+')
            data.insert(data.index(obj), '(-')
            data.pop(data.index(obj))
            print(data)
            parse_parens(data)



        elif obj == '(-':
            data[data.index(obj) + 1] = data[data.index(obj) + 1] * -1
            data.insert(data.index(obj), '(')
            data.pop(data.index(obj))
            print(data)
            parse_parens(data)

        elif obj == '-(':
            if data[data.index(obj) + 2] not in end_paren:
                start = data[data.index(obj) + 1]
                operator = data[data.index(obj) + 2]
                stop = data[data.index(obj) + 3]
                result = operate(start, operator, stop)
                buffer = data[:data.index(obj)] + buffer
                buffer.append(obj)
                buffer.append(result)
                buffer.extend(data[data.index(obj) + 4:])
                print(buffer)
                parse_parens(buffer)

            elif data[data.index(obj) + 2] in end_paren and data[data.index(obj) - 1] == '@':
                data[data.index(obj) + 1] = data[data.index(obj) + 1] * -1
                if data[data.index(obj) + 2] == ')-(-':
                    print(data[data.index(obj):])
                    data.insert(data.index(obj) + 2, '-(-')
                    data.pop(data.index(obj) + 3)
                    data.pop(data.index(obj))

                elif data[data.index(obj) + 2] == ')+(-':
                    print(data[data.index(obj):])
                    data.insert(data.index(obj) + 2, '+(-')
                    data.pop(data.index(obj) + 3)
                    data.pop(data.index(obj))

                elif data[data.index(obj) + 2] == ')+(':
                    print(data[data.index(obj):])
                    data.insert(data.index(obj) + 2, '+(')
                    data.pop(data.index(obj) + 3)
                    data.pop(data.index(obj))

                elif data[data.index(obj) + 2] == ')-(':
                    print(data[data.index(obj):])
                    data.insert(data.index(obj) + 2, '-(')
                    data.pop(data.index(obj) + 3)
                    data.pop(data.index(obj))

            elif data[data.index(obj) + 2] in end_paren and data[data.index(obj) - 1] != '@':
                if data[data.index(obj) + 2] == ')-(-':
                    print(data[data.index(obj):])
                    data.insert(data.index(obj), '-')
                    data.insert(data.index(obj) + 2, '-(-')
                    data.pop(data.index(obj) + 3)
                    data.pop(data.index(obj))
                elif data[data.index(obj) + 2] == ')+(-':
                    print(data[data.index(obj):])
                    data.insert(data.index(obj), '-')
                    data.insert(data.index(obj) + 2, '+(-')
                    data.pop(data.index(obj) + 3)
                    data.pop(data.index(obj))
                elif data[data.index(obj) + 2] == ')+(':
                    print(data[data.index(obj):])
                    data.insert(data.index(obj), '-')
                    data.insert(data.index(obj) + 2, '+(')
                    data.pop(data.index(obj) + 3)
                    data.pop(data.index(obj))
                elif data[data.index(obj) + 2] == ')-(':
                    print(data[data.index(obj):])
                    data.insert(data.index(obj), '-')
                    data.insert(data.index(obj) + 2, '+(')
                    data.pop(data.index(obj) + 3)
                    data.pop(data.index(obj))

        if obj == '(':
            if data[data.index(obj) + 2] not in end_paren:
                start = data[data.index(obj) + 1]
                operator = data[data.index(obj) + 2]
                stop = data[data.index(obj) + 3]
                result = operate(start, operator, stop)
                buffer.append(obj)
                buffer.append(result)
                buffer.extend(data[data.index(obj) + 4:])
                buffer = data[:data.index(obj)] + buffer
                print(f"{buffer} buffer")
                parse_parens(buffer)

            if data[data.index(obj) + 2] in end_paren:

                if data[data.index(obj) + 2] == ')-(-':
                    data.insert(data.index(obj) + 2, '-(-')
                    data.pop(data.index(obj) + 3)
                    data.pop(data.index(obj))
                    print(data)

                elif data[data.index(obj) + 2] == ')-(':
                    data.insert(data.index(obj) + 2, '-(')
                    data.pop(data.index(obj) + 3)
                    data.pop(data.index(obj))
                    print(data)

                elif data[data.index(obj) + 2] == ')+(-':
                    print(data[data.index(obj):])
                    print('()+')
                    data.insert(data.index(obj) + 2, '+(-')
                    data.pop(data.index(obj) + 3)
                    data.pop(data.index(obj))

                elif data[data.index(obj) + 2] == ')+(':
                    data.insert(data.index(obj) + 2, '+(')
                    data.pop(data.index(obj) + 3)
                    data.pop(data.index(obj))
                    print(data)

                elif data[data.index(obj) + 2] == ')':
                    data.pop(data.index(obj) + 2)
                    data.pop(data.index(obj))
                    print(f"{data} This is data")


parse_parens(data2)