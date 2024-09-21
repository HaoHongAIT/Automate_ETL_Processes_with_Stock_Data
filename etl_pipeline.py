from ETL.extract.multi_threading import MultiThreading
from ETL.transform import *
from ETL.load.load import Load
from ETL import *
import pandas as pd
from ETL.transform.transform import Transform
from datetime import date

TIME ="2024-09-14"
# TIME = date.today().strftime(r"%Y-%m-%d")
# time_range = f'01/01/2024 - {TIME}'
# stock_codes = pd.read_excel(r'./data/document/code_stock.xlsx')['ticker'].to_list()[0:200]

# stock_codes = pd.read_csv(r'./data/transformed/2024-09-14/prices_history.csv')
import csv

# INGESTION
# crawler = MultiThreading(threads=10, code_list=stock_codes)
# crawler.run(time_range=time_range)

# # TRANSFORM > Transformed Data
transform_pipeline = Transform(time=TIME)
transform_pipeline.run()
#
# Load > Available Data for Analysis
load2db = Load()
load2db.run(init=False)



# import glob
# import re
# path = glob.glob(f".\\data\\raw\\2024-09-14\\*.csv")
# for file_path in path:
#     df = pd.read_csv(file_path)
#     df['ticker'] = str(re.search(r'\\[\d\-]+\\([a-zA-Z0-9]+)_\d+\.csv$', file_path).group(1))
#     df.to_csv(file_path, index=False)

# df = pd.read_csv('./data/transformed/2024-09-14/prices_history.csv')
# print(df.max())

