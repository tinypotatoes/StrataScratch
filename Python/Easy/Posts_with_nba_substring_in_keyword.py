"""
Posts with 'nba' substring in keyword
https://platform.stratascratch.com/coding/9768-find-all-posts-with-the-keyword-nba?code_type=2

Difficulty: Easy
Find all posts with a keyword that contains 'nba' substring.

DataFrames:
(facebook posts)
post_id          int
poster           int
post_text        varchar
post_keywords    varchar
post_date        datetime
"""

# Import your libraries
import pandas as pd

# Start writing code
result = facebook_posts[facebook_posts['post_keywords'].str.contains('nba')]
