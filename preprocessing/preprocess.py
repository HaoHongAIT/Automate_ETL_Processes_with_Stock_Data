import pandas as pd
import re


def preprocess(ticker):
    df = pd.read_csv(f"./data/raw/{ticker}.csv")
    # Convert the 'date' column to datetime format (dd/mm/yyyy)
    df['date'] = pd.to_datetime(df['date'], format='%d/%m/%Y')
    # Replace '--' with 'N/A' in the 'adjusting_price' column
    df['adjusting_price'] = df['adjusting_price'].replace('--', 'N/A')
    # Extract the value inside the parentheses from the 'rate_change' column
    df['rate_change'] = df['rate_change'].apply(lambda x: re.search(r'\(([-+]?\d*\.?\d+)\s*%', x).group(1) if pd.notnull(x) else x)

    df['order_matching_volume'] = [int(value.replace(',', '')) for value in df['order_matching_volume']]
    df['order_matching_value'] = [float(value.replace(',', '')) for value in df['order_matching_value']]
    df['block_trade_volume'] = [int(value.replace(',', '')) for value in df['block_trade_volume']]
    return df


ticker_names = ['fpt']
ticker_dict = {}
root_folder = './data/raw/'
for file_name in ticker_names:
    path = f"{root_folder}{file_name}.csv"
    ticker = pd.read_csv(path)
    #ticker['Date/Time'] = pd.to_datetime(ticker['Date/Time'])
    #ticker.index = ticker['Date/Time']
    #ticker = ticker.drop(['Date/Time'], axis=1)
    #ticker['Fluctuation'] = ticker['Close'] - ticker['Open']
    ticker_dict[file_name] = ticker
df = pd.DataFrame()
for ticker in ticker_dict:
    df = pd.concat([df, ticker_dict[ticker]])


def train_test_split(ticker_df, test_size  = 0.15, valid_size = 0.15):
    test_split_idx  = int(len(ticker_df) * (1-test_size))
    valid_split_idx = int(len(ticker_df) * (1-(valid_size+test_size)))
    train_df  = ticker_df.iloc[:valid_split_idx].copy()
    valid_df  = ticker_df.iloc[valid_split_idx+1:test_split_idx].copy()
    test_df   = ticker_df.iloc[test_split_idx+1:].copy()
    return train_df, valid_df, test_df

def drop(ticker_df, cols=None, frows=None):
    if cols:
        ticker_df = ticker_df.drop(cols, axis=1)
    elif frows:
        ticker_df = ticker_df.tail(-frows)
    return ticker_df

def xy_split(train, valid, test, y_col):
    y_train = train[y_col].copy()
    X_train = train.drop([y_col], axis=1)

    y_valid = valid[y_col].copy()
    X_valid = valid.drop([y_col], axis=1)

    y_test  = test[y_col].copy()
    X_test  = test.drop([y_col], axis=1)
    return y_train, X_train, y_valid, X_valid, y_test, X_test


def calc_MA(ticker_df, time_dict):
    for unit in time_dict:
        for ma in time_dict[unit]:
            column_name = f"MA{ma}_" + unit
            if unit == 'minutes':
                time_i = timedelta(minutes=ma)
            elif unit == 'hours':
                time_i = timedelta(hours=ma)
            elif unit == 'days':
                time_i = timedelta(days=ma)
            ticker_df[column_name] = ticker_df['Close'].rolling(time_i).mean()


def calc_SMA(ticker_df, time_dict):
    for unit in time_dict:
        for sma in time_dict[unit]:
            column_name = f"SMA{sma}_" + unit
            if unit == 'minutes':
                time_i = timedelta(minutes=sma)
            elif unit == 'hours':
                time_i = timedelta(hours=sma)
            elif unit == 'days':
                time_i = timedelta(days=sma)
            ticker_df[column_name] = ticker_df['Close'].rolling(time_i).mean().shift()


def calc_EMA(ticker_df, time_dict):
    for unit in time_dict:
        for ema in time_dict['days']:
            column_name = f"EMA{ema}"
            ticker_df[column_name] = ticker_df['Close'].ewm(ema).mean().shift()


def calc_RSI(ticker_df, days=14):
    close = ticker_df['Close']
    delta = close.diff()
    delta = delta[1:]
    pricesUp = delta.copy()
    pricesDown = delta.copy()
    pricesUp[pricesUp < 0] = 0
    pricesDown[pricesDown > 0] = 0
    rollUp = pricesUp.rolling(days).mean()
    rollDown = pricesDown.abs().rolling(days).mean()
    rs = rollUp / rollDown
    rsi = 100.0 - (100.0 / (1.0 + rs))
    ticker_df['RSI'] = rsi.fillna(0)

def calc_MACD(ticker_df):
    EMA_12 = pd.Series(ticker_df['Close'].ewm(span=12, min_periods=12).mean())
    EMA_26 = pd.Series(ticker_df['Close'].ewm(span=26, min_periods=26).mean())
    ticker_df['MACD'] = pd.Series(EMA_12 - EMA_26)
    ticker_df['MACD_signal'] = pd.Series(ticker_df.MACD.ewm(span=9, min_periods=9).mean())


if __name__ == '__main__':
    time_dict = {'minutes': [5, 15, 30], 'hours': [1, 6, 12], 'days': [1, 10, 15, 30]}
    FPT_ticker = ticker_dict['FPT'].copy()
    calc_MA(FPT_ticker, time_dict)
    calc_SMA(FPT_ticker, time_dict)
    calc_EMA(FPT_ticker, time_dict)
    calc_RSI(FPT_ticker)
    calc_MACD(FPT_ticker)
    FPT_ticker.columns

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