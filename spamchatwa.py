import pyautogui
import time
import keyboard
import sys

while True:
    pyautogui.typewrite("I Love You Sayang")
    pyautogui.press("enter")
    if keyboard.is_pressed("shift"):
        sys.exit()