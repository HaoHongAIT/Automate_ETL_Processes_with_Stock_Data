from time import sleep
import pandas as pd
from selenium.webdriver.common.by import By
import os

def save(lst, ticker, cols, index):
    folder_path = f"./data/raw/{ticker}"
    if not os.path.exists(folder_path):
        os.mkdir(folder_path)
    try:
        num_cols = len(cols)
        sub_lst = [lst[i:i + num_cols] for i in range(0, len(lst), num_cols)]
        full_path = os.path.join(folder_path, f"{ticker}_{index}.csv")
        pd.DataFrame(sub_lst[1:], columns=cols).to_csv(full_path, index=False)
        print(f"Save Successfully >> {full_path}")

    except Exception as e:
        print(e)

def get_price_history(browser, ticker, time=None):
    url = f"https://s.cafef.vn/lich-su-giao-dich-{ticker}-1.chn"
    browser.get(url)
    sleep(2)
    if time:
        search_bar = browser.find_element(
            By.ID, 'date-inp-disclosure')
        browser.execute_script(
            f"arguments[0].value = '{time}' ", search_bar)
        browser.find_element(By.ID, 'owner-find').click()

    class_name = ""
    data = []
    while "enable" not in class_name:
        elements = browser.find_elements(By.CSS_SELECTOR, ".render-table-owner td")
        data += [element.text for element in elements]
        next_page = browser.find_element(By.ID, "paging-right")
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


def get_order_flow_stat(browser, ticker, time=None):
    url = f"https://s.cafef.vn/lich-su-giao-dich-{ticker}-2.chn"
    browser.get(url)
    sleep(2)

    if time:
        search_bar = browser.find_element(By.ID, 'date-inp-disclosure')
        browser.execute_script(f"arguments[0].value = '{time}' ", search_bar)
        browser.find_element(By.ID, 'owner-find').click()
    class_name = ""
    data = []
    while "enable" not in class_name:
        elements = browser.find_elements(
            By.CSS_SELECTOR, ".render-table-owner td")
        data += [element.text for element in elements]
        next_page = browser.find_element(By.ID, "paging-right")
        next_page.click()
        class_name = next_page.get_attribute("class")
    sleep(2)
    # SAVE FILE
    cols = ["date", "rate_change", "buy_orders", "buy_volume", "average_buy_order_volume",
            "sell_orders", "sell_volume", "average_sell_order_volume", "net_volume"]
    save(ticker=ticker, lst=data, cols=cols, index=2)
    print("Get Order Flow Statistics Complete")


def get_foreign_investors(browser, ticker, time=None):
    url = f"https://s.cafef.vn/lich-su-giao-dich-{ticker}-3.chn"
    browser.get(url)
    sleep(2)

    if time:
        search_bar = browser.find_element(By.ID, 'date-inp-disclosure')
        browser.execute_script(f"arguments[0].value = '{time}' ", search_bar)
        browser.find_element(By.ID, 'owner-find').click()

    class_name = ""
    data = []
    while "enable" not in class_name:
        elements = browser.find_elements(
            By.CSS_SELECTOR, ".render-table-owner td")
        data += [element.text for element in elements]
        next_page = browser.find_element(By.ID, "paging-right")
        next_page.click()
        class_name = next_page.get_attribute("class")
    sleep(2)
    # SAVE FILE
    cols = ["date", "rate_change", "net_trading_volume", "net_trading_value_billion_vnd",
            "buy_volume", "buy_value_billion_vnd", "sell_volume", "sell_value_billion_vnd",
            "remaining_room", "current_ownership"]
    save(ticker=ticker, lst=data, cols=cols, index=3)
    print("Get Foreign Investors Complete")

def get_proprietary_trading(browser, ticker, time=None):
    url = f"https://s.cafef.vn/lich-su-giao-dich-{ticker}-4.chn"
    print("Get Proprietary Trading Complete")
    browser.get(url)
    sleep(2)

    if time:
        search_bar = browser.find_element(By.ID, 'date-inp-disclosure')
        browser.execute_script(f"arguments[0].value = '{time}' ", search_bar)
        browser.find_element(By.ID, 'owner-find').click()

    class_name = ""
    data = []
    while "enable" not in class_name:
        elements = browser.find_elements(
            By.CSS_SELECTOR, ".render-table-owner td")
        data += [element.text for element in elements]
        next_page = browser.find_element(By.ID, "paging-right")
        next_page.click()
        class_name = next_page.get_attribute("class")
        sleep(1)
    # SAVE FILE
    cols = ["ticker", "date", "buy_volume", "buy_value_bil_vnd",
            "sell_volume", "sell_value_bil_vnd", "net_trading_volume",
            "net_trading_value_bil_vnd"]

    save(ticker=ticker, lst=data, cols=cols, index=4)
    print("Get Proprietry Trading Complete")


def get_data(browser, ticker, time_range=None):
    try:
        get_price_history(browser=browser, ticker=ticker, time=time_range)
        # get_order_flow_stat(browser=browser, ticker=ticker, time=time_range)
        # get_foreign_investors(browser=browser, ticker=ticker, time=time_range)
        # get_proprietary_trading(browser=browser, ticker=ticker, time=time_range)
        print("Web Scraping Complete "+ ticker)

    except Exception as e:
        print(e)
        print("Web Scraping Fail")

    finally:
        browser.close()