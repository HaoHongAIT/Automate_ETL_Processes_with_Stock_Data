## About

## How the market work?
Nhu cầu trong kinh tế học được hiểu là nhu cầu tiêu dùng (sở thích tiêu dùng). Trong kinh tế học, nhu cầu nếu không có khả năng tài chính để đáp ứng cho sở thích 
tiêu dùng thì không thể gọi là nhu cầu. 
- => Thị trường (hàng hóa, sản phẩm,...) luôn vận động theo nhu cầu => các nhà
phân phối luôn tìm cách tạo ra những sản phẩm có giá trị phù hợp với sở thích của 
người dùng => người dùng cần mua những sản phẩm đang cần, thích thì đến 
nơi phân phối sản phẩm để thực hiện giao dịch => từ đây có một khái niệm gọi ,lli2mà mua bán.



# 📈 **Stockastic**
### **Predicting Stocks with ML**

**Stockastic is an ML-powered stock price prediction app built with Python and Streamlit. It utilizes machine learning models to forecast stock prices and help investors make data-driven decisions.**

## 🏗️ **How It's Built**

Stockastic is built with these core frameworks and modules:

- **Streamlit** - To create the web app UI and interactivity 
- **YFinance** - To fetch financial data from Yahoo Finance API
- **StatsModels** - To build the ARIMA time series forecasting model
- **Plotly** - To create interactive financial charts

The app workflow is:

1. User selects a stock ticker
2. Historical data is fetched with YFinance
3. ARIMA model is trained on the data 
4. Model makes multi-day price forecasts
5. Results are plotted with Plotly

## 🎯 **Key Features**

- **Real-time data** - Fetch latest prices and fundamentals 
- **Financial charts** - Interactive historical and forecast charts
- **ARIMA forecasting** - Make statistically robust predictions
- **Backtesting** - Evaluate model performance
- **Responsive design** - Works on all devices

## 🚀 **Getting Started**

### **Local Installation**

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

## 📈 **Future Roadmap**

Some potential features for future releases:

- **More advanced forecasting models like LSTM**
- **Quantitative trading strategies**
- **Portfolio optimization and tracking**
- **Additional fundamental data**
- **User account system**

## **⚖️ Disclaimer**
**This is not financial advice! Use forecast data to inform your own investment research. No guarantee of trading performance.**