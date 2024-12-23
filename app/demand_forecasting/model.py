import pandas as pd
from statsmodels.tsa.arima.model import ARIMA

def forecast_sales(data_path, steps=30):
    data = pd.read_csv(data_path, parse_dates=['date'], index_col='date')
    model = ARIMA(data['sales'], order=(5, 1, 0))  
    model_fit = model.fit()
    forecast = model_fit.forecast(steps=steps)
    return forecast
