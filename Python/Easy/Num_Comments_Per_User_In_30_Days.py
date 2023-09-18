"""
Number of Comments Per User in 30 days before 2020-02-10
https://platform.stratascratch.com/coding/2004-number-of-comments-per-user-in-past-30-days?code_type=2

Difficulty: Easy

Return the total number of comments received for each user in the 30 or less days before 2020-02-10. Don't output users who haven't received any comment in the defined time period.

DataFrame: 
user_id 				int
created_at 				datetime
number_of_comments		int
"""

# Import your libraries
import pandas as pd
from datetime import timedelta

# Start writing code
offset = pd.to_datetime('2020-02-10') - timedelta(days=30)
df = fb_comments_count[fb_comments_count.created_at.between(offset, '2020-02-10', inclusive='both')]
df.groupby('user_id')['number_of_comments'].sum().reset_index()
