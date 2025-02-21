-- 코드를 작성해주세요
SELECT A.ID, IF(B.PARENT_ID IS NULL, 0, COUNT(A.ID)) AS CHILD_COUNT
FROM ECOLI_DATA AS A LEFT JOIN ECOLI_DATA AS B ON A.ID = B.PARENT_ID
GROUP BY A.ID
ORDER BY A.ID;