# Web Scraping and Trade Market Analysis
## ✅ Todo list
- [x] [Web scraping](/web_scraping/README.md) (source: cafef.vn)
- [ ] Crawl multi-threading 
- [ ] Automatic crawling
- [ ] Analysis and Predict
- [ ] **Quantitative trading strategies**
- [ ] **Portfolio optimization and tracking**
- [ ] **Additional fundamental data**
- [ ] **User account system**

## 📈 About
By analyzing fundamental factors or quantitative factors to predict the rise and fall of stock prices, investors will make decisions to buy or sell stocks to seek profits. However, the stock market always has unexpected factors that do not align with users' subjective intentions, so predicting market trends is a crucial task that has been attracting the attention of investors, economists, and scientists.

In this project, please help stock investors build a model to predict the prices of some popular stocks in the current Vietnamese market.

## 🎯 Key Future
- **Real-time data** - Fetch latest prices and fundamentals 
- **Financial charts** - Interactive historical and forecast charts
- **ARIMA forecasting** - Make statistically robust predictions
- **Backtesting** - Evaluate model performance
- **Responsive design** - Works on all devices

## 🏗️ **How It's Built**

Stockastic is built with these core frameworks and modules:

- **Streamlit** - To create the web app UI and interactivity 
- **YFinance** - To fetch financial data from Yahoo Finance API
- **StatsModels** - To build the ARIMA time series forecasting model
- **Plotly** - To create interactive financial charts

The app workflow is:

1. User selects a stock ticker
2. Historical data is fetched with YFinance
3. AI model is trained on the data 
4. Model makes multi-day price forecasts
5. Results are plotted with Plotly

## 🚀 Getting Start
1. Clone the repo
```bash
git clone https://github.com/HaoHongAIT/Web_Scraping_and_Trade_Market_Analysis.git
```
2. Install requirements
```bash
pip install -r requirements.txt
```
3. Run the app
```bash
streamlit run Main.py
```
The app will be live at ```http://localhost:8501```



## ⚖️ Disclaimer
**This is not financial advice! Use forecast data to inform your own investment research. No guarantee of trading performance.**