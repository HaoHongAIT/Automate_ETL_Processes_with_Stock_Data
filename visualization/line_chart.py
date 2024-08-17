import time
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from plotly.subplots import make_subplots
import plotly.graph_objects as go
plt.style.use("fivethirtyeight")


def line_chart(col, ticker_list):
    plt.figure(figsize=(15, 10))
    plt.subplots_adjust(top=1.25, bottom=1.2)
    for i in range(len(ticker_list)):
        ticker = ticker_list[i]
        plt.subplot(2, 2, i + 1)
        df[df['Ticker'] == ticker][col].plot()
        plt.ylabel(col)
        plt.xlabel(None)
        plt.title(f"{col} Price of {ticker}")
    plt.tight_layout()


def prediction_plot(ticker_df, y_col, test_size=0.15, valid_size=0.15):
    test_split_idx = int(len(ticker_df) * (1 - test_size))
    predicted_prices = ticker_df.iloc[test_split_idx + 1:].copy()
    predicted_prices[y_col] = y_pred
    fig = make_subplots(rows=2, cols=1)
    fig.add_trace(go.Scatter(x=ticker_df.index, y=ticker_df[y_col],
                             name='Truth', marker_color='LightSkyBlue'),
                  row=1, col=1)

    fig.add_trace(go.Scatter(x=predicted_prices.index,
                             y=predicted_prices[y_col],
                             name='Prediction', marker_color='MediumPurple'),
                  row=1, col=1)
    fig.add_trace(go.Scatter(x=predicted_prices.index,
                             y=y_test, name='Truth',
                             marker_color='LightSkyBlue', showlegend=False),
                  row=2, col=1)
    fig.add_trace(go.Scatter(x=predicted_prices.index,
                             y=y_pred, name='Prediction',
                             marker_color='MediumPurple',
                             showlegend=False),
                  row=2, col=1)
    fig.show()


def plot_dataset(train, val, test, col):
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=train.index, y=train[col], name='Training'))
    fig.add_trace(go.Scatter(x=val.index, y=val[col], name='Validation'))
    fig.add_trace(go.Scatter(x=test.index, y=test[col], name='Test'))
    fig.show()


if __name__ == '__main__':
    pass
    # line_chart('Fluctuation',ticker_names)
    line_chart('Close', ticker_names)