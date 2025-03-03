SELECT DISTINCT A.user_id AS user_id, IF(B.rate IS NULL, 0, B.rate) AS confirmation_rate
FROM Signups AS A
         LEFT JOIN
     (SELECT user_id, ROUND(SUM(action LIKE 'confirmed') / COUNT(*), 2) AS rate
      FROM Confirmations
      GROUP BY user_id) AS B
     ON A.user_id = B.user_id