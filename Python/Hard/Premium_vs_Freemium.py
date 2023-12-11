"""
Premium vs Freemium
https://platform.stratascratch.com/coding/10300-premium-vs-freemium?code_type=2

Difficulty: Hard

Find the total number of downloads for paying and non-paying users by date. Include only records where non-paying customers have more downloads than paying customers. The output should be sorted by earliest date first and contain 3 columns date, non-paying downloads, paying downloads.

Tables:
(ms_user_dimension)
user_id           int
acc_id            int

(ms_acc_dimension)
acc_id            int
paying_customer   varchar

(ms_download_facts)
date              datetime
user_id           int
downloads         int
"""
# Import your libraries
import pandas as pd

# Start writing code
ms_user_dimension.head()

df = ms_user_dimension.merge(ms_acc_dimension, on="acc_id")
df = df.merge(ms_download_facts, on="user_id")
df["date"] = df["date"].dt.to_period("D")
df2 = df.pivot_table(index="date", values="downloads", columns="paying_customer", aggfunc="sum").reset_index()
result = df2[df2["no"] > df2["yes"]]
