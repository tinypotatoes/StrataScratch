"""
Finding User Purchases
https://platform.stratascratch.com/coding/10322-finding-user-purchases?code_type=2

Difficulty: Medium

Write a query that'll identify returning active users. A returning active user is a user that has made a second purchase within 7 days of any other of their purchases. Output a list of user_ids of these returning active users.

Tables:
(amazon_transactions)
id             int
user_id        int
item           varchar
created_at     datetime
revenue        int
"""

# Import your libraries
import pandas as pd

# Start writing code
df = pd.merge(amazon_transactions, amazon_transactions, on="user_id")
df_filtered = df[(df['id_x'] != df['id_y']) & ((df['created_at_x'] - df['created_at_y']).dt.days.between(0,7))]
result = df_filtered["user_id"].unique()
