-- 코드를 입력하세요
SET @TOTAL = (SELECT COUNT(*) AS COUNT
    FROM USER_INFO
    WHERE YEAR(JOINED) = 2021);

SELECT YEAR(B.SALES_DATE) AS YEAR, MONTH(B.SALES_DATE) AS MONTH
        ,COUNT(DISTINCT A.USER_ID) AS PURCHASED_USERS
        ,ROUND(COUNT(DISTINCT A.USER_ID) / @TOTAL, 1) AS PUCHASED_RATIO
FROM (SELECT USER_ID
    FROM USER_INFO
    WHERE YEAR(JOINED) = 2021) AS A, ONLINE_SALE AS B
WHERE A.USER_ID = B.USER_ID
GROUP BY YEAR, MONTH
ORDER BY YEAR, MONTH;