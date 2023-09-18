/*

Submission Types
https://platform.stratascratch.com/coding/2002-submission-types?code_type=1

Difficulty: Easy
Write a query that returns the user ID of all users that have created at least one ‘Refinance’ submission and at least one ‘InSchool’ submission.

Tables
(loans)
id          int
user_id     int
created_at  datetime
status      varchar
type        varchar

*/

SELECT user_id
FROM loans
WHERE loans.type = 'Refinance'

INTERSECT

SELECT user_id
FROM loans
WHERE loans.type = 'InSchool';
