import random

messages = ['It is certain',
            'It is decidedly so',
            'Yes definitely',
            'Reply hazy try again',
            'Ask again later',
            'Concentrate and ask again',
            'My reply is no',
            'Outlook not so good',
            'Very doubtful']

print(messages[random.randint(0, len(messages) - 1)])

# print some patterns

for i in range(0, 5):
    for j in range(i + 1):
        print('*', end=" ")
    print()

print()
# mirror

for i in range(0, 5):
    for j in range(5 - i - 1):
        print(' ', end=" ")
    for j in range(i + 1):
        print('*', end=" ")
    print()

print()


# Comma code

def converttoList(spam, result=""):
    for i in range(0, len(spam)):
        if (i != len(spam) - 1):
            result = result + spam[i] + ","
        else:
            result = result + "and " + spam[i]
    return result


spam = ['apples', 'bananas', 'tofu', 'cats']

print(converttoList(spam))

grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]


def printpatter(grid):
    for i in range(len(grid[0])):
        for j in range(len(grid)):
            print(grid[j][i], end=" ")
        print()


printpatter(grid)

message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
count = {}

for chara in message:
    count.setdefault(chara, 0)
    count[chara] = count[chara] + 1

print(count)
