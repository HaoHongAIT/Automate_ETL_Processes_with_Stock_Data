from time import sleep
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from time import sleep
from queue import Queue
import pandas as pd
import threading


def read_doc():
    pass


def somthig(df):
    for i in range(0, len(lst), 11):
        df['date'].append(lst[i])
        df['closed_price'].append(lst[i+1])
        df['adjusted_price'].append(lst[i+2])
        df['col 1'].append(lst[i+3])
        df['col 2'].append(lst[i+4])
        df['col 3'].append(lst[i+5])
        df['col 4'].append(lst[i+6])
        df['col 5'].append(lst[i+7])
        df['col 6'].append(lst[i+8])
        df['col 7'].append(lst[i+9])
        df['col 8'].append(lst[i+10])


def get_Data(browser, stock_code, index) -> list:
    """
    get data from table at url
    """
    data = []
    browser.get(
        f"https://s.cafef.vn/lich-su-giao-dich-{stock_code}-{index}.chn")
    # sleep(2)
    while True:
        try:
            elements = browser.find_elements(
                By.CSS_SELECTOR, ".render-table-owner td")
            data += [element.text for element in elements]
            nextpage = browser.find_element(
                By.XPATH, "/html/body/form/div[3]/div[2]/div[1]/div[3]/div/div[3]/div[3]").click()
            sleep(1)
            print(len(data))
        except:
            break
    browser.close()
    return data


if __name__ == '__main__':
    options = Options()
    options.headless = False
    options.add_argument("--window-size=1920,1080")
    service = Service(executable_path='./chromedriver.exe')
    browser = webdriver.Chrome(service=service, options=options)
    lst = get_Data(browser=browser, stock_code='fpt', index=1)
    ## bat dau luu
    