from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from time import sleep
from queue import Queue
import pandas as pd
import threading
import GetData

# https://googlechromelabs.github.io/chrome-for-testing/#stable


class MultiThreading:
    def __init__(self, threads):
        self.url_list = []
        self.df = pd.DataFrame({'category': [], 'title': [], 'brief': [
        ], 'date': [], 'content': [], 'sources': []})
        self.threads = threads
        self.browsers = []
        self.options = Options()
        self.options.headless = False
        self.options.add_argument("--window-size=1920,1080")
        self.service = Service(executable_path='./chromedriver.exe')

    def open_MultiBrowsers(self):
        try:
            self.browsers = [webdriver.Chrome(
                service=self.service, options=self.options) for _ in range(self.threads)]
            print(f"open {self.threads} browser successfully")
        except:
            print("open multi-browser is fail")

    def crawl_datatable(self):
        pass

    def crawl_news(self):
        pass


if __name__ == '__main__':
    threads = 6  # number of stock code
    multi_threading = MultiThreading(threads=threads)
    max_page = 264

    try:  # Get url
        for page_i in range(1, max_page, multi_threading.threads):
            multi_threading.open_MultiBrowsers()
            multi_threading.crawl_Urls(page=page_i)
        # Crawl data from table
        current_url = 0
        for i in range(current_url, len(multi_threading.url_list), multi_threading.threads):
            multi_threading.open_MultiBrowsers()
            multi_threading.crawl_News(url_index=current_url)
    except:
        pass
    # Save
    multi_threading.df.to_csv(f'./coffee.csv')
    print("save successfully")
