import pandas as pd
import re


def transform(ticker):
    # Read csv file
    df = pd.read_csv(f"./data/raw/{ticker}.csv")
    # Convert the 'date' column to datetime format (dd/mm/yyyy)
    df['date'] = pd.to_datetime(df['date'], format='%d/%m/%Y')
    # Replace '--' with 'N/A' in the 'adjusting_price' column
    df['adjusting_price'] = df['adjusting_price'].replace('--', 'N/A')
    # Extract the value inside the parentheses from the 'rate_change' column
    rate = lambda x: re.search(r'\(([-+]?\d*\.?\d+)\s*%', x).group(1) if pd.notnull(x) else x
    df['rate_change'] = df['rate_change'].apply(rate)

    df['order_matching_volume'] = [int(value.replace(',', '')) for value in df['order_matching_volume']]
    df['order_matching_value'] = [float(value.replace(',', '')) for value in df['order_matching_value']]
    df['block_trade_volume'] = [int(value.replace(',', '')) for value in df['block_trade_volume']]
    return df
