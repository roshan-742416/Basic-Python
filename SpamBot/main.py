# SpamBot

# Import relevant modules
import time
import pyautogui

# FAIL-SAFE - DO NOT DISABLE THIS
pyautogui.FAILSAFE = True

def SendMessage():
    time.sleep(4)  # Pause for 4 sec
    text = open('Spam.txt')
    for each_line in text:
        pyautogui.typewrite(each_line)
        pyautogui.press('enter')


SendMessage()
