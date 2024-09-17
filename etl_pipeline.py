from ETL.extract.multi_threading import MultiThreading
from ETL.transform import *
from ETL.load import load
from ETL import *
import pandas as pd
from ETL.transform.transform import Transform

# stock_codes = pd.read_excel(r'./data/document/code_stock.xlsx')['ticker'].to_list()[0:200]
# time_range = f'01/01/2024 - {TODAY}'
# crawler = MultiThreading(threads=10, code_list=stock_codes)
# crawler.run(time_range=time_range)

# TRASFORM > Transformed Data
transform1 = Transform()
transform1.run()

#     ## Load > Available Data for Analysis
#     load.run(ticker=ticker)


# import glob
# import re
# path = glob.glob(f".\\data\\raw\\2024-09-14\\*.csv")
# for file_path in path:
#     df = pd.read_csv(file_path)
#     df['ticker'] = str(re.search(r'\\[\d\-]+\\([a-zA-Z0-9]+)_\d+\.csv$', file_path).group(1))
#     df.to_csv(file_path, index=False)



