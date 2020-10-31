import pyautogui
import time

def spam ():
    pesan  = ("I LOVE YOU <3")
    jumlah = int(input("Berapa biji?"))
    time.sleep (3)
    for _ in range (jumlah):
        pyautogui.typewrite(pesan)
        pyautogui.press("enter")


spam()