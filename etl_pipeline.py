from ETL.extract.multi_threading import MultiThreading
from ETL.transform import transform
from ETL.load import load
import pandas as pd
from datetime import date


stock_codes = pd.read_excel(r'./data/document/code_stock.xlsx')['ticker'].to_list()[:10]
today = date.today().strftime(r"%d/%m/%Y")
time_range = f'01/01/2024 - {today}'


crawler = MultiThreading(threads=10, code_list=stock_codes)
crawler.run(time_range=time_range)
transform.run(ticker=ticker)
# # ETL
# for ticker in tickers:
#     extract = MultiThreading(tickers=tickers)
#     ## EXTRACT > Raw Data
#     raw_data = ticker_crawler.run(time_range=time_range)
#     ## TRASFORM > Transformed Data
#     transform.run(ticker=ticker)
#     ## Load > Available Data for Analysis
#     load.run(ticker=ticker)
