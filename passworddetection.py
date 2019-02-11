import re

passw = 'A02525010101'


def checkpass():
    if len(passw) < 8:
        print('Password is short')
        return
    passwordlowerregex = re.compile(r'[a-z]+')
    passwordupperregex = re.compile(r'[A-Z]+')
    passworddigitregex = re.compile(r'[0-9]+')
    match = passwordlowerregex.search(passw)
    match1 = passwordupperregex.search(passw)
    match2 = passworddigitregex.search(passw)
    if match is None:
        print('There is should be at least one lowercase letter')
    elif match1 is None:
        print('There is should be at least one uppercase letter')
    elif match2 is None:
        print('There is should be at least one digit letter')
    else:
        print('Password is good')


checkpass()
