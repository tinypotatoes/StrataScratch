/*
Recent Refinance Submissions
https://platform.stratascratch.com/coding/2003-recent-refinance-submissions?code_type=1

Difficulty: Medium

Write a query that joins this submissions table to the loans table and returns the total loan balance on each user’s most recent ‘Refinance’ submission. Return all users and the balance for each of them.

Tables
(loans)
id          int
user_id     int
created_at  datetime
status      varchar
type        varchar

(submissions)
id               int
balance          float
interest_rate    float
rate_type        varchar
loan_id          int
*/

SELECT l.user_id, balance
FROM 
    (SELECT DISTINCT 
        id, 
        user_id, 
        created_at,
        MAX(created_at) OVER (PARTITION BY user_id, type) most_recent
    FROM loans
    WHERE type = 'Refinance') l
JOIN submissions ON l.id = submissions.loan_id
WHERE most_recent = created_at;
