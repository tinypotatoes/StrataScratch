"""
Monthly Percent Difference
https://platform.stratascratch.com/coding/10319-monthly-percentage-difference?code_type=2

Difficulty: Hard

Given a table of purchases by date, calculate the month-over-month percentage change in revenue. The output should include the year-month date (YYYY-MM) and percentage change, rounded to the 2nd decimal point, and sorted from the beginning of the year to the end of the year.

The percentage change column will be populated from the 2nd month forward and can be calculated as ((this month's revenue - last month's revenue) / last month's revenue)*100.

Tables:
(sf_transactions)
id               int
created_at       datetime
value            int
purchase_id      int
"""

# Import your libraries
import pandas as pd
pd.options.display.float_format = "{:,.2f}".format

sf_transactions["date"] = sf_transactions["created_at"].dt.to_period("M")

df = sf_transactions.groupby("date")["value"].sum().reset_index(name="month_total")
df["last_month"] = df["month_total"].shift(1)
df["percent_change"] = ((df["month_total"] - df ["last_month"]) / df ["last_month"]) * 100

result = df[["date", "percent_change"]]
