"""
Comments Distribution
https://platform.stratascratch.com/coding/10297-comments-distribution?code_type=2

Difficulty: Hard

Write a query to calculate the distribution of comments by the count of users that joined Meta/Facebook between 2018 and 2020, for the month of January 2020.

The output should contain a count of comments and the corresponding number of users that made that number of comments in Jan-2020. For example, you'll be counting how many users made 1 comment, 2 comments, 3 comments, 4 comments, etc in Jan-2020. Your left column in the output will be the number of comments while your right column in the output will be the number of users. Sort the output from the least number of comments to highest.

To add some complexity, there might be a bug where an user post is dated before the user join date. You'll want to remove these posts from the result.

Tables:
(fb_users)
id            int
name          varchar
joined_at     datetime
city_id       int
device        int

(fb_comments)
user_id       int
body          varchar
created_at    datetime
"""
# Import your libraries
import pandas as pd

# Start writing code
df = fb_users.merge(fb_comments, right_on="user_id", left_on="id")

df = df[df['created_at'] > df['joined_at']]
df = df[df['joined_at'].dt.year.isin([2018, 2019, 2020])]
df = df[(df["created_at"].dt.year == 2020) & (df["created_at"].dt.month == 1)]

df_count = df.groupby("id")["body"].count().reset_index()
result = df_count.groupby("body").count().reset_index(names="number_commends_made")
