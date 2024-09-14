from ETL.extract.multi_threading import MultiThreading
from ETL.transform import transform
from ETL.load import load
from ETL import *
import pandas as pd


stock_codes = pd.read_excel(r'./data/document/code_stock.xlsx')['ticker'].to_list()[41:200]
time_range = f'01/01/2024 - {TODAY}'
crawler = MultiThreading(threads=10, code_list=stock_codes)
crawler.run(time_range=time_range)

# transform.run(ticker=ticker)
# # ETL
#     extract = MultiThreading(tickers=tickers)
#     ## EXTRACT > Raw Data
#     raw_data = ticker_crawler.run(time_range=time_range)
#     csv > glob >
#     ## TRASFORM > Transformed Data
#     transform.run(ticker=ticker)
#     ## Load > Available Data for Analysis
#     load.run(ticker=ticker)
