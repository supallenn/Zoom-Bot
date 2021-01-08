import time
from datetime import datetime
from pynput.keyboard import Controller, Key
from data import zoom
import webbrowser
import keyboard
import pynput

keyboardd = Controller()

isStarted = False

for i in zoom:
    while True:
        if isStarted == False:
            if datetime.now().hour == int(i[1].split(':')[0]) and datetime.now().minute == int(i[1].split(':')[1]) and datetime.now().second == int(i[1].split(':')[2]):
                webbrowser.open(i[0])
                time.sleep(5)
                keyboard.write(i[3])
                time.sleep(2)
                keyboardd.press(Key.enter)
                time.sleep(300)
                keyboardd.press(Key.alt_l)
                keyboardd.press('h')
                keyboardd.release('h')
                keyboardd.release(Key.alt_l)
                time.sleep(1)
                keyboard.write(i[4])
                keyboardd.press(Key.enter)
                time.sleep(3)
                keyboardd.press(Key.alt_l)
                keyboardd.press('h')
                keyboardd.release('h')
                keyboardd.release(Key.alt_l)
                isStarted = True
        elif isStarted == True:
            if datetime.now().hour == int(i[2].split(':')[0]) and datetime.now().minute == int(i[2].split(':')[1]) and datetime.now().second == int(i[1].split(':')[2]):
                keyboardd.press(Key.alt_l)
                keyboardd.press('q')
                keyboardd.release('q')
                keyboardd.release(Key.alt_l)
                time.sleep(1)
                keyboardd.press(Key.enter)
                isStarted = False
                break
