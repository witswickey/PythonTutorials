import pyautogui
import pyperclip
import time

# print(pyautogui.position())

print('Connecting to Global protect ..')
pyautogui.click(201, 1072)

time.sleep(2)

pyautogui.typewrite('441993')

pyautogui.press('enter')

time.sleep(1)

pyautogui.click(532, 616)

print(pyperclip.paste())

password = pyperclip.paste()

pyautogui.click(159, 1062)

# print(pyautogui.position())

time.sleep(5)

pyautogui.click(1701, 934)

time.sleep(10)

pyautogui.click(1666, 881)

pyautogui.typewrite(password)

pyautogui.click(1678, 954)

time.sleep(20)

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
    print('Done')
