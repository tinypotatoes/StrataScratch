/*

Activity Rank
https://platform.stratascratch.com/coding/10351-activity-rank?code_type=1

Difficutly: Medium
Find the email activity rank for each user. Email activity rank is defined by the total number of emails sent. The user with the highest number of emails sent will have a rank of 1, and so on. Output the user, total emails, and their activity rank. Order records by the total emails in descending order. Sort users with the same number of emails in alphabetical order.
In your rankings, return a unique value (i.e., a unique rank) even if multiple users have the same number of emails. For tie breaker use alphabetical order of the user usernames.

Tables:
(google_gmail_emails)
id         int
from_user  varchar
to_user    varchar
day        int

/*

SELECT 
    from_user AS user,
    COUNT(*) AS total_emails,
    ROW_NUMBER() OVER (ORDER BY COUNT(*) DESC, from_user ASC) AS rank
FROM google_gmail_emails
GROUP BY from_user;
