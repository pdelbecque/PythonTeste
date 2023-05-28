import pyautogui, sys, time

def on_click(x, y, button, pressed):
    print(f'{x=}, {y=}, {button=}, {pressed=}')


print('Press Ctrl-C to quit.')

print('ecran :' + str(pyautogui.size()))
try:
    while not pyautogui.mouseDown():
        time.sleep(5)
        print('clique ' + str(pyautogui.mouseDown()))
        print('clique ' + str(pyautogui.mouseUp()))

        pyautogui.mouseDown()

except KeyboardInterrupt:
    print('\n') 
    