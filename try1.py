from NeuroPy import NeuroPy
import pyautogui as pi
from win32api import GetSystemMetrics
import pytweening
import time


def map(x, oFrom, oTo, nFrom, nTo):
    return x * ((nTo-nFrom)/(oTo-oFrom))
    pass


print("Width =", GetSystemMetrics(0))
print("Height =", GetSystemMetrics(1))

ob = NeuroPy("COM3")
ob.start()
while(True):
    print(ob.attention)
    pi.moveTo(map(ob.attention+1, 1, 100, 1, GetSystemMetrics(0)),
              map(ob.meditation+1, 1, 100, 1, GetSystemMetrics(1)), pytweening.easeInQuad(0.75))
    # time.sleep(0.1)
