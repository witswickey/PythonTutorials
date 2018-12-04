def collatz(number):
    if (number % 2) == 0:
        return int(number / 2)
    else:
        return number * 3 + 1


print('Enter the magic number')
num = int(input())
ret = collatz(num)
while ret != 1:
    print(ret, sep='\n')
    ret = collatz(ret)

print('Printed sequence is Collatz sequence')
