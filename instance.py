from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

def get_online(driver):
    pass


def get_ping(driver):
    pass

def get_total(driver, x):
    total = driver.find_elements(By.CLASS_NAME, "wheel-color-stats__total")
    text = ""
    if x == 2:
        text = total[0].text
    elif x == 3:
        text = total[1].text
    elif x == 5:
        text = total[2].text
    elif x == 20:
        text = total[3].text
    return text
    # return total

def get_percent(a, b):
    return abs((a - b) / ((a + b) / 2)) * 100
