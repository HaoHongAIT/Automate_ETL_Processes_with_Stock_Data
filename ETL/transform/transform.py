import pandas as pd
import re
# from datetime import date
import glob
import os


# TODAY = date.today().strftime(r"%Y-%m-%d")
def obj_to_int(values):
    lst = []
    for value in values:
        if isinstance(value, str): lst.append(int(value.replace(',', '')))
        elif isinstance(value, int): lst.append(value),
    return lst

def obj_to_float(values):
    lst = []
    for value in values:
        if isinstance(value, str): lst.append(float(value.replace(',', '')))
        elif isinstance(value, int): lst.append(float(value)),
        elif isinstance(value, float): lst.append(value)
    return lst



class Transform:
    def __init__(self):
        self.save_folder = f".\\data\\transformed\\2024-09-14"
        if not os.path.exists(self.save_folder):
            os.makedirs(self.save_folder)

    def combine_csv(self):
        df1, df2, df3, df4 = pd.DataFrame(), pd.DataFrame(), pd.DataFrame(), pd.DataFrame()
        # path = glob.glob(f".\\data\\raw\\{TODAY}\\*.csv")
        path = glob.glob(".\\data\\raw\\2024-09-14\\*.csv")
        for file_path in path:
            tmp = pd.read_csv(file_path)
            if "_1." in file_path: df1 = df1._append(tmp, ignore_index=True)

            elif "_2." in file_path: df2 = df2._append(tmp, ignore_index=True)

            elif "_3." in file_path: df3 = df3._append(tmp, ignore_index=True)

            elif "_4." in file_path: df4 = df4._append(tmp, ignore_index=True)
        csv_info = f"""CSV Info:
        ---\ndataframe 1:\n{df1.dtypes}\n---
        ---\ndataframe 2:\n{df2.dtypes}\n---
        ---\ndataframe 3:\n{df3.dtypes}\n---
        ---\ndataframe 4:\n{df4.dtypes}\n---
        """
        print(csv_info)
        return df1, df2, df3, df4

    def trans_price_history(self, df):
        df['date'] = pd.to_datetime(df['date'], format='%d/%m/%Y')
        df['adjusting_price'] = df['adjusting_price'].replace('--', 'N/A')
        rate = lambda x: float(re.search(r'\(([-+]?\d*\.?\d+)\s*%', x).group(1)) if pd.notnull(x) else float(x)
        df['rate_change'] = df['rate_change'].apply(rate)
        df['order_matching_volume'] = obj_to_int(df["order_matching_volume"].tolist())
        df['block_trade_volume'] = obj_to_int(df["block_trade_volume"].tolist())
        df['block_trade_value'] = obj_to_float(df["block_trade_value"].tolist())
        df['order_matching_value'] = obj_to_float(df['order_matching_value'].tolist())
        # df.to_csv(f"./data/transformed/{TODAY}/transformed_trans_price_history.csv", index=False)
        df.to_csv(f"{self.save_folder}\\price_history.csv", index=False)
        print(df.dtypes)


    def trans_order_flow_stat(self, df):
        df['date'] = pd.to_datetime(df['date'], format='%d/%m/%Y')
        
        df['buy_orders'] = obj_to_int(df["buy_orders"].tolist())
        df['buy_volume'] = obj_to_int(df["buy_volume"].tolist())
        df['average_sell_order_volume'] = obj_to_int(df["average_sell_order_volume"].tolist())
        df['sell_orders'] = obj_to_int(df["sell_orders"].tolist())
        df['sell_volume'] = obj_to_int(df["sell_volume"].tolist())
        df['net_volume'] = obj_to_int(df["net_volume"].tolist())

        df['average_buy_order_volume'] = obj_to_float(df['average_buy_order_volume'])
        df.drop(columns=['rate_change'], inplace=True)
        # df.to_csv(f"./data/transformed/{TODAY}/transformed_trans_order_flow_stat.csv",  index=False)
        df.to_csv(f"{self.save_folder}\\order_flow_stat.csv", index=False)
        print(df.dtypes)

    def trans_foreign_investors(self, df):
        df['date'] = pd.to_datetime(df['date'], format='%d/%m/%Y')

        df['net_trading_volume'] = obj_to_int(df['net_trading_volume'].tolist())
        df['buy_volume'] = obj_to_int(df['buy_volume'].tolist())
        df['sell_volume'] = obj_to_int(df['sell_volume'].tolist())
        df['remaining_room'] = obj_to_int(df['remaining_room'].tolist())
        owership = lambda x: x.replace("%","")
        df['current_ownership'] = df['current_ownership'].apply(owership)
        df['current_ownership'] = obj_to_float(df['current_ownership'].tolist())
        df.drop(columns=['rate_change'], inplace=True)
        # df.to_csv(f"./data/transformed/{TODAY}/transformed_trans_foreign_investors.csv",  index=False)
        df.to_csv(f"{self.save_folder}\\foreign_investors.csv", index=False)
        print(df.dtypes)

    def trans_proprietary_trading(self, df):
        df['date'] = pd.to_datetime(df['date'], format='%d/%m/%Y')
        df['buy_volume'] = obj_to_int(df['buy_volume'].tolist())
        df['sell_volume'] = obj_to_int(df['sell_volume'].tolist())
        df["net_trading_volume"] = obj_to_int(df["net_trading_volume"].tolist())
        # df.to_csv(f"./data/transformed/{TODAY}/transformed_trans_proprietary_trading.csv",  index=False)
        df.to_csv(f"{self.save_folder}\\proprietary_trading.csv", index=False)
        print(df.dtypes)

    def run(self):

        df1, df2, df3, df4 = self.combine_csv()
        self.trans_price_history(df1)
        self.trans_order_flow_stat(df2)
        self.trans_foreign_investors(df3)
        self.trans_proprietary_trading(df4)
