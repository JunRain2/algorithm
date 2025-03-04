SELECT B.name AS Department, A.name AS Employee, A.salary AS Salary
FROM Employee AS A JOIN Department AS B ON A.departmentId = B.id
WHERE (A.departmentId, A.salary) IN (SELECT departmentId, salary
                                     FROM Employee
                                     WHERE A.departmentId = departmentId
                                     ORDER BY salary DESC
                                     LIMIT 3);
