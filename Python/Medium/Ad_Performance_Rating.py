"""
Ad Performance Rating
https://platform.stratascratch.com/coding/2155-ad-performance-rating/official-solution?code_type=2&utm_source=newsletter&utm_medium=click&utm_campaign=111423+python+question

Difficulty: Medium

Following a recent advertising campaign, the marketing department wishes to classify its efforts based on the total number of units sold for each product.
You have been tasked with calculating the total number of units sold for each product and categorizing ad performance based on the following criteria for items sold:

Outstanding: 30+
Satisfactory: 20 - 29
Unsatisfactory: 10 - 19
Poor: 1 - 9

Your output should contain the product ID, total units sold in descending order, and its categorized ad performance.

Tables:
(marketing_campign)
user_id       int
created_at    datetime
product_id    int
quantity      int
price         int
"""

# Import your libraries
import pandas as pd
import numpy as np

# Start writing code
df = marketing_campaign[['product_id', 'quantity']]
df_grouped = df.groupby('product_id').quantity.sum().reset_index()

conditions = [
    (df_grouped['quantity'] <= 9),
    (df_grouped['quantity'] > 9) & (df_grouped['quantity'] <= 19),
    (df_grouped['quantity'] > 19) & (df_grouped['quantity'] <= 29),
    (df_grouped['quantity'] >= 30)
    ]
    
values = ['Poor', 'Unsatisfactory', 'Satisfactory', 'Outstanding']

df_grouped['ad_performance'] = np.select(conditions, values)
df_grouped.sort_values(by=['quantity'], ascending=False)
