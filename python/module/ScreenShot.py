import pyautogui
import cv2
import numpy as np


img = pyautogui.screenshot(region=[0,0,100,100])
img = cv2.cvtColor(np.asarray(img), cv2.COLOR_BGR2BGR)

img.save('screenshopt.png')