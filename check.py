#마우스 위치 알아내기
import pyautogui
from datetime import datetime
currentMouseX, currentMouseY = pyautogui.position()
print('{0},{1}'.format(currentMouseX, currentMouseY))

#날짜 알아내기
today_day = datetime.today().day
print(today_day)
