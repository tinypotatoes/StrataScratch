"""
Workers With The Highest Salaries
https://platform.stratascratch.com/coding/10353-workers-with-the-highest-salaries?code_type=2

Difficulty: Easy

Tables:
(worker)
worker_id         int
first_name        varchar
last_name         varchar
salary            int
joining_date      datetime
department        varchar

(title)
worker_ref_id:    int
worker_title      varchar
affected_from     datetime
"""

# Import your libraries
import pandas as pd

# Start writing code
merged_df = worker.merge(title, left_on="worker_id", right_on="worker_ref_id")
result = merged_df[worker.salary == worker.salary.max()][["worker_title"]]
