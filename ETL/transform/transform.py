import pandas as pd
import re



def trans_price_history(ticker,index=1):
    df = pd.read_csv(f"./data/raw/{ticker}/{ticker}_{index}.csv")
    df['date'] = pd.to_datetime(df['date'], format='%d/%m/%Y')
    df['adjusting_price'] = df['adjusting_price'].replace('--', 'N/A')
    rate = lambda x: re.search(r'\(([-+]?\d*\.?\d+)\s*%', x).group(1) if pd.notnull(x) else x
    df['rate_change'] = df['rate_change'].apply(rate)
    df['order_matching_volume'] = [int(value.replace(',', '')) for value in df['order_matching_volume']]
    df['order_matching_value'] = [float(value.replace(',', '')) for value in df['order_matching_value']]
    df['block_trade_volume'] = [int(value.replace(',', '')) for value in df['block_trade_volume']]
    df['ticker'] = ticker.lower()


    print("Transform Complete Price History")
    return df

def trans_order_flow_stat(ticker, index=2):
    df = pd.read_csv(f"./data/raw/{ticker}/{ticker}_{index}.csv")
    df['date'] = pd.to_datetime(df['date'], format='%d/%m/%Y')

    # rate = lambda x: re.search(r'\(\s*([-+]?\d*\.?\d+)\s*%', x).group(1) if pd.notnull(x) else x
    # df['rate_change'] = df['rate_change'].apply(rate)

    df['buy_orders'] = [int(value.replace(',', '')) for value in df['buy_orders']]
    df['buy_volume'] = [int(value.replace(',', '')) for value in df['buy_volume']]

    df['average_buy_order_volume'] = [float(value.replace(',', '')) for value in df['average_buy_order_volume']]

    df['sell_orders'] = [int(value.replace(',', '')) for value in df['sell_orders']]
    df['sell_volume'] = [int(value.replace(',', '')) for value in df['sell_volume']]
    df['average_sell_order_volume'] = [int(value.replace(',', '')) for value in df['average_sell_order_volume']]
    df['net_volume'] = [int(value.replace(',', '')) for value in df['net_volume']]
    df['ticker'] = ticker.lower()


    df.drop(columns=['rate_change', ])
    print("Transform Complete Order Flow Statistics")
    df.to_csv(f"./data/raw/{ticker}/transformed_{ticker}_{index}.csv",  index=False)

def trans_foreign_investors(ticker, index=3):
    df = pd.read_csv(f"./data/raw/{ticker}/{ticker}_{index}.csv")
    df['date'] = pd.to_datetime(df['date'], format='%d/%m/%Y')
    # rate = lambda x: re.search(r'\(\s*([-+]?\d*\.\d+)\s*%\)', x).group(1) if pd.notnull(x) else x
    # df['rate_change'] = df['rate_change'].apply(rate)
    df['net_trading_volume'] = [int(value.replace(',', '')) for value in df['net_trading_volume']]
    df['buy_volume'] = [int(value.replace(',', '')) for value in df['buy_volume']]
    df['sell_volume'] = [int(value.replace(',', '')) for value in df['sell_volume']]
    df['remaining_room'] = [int(value.replace(',', '')) for value in df['remaining_room']]
    df['current_ownership'] = [float(value.replace('%', '')) for value in df['current_ownership']]
    # Add ticker code
    df['ticker'] = ticker.lower()

    df.drop(columns=['rate_change', ])
    print("Transform Complete Foreign Investors")
    df.to_csv(f"./data/raw/{ticker}/transformed_{ticker}_{index}.csv",  index=False)

def trans_proprietary_trading(ticker, index=4):
    df = pd.read_csv(f"./data/raw/{ticker}/{ticker}_{index}.csv")
    df["ticker"] = ticker.lower()
    df['date'] = pd.to_datetime(df['date'], format='%d/%m/%Y')
    df['buy_volume'] = [int(value.replace(',', '')) for value in df['buy_volume']]
    df['sell_volume'] = [int(value.replace(',', '')) for value in df['sell_volume']]
    df["net_trading_volume"] = [int(value.replace(',', '')) for value in df["net_trading_volume"]]
    df['ticker'] = ticker.lower()
    print("Transform Complete Proprietary Trading")
    df.to_csv(f"./data/raw/{ticker}/transformed_{ticker}_{index}.csv",  index=False)

def run(ticker):
    trans_price_history(ticker=ticker)
    trans_foreign_investors(ticker=ticker)
    trans_order_flow_stat(ticker=ticker)
    trans_proprietary_trading(ticker=ticker)