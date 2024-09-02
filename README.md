# Web Scraping and Trade Market Analysis

## ✅ Todo list
- [x] Extract stock data from cafef.vn (not include news)
- [x] Transform raw data to available datatype for analysis
- [x] Load transformed data to database
- [ ] Crawl multi-threading 
- [ ] Analysis and Forecast future trend, price of stock
- [ ] Story telling with a dashboard
- [ ] Automatic update

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

## 📁 Repository Structure
```
📦
├─ README.md                 # General project documentation
├─ constants.py              # Shared constants and configurations used across the project
├─ data                      # Containt all data
│  ├─ raw                  
│  ├─ transformed       
│  ├─ image
│  └─ document
├─ forecast                  # Code and configuration for distributed training
│  ├─ models
│  ├─ preprocessing
│  ├─ train.ipynb
│  │  ├─ 
│  │  ├─ 
│  │  └─ 
│  └─ weights                # Folder containing a pre-trained model
│     └─ model.h5            # Saved weights for the pre-trained model
├─ pages
├─ visualization
├─ mlflow                    # Code and configuration for the MLflow component
│  └─ Dockerfile             # Dockerfile for the MLflow component
├─ model_repo                # Repository for storing the trained model
│  └─ yolov8n_car            # Folder for the YOLOv8 car detection model
│     ├─ 1                   # Version 1 of the model
│     │  └─ model.onnx       # ONNX format of the trained model
│     └─ config.pbtxt        # Triton Inference Server configuration for the model
├─ notebooks                 # Folder for Jupyter Notebooks (likely for debugging/exploration)
│  └─ debug.ipynb            # Sample Jupyter Notebook for debugging
├─ requirements.txt          # Python dependencies for the project
└─ streaming                 # Code and configuration for the data streaming component
   ├─ Dockerfile             # Dockerfile for the streaming component
   └─ run.sh                 # Script to run the streaming component
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
3. Run the app
```bash
streamlit run Main.py
```
The app will be live at ```http://localhost:8501```



## ⚖️ Disclaimer
**This is not financial advice! Use forecast data to inform your own investment research. No guarantee of trading performance.**