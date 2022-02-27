import pyautogui
pyautogui.FAILSAFE = False
import ctypes

user  = ctypes.windll.user32
width = user.GetSystemMetrics(0)
height = user.GetSystemMetrics(1)

pyautogui.click(0,height)
print("Start Button Clicked")
pyautogui.typewrite("  SalesMate + ",0.1)
print("SalesMate + Types")
pyautogui.press("enter",1,10)
print("SalesMate Software Opened")
pyautogui.press(["alt","s"])
pyautogui.press("n")
pyautogui.press("enter",2,1)
pyautogui.typewrite("Rice",0.1)
pyautogui.press("tab")
pyautogui.typewrite("Rice")
pyautogui.press("tab",6,0.1)
pyautogui.typewrite("2000")
pyautogui.press("tab",9,0.1)
pyautogui.press("enter",3,0.1)
pyautogui.press("tab",16,0.1)
pyautogui.press("enter")