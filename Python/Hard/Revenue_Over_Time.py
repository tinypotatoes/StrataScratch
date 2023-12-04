"""
Revenue Over Time 
https://platform.stratascratch.com/coding/10314-revenue-over-time?code_type=2

Difficulty: Hard

Find the 3-month rolling average of total revenue from purchases given a table with users, their purchase amount, and date purchased. Do not include returns which are represented by negative purchase values. Output the year-month (YYYY-MM) and 3-month rolling average of revenue, sorted from earliest month to latest month.

A 3-month rolling average is defined by calculating the average total revenue from all user purchases for the current month and previous two months. The first two months will not be a true 3-month rolling average since we are not given data from last year. Assume each month has at least one purchase.

Tables:
(amazon_purchases)
user_id         int
created_at      datetime
purchase_amt    int
"""

# Import your libraries
import pandas as pd

# Start writing code
amazon_purchases.head()

amazon_purchases["date"] = amazon_purchases["created_at"].dt.to_period("M")

amazon_purchases = amazon_purchases[amazon_purchases["purchase_amt"] > 0]
df = amazon_purchases.groupby("date")["purchase_amt"].sum().reset_index(name="month_total")
df.set_index("date", inplace=True)

rolling_avg = df.rolling(3, min_periods = 1).mean()
result = rolling_avg.to_records()
