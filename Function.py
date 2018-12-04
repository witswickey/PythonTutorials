import random

print('i have a number to guess between 50-100')
secretnumber = random.randint(50, 70)

for i in range(1, 7):
    print(' guess the number')
    num = int(input())
    if num > secretnumber:
        print('too high, guess lower')
    elif num < secretnumber:
        print('too less, guess higher ')
    else:
        break

if num == secretnumber:
    print('Correct guess')
else:
    print('wrong guess , number was', secretnumber)
