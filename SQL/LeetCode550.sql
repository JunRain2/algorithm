SELECT ROUND(
               COUNT(DISTINCT A.player_id)/(SELECT COUNT(DISTINCT player_id) FROM Activity)
           , 2) AS fraction
FROM Activity AS A, Activity AS B
WHERE A.player_id = B.player_id
  AND DATE_ADD(A.event_date, INTERVAL 1 DAY) = B.event_date;