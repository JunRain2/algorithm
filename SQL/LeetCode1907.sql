SELECT
    CASE
        WHEN income > 50000 THEN 'High Salary'
        WHEN income >= 20000 THEN 'Average Salary'
        ELSE 'Low Salary'
        END AS category
     ,COUNT(*) AS accounts_count
FROM Accounts
GROUP BY Category