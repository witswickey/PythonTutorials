print(abs(-5))


def print_swap(a, b):  # 7,4
    a = a + b  # 11
    b = a - b  # 7
    a = a - b  # 4
    print(a, b)


print_swap(7, 4)

mod_5 = lambda x: x % 5  # Lamda functions

print(max(100, 51, 14, key=mod_5))


def roundoff(num):
    return round(num)


print(roundoff(9.1454785))

print(len("My name is " + "Ankit"))
