import pyperclip
import re

str = pyperclip.paste()

phoneregex = re.compile(r'\d{10}')
print(phoneregex.findall(str))

emailregex = re.compile(r'''(
    [a-zA-Z0-9.%_+-]+  #usrname
    @                   #@
    [a-zA-Z0-9.-]+   #domain
    .
    [a-zA-Z]{2,4}
    )''', re.VERBOSE)

print(emailregex.findall(str))
