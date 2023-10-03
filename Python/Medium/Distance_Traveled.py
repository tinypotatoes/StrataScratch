"""
Distance Traveled
https://platform.stratascratch.com/coding/10324-distances-traveled?code_type=2


Difficutly: Medium

Find the top 10 users that have traveled the greatest distance. Output their id, name and a total distance traveled.

Tables:
(lyft_rides_log)
id          int
user_id     int
distance    int

(lyft_users)
id          int
name        varchar
"""

# Import your libraries
import pandas as pd

# Start writing code
df_merged = pd.merge(lyft_rides_log, lyft_users, left_on="user_id", right_on="id")
df_merged = df_merged.groupby(['user_id', "name"])['distance'].sum().reset_index()
df_merged.nlargest(10, 'distance')
