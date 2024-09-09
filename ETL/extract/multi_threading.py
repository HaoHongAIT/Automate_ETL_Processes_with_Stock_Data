import threading
from web_scraping import *
import pandas as pd
from queue import Queue
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

    def close_multi_browser(self):
        self.browsers = []

    def load_browser(self, ticker_i, ticker_df, time_range=None):
        queue = Queue(self.threads) # Control Threads
        for thread_i in range(self.threads):
            browser_i = self.browsers[thread_i]
            th = threading.Thread(target=lambda b_i, df, index, q, t: q.put(get_data(b_i, #browser_i
                                                                                     df['ticker'][index], #stock code
                                                                                     t)), #time_range
                                  args=(browser_i, ticker_df, ticker_i + thread_i, queue, time_range))

            th.start()

        try:
            sleep(10)
            for _ in range(self.threads):
                queue.get()

        except Exception as e:
            print(e)


if __name__ == "__main__":
    ticker_df = pd.read_excel(r'./data/document/code_stock.xlsx')
    num_tickers = len(ticker_df)
    time_range = "01/07/2024 - 31/08/2024"
    crawler = MultiThreading(threads=2)

    for ticker_i in range(0, num_tickers, crawler.threads):
        crawler.open_multi_browser()
        crawler.load_browser(ticker_i, ticker_df)
        crawler.close_multi_browser()


