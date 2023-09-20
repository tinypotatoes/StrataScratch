/*
Distances Traveled
https://platform.stratascratch.com/coding/10324-distances-traveled?code_type=1

Difficutly: Medium

Find the top 10 users that have traveled the greatest distance. Output their id, name and a total distance traveled.

Tables:
(lyft_rides_log)
id          int
user_id     int
distance    int

(lyft_users)
id:         int
name        varchar

*/

SELECT 
    users.id,
    users.name,
    SUM(log.distance) AS total_distasnce
FROM lyft_rides_log log
JOIN lyft_users users ON log.user_id = users.id
GROUP BY 
    users.id, 
    users.name
ORDER BY SUM(log.distance) DESC
LIMIT 10;
