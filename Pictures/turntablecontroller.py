import os
import pyautogui

# Got the following from: https://pyautogui.readthedocs.io/en/latest/screenshot.html

scanbuttonxy = pyautogui.locateOnScreen('scan_start.png', confidence=0.5)
# scanbuttonxy returns: 
# Box(left=1416, top=562, width=50, height=41)
scanbuttoncenter = pyautogui.center(scanbuttonxy)
# using scanbuttoncenter returns: 
# Point(x=1441, y=582)
# button7point[0]
# 1441
# button7point.x
# 1441
scanbuttonx, scanbuttony = pyautogui.center(scanbuttonxy)
pyautogui.click(scanbuttonx, scanbuttony)  # clicks the center of where the 7 button was found
# pyautogui.click('scan_start.png') # a shortcut version to click on the center of where the 7 button was found