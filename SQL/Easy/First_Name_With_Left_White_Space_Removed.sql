/*
First Name With Left White Space Removed
https://platform.stratascratch.com/coding/9830-print-the-first-name-after-removing-white-spaces-from-the-right-side?code_type=1

Difficulty: Easy

Print the first name after removing white spaces from the right side.
Tables
(worker_ws)
worker_id     int
first_name    varchar
last_name     varchar
salary        int
joining_date  datetime
department    varchar


*/

SELECT LTRIM(first_name) AS first_name_trimed
FROM worker_ws;
