# Web Scraping and Trade Market Analysis

## 📈 About
By analyzing fundamental factors or quantitative factors to predict the rise and fall of stock prices, investors will make decisions to buy or sell stocks to seek profits. However, the stock market always has unexpected factors that do not align with users' subjective intentions, so predicting market trends is a crucial task that has been attracting the attention of investors, economists, and scientists.

In this project, please help stock investors build a model to predict the prices of some popular stocks in the current Vietnamese market.

## 🎯 Key Future
- [x] Extract stock data from cafef.vn (not include news)
- [x] Transform raw data to available datatype for analysis
- [x] Load transformed data to database
- [x] Crawl multi-threading 
- [ ] Analysis and Forecast future trend, price of stock
- [ ] Story telling with a dashboard
- [ ] Automatic update

## 📁 Repository Structure
```
📦
├─ README.md                 # General project documentation
├─ data                      # Containt all data in this project
│  ├─ raw                    # CSV files
│  ├─ transformed       
│  ├─ image
│  └─ document
├─ ETL                       # ETL process
│  ├─ extract                # 
│  ├─ transform              #
│     ├─ transform.py        #
│  ├─ load                 
│  └─ airflow                # 
├─ visualization             # Power BI
├─ chromedriver.exe          # Chrome Driver 
├─ stock_market.db           #
├─ etl_pipeline.py           #
└─ requirements.txt          # library
```

## 🚀 Getting Start
1. Clone the repo
```bash
git clone https://github.com/HaoHongAIT/Web_Scraping_and_Trade_Market_Analysis.git
```
2. Install requirements
```bash
pip install -r requirements.txt
```

## ⚖️ Disclaimer
**This is not financial advice! Use forecast data to inform your own investment research. No guarantee of trading performance.**