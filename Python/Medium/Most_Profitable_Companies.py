"""
Most Profitable Companies
https://platform.stratascratch.com/coding/10354-most-profitable-companies?code_type=2

Difficutly: Medium
Find the 3 most profitable companies in the entire world. Output the result along with the corresponding company name. Sort the result based on profits in descending order.

Tables:
(forbes_global_2010_2014)
company            varchar
sector             varchar
industry           varchar
continent          varchar
country            varchar
marketvalue        float
sales              float
profits            float
assets             float
rank               int
forbeswebpage      varchar
"""

# Import your libraries
import pandas as pd

# Start writing code
result = forbes_global_2010_2014.sort_values(['profits'], ascending=False)
result = result[['company', 'profits']].head(3)
