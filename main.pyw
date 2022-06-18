import main
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import webbrowser
import time
import datetime
from pygame import mixer
import pyperclip
from tkinter import *
import sys
from subprocess import CREATE_NO_WINDOW
import os


def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.dirname(__file__)
    return os.path.join(base_path, relative_path)

promo_code = ""
i = 0

window = Tk()

window.title("FAILHACK")
window.iconbitmap(resource_path('./resources/betting.ico'))
window.geometry("375x410")
window.resizable(False, False)

status = Text(height=1)
text = Text()
text.pack()
status.pack()

s = Service(resource_path('./driver/chromedriver.exe'))
s.creationflags = CREATE_NO_WINDOW
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")

driver=webdriver.Chrome(service=s, options=chrome_options)
driver.set_window_size(500, 800)
driver.get("https://csfail.net/")

status.insert(1.0, "Status: Loaded")

mixer.init()
text.insert(END, datetime.datetime.now().strftime("%H:%M") + " Loaded. Waiting promo.")

def update_status(text):
    status.config(state="normal")
    status.delete(1.0, END)
    status.insert(1.0, text)
    status.config(state="disabled")

def worker():
    try:
        message = driver.find_elements(By.CLASS_NAME, "message__text")
        if message:
            update_status(datetime.datetime.now().strftime("%H:%M") + " Status: Active")
        else:
            update_status(datetime.datetime.now().strftime("%H:%M") + " Status: Unactive")

        uses = driver.find_elements(By.CLASS_NAME, "promo__uses")
        code = driver.find_elements(By.CLASS_NAME, "promo__code")
        type = driver.find_elements(By.CLASS_NAME, "promo__type")
        if code and type:
            if main.promo_code != code[-1].text:
                main.promo_code = code[-1].text

                pyperclip.copy(main.promo_code)
                mixer.music.load(resource_path('./resources/miui_12_notification.mp3'))
                mixer.music.play(0)

                now = datetime.datetime.now()

                text.insert(END, "\n" + now.strftime("%H:%M") + " [" + main.promo_code + "] "+ "(" + type[-1].text + ") " + uses[-1].text)
    except:
        pass
    window.after(200, worker)

def on_closing():
    driver.quit()
    sys.exit()

window.protocol("WM_DELETE_WINDOW", on_closing)

window.after(200, worker)
mainloop()






# promo_code = ""
# s = Service('chromedriver102.exe')
#
# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument("--headless")
#
# mixer.init()
# mixer.music.load(r'notification.mp3')
#
# driver=webdriver.Chrome(service=s, options=chrome_options)
# driver.set_window_size(400, 800)
# driver.get("https://csfail.net/")
#
# while True:
#     try:
#         uses = driver.find_elements(By.CLASS_NAME, "promo__uses")
#         code = driver.find_elements(By.CLASS_NAME, "promo__code")
#         type = driver.find_elements(By.CLASS_NAME, "promo__type")
#         if code and type:
#             if promo_code != code[-1].text:
#                 promo_code = code[-1].text
#
#                 pyperclip.copy(promo_code)
#                 mixer.music.play(0)
#
#                 now = datetime.datetime.now()
#                 print(now.strftime("%H:%M") + " [" + promo_code + "] "+ "(" + type[-1].text + ") " + uses[-1].text)
#     except:
#         pass

























# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
# import time
# import datetime
# from pygame import mixer
# import pygame
# import pyperclip
# import os
# import sys
# import atexit
# import signal
#
#
# def resource_path(relative_path):
#     try:
#         base_path = sys._MEIPASS
#     except Exception:
#         base_path = os.path.dirname(__file__)
#     return os.path.join(base_path, relative_path)
#
# loop = True
#
# promo_code = ""
# s = Service(resource_path('./driver/chromedriver.exe'))
# os.system('CLS')
# print(datetime.datetime.now().strftime("%H:%M") + " Started.")
#
# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument("--headless")
# chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
# print(datetime.datetime.now().strftime("%H:%M") + " Loaded. Waiting promo.")
#
# mixer.init()
# mixer.music.load(resource_path('./resources/xiaomi_bubble.mp3'))
# mixer.music.play(0)
#
# driver=webdriver.Chrome(service=s, options=chrome_options)
# driver.set_window_size(400, 600)
# driver.get("https://csfail.net/")
#
# while loop:
#     try:
#         keys = pygame.key.get_pressed()
#
#         uses = driver.find_elements(By.CLASS_NAME, "promo__uses")
#         code = driver.find_elements(By.CLASS_NAME, "promo__code")
#         type = driver.find_elements(By.CLASS_NAME, "promo__type")
#         if code and type:
#             if promo_code != code[-1].text:
#                 promo_code = code[-1].text
#
#                 pyperclip.copy(promo_code)
#                 mixer.music.load(resource_path('./resources/miui_12_notification.mp3'))
#                 mixer.music.play(0)
#
#                 now = datetime.datetime.now()
#                 print(now.strftime("%H:%M") + " [" + promo_code + "] "+ "(" + type[-1].text + ") " + uses[-1].text)
#     except:
#         mixer.music.load(resource_path('./resources/redmi.mp3'))
#         mixer.music.play(0)
