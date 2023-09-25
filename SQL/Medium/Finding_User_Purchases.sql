/*
Finding User Purchases
https://platform.stratascratch.com/coding/10322-finding-user-purchases?code_type=1

Difficutly: Medium

Write a query that'll identify returning active users. A returning active user is a user that has made a second purchase within 7 days of any other of their purchases. Output a list of user_ids of these returning active users.

Tables:
(amazon_transactions)
id             int
user_id        int
item           varchar
created_at     datetime
revenue        int
*/

SELECT 
    DISTINCT(t1.user_id)
FROM amazon_transactions t1
JOIN amazon_transactions t2 ON t1.user_id = t2.user_id
WHERE  t1.id != t2.id
    AND t1.created_at - t2.created_at BETWEEN 0 and 7
ORDER BY user_id;
