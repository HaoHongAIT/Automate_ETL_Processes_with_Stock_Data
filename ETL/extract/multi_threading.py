import threading
from queue import Queue
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from .web_scraping import *
# from ..log import add_to_log


class MultiThreading:
    def __init__(self, threads, code_list):
        self.threads = threads
        self.browsers = []
        self.code_list = code_list

    def open_multi_browser(self):
        options = Options()
        options.headless = False
        options.add_argument("--window-size=1920,1080")
        service = Service(executable_path='./chromedriver.exe')
        try:
            self.browsers = [webdriver.Chrome(service=service, options=options) for _ in range(self.threads)]
            print(f"Open {self.threads} browsers successfully")

        except Exception as e:
            print(e)

    def close_multi_browser(self):
        self.browsers = []
        print(f"Close {self.threads} browser successfully")

    def load_browser(self, ticker_i, time_range=None):
        queue = Queue(self.threads)  # Control Threads with Queue
        for thread_i in range(self.threads):
            browser_i = self.browsers[thread_i]
            # b_i: browser ith, df: dataframe stock code, q: queue, t: time_range
            th = threading.Thread(target=lambda q, b_i, lst, index, t: q.put(get_data(b_i, lst[index], t)),
                                  args=(queue, browser_i, self.code_list, ticker_i + thread_i, time_range))
            th.start()

        try:
            for _ in range(self.threads):
                add_to_log(queue.get())

        except Exception as e:
            print(e)

    def run(self, time_range=None):
        num_tickers = len(self.code_list)
        for ticker_i in range(0, num_tickers, self.threads):
            self.open_multi_browser()
            self.load_browser(ticker_i, time_range)
            self.close_multi_browser()