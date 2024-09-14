import pandas as pd
import re
from datetime import date
import glob

TODAY = date.today().strftime(r"%Y-%m-%d")

class Transform:
    def __init__(self):
        pass

    def combine_csv(self):
        df1, df2, df3, df4 = pd.DataFrame(), pd.DataFrame(), pd.DataFrame(), pd.DataFrame()
        path = glob.glob(f".\\data\\raw\\{TODAY}\\*.csv")
        for file_path in path:
            tmp = pd.read_csv(file_path)
            if "_1." in file_path:
                df1._append(tmp, ignore_index=True)
                break
            if "_2." in file_path:
                df2._append(tmp, ignore_index=True)
                break
            if "_3." in file_path:
                df3._append(tmp, ignore_index=True)
                break
            if "_4." in file_path:
                df4._append(tmp, ignore_index=True)
                break

        return df1, df2, df3, df4


    def trans_price_history(self, df,index=1):
        df['date'] = pd.to_datetime(df['date'], format='%d/%m/%Y')
        df['adjusting_price'] = df['adjusting_price'].replace('--', 'N/A')
        rate = lambda x: re.search(r'\(([-+]?\d*\.?\d+)\s*%', x).group(1) if pd.notnull(x) else x
        df['rate_change'] = df['rate_change'].apply(rate)
        df['order_matching_volume'] = [int(value.replace(',', '')) for value in df['order_matching_volume']]
        df['order_matching_value'] = [float(value.replace(',', '')) for value in df['order_matching_value']]
        df['block_trade_volume'] = [int(value.replace(',', '')) for value in df['block_trade_volume']]
        df.to_csv(f"./data/transformed/{TODAY}/transformed_trans_price_history.csv", index=False)


    def trans_order_flow_stat(self, df, index=2):
        df['date'] = pd.to_datetime(df['date'], format='%d/%m/%Y')
        df['buy_orders'] = [int(value.replace(',', '')) for value in df['buy_orders']]
        df['buy_volume'] = [int(value.replace(',', '')) for value in df['buy_volume']]
        df['average_buy_order_volume'] = [float(value.replace(',', '')) for value in df['average_buy_order_volume']]
        df['sell_orders'] = [int(value.replace(',', '')) for value in df['sell_orders']]
        df['sell_volume'] = [int(value.replace(',', '')) for value in df['sell_volume']]
        df['average_sell_order_volume'] = [int(value.replace(',', '')) for value in df['average_sell_order_volume']]
        df['net_volume'] = [int(value.replace(',', '')) for value in df['net_volume']]
        df.drop(columns=['rate_change'], inplace= True)
        print("Transform Complete Order Flow Statistics")
        df.to_csv(f"./data/transformed/{TODAY}/transformed_trans_order_flow_stat.csv",  index=False)

    def trans_foreign_investors(self, df, index=3):
        df['date'] = pd.to_datetime(df['date'], format='%d/%m/%Y')
        df['net_trading_volume'] = [int(value.replace(',', '')) for value in df['net_trading_volume']]
        df['buy_volume'] = [int(value.replace(',', '')) for value in df['buy_volume']]
        df['sell_volume'] = [int(value.replace(',', '')) for value in df['sell_volume']]
        df['remaining_room'] = [int(value.replace(',', '')) for value in df['remaining_room']]
        df['current_ownership'] = [float(value.replace('%', '')) for value in df['current_ownership']]
        df.drop(columns=['rate_change'], inplace= True)
        print("Transform Complete Foreign Investors")
        df.to_csv(f"./data/transformed/{TODAY}/transformed_trans_foreign_investors.csv",  index=False)

    def trans_proprietary_trading(self, df, index=4):
        df['date'] = pd.to_datetime(df['date'], format='%d/%m/%Y')
        df['buy_volume'] = [int(value.replace(',', '')) for value in df['buy_volume']]
        df['sell_volume'] = [int(value.replace(',', '')) for value in df['sell_volume']]
        df["net_trading_volume"] = [int(value.replace(',', '')) for value in df["net_trading_volume"]]
        df['ticker'] = ticker.lower()
        print("Transform Complete Proprietary Trading")
        df.to_csv(f"./data/transformed/{TODAY}/transformed_trans_proprietary_trading.csv",  index=False)

    def run(self):
        df1, df2, df3, df4 = self.combine_csv()
        trans_price_history(df1)
        trans_foreign_investors(df2)
        trans_order_flow_stat(df3)
        trans_proprietary_trading(df4)