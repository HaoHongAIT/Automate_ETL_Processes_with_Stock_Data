from time import timedelta
import pandas as pd


def calc_fluctuation(df):
    df['fluctuation'] = df['close'] - df['opem']
    return df


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
