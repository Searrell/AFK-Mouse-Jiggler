import pyautogui as screen

import random

import time



x, y = screen.size()

while True:

    x1 = random.randint(0, x)

    y1 = random.randint(0, y)

    screen.moveTo(x1, y1)

    screen.click(int(x/2), y-30)

    time.sleep(random.randint(0, 60))
