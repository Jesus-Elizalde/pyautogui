import pyautogui
import time

# delay for 1 second
time.sleep(1)


# Opens a new tab
pyautogui.hotkey("command","t")

# Search youtube
pyautogui.write("https://www.youtube.com/")
pyautogui.hotkey("enter")
