SELECT DISTINCT l1.num AS ConsecutiveNums
FROM Logs l1
         JOIN Logs l2 ON l1.id = l2.id - 1
         JOIN Logs l3 ON l1.id = l3.id - 2
WHERE l1.num = l2.num AND l2.num = l3.num;

SELECT DISTINCT num AS ConsecutiveNums
FROM (
         SELECT num,
                LAG(num) OVER (ORDER BY id) AS prev_num,
                 LEAD(num) OVER (ORDER BY id) AS next_num
         FROM Logs
     ) t
WHERE num = prev_num AND num = next_num;
