import pyautogui
import random
import time

print('Press Ctrl-C to quit.')
print(__name__)

try :
    while True :
        x = random.randint(600, 700)
        y = random.randint(200, 600)
        pyautogui.moveTo(x, y, 0.5)
        time.sleep(60)
except KeyboardInterrupt:
    print('\n')


