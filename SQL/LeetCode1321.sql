#Write your MySQL query statement below
SELECT A.visited_on, SUM(B.amount) AS amount, ROUND(AVG(B.amount), 2) AS average_amount
FROM Customer AS A
         LEFT JOIN Customer AS B ON B.visited_on BETWEEN DATE_SUB(A.visited_on, INTERVAL 6 DAY) AND A.visited_on
GROUP BY A.customer_id
ORDER BY A.visited_on;