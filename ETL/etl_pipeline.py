from ETL.extract import web_scraping
from ETL.transform import transform
from ETL.load import load

tickers = ['fpt']
time_range = '01/07/2024 - 17/08/2024'

# ETL
for ticker in tickers:                  
    ticker_crawler = web_scraping.Crawl(tickers=tickers)    
    ## EXTRACT > Raw Data
    raw_data = ticker_crawler.run(time_range=time_range)
    ## TRASFORM > Transformed Data
    transform.run(ticker=ticker)
    ## Load > Available Data for Analysis
    load.run(ticker=ticker)


        

