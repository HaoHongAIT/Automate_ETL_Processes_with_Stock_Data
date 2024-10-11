# Web Scraping and Trade Market Analysis

## 📈 About
By analyzing fundamental factors or quantitative factors to predict the rise and fall of stock prices, investors will make decisions to buy or sell stocks to seek profits. However, the stock market always has unexpected factors that do not align with users' subjective intentions, so predicting market trends is a crucial task that has been attracting the attention of investors, economists, and scientists.

## 🎯 Key Future
- [x] Extract stock data from cafef.vn (not include news)
- [x] Transform raw data to available datatype for analysis
- [x] Load transformed data to the database
- [x] Crawl multi-threading 
- [ ] Storytelling with a dashboard
- [ ] Automatic update

## 📁 Repository Structure
```
📦
├─ README.md                 # General project documentation
├─ ETL                       # ETL process
│  ├─ extract                # Extract phase
│  ├─ transform              # Transform phase
│  ├─ load                   # Load pipeline
│  └─ data                   # Containt all data in this project
├─ dags                      # airflow
├─ visualization             # Power BI
├─ chromedriver.exe          # Chrome Driver for crawling
├─ stock_market.db           # SQLite database
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
**This is not financial advice! Use forecast data to inform your investment research. There is no guarantee of trading performance.**
