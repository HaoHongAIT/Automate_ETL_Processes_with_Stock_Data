from xgboost import XGBRegressor, plot_importance
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.metrics import mean_squared_error


%%time
parameters = {
    'n_estimators': [1_000_000],
    'max_depth': [3, 8, 10, 12],
    'gamma': [0.001, 0.005, 0.01, 0.02],
    'learning_rate': [0.1],
    'early_stopping_rounds': [20],
    'random_state': [42]
}
eval_set = [(X_train, y_train), (X_valid, y_valid)]
xgboost = XGBRegressor(eval_set=eval_set, objective='reg:squarederror',
                       eval_metric=mean_squared_error, verbose=False)
clf = GridSearchCV(xgboost, parameters)
clf.fit(X_train, y_train,eval_set=eval_set)
print(f'Best params: {clf.best_params_}')
print(f'Best validation score = {clf.best_score_}')

%%time
model = XGBRegressor(**clf.best_params_, objective='reg:squarederror')
model.fit(X_train, y_train, eval_set=eval_set, verbose=False)

plot_importance(model,max_num_features=15)
y_pred = model.predict(X_test)
print(f'y_true = {np.array(y_test)[:5]}')
print(f'y_pred = {y_pred[:5]}')
print(f'mean_squared_error = {mean_squared_error(y_test, y_pred)}')
# prediction_plot(FPT_ticker, y_col='Fluctuation')
prediction_plot(FPT_ticker, y_col='Close')