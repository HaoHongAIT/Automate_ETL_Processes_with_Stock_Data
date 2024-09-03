import threading
from web_scraping import *
from time import sleep

import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service





class MultiThreading:
    def __init__(self, threads):
        self.threads = threads
        self.browsers = []
        self.options = Options()
        self.options.headless = False
        self.options.add_argument("--window-size=1920,1080")
        self.service = Service(executable_path='./chromedriver.exe')

    def open_multi_browser(self):
        try:
            self.browsers = [webdriver.Chrome(service=self.service, options=self.options) for _ in range(self.threads)]
            print(f"open {self.threads} browser successfully")
        except:
            print("open multi-browser failed")

    def load_browser(self, ticker_i, ticiker_df):
        for thread_i in range(self.threads):
            browser = self.browsers[thread_i]
            t = threading.Thread(target=get_data,
                                 args=(browser,
                                       ticker_df['ticker'][ticker_i+thread_i].lower(),
                                       None))
            t.start()



if __name__ == "__main__":
    ticker_df = pd.read_excel(r'./data/document/code_stock.xlsx')
    num_tickers = len(ticker_df)
    crawler = MultiThreading(threads=2)

    try:
        crawler.open_multi_browser()
        for ticker_i in range(0, num_tickers, 2):
            crawler.load_browser(ticker_i, ticker_df)
        print("Web Scraping Complete")

    except:
        print("Web Scraping Fail")



