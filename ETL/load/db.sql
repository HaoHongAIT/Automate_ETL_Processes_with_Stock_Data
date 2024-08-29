-- Ticker
CREATE TABLE stock_ticker (
    ticker TEXT PRIMARY KEY,
    name TEXT,
    platform TEXT
);

-- transformed_fpt_1.csv
CREATE TABLE prices_history (
    date DATE NOT NULL,
    close REAL NOT NULL,
    adjusting_price REAL NULL,
    rate_change REAL NOT NULL,
    order_matching_volume INTEGER NOT NULL,
    order_matching_value REAL NOT NULL,
    put_through_volume INTEGER NOT NULL,
    put_through_value REAL NOT NULL,
    open_value REAL NOT NULL,
    highest_value REAL NOT NULL,
    lowest_value REAL NOT NULL,
    ticker TEXT NOT NULL,
    FOREIGN KEY(ticker) REFERENCES stock_ticker(ticker),
    PRIMARY KEY (date, ticker)
);
-- transformed_fpt_2.csv
-- buy_orders,buy_volume,average_buy_order_volume,sell_orders,sell_volume,
-- average_sell_order_volume,net_volume,ticker
CREATE TABLE order_flow_stat(
    date DATE NOT NULL ,
    buy_orders INTEGER NOT NULL,
    buy_volume INTEGER NOT NULL,
    average_buy_order_volume REAL NOT NULL,
    sell_orders INTEGER NOT NULL,
    sell_volume INTEGER NOT NULL,
    average_sell_order_volume REAL NOT NULL,
    net_volume INTEGER NOT NULL,
    ticker TEXT NOT NULL,
    FOREIGN KEY (ticker) REFERENCES stock_ticker(ticker),
    PRIMARY KEY (date, ticker)
);
-- transformed_fpt_3.csv
CREATE TABLE foreign_investors (
    date DATE NOT NULL ,
    net_trading_volume INTEGER NOT NULL,
    net_trading_value_billion_vnd REAL NOT NULL,
    buy_volume INTEGER NOT NULL,
    buy_value_billion_vnd REAL NOT NULL,
    sell_volume INTEGER NOT NULL,
    sell_value_billion_vnd REAL NOT NULL,
    remaining_room INTEGER NOT NULL,
    current_ownership REAL NOT NULL,
    ticker TEXT NOT NULL,
    FOREIGN KEY(ticker) REFERENCES stock_ticker(ticker),
    PRIMARY KEY (date, ticker)
);


-- transformed_fpt_4.csv
CREATE TABLE proprietary_trading (
    ticker TEXT NOT NULL,
    date DATE NOT NULL,
    buy_volume INTEGER NOT NULL,
    buy_value_bil_vnd REAL NOT NULL,
    sell_volume INTEGER NOT NULL,
    sell_value_bil_vnd REAL NOT NULL,
    net_trading_volume INTEGER NOT NULL,
    net_value_bil_vnd REAL NOT NULL,
    FOREIGN KEY(ticker) REFERENCES stock_ticker(ticker),
    PRIMARY KEY (date, ticker)
);
