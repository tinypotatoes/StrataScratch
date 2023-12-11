"""
Naive Forecasting
https://platform.stratascratch.com/coding/10313-naive-forecasting?code_type=2

Difficulty: Hard

Some forecasting methods are extremely simple and surprisingly effective. Naïve forecast is one of them; we simply set all forecasts to be the value of the last observation. Our goal is to develop a naïve forecast for a new metric called "distance per dollar" defined as the (distance_to_travel/monetary_cost) in our dataset and measure its accuracy.

To develop this forecast,  sum "distance to travel"  and "monetary cost" values at a monthly level before calculating "distance per dollar". This value becomes your actual value for the current month. The next step is to populate the forecasted value for each month. This can be achieved simply by getting the previous month's value in a separate column. Now, we have actual and forecasted values. This is your naïve forecast. Let’s evaluate our model by calculating an error matrix called root mean squared error (RMSE). RMSE is defined as sqrt(mean(square(actual - forecast)). Report out the RMSE rounded to the 2nd decimal spot.

Tables:
(uber_request_logs)
request_id                     int
request_date                   datetime
request_status                 varchar
distance_to_travel             float
monetary_cost                  float
driver_to_client_distance      float
"""
# Import your libraries
import pandas as pd
import numpy as np

# Start writing code
uber_request_logs["request_date"] = uber_request_logs["request_date"].dt.to_period("M")
df = uber_request_logs.groupby("request_date")["distance_to_travel", "monetary_cost"].sum().reset_index()

df["distance_per_dollar"] = df["distance_to_travel"] / df["monetary_cost"]
df["forecast"] = df["distance_per_dollar"].shift(1)

# RMSE is sqrt(mean(square(actual - forecast))) then we want to round to 2 decimal places
RMSE = round(np.sqrt(np.mean(np.square(df["distance_per_dollar"] - df["forecast"]))), 2)
