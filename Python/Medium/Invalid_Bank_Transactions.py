'''
Invalid Bank Transactions
https://platform.stratascratch.com/coding/2143-invalid-bank-transactions?code_type=2

Difficulty: Medium

Bank of Ireland has requested that you detect invalid transactions in December 2022. An invalid transaction is one that occurs outside of the bank's normal business hours. The following are the hours of operation for all branches:

Monday - Friday 09:00 - 16:00
Saturday & Sunday Closed
Irish Public Holidays 25th and 26th December

Determine the transaction ids of all invalid transactions.

Tables:
(boi_transactions)
transaction_id    int
time_stamp        datetime
'''

# Import your libraries
import pandas as pd

# Start writing code
boi_transactions["time_stamp"] = pd.to_datetime(boi_transactions["time_stamp"])
boi_transactions["day"] = boi_transactions["time_stamp"].dt.day
boi_transactions["hour"] = boi_transactions["time_stamp"].dt.hour
boi_transactions["week_day"] = boi_transactions["time_stamp"].dt.weekday

weekends = boi_transactions[boi_transactions["week_day"] >= 5]
out_hours = boi_transactions[~boi_transactions["hour"].between(9,15)]
holiday = boi_transactions[(boi_transactions["day"] == 25) | (boi_transactions["day"] == 26)]

pd.concat([weekends, out_hours, holiday])["transaction_id"].drop_duplicates()
