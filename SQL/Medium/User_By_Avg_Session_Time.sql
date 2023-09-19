/*
Users By Average Session Time
https://platform.stratascratch.com/coding/10352-users-by-avg-session-time?code_type=1

Difficutly: Medium
Calculate each user's average session time. A session is defined as the time difference between a page_load and page_exit. For simplicity, assume a user has only 1 session per day and if there are multiple of the same events on that day, consider only the latest page_load and earliest page_exit, with an obvious restriction that load time event should happen before exit time event . Output the user_id and their average session time.

Tables:
(facebook_web_log)
user_id      int
timestamp    datetime
action       varchar

*/

WITH all_user_session AS (
    SELECT 
        user_id,
        DATE(timestamp),
        MAX(CASE
                WHEN action = 'page_load' THEN timestamp
            END) AS pg_load,
        MIN(CASE
                WHEN action = 'page_exit' THEN timestamp
            END) AS pg_exit
    FROM facebook_web_log
    GROUP BY user_id, date
) 

SELECT 
    user_id,
    AVG(pg_exit - pg_load) AS avg_time
FROM all_user_session
GROUP BY user_id
HAVING AVG(pg_exit - pg_load) IS NOT NULL;
