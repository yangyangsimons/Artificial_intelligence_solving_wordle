
from PIL import ImageGrab
import keyboard as kb
import time 

def __ScreenShot__(top):
    screenShot = ImageGrab.grab(bbox=(1105, top, 1775, top + 135))
    screenShot.save("data/screenshot/img2.png") 


top = 425
top = top + 1 * 135
kb.wait('enter')
print("please wait for 3 seconds")
time.sleep(2)
__ScreenShot__(top)