from time import sleep
import pandas as pd
from selenium.webdriver.common.by import By
import os
from datetime import date

SLEEP_TIME = 1
ATTRIBUTE_NAMES = {1: ["date", "close", "adjusting_price", "rate_change", "order_matching_volume",
                       "order_matching_value", "block_trade_volume", "block_trade_value", "open", "high", "low"],
                   2: ["date", "rate_change", "buy_orders", "buy_volume", "average_buy_order_volume",
                       "sell_orders", "sell_volume", "average_sell_order_volume", "net_volume"],
                   3: ["date", "rate_change", "net_trading_volume", "net_trading_value_billion_vnd", "buy_volume",
                       "buy_value_billion_vnd", "sell_volume", "sell_value_billion_vnd", "remaining_room",
                       "current_ownership"],
                   4: ["ticker", "date", "buy_volume", "buy_value_bil_vnd", "sell_volume", "sell_value_bil_vnd",
                       "net_trading_volume", "net_trading_value_bil_vnd"]}
log = ""


def save(lst, ticker, cols, index):
    num_records, num_cols = len(lst), len(cols)
    # Check Blank Table
    global log
    if num_records < num_cols:
        log += f"No {ticker.upper()} Data:\n>> https://s.cafef.vn/lich-su-giao-dich-{ticker}-{index}.chn\n"

    else:
        # Check exist folder
        # folder_path = os.path.join(ROOT_DIR, f"data\\raw\\{date.today().strftime(r'%Y-%m-%d')}")
        folder_path = f"./data/raw/{date.today().strftime(r'%Y-%m-%d')}"
        if not os.path.exists(folder_path):
            os.mkdir(folder_path)
        # Save list data to csv file
        try:
            sub_lst = [lst[i:i + num_cols] for i in range(0, num_records, num_cols)]
            full_path = os.path.join(folder_path, f"{ticker}_{index}.csv")
            pd.DataFrame(sub_lst[1:], columns=cols).to_csv(full_path, index=False)

        except Exception as e:
            log += f"{e}\n"


def get_data_from_element(browser, ticker, index, time_range=None):
    url = f"https://s.cafef.vn/lich-su-giao-dich-{ticker}-{index}.chn"
    browser.get(url)
    sleep(SLEEP_TIME)
    if time_range:
        search_bar = browser.find_element(By.ID, 'date-inp-disclosure')
        browser.execute_script(f"arguments[0].value = '{time_range}' ", search_bar)
        browser.find_element(By.ID, 'owner-find').click()
        sleep(SLEEP_TIME)

    class_name, data = "", []
    while "enable" not in class_name:
        elements = browser.find_elements(By.CSS_SELECTOR, ".render-table-owner td")
        data += [element.text for element in elements]
        next_page = browser.find_element(By.ID, "paging-right")
        next_page.click()
        class_name = next_page.get_attribute("class")
        sleep(SLEEP_TIME)

    save(ticker=ticker, lst=data, cols=ATTRIBUTE_NAMES[index], index=index)


def get_data(browser, ticker_code, time_range=None):
    ticker = ticker_code.lower()
    global log
    for i in range(1, 5):
        try:
            get_data_from_element(browser=browser, ticker=ticker, index=i, time_range=time_range)
        except Exception as e:
            log += f"{i}\n {e}-----------------\n"

    browser.close()
    return log
