(SELECT A.id, A.visit_date, A.people
FROM Stadium AS A
    JOIN Stadium AS B ON A.id - 1 = B.id
    JOIN Stadium AS C ON A.id + 1 = C.id
WHERE A.people >= 100 AND B.people >= 100 AND C.people >= 100
UNION
SELECT A.id, A.visit_date, A.people
FROM Stadium AS A
    JOIN Stadium AS B ON A.id + 1 = B.id
    JOIN Stadium AS C ON A.id + 2 = C.id
WHERE A.people >= 100 AND B.people >= 100 AND C.people >= 100
UNION
SELECT A.id, A.visit_date, A.people
FROM Stadium AS A
    JOIN Stadium AS B ON A.id - 1 = B.id
    JOIN Stadium AS C ON A.id - 2 = C.id
WHERE A.people >= 100 AND B.people >= 100 AND C.people >= 100)
ORDER BY visit_date