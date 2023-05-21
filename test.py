import pyautogui
pyautogui.screenshot('valider.png', region=(515, 531, 180, 25))
location = pyautogui.locateOnScreen('valider.png')
pyautogui.click(location)
print(location)

