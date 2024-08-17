from web_scraping import WebScraping
from preprocessing import preprocess

if __name__ == '__main__':
    # WEB SCRAPING
    ticker, index = 'fpt', [1]
    url = f"https://s.cafef.vn/lich-su-giao-dich-{ticker}-{index}.chn"
    fpt_crawler = WebScraping.Crawl(ticker, url, index)

    ## get data
    fpt_data = fpt_crawler.get_Data(time=None)
    ## save
    fpt_crawler.save(lst=fpt_data, filename="fpt")

    # PREPROCESS
    ##

    ## save
    # FORECAST

    # FORECAST orecast

    # implement

    # automatation

    lst = get_Data(browser=browser, ticker='fpt', index=1)
    list_to_csv(lst=lst, dic=dic, ticker='fpt')
    list_to_csv = preprocess.preprocess()
