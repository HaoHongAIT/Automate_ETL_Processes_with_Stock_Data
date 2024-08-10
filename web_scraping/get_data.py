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


def list_to_csv(lst, stock_code) -> dict:
    dic = {"date": [], "closing_price": [], "adjusting_price": [], "rate_change": [],
           "order_matching_volumn": [], "order_matching_value": [],
           "block_trade_volume": [], "block_trade_value": [],
           "open_price": [], "max_price": [], "min_price": []}

    for i in range(0, len(lst), 11):
        dic['date'].append(lst[i])
        dic['closing_price'].append(lst[i+1])
        dic['adjusting_price'].append(lst[i+2])
        dic['rate_change'].append(lst[i+3])
        dic['order_matching_volumn'].append(lst[i+4])
        dic['order_matching_value'].append(lst[i+5])
        dic['block_trade_volume'].append(lst[i+6])
        dic['block_trade_value'].append(lst[i+7])
        dic['open_price'].append(lst[i+8])
        dic['max_price'].append(lst[i+9])
        dic['min_price'].append(lst[i+10])
    pd.DataFrame(dic).to_csv(f"./data/{stock_code}.csv")


def get_Data(browser, stock_code, index) -> list:
    """get data from table at url
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
        except RuntimeError:
            print("crawl end")
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
    dic = list_to_csv(lst=lst, stock_code='fpt')
