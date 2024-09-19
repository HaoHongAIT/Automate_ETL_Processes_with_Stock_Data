import pandas as pd
import re
import glob
import os


def obj_to_int(values) -> list:
    lst = []
    for value in values:
        if isinstance(value, str): lst.append(int(value.replace(',', '')))
        elif isinstance(value, int): lst.append(value),
    return lst

def obj_to_float(values) -> list:
    lst = []
    for value in values:
        if isinstance(value, str): lst.append(float(value.replace(',', '')))
        elif isinstance(value, int): lst.append(float(value)),
        elif isinstance(value, float): lst.append(value)
    return lst

def combine_csv(char, folder_path, show_info=False) -> pd.DataFrame:
    df = pd.DataFrame()
    path = glob.glob(folder_path + "\\*.csv")
    for file_path in path:
        tmp = pd.read_csv(file_path)
        if  char in file_path: df = df._append(tmp, ignore_index=True)

    if show_info:
        print(f"CSV Info: ---\ndataframe:\n{df.dtypes}\n---")

    return df


class Transform:
    def __init__(self, time):
        self.save_folder = f".\\data\\transformed\\{time}"
        self.raw_folder = f".\\data\\raw\\{time}"
        if not os.path.exists(self.save_folder):
            os.makedirs(self.save_folder)

    def trans_price_history(self):
        df = combine_csv(char="_1.", folder_path=self.raw_folder)
        df['date'] = pd.to_datetime(df['date'], format='%d/%m/%Y')
        df['adjusting_price'] = df['adjusting_price'].replace('--', 'N/A')
        rate = lambda x: float(re.search(r'\(([-+]?\d*\.?\d+)\s*%', x).group(1)) if pd.notnull(x) else float(x)
        df['rate_change'] = df['rate_change'].apply(rate)
        df['order_matching_volume'] = obj_to_int(df["order_matching_volume"].tolist())
        df['block_trade_volume'] = obj_to_int(df["block_trade_volume"].tolist())
        df['block_trade_value'] = obj_to_float(df["block_trade_value"].tolist())
        df['order_matching_value'] = obj_to_float(df['order_matching_value'].tolist())
        df.drop_duplicates(inplace=True)
        df.to_csv(f"{self.save_folder}\\prices_history.csv", index=False)

    def trans_order_flow_stat(self):
        df = combine_csv(char="_2.", folder_path=self.raw_folder)
        df['date'] = pd.to_datetime(df['date'], format='%d/%m/%Y')
        df['buy_orders'] = obj_to_int(df["buy_orders"].tolist())
        df['buy_volume'] = obj_to_int(df["buy_volume"].tolist())
        df['average_sell_order_volume'] = obj_to_int(df["average_sell_order_volume"].tolist())
        df['sell_orders'] = obj_to_int(df["sell_orders"].tolist())
        df['sell_volume'] = obj_to_int(df["sell_volume"].tolist())
        df['net_volume'] = obj_to_int(df["net_volume"].tolist())
        df['average_buy_order_volume'] = obj_to_float(df['average_buy_order_volume'])
        df.drop(columns=['rate_change'], inplace=True)
        df.drop_duplicates(inplace=True)
        df.to_csv(f"{self.save_folder}\\order_flow_stat.csv", index=False)

    def trans_foreign_investors(self):
        df = combine_csv(char="_3.", folder_path=self.raw_folder)
        df['date'] = pd.to_datetime(df['date'], format='%d/%m/%Y')
        df['net_trading_volume'] = obj_to_int(df['net_trading_volume'].tolist())
        df['buy_volume'] = obj_to_int(df['buy_volume'].tolist())
        df['sell_volume'] = obj_to_int(df['sell_volume'].tolist())
        df['remaining_room'] = obj_to_int(df['remaining_room'].tolist())
        df['current_ownership'] = df['current_ownership'].apply(lambda x: x.replace("%",""))
        df['current_ownership'] = obj_to_float(df['current_ownership'].tolist())
        df.drop(columns=['rate_change'], inplace=True)
        df.drop_duplicates(inplace=True)
        df.to_csv(f"{self.save_folder}\\foreign_investors.csv", index=False)

    def trans_proprietary_trading(self):
        df = combine_csv(char="_4.", folder_path=self.raw_folder)
        df['date'] = pd.to_datetime(df['date'], format='%d/%m/%Y')
        df['buy_volume'] = obj_to_int(df['buy_volume'].tolist())
        df['sell_volume'] = obj_to_int(df['sell_volume'].tolist())
        df["net_trading_volume"] = obj_to_int(df["net_trading_volume"].tolist())
        df.drop_duplicates(inplace=True)
        df.to_csv(f"{self.save_folder}\\proprietary_trading.csv", index=False)

    def run(self):
        self.trans_price_history()
        self.trans_order_flow_stat()
        self.trans_foreign_investors()
        self.trans_proprietary_trading()
