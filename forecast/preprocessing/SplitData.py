import pandas as pd


def train_test_split(df, test_size=0.15, valid_size=0.15):
    test_split_idx = int(len(df) * (1 - test_size))
    valid_split_idx = int(len(df) * (1 - (valid_size + test_size)))
    train_df = df.iloc[:valid_split_idx].copy()
    valid_df = df.iloc[valid_split_idx + 1:test_split_idx].copy()
    test_df = df.iloc[test_split_idx + 1:].copy()
    return train_df, valid_df, test_df


def drop(df, cols=None, frows=None):
    if cols:
        df = df.drop(cols, axis=1)
    elif frows:
        df = df.tail(-frows)
    return df


def xy_split(train, valid, test, y_col):
    y_train = train[y_col].copy()
    X_train = train.drop([y_col], axis=1)

    y_valid = valid[y_col].copy()
    X_valid = valid.drop([y_col], axis=1)

    y_test = test[y_col].copy()
    X_test = test.drop([y_col], axis=1)
    return y_train, X_train, y_valid, X_valid, y_test, X_test
