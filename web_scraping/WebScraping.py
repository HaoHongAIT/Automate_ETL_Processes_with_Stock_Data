from time import sleep
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from time import sleep
import pandas as pd
from preprocessing import preprocess


class Crawl:
    def __init__(self, ticker, url, index):
        self.dic = {"date": [], "closing_price": [], "adjusting_price": [], "rate_change": [],
                    "order_matching_volume": [], "order_matching_value": [],
                    "block_trade_volume": [], "block_trade_value": [],
                    "open_price": [], "high": [], "low": []}
        self.ticker_info = {'ticker': ticker, 'index': [i for i in index], 'url': url}
        options = Options()
        options.headless = False
        options.add_argument("--window-size=1920,1080")
        service = Service(executable_path='./chromedriver.exe')
        self.browser = webdriver.Chrome(service=service, options=options)

    def save(self, lst, filename):
        for i in range(0, len(lst), 11):
            self.dic['date'].append(lst[i])
            self.dic['closing_price'].append(lst[i + 1])
            self.dic['adjusting_price'].append(lst[i + 2])
            self.dic['rate_change'].append(lst[i + 3])
            self.dic['order_matching_volume'].append(lst[i + 4])
            self.dic['order_matching_value'].append(lst[i + 5])
            self.dic['block_trade_volume'].append(lst[i + 6])
            self.dic['block_trade_value'].append(lst[i + 7])
            self.dic['open_price'].append(lst[i + 8])
            self.dic['high'].append(lst[i + 9])
            self.dic['low'].append(lst[i + 10])
        pd.DataFrame(self.dic).to_csv(f"./data/raw/{filename}.csv")

    def get_Data(self, time=None) -> list:
        data = []
        self.browser.get(self.ticker_info['url'])
        if time:
            search_bar = self.browser.find_element(By.ID, 'date-inp-disclosure')
            self.browser.execute_script(time, search_bar)
            self.browser.find_element(By.ID, 'owner-find').click()
            sleep(1)

        class_name = ""
        while "enable" not in class_name:
            try:
                elements = self.browser.find_elements(
                    By.CSS_SELECTOR, ".render-table-owner td")
                data += [element.text for element in elements]
                next_page = self.browser.find_element(By.ID, "paging-right")
                next_page.click()
                class_name = next_page.get_attribute("class")
                sleep(1)
            except:
                print("Crawling Completely")
                break
        self.browser.close()
        return data
