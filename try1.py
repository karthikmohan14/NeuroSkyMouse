from NeuroPy import NeuroPy
import pyautogui as pi
from win32api import GetSystemMetrics
import pytweening
import time
import win32gui

def map(x, oFrom, oTo, nFrom, nTo):
    return x * ((nTo-nFrom)/(oTo-oFrom))
    pass


print("Width =", GetSystemMetrics(0))
print("Height =", GetSystemMetrics(1))

ob = NeuroPy("COM6")
ob.start()
count=0
flag=1
lastAttention = 0
while(True):
    # print(ob.attention, "blink",ob.blinkStrength)
    # pi.moveTo(map(ob.attention+1, 1, 100, 1, GetSystemMetrics(0)),
    #           map(ob.meditation+1, 1, 100, 1, GetSystemMetrics(1)), pytweening.easeInQuad(0.75))
    # pi.moveTo(map(ob.highBeta+1, 1, 100, 1, GetSystemMetrics(0)),
            #   100, pytweening.easeInQuad(0.75))
    # print(ob.blinkStrength)
    # time.sleep(0.1)
    # print("alpha ",ob.highAlpha," ",ob.lowAlpha," Beta ",ob.highBeta," ",ob.lowBeta)
    flags, hcursor, (x,y) = win32gui.GetCursorInfo()
    if(ob.attention == 0):
        print(ob.attention)
    if(ob.highAlpha>ob.highBeta and ob.attention > 1):
        count+=1
        # print("moving cursor ..",count)
    elif((count)>=4):
        flag=flag*-1
        print("toggling direction")
        # print("stopping")
        # break
        count = 0
    else:
        count = 0        
        
    if (flag > 0):    
        print("along y")
        # pi.moveTo(map(ob.attention, 1, 100, 1, GetSystemMetrics(0))+1,  x, pytweening.easeInQuad(0.5))
        if(ob.attention > lastAttention):
            lastAttention = ob.attention
            pi.moveTo(x, map(ob.attention, 1, 100, 1, GetSystemMetrics(1))+1, pytweening.easeInQuad(0.5))
        else:
            pi.moveTo(x, map(ob.attention-2, 1, 100, 1, GetSystemMetrics(1))+1, pytweening.easeInQuad(0.5))
    else:
        # pi.moveTo(y,  map(ob.attention, 1, 100, 1, GetSystemMetrics(1))+1, pytweening.easeInQuad(0.5))
        print("along x")
        if(ob.attention > lastAttention):
            lastAttention = ob.attention
            pi.moveTo(map(ob.attention, 1, 100, 1, GetSystemMetrics(1))+1,y, pytweening.easeInQuad(0.5))
        else:
            pi.moveTo(map(ob.attention-2, 1, 100, 1, GetSystemMetrics(1))+1,y, pytweening.easeInQuad(0.5))
    # ob.save()
    # print("alpha ",ob.highAlpha," ",ob.lowAlpha," Beta ",ob.highBeta," ",ob.lowBeta)
ob.stop()
ob.save()