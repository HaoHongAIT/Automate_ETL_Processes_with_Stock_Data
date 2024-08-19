from time import sleep
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


def save(lst, ticker, cols, index):
    path = f"./data/raw/{ticker}.csv"    
    num_cols = len(cols)
    sub_lst = [lst[i:i+num_cols] for i in range(0, len(lst), num_cols)]
    pd.DataFrame(sub_lst [1:], columns=cols).to_csv(f"./data/raw/{ticker}_{index}", index=False)
    print(f"Save Successfully... {path}")

class Crawl:
    def __init__(self, tickers):
        self.tickers = tickers
        options = Options()
        options.headless = False
        options.add_argument("--window-size=1920,1080")
        service = Service(executable_path='./chromedriver.exe')
        self.browser = webdriver.Chrome(service=service, options=options)

    def get_price_history(self, ticker, time=None) -> list:
        url = f"https://s.cafef.vn/lich-su-giao-dich-{ticker}-1.chn"
        self.browser.get(url)
        if time:
            search_bar = self.browser.find_element(
                By.ID, 'date-inp-disclosure')
            self.browser.execute_script(
                f"arguments[0].value = '{time}' ", search_bar)
            self.browser.find_element(By.ID, 'owner-find').click()
            sleep(1)

        class_name = ""
        data = []
        while "enable" not in class_name:
            elements = self.browser.find_elements(
                By.CSS_SELECTOR, ".render-table-owner td")
            data += [element.text for element in elements]
            next_page = self.browser.find_element(By.ID, "paging-right")
            next_page.click()
            class_name = next_page.get_attribute("class")
            sleep(1)
        # SAVE FILE
        cols = ["date", "close", "adjusting_price", "rate_change", 
                "order_matching_volume", "order_matching_value",
                "block_trade_volume", "block_trade_value", 
                "open", "high", "low"]
        save(ticker=ticker, lst=data, cols=cols, index=1)
        print("Get Price History Complete")
        # self.browser.close()
        return data

    def get_order_flow_stat(self, ticker, time=None):
        url = f"https://s.cafef.vn/lich-su-giao-dich-{ticker}-2.chn"
        self.browser.get(url)
        if time:
            search_bar = self.browser.find_element(
                By.ID, 'date-inp-disclosure')
            self.browser.execute_script(f"arguments[0].value = '{time}' ", search_bar)
            self.browser.find_element(By.ID, 'owner-find').click()
            sleep(1)
        class_name = ""
        data = []
        while "enable" not in class_name:
            elements = self.browser.find_elements(
                By.CSS_SELECTOR, ".render-table-owner td")
            data += [element.text for element in elements]
            next_page = self.browser.find_element(By.ID, "paging-right")
            next_page.click()
            class_name = next_page.get_attribute("class")
            sleep(1)
        # SAVE FILE
        cols = ["date", "rate_change", "buy_orders", "buy_volume", "average_buy_order_volume",
                "sell_orders", "sell_volume", "average_sell_order_volume", "net_volume" ]
        save(ticker=ticker, lst=data, cols=cols, index=2)
        print("Get Order Flow Statistics Complete")
        # self.browser.close()

    def get_foreign_investors(self, ticker, time=None):
        url = f"https://s.cafef.vn/lich-su-giao-dich-{ticker}-3.chn"
        self.browser.get(url)
        if time:
            search_bar = self.browser.find_element(
                By.ID, 'date-inp-disclosure')
            self.browser.execute_script(
                f"arguments[0].value = '{time}' ", search_bar)
            self.browser.find_element(By.ID, 'owner-find').click()
            sleep(1)
            
        class_name = ""
        data = []
        while "enable" not in class_name:
            elements = self.browser.find_elements(
                By.CSS_SELECTOR, ".render-table-owner td")
            data += [element.text for element in elements]
            next_page = self.browser.find_element(By.ID, "paging-right")
            next_page.click()
            class_name = next_page.get_attribute("class")
            sleep(1)
        # SAVE FILE
        cols = ["date", "rate_change", "net_trading_volume", "net_trading_value_billion_vnd",
                "buy_volume", "buy_value_billion_vnd", "sell_volume", "sell_value_billion_vnd",
                "remaining_room", "current_ownership"]
        save(ticker=ticker, lst=data, cols=cols, index=3)
        print("Get Foreign Investors Complete")
        # self.browser.close()

    def get_proprietary_trading(self, ticker, time=None):
        url = f"https://s.cafef.vn/lich-su-giao-dich-{ticker}-4.chn"
        print("Get Proprietary Trading Complete")
        self.browser.get(url)
        if time:
            search_bar = self.browser.find_element(
                By.ID, 'date-inp-disclosure')
            self.browser.execute_script(
                f"arguments[0].value = '{time}' ", search_bar)
            self.browser.find_element(By.ID, 'owner-find').click()
            sleep(1)

        class_name = ""
        data = []
        while "enable" not in class_name:
            elements = self.browser.find_elements(
                By.CSS_SELECTOR, ".render-table-owner td")
            data += [element.text for element in elements]
            next_page = self.browser.find_element(By.ID, "paging-right")
            next_page.click()
            class_name = next_page.get_attribute("class")
            sleep(1)
        # SAVE FILE
        cols = ["ticker", "date", "buy_volume", "buy_value_bil_vnd",
                "sell_volume", "sell_value_bil_vnd", "net_trading_volume",
                "net_trading_value_bil_vnd"]

        save(ticker=ticker, lst=data, cols=cols, index=4)
        print("Get Proprietry Trading Complete")
        # self.browser.close()

    def run(self, time_range=None) -> list:
            for ticker in self.tickers:
                self.get_price_history(ticker=ticker, time=time_range)
                self.get_order_flow_stat(ticker=ticker, time=time_range)
                self.get_foreign_investors(ticker=ticker, time=time_range)
                self.get_proprietary_trading(ticker=ticker, time=time_range)

            self.browser.close()
            print("Web Scraping Complete")




