import pyautogui as pg
import random
import time
while True:
    x = random.randint(500,600)
    y = random.randint(600,700)
    pg.moveTo(x,y,0.5)
    time.sleep(4)

