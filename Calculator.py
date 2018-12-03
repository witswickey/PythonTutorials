def calculator(a, b, ops):
    if (ops == '+'):
        return a + b
    elif (ops == '-'):
        return abs(a - b)

    elif (ops == '*'):
        return a * b
    elif (ops == '/'):
        return a / b
    return -1


spam = 0
while (spam < 5):
    print(calculator(2, 4, '/'))
    spam += 1
print('next')

help(input)

name = ''
while name != 'your name':
    name = input("Type your name")
print('Thank you')

print('commited')
