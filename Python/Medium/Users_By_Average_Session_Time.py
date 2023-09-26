"""
Users By Average Session Time
https://platform.stratascratch.com/coding/10352-users-by-avg-session-time?code_type=2

Difficulty: Medium

Calculate each user's average session time. A session is defined as the time difference between a page_load and page_exit. For simplicity, assume a user has only 1 session per day and if there are multiple of the same events on that day, consider only the latest page_load and earliest page_exit, with an obvious restriction that load time event should happen before exit time event . Output the user_id and their average session time.

Tables:
(facebook_web_log)
user_id     int
timestamp   datetime
action      varchar
"""

# Import your libraries
import pandas as pd
import numpy as np

# Start writing code
facebook_web_log.head()

page_load_df = facebook_web_log[facebook_web_log['action'] == 'page_load']
page_load_df['day'] = page_load_df['timestamp'].dt.date
page_load_df = page_load_df.groupby(['user_id', 'day'], as_index=False).max()

page_exit_df = facebook_web_log[facebook_web_log['action'] == 'page_exit']
page_exit_df['day'] = page_exit_df['timestamp'].dt.date
page_exit_df = page_exit_df.groupby(['user_id', 'day'], as_index=False).max()

result = pd.merge(page_load_df, page_exit_df, on=['user_id', 'day'])
result['difference'] = result['timestamp_y'] - result['timestamp_x']
result.groupby('user_id').apply(np.mean)
