import pyperclip

list = pyperclip.paste()

newlist = list.splitlines()

for i in range(0, len(newlist)):
    newlist[i] = "* " + newlist[i]

for str in newlist:
    print(str, end='\n')

list = '\n'.join(newlist)
pyperclip.copy(list)
