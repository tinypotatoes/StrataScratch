/*
Workers With The Highest Salaries
https://platform.stratascratch.com/coding/10353-workers-with-the-highest-salaries?code_type=1

Difficutly: Medium

You have been asked to find the job titles of the highest-paid employees.

Your output should include the highest-paid title or multiple titles with the same salary.

Tables
(worker)
worker_id       int
first_name      varchar
last_name       varchar
salary          int
joining_date    datetime
department      varchar
(title)
worker_ref_id   int
worker_title    varchar
affected_from   datetime

*/

SELECT title.worker_title AS best_paid_title
FROM worker
JOIN title ON worker.worker_id = title.worker_ref_id
WHERE salary = (SELECT MAX(salary) FROM worker);
