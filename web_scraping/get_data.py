from time import sleep
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from time import sleep
from queue import Queue
import pandas as pd
import threading

df = {"date":[], "closed_price":[], "adjusted_price":[],
      "change": []}


if __name__ == '__main__':    
    categories = [1]
    stock_codes = ["fpt"]
    options = Options()
    options.headless = False
    options.add_argument("--window-size=1920,1080")
    service = Service(executable_path='./chromedriver.exe')
    browser = webdriver.Chrome(service=service, options=options)
    for stock_code in stock_codes:
        for i in categories:            
          browser.get(f"https://s.cafef.vn/lich-su-giao-dich-{stock_code}-{i}.chn")                            
          elements = browser.find_elements(By.CSS_SELECTOR, ".render-table-owner td")
        #   links = [element.text for element in elements]                     
        #   break          
    browser.close()    