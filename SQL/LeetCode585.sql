SELECT ROUND(SUM(s), 2) AS tiv_2016
FROM (SELECT SUM(tiv_2016) AS s
      FROM Insurance
      WHERE (lat, lon) IN (SELECT lat, lon
                           FROM Insurance
                           GROUP BY lat, lon
                           HAVING COUNT(*) = 1)
      GROUP BY tiv_2015
      HAVING COUNT(*) > 1) AS A