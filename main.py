import pyautogui
from time import sleep
from pyfiglet import figlet_format as figlet
from termcolor import colored
import random

banner = figlet('yuuhakobe', font='smslant')
c = colored(banner, 'magenta')
print(c)

messages = [
    'Yow my name is YuuHakobe ',
    'Add yours text here in new lines ',
]

def spam(value):
    count = 0
    while count != value:
        count += 1
        x = random.choice(messages)
        sleep(0.5)
        pyautogui.write(x)
        pyautogui.press('enter')

spam(30)
