#! python3

print("hello".ljust(10))

password = {'luggage': "sdfdsffdsf",
            'email': "sdfdsfaedsad",
            'blog': "dsfdsfdsfdsf"}

import pyperclip
import sys

if (len(sys.argv) < 2):
    print('Parameter missing')
    sys.exit()
else:
    print(sys.argv[1])
    account = sys.argv[1]
    if account in password:
        pyperclip.copy(password[account])
        file1 = open("file.txt", "a")
        file1.write(pyperclip.paste())
        file1.close()
