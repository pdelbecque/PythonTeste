import pyautogui
import time

print ("debut")
# time.sleep(10)
x, y = pyautogui.position()
positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
print(positionStr, end='')

pyautogui.screenshot('valider.png', region=(1290, 450, 180, 25))
print("suite")
location = pyautogui.locateOnScreen('valider.png')
pyautogui.click(location)
print(location)

