from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import chromedriver_autoinstaller
import subprocess
import shutil
import time
from selenium.webdriver.chrome.options import Options
import pyautogui as pg
import pyperclip
import os

os.system('Chrome.lnk')
pg.moveTo(1,1,duration = 0.01)

w = pg.locateOnScreen('3.png')
pg.click(w)
# "코딩유치원"을 클립보드에 저장
pyperclip.copy("하나님의 교회")

# 클립보드에 있는 내용을 붙여넣기
pg.hotkey("ctrl", "v")
pg.press('enter')



def wating_img(name):
    while True:
        find_img = pg.locateOnScreen(name)
        if find_img == None:
            print(find_img)
            time.sleep(2)
        else:
            break
        pg.click(name)

wating_img('4.png')
time.sleep(0.5)

if pg.locateOnScreen('ko1.png'):
    w = pg.locateOnScreen('ko1.png')
    pg.click(w)

elif pg.locateOnScreen('en1.png'):
    w = pg.locateOnScreen('en1.png')
    pg.click(w)
else:
    w = pg.locateOnScreen('es1.png')

    pg.click(w)




