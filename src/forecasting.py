# Import some libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from prophet import Prophet
from statsmodels.tsa.arima.model import ARIMA
from sklearn.metrics import mean_absolute_error, mean_squared_error
import numpy as np

# Load dataset and establish time-series structure
def load_data(path="../data/cleaned/sales_clean.csv"):
    sales = pd.read_csv(path)
    sales["Order Date"] = pd.to_datetime(sales["Order Date"])
    monthly_sales = sales.groupby(pd.Grouper(key="Order Date", freq="ME"))["Sales"].sum().reset_index()
    return monthly_sales

# 
def visualize_trend(monthly_sales):
    plt.figure(figsize=(12,6))
    sns.lineplot(data=monthly_sales, x="Order Date", y="Sales")
    plt.title("Monthly Sales Trend")
    plt.xlabel("Month")
    plt.ylabel("Total Sales")
    plt.tight_layout()
    plt.show()

#
def prophet_forecast(monthly_sales, periods=12):
    prophet_df = monthly_sales.rename(columns={"Order Date":"ds","Sales":"y"})
    model = Prophet()
    model.fit(prophet_df)
    future = model.make_future_dataframe(periods=periods, freq="ME")
    forecast = model.predict(future)
    model.plot(forecast)
    plt.title("Prophet Forecast")
    plt.show()
    model.plot_components(forecast)
    plt.show()
    return forecast

# 
def arima_forecast(monthly_sales):
    train_size = int(len(monthly_sales) * 0.8)
    train, test = monthly_sales["Sales"][:train_size], monthly_sales["Sales"][train_size:]
    model = ARIMA(train, order=(1,1,1))
    fit = model.fit()
    forecast = fit.forecast(steps=len(test))
    plt.figure(figsize=(12,6))
    plt.plot(monthly_sales["Order Date"][train_size:], test, label="Actual")
    plt.plot(monthly_sales["Order Date"][train_size:], forecast, label="ARIMA Forecast")
    plt.legend()
    plt.title("ARIMA Forecast vs Actual")
    plt.show()
    return test, forecast

#
def compare_accuracy(prophet_df, forecast_prophet, test, forecast_arima):
    mae_prophet = mean_absolute_error(prophet_df["y"].iloc[-12:], forecast_prophet["yhat"].iloc[-12:])
    rmse_prophet = np.sqrt(mean_squared_error(prophet_df["y"].iloc[-12:], forecast_prophet["yhat"].iloc[-12:]))
    mae_arima = mean_absolute_error(test, forecast_arima)
    rmse_arima = np.sqrt(mean_squared_error(test, forecast_arima))
    print("Prophet MAE:", mae_prophet, "RMSE:", rmse_prophet)
    print("ARIMA MAE:", mae_arima, "RMSE:", rmse_arima)

#
if __name__ == "__main__":
    monthly_sales = load_data()
    visualize_trend(monthly_sales)
    forecast_prophet = prophet_forecast(monthly_sales)
    test, forecast_arima = arima_forecast(monthly_sales)
    prophet_df = monthly_sales.rename(columns={"Order Date":"ds","Sales":"y"})
    compare_accuracy(prophet_df, forecast_prophet, test, forecast_arima)