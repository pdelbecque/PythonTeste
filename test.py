
#%%
import pyautogui
import time
#import PIL
from PIL import Image       

print ("debut")
#%%
time.sleep(10)
x, y = pyautogui.position()
positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
print(positionStr, end='')
#%%
nomFichier ='valider.png'
try:
 with open(nomFichier): pass
except IOError:
 print("Erreur! Le fichier n' pas pu être ouvert")
#%%
pyautogui.screenshot(nomFichier, region=(x, y, 15, 15))
print("suite")
location = pyautogui.locateOnScreen('valider.png')
#pyautogui.click(location)
print(location)
#%%
imageLue = Image.open('valider.png')

#Afficher l'image
imageLue.show()
#%%