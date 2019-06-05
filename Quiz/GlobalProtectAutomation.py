import configparser
import os
import time

import pyautogui
import pyperclip

# print(pyautogui.position())


config = configparser.RawConfigParser()
config.read('C:\GlobalAuto.properties')

RSAPass = config.get('Auth', 'global.rsakey')
Globusername = config.get('Auth', 'global.username')

print('Connecting to RSA  ..')
# pyautogui.doubleClick(44, 158)#(x=1784, y=953)

os.startfile("C:/Program Files (x86)/RSA SecurID Software Token/SecurID.exe")

time.sleep(1)
print('Supplying password')
pyautogui.typewrite(RSAPass)

pyautogui.press('enter')

time.sleep(1)
print('Copying password')

pyautogui.hotkey('ctrl', 'c')

time.sleep(1)  # to be removed

Rsakey = pyperclip.paste()
print('Closing RSA with Key', Rsakey)
pyautogui.hotkey('alt', 'F4')

print('Connecting to Global Protect  .. Click')

os.startfile("C:/Program Files/Palo Alto Networks/GlobalProtect/PanGPA.exe")

time.sleep(2)

print('Click connect button')
# pyautogui.press('enter')
time.sleep(1)
pyautogui.click(1746, 936)
time.sleep(8)
pyautogui.press('enter')

time.sleep(8)

pyautogui.hotkey('ctrl', 'a')
pyautogui.press('delete')
time.sleep(1)
pyautogui.typewrite(Globusername)
print('Click password button')
# pyautogui.click(1729,875)
pyautogui.press('tab')

time.sleep(3)
print('Supplying paaword')

pyautogui.typewrite(Rsakey)

time.sleep(4)

pyautogui.hotkey('ctrl', 'a')
pyautogui.hotkey('ctrl', 'c')
ifValue = ' '
ifValue = pyperclip.paste()

print('ifvalue is ', ifValue)

if ifValue != ' ':
    print('Its cool')
    pyautogui.press('enter')
else:
    pyautogui.typewrite(Rsakey)
    pyautogui.press('enter')

time.sleep(4)

pyautogui.hotkey('alt', 'F4')

# comment here
'''

input1 = input('you wish to connect IBM also Y/N')
print()
print(input1)

if input1 == 'Y' or input1 == 'y':
    print('Connecting to IBM Cisco connect ..')
    pyautogui.click(251, 1054)

    pyautogui.click(1167, 515)

    pyautogui.click(507, 459)
    time.sleep(5)
    pyautogui.typewrite('Sarkara1')
    time.sleep(8)
    pyautogui.click(586, 534)
    time.sleep(2)
    pyautogui.press('enter')
    time.sleep(10)
'''
print('Enjoy!!! With Love')
time.sleep(3)
