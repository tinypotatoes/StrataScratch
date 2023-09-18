/*

Variable vs Fixed Rates
https://platform.stratascratch.com/coding/2000-variable-vs-fixed-rates?code_type=1

Difficulty: Medium

Write a query that returns binary description of rate type per loan_id. The results should have one row per loan_id and two columns: for fixed and variable type.

Tables:
(submissions)
id                int
balance           float
interest_rate     float
rate_type         varchar
loan_id           int

*/



SELECT loan_id,
    CASE
        WHEN rate_type = 'fixed' THEN 1
        ELSE 0
    END AS fixed,
    CASE
        WHEN rate_type = 'variable' THEN 1
        ELSE 0
    END AS variable
    
FROM submissions;
