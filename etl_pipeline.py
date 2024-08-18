from ETL.extract import WebScraping
from ETL.transform import transform

tickers, categories = ['fpt'], [1, 2, 3, 4]
timestamp = '01/07/2024 - 17/08/2024'

# ETL
for ticker in tickers:
    for c in categories:            
        url = f"https://s.cafef.vn/lich-su-giao-dich-{ticker}-{c}.chn"
        ticker_crawler = WebScraping.Crawl(ticker=ticker, url=url, index=c)    
        ## EXTRACT > Raw Data
        raw_data = ticker_crawler.get_ticker(time=timestamp)        
        ticker_crawler.save(lst=raw_data, ticker=ticker)   
        ## TRASFORM > Transformed Data
        dataframe = transform.ticker(ticker=ticker)
        print(dataframe)
        
        break

## Load > Available Data
        

