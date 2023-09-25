/*
New Products
https://platform.stratascratch.com/coding/10318-new-products?code_type=1

Difficutly: Medium

You are given a table of product launches by company by year. Write a query to count the net difference between the number of products companies launched in 2020 with the number of products companies launched in the previous year. Output the name of the companies and a net difference of net products released for 2020 compared to the previous year.

Tables:
(car_launches)
year            int
company_name    varchar
product_name    varchar

*/

SELECT 
    company_name,
    sum(
        CASE
            WHEN year = 2019  THEN -1
            WHEN year = 2020 THEN 1
        END) AS net_products
FROM car_launches
GROUP BY company_name
ORDER BY net_products DESC
