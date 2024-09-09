from time import sleep
import pandas as pd
from selenium.webdriver.common.by import By
import os

SLEEP_TIME = 2


def save(lst, ticker, cols, index):
    num_records, num_cols = len(lst), len(cols)
    # Check Null List
    if num_records < num_cols:
        print("Don't Have Data")
        return

    folder_path = f"./data/raw/{ticker}"
    if not os.path.exists(folder_path):
        os.mkdir(folder_path)
    try:

        sub_lst = [lst[i:i + num_cols] for i in range(0, num_records, num_cols)]
        full_path = os.path.join(folder_path, f"{ticker}_{index}.csv")
        pd.DataFrame(sub_lst[1:], columns=cols).to_csv(full_path, index=False)
        print(f"Save Successfully >> {full_path}")

    except Exception as e:
        print(e)


def get_data_from_element(browser, url, time_range):
    browser.get(url)
    sleep(SLEEP_TIME)
    if time_range:
        search_bar = browser.find_element(By.ID, 'date-inp-disclosure')
        browser.execute_script(f"arguments[0].value = '{time_range}' ", search_bar)
        browser.find_element(By.ID, 'owner-find').click()
        sleep(3)

    class_name = ""
    data = []
    while "enable" not in class_name:
        elements = browser.find_elements(By.CSS_SELECTOR, ".render-table-owner td")
        data += [element.text for element in elements]
        next_page = browser.find_element(By.ID, "paging-right")
        next_page.click()
        class_name = next_page.get_attribute("class")
        sleep(3)
    return data


def get_price_history(browser, ticker, time_range=None):
    url = f"https://s.cafef.vn/lich-su-giao-dich-{ticker}-1.chn"
    data = get_data_from_element(browser, url, time_range)
    cols = ["date", "close", "adjusting_price", "rate_change",
            "order_matching_volume", "order_matching_value",
            "block_trade_volume", "block_trade_value",
            "open", "high", "low"]
    save(ticker=ticker, lst=data, cols=cols, index=1)
    print("Get Price History Complete")


def get_order_flow_stat(browser, ticker, time_range=None):
    url = f"https://s.cafef.vn/lich-su-giao-dich-{ticker}-2.chn"
    data = get_data_from_element(browser, url, time_range)
    cols = ["date", "rate_change", "buy_orders", "buy_volume", "average_buy_order_volume",
            "sell_orders", "sell_volume", "average_sell_order_volume", "net_volume"]
    save(ticker=ticker, lst=data, cols=cols, index=2)
    print("Get Order Flow Statistics Complete")


def get_foreign_investors(browser, ticker, time_range=None):
    url = f"https://s.cafef.vn/lich-su-giao-dich-{ticker}-3.chn"
    data = get_data_from_element(browser, url, time_range)
    cols = ["date", "rate_change", "net_trading_volume", "net_trading_value_billion_vnd",
            "buy_volume", "buy_value_billion_vnd", "sell_volume", "sell_value_billion_vnd",
            "remaining_room", "current_ownership"]
    save(ticker=ticker, lst=data, cols=cols, index=3)
    print("Get Foreign Investors Complete")


def get_proprietary_trading(browser, ticker, time_range=None):
    url = f"https://s.cafef.vn/lich-su-giao-dich-{ticker}-4.chn"
    data = get_data_from_element(browser, url, time_range)
    cols = ["ticker", "date", "buy_volume", "buy_value_bil_vnd",
            "sell_volume", "sell_value_bil_vnd", "net_trading_volume",
            "net_trading_value_bil_vnd"]
    save(ticker=ticker, lst=data, cols=cols, index=4)
    print("Get Proprietry Trading Complete")


def get_data(browser, ticker_code, time_range=None):
    ticker = ticker_code.lower()
    try:
        get_price_history(browser=browser, ticker=ticker, time_range=time_range)
        get_order_flow_stat(browser=browser, ticker=ticker, time_range=time_range)
        get_foreign_investors(browser=browser, ticker=ticker, time_range=time_range)
        get_proprietary_trading(browser=browser, ticker=ticker, time_range=time_range)
        print("Web Scraping Complete >> " + ticker.upper())

    except Exception as e:
        print(e)
        print("Web Scraping Fail")

    finally:
        browser.close()
