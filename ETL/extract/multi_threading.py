import threading
from web_scraping import *
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service



class MultiThreading:
    def __init__(self, threads):
        self.threads = threads
        self.browsers = []

    def open_multi_browser(self):
        options = Options()
        options.headless = False
        options.add_argument("--window-size=1920,1080")
        service = Service(executable_path='./chromedriver.exe')
        try:
            self.browsers = [webdriver.Chrome(service=service, options=options) for _ in range(self.threads)]
            print(f"open {self.threads} browser successfully")

        except:
            print("open multi-browser failed")

    def load_browser(self, ticker_i, ticker_df):
        time_range = "01/07/2024 - 31/08/2024"
        for thread_i in range(self.threads):
            browser_i = self.browsers[thread_i]
            t = threading.Thread(target=get_data, args=(browser_i, ticker_df['ticker'][ticker_i+thread_i].lower(),
                                                        time_range))
            t.start()


if __name__ == "__main__":
    ticker_df = pd.read_excel(r'./data/document/code_stock.xlsx')
    # ticker_df = pd.read_excel(r'./data/document/test.xlsx')
    num_tickers = len(ticker_df)
    crawler = MultiThreading(threads=2)
    crawler.open_multi_browser()
    for ticker_i in range(0, 10, crawler.threads):
        crawler.load_browser(ticker_i, ticker_df)
    print("Multi Threading Web Scraping Complete")

