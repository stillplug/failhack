import instance

import main
import instance
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
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

window = Tk()
window.title("FAILHACK v1.7")
window.iconbitmap(resource_path('./resources/grave.ico'))
window.geometry("430x410")

promo_frame = Frame(window)
promo_frame.pack(side="top")

benefit_frame = Frame(window)
benefit_frame.pack()

status_frame = Frame(window)
status_frame.pack(side="bottom")

text = Text(promo_frame)
text.pack()
status = Text(status_frame, height=1)
status.pack()


s = Service(resource_path('./driver/chromedriver.exe'))
s.creation_flags = CREATE_NO_WINDOW

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")

driver=webdriver.Chrome(service=s, options=chrome_options)
driver.set_window_size(1920, 1080)
driver.get("https://csfail.org/uk/bonuses")

status.insert(1.0, "Статус: Активний")

mixer.init()
text.insert(END, datetime.datetime.now().strftime("%H:%M") + " Завантажено. Очікування промокодів.")

def update_status(text):
    status.config(state="normal")
    status.delete(1.0, END)
    status.insert(1.0, text)
    status.config(state="disabled")

def worker():
    try:
        message = driver.find_elements(By.CLASS_NAME, "message__text")
        if message:
            update_status(datetime.datetime.now().strftime("%H:%M") + " Статус: Активний")
        else:
            update_status(datetime.datetime.now().strftime("%H:%M") + " Статус: Неактивний")
        # calculate_benefit()
        uses = driver.find_elements(By.CLASS_NAME, "promo__uses")
        code = driver.find_elements(By.CLASS_NAME, "promo__code")
        type = driver.find_elements(By.CLASS_NAME, "promo__type")
        if code and type:
            if code != "" and type != "":
                if main.promo_code != code[-1].text:
                    main.promo_code = code[-1].text

                    pyperclip.copy(main.promo_code)
                    if "обичка" in type[-1].text.lower():
                        mixer.music.load(resource_path('./resources/miui_12_notification.mp3'))
                        mixer.music.play(0)
                    elif "спец" in type[-1].text.lower():
                        mixer.music.load(resource_path('./resources/iphone_notification.mp3'))
                        mixer.music.play(0)

                    now = datetime.datetime.now()
                    text.insert(END, "\n" + now.strftime("%H:%M") + " " + main.promo_code + " "+ "(" + type[-1].text + ") " + uses[-1].text)
    except:
        pass

    window.after(750, worker)

def on_closing():
    driver.quit()
    sys.exit()

window.protocol("WM_DELETE_WINDOW", on_closing)

window.after(250, worker)
# window.attributes("-topmost", True)
mainloop()

