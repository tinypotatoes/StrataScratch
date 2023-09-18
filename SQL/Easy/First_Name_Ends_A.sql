/*
Find all workers whose first name ends with the letter 'a'.
https://platform.stratascratch.com/coding/9841-find-all-workers-whose-first-name-ends-with-the-letter-a?code_type=1

Difficulty: Easy

Tables:
(worker)
worker_id      int
first_name     varchar
last_name      varchar
salary         int
joining_date   datetime
department     varchar

*/

SELECT * 
FROM worker
WHERE worker.first_name LIKE '%a'
