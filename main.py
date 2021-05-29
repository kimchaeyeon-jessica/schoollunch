import pyautogui
import time
import pyperclip
import json
import requests
from datetime import datetime

pyautogui.click(94,1059)
time.sleep(1)
pyautogui.typewrite("kakaotalk")
time.sleep(1)
pyautogui.moveTo(94,520)
time.sleep(1)
pyautogui.doubleClick()
time.sleep(20)
pyautogui.click(838,338)
time.sleep(1)
pyautogui.click(1082,276)
time.sleep(1)
pyperclip.copy("3학년 애반(선미쌤)")
pyautogui.hotkey("ctrl", "v")
time.sleep(1)
pyautogui.moveTo(980,384)
pyautogui.doubleClick()

today_month = datetime.today().month
today_day = datetime.today().day
pyautogui.typewrite(str(today_month))
pyautogui.typewrite('/')
pyautogui.typewrite(str(today_day))
pyperclip.copy(" 점심")
pyautogui.hotkey("ctrl", "v")
pyautogui.hotkey('shift', 'enter')

menuTable={}
url = 'https://schoolmenukr.ml/api/high/B100000516?year=2021&month=5'
response = requests.get(url)
school_menu = json.loads(response.text)
print(school_menu["menu"][0]["lunch"])
for i in school_menu['menu']:
    menuTable[int(i['date'])]=i['lunch']
for i in menuTable[31]:
    pyperclip.copy(i)
    pyautogui.hotkey("ctrl","v")
    pyautogui.hotkey('shift', 'enter')
pyautogui.press('backspace')
pyautogui.press('enter')


