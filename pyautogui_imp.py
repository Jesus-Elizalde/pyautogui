import pyautogui

res = pyautogui.locateOnScreen("edit.png")
print(res)
print(pyautogui.center(res))
