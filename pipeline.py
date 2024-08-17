from web_scraping import WebScraping
from preprocessing import preprocess

if __name__ == '__main__':
    # WEB SCRAPING
    ticker, index = 'fpt', [1]
    url = f"https://s.cafef.vn/lich-su-giao-dich-{ticker}-{index}.chn"
    fpt_crawler = WebScraping.Crawl(ticker, url, index)

    ## get data
    fpt_data = fpt_crawler.get_Data(time='01/07/2024 - 17/08/2024')
    ## save
    fpt_crawler.save(lst=fpt_data, filename="fpt") #raw csv

    # PREPROCESS
    ##
    dataframe = preprocess.preprocess(ticker = 'fpt') #preprocess csv
    print(dataframe)
    ## save
    # FORECAST

    # FORECAST orecast

    # implement

    # automatation


