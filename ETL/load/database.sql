CREATE TABLE stock_ticker (
    ticker TEXT UNIQUE PRIMARY KEY,
    name TEXT NOT NULL,
    platform TEXT
);

CREATE TABLE prices_history (
    date DATE NOT NULL,
    close REAL NOT NULL,
    adjusting_price REAL NULL,
    rate_change REAL NOT NULL,
    order_matching_volume INTEGER NOT NULL,
    order_matching_value REAL NOT NULL,
    block_trade_volume INTEGER NOT NULL,
    block_trade_value REAL NOT NULL,
    open REAL NOT NULL,
    high REAL NOT NULL,
    low REAL NOT NULL,
    ticker TEXT NOT NULL,
    FOREIGN KEY(ticker) REFERENCES stock_ticker(ticker),
    PRIMARY KEY (date, ticker)
);

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

CREATE TABLE proprietary_trading (
    ticker TEXT NOT NULL,
    date DATE NOT NULL,
    buy_volume INTEGER NOT NULL,
    buy_value_bil_vnd REAL NOT NULL,
    sell_volume INTEGER NOT NULL,
    sell_value_bil_vnd REAL NOT NULL,
    net_trading_volume INTEGER NOT NULL,
    net_trading_value_bil_vnd REAL NOT NULL,
    FOREIGN KEY(ticker) REFERENCES stock_ticker(ticker),
    PRIMARY KEY (date, ticker)
);