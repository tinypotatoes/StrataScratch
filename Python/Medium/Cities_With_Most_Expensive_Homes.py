"""
Cities With The Most Expensive Homes
https://platform.stratascratch.com/coding/10315-cities-with-the-most-expensive-homes?code_type=2

Difficulty: Medium

Write a query that identifies cities with higher than average home prices when compared to the national average. Output the city names.

Tables:
(zillow_transactions)
id               int
state            varchar
city             varchar
street_address   varchar
mkt_price        int
"""

# Import your libraries
import pandas as pd

# Start writing code
nat_avg = zillow_transactions.mkt_price.mean()
df = zillow_transactions.groupby('city')['mkt_price'].mean().reset_index(name='avg_price_of_city')
result = df[df['avg_price_of_city'] > nat_avg]
result = result[['city']]
