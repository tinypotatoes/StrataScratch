"""
New Products
https://platform.stratascratch.com/coding/10318-new-products?code_type=2

Difficulty: Medium

You are given a table of product launches by company by year. Write a query to count the net difference between the number of products companies launched in 2020 with the number of products companies launched in the previous year. Output the name of the companies and a net difference of net products released for 2020 compared to the previous year.

Tables:
(car_launches)
year            int
company_name    varchar
product_name    varchar
"""

# Import your libraries
import pandas as pd

# Start writing code
df_2020 = car_launches[car_launches['year'] == 2020].groupby('company_name')['product_name'].count().reset_index()
df_2019 = car_launches[car_launches['year'] == 2019].groupby('company_name')['product_name'].count().reset_index()

df = pd.merge(df_2020, df_2019, on='company_name')
df['diff'] = df["product_name_x"] - df['product_name_y']
df[["company_name", "diff"]]
