/*
Cities With The Most Expensive Homes
https://platform.stratascratch.com/coding/10315-cities-with-the-most-expensive-homes?code_type=1

Difficutly: Medium

Write a query that identifies cities with higher than average home prices when compared to the national average. Output the city names.

Tables:
(zillow_transactions)
id               int
state            varchar
city             varchar
street_address   varchar
mkt_price        int

*/

SELECT city
FROM zillow_transactions
GROUP BY city
HAVING 
    AVG(mkt_price) > (SELECT AVG(mkt_price) FROM zillow_transactions);
