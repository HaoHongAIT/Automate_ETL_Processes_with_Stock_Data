import pandas as pd
import re


def preprocess(ticker):
    df = pd.read_csv(f"./data/raw/{ticker}.csv")
    # Convert the 'date' column to datetime format (dd/mm/yyyy)
    df['date'] = pd.to_datetime(df['date'], format='%d/%m/%Y')
    # Replace '--' with 'N/A' in the 'adjusting_price' column
    df['adjusting_price'] = df['adjusting_price'].replace('--', 'N/A')
    # Extract the value inside the parentheses from the 'rate_change' column
    df['rate_change'] = df['rate_change'].apply(
        lambda x: re.search(r'\(([-+]?\d*\.?\d+)\s*%', x).group(1) if pd.notnull(x) else x)

    replace_cell = lambda col: [int(value.replace(',', '')) for value in col]
    df['order_matching_volume'] = replace_cell(df['order_matching_volume'])
    df['order_matching_value'] = replace_cell(df['order_matching_value'])
    df['block_trade_volume'] = replace_cell(df['block_trade_volume'])

    # df['order_matching_volume'] = [int(value.replace(',', '')) for value in df['order_matching_volume']]
    # df['order_matching_value'] = [float(value.replace(',', '')) for value in df['order_matching_value']]
    # df['block_trade_volume'] = [int(value.replace(',', '')) for value in df['block_trade_volume']]
    return df


ticker_names = ['fpt']
ticker_dict = {}
root_folder = './data/raw/'
for file_name in ticker_names:
    path = f"{root_folder}{file_name}.csv"
    ticker = pd.read_csv(path)
    # ticker['Date/Time'] = pd.to_datetime(ticker['Date/Time'])
    # ticker.index = ticker['Date/Time']
    # ticker = ticker.drop(['Date/Time'], axis=1)
    # ticker['Fluctuation'] = ticker['Close'] - ticker['Open']
    ticker_dict[file_name] = ticker
df = pd.DataFrame()
for ticker in ticker_dict:
    df = pd.concat([df, ticker_dict[ticker]])

if __name__ == '__main__':
    # FPT_ticker['Fluctuation'] = FPT_ticker['Fluctuation'].shift(-1)
    FPT_ticker['Close'] = FPT_ticker['Close'].shift(-1)
    # drop_cols = ['Close', 'Open', 'Low', 'High', 'Open Interest', 'Ticker']
    FPT_ticker = drop(FPT_ticker, cols=['Open', 'Low', 'High', 'Open Interest', 'Ticker'], frows=3300)
    FPT_ticker = FPT_ticker[:-1]
    FPT_ticker.columns

    FPT_train, FPT_valid, FPT_test = train_test_split(FPT_ticker)
    # plot_dataset(FPT_train, FPT_valid, FPT_test, col='Fluctuation')
    plot_dataset(FPT_train, FPT_valid, FPT_test, col='Close')

    # y_train, X_train, y_valid, X_valid, y_test, X_test = xy_split(FPT_train, FPT_valid, FPT_test, y_col='Fluctuation')
    y_train, X_train, y_valid, X_valid, y_test, X_test = xy_split(FPT_train, FPT_valid, FPT_test, y_col='Close')
    num_epochs = 1_000_000
    patience = 20
    learning_rate = 0.1
