/*
Election Results
https://platform.stratascratch.com/coding/2099-election-results?code_type=1

Difficutly: Medium

The election is conducted in a city and everyone can vote for one or more candidates, or choose not to vote at all. Each person has 1 vote so if they vote for multiple candidates, their vote gets equally split across these candidates. For example, if a person votes for 2 candidates, these candidates receive an equivalent of 0.5 vote each.
Find out who got the most votes and won the election. Output the name of the candidate or multiple names in case of a tie. To avoid issues with a floating-point error you can round the number of votes received by a candidate to 3 decimal places.

Tables:
(voting_results)
voter        varchar
candidate    varchar
*/

WITH weight AS (
    SELECT 
        voter, 
        ROUND(1.0 / COUNT(*), 3) AS weight_vote
    FROM voting_results
    WHERE candidate IS NOT NULL
    GROUP BY voter
)

SELECT candidate
FROM voting_results
LEFT JOIN weight ON voting_results.voter = weight.voter
GROUP BY candidate
ORDER BY SUM(weight_vote) DESC
LIMIT 1;
