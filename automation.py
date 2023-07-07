import pyautogui
import time

time.sleep(1)

channel_name = pyautogui.prompt(text="Enter youtube channel",title="Enter youtube channel")
print(channel_name)

pyautogui.moveTo(1624,350)
pyautogui.click(1624,350,duration=1)

pyautogui.hotkey("command","t")

pyautogui.write("https://www.youtube.com/")
pyautogui.hotkey("enter")

pyautogui.moveTo(1644,63)
pyautogui.click(1644,63,duration=1)

pyautogui.write(channel_name)
pyautogui.hotkey("enter")

pyautogui.moveTo(2426,220)
pyautogui.click(2426,220,duration=1)
