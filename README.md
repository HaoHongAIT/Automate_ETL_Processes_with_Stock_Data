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
├─ distributed_training      # Code and configuration for distributed training
│  ├─ Dockerfile             # Dockerfile for the distributed training component
│  ├─ README_distributed.md  # Documentation for the distributed training component
│  ├─ build.sh               # Script to build the distributed training Docker image
│  ├─ mwt.py                 # Main logic for the Multi-Worker Training component
│  ├─ nets                   # Neural network architecture definitions
│  │  └─ nn.py               # Neural network model implementation
│  ├─ test                   # Test configuration for the distributed training
│  │  └─ test.yaml           # Test deployment configuration
│  ├─ utils                  # Utility functions for the distributed training
│  │  ├─ config.py           # Configuration handling for the distributed training
│  │  ├─ dataset.py          # Dataset-related utilities
│  │  └─ image_utils.py      # Image processing utilities
│  └─ weights                # Folder containing a pre-trained model
│     └─ model.h5            # Saved weights for the pre-trained model
├─ docker-compose.yml        # Docker Compose configuration for the entire project
├─ images                    # Folder for storing project-related images
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
   ├─ README_streaming.md    # Documentation for the streaming component
   ├─ docker-compose.yml     # Docker Compose configuration for the streaming component
   ├─ kafka_connector        # Configuration for the Kafka connector
   │  └─ connect-timescaledb-sink.json # Kafka connector configuration for TimescaleDB sink
   ├─ produce.py             # Script to produce sample data for the streaming component
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