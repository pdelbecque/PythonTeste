
import pyautogui
import time
from PIL import Image       

def Present(nom):
    try:
       if open(nom):
        return False
    except IOError:
        return True


i=0
nomFichier = 'Croix'+str(i).rjust(3,'0')+'.png'
while not Present(nomFichier):
    i +=1
    nomFichier = 'Croix'+str(i).rjust(3,'0')+'.png'
    print(nomFichier)
time.sleep(10)
x, y = pyautogui.position()
positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
print(positionStr, end='')
pyautogui.screenshot(nomFichier, region=(x, y, 15, 15))
time.sleep(5)
location = pyautogui.locateOnScreen(nomFichier)
#pyautogui.click(location)
#%%
imageLue = Image.open(nomFichier)

#Afficher l'image
imageLue.show()

# %%
