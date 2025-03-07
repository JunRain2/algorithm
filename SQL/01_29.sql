# 1번
CREATE TABLE registered_member
(
    id       INT PRIMARY KEY,
    name     VARCHAR(20) NOT NULL,
    age      INT         NOT NULL,
    gender   VARCHAR(10) NOT NULL,
    address  VARCHAR(100),
    grade    INT         NOT NULL,
    datetime DATETIME    NOT NULL
);

CREATE TABLE retired_member
(
    id       INT PRIMARY KEY,
    name     VARCHAR(20) NOT NULL,
    age      INT         NOT NULL,
    gender   VARCHAR(10) NOT NULL,
    address  VARCHAR(100),
    grade    INT         NOT NULL,
    datetime DATETIME    NOT NULL
);

# 2번
INSERT INTO registered_member
VALUES (1, '나동빈', 30, '남성', '경기', 5, '2012-05-03 13:00:00'),
       (2, '홍길동', 20, '남성', '경기', 3, '2012-06-12 15:00:00'),
       (3, '김영희', 32, '여성', '서울', 3, '2012-08-14 21:00:00'),
       (4, '이순신', 24, '남성', '서울', 5, '2012-07-14 14:00:00'),
       (5, '임꺽정', 45, '남성', '인천', 2, '2012-08-08 15:00:00'),
       (6, '임민정', 33, '여성', '인천', 5, '2012-07-29 11:00:00'),
       (7, '김성민', 37, '남성', NULL, 4, '2012-10-21 13:00:00'),
       (8, '박지은', 33, '여성', '서울', 3, '2012-05-08 14:00:00'),
       (9, '이선희', 32, '여성', NULL, 1, '2012-09-26 12:00:00');

INSERT INTO retired_member
VALUES (1, '나동빈', 30, '남성', '경기', 4, '2012-08-03 13:00:00'),
       (2, '홍길동', 20, '남성', '경기', 5, '2012-02-12 15:00:00'),
       (3, '김영희', 32, '여성', '서울', 2, '2012-11-14 21:00:00'),
       (4, '이순신', 24, '남성', '서울', 4, '2012-08-14 14:00:00'),
       (5, '임꺽정', 45, '남성', '인천', 3, '2012-09-08 15:00:00'),
       (21, '강민철', 32, '여성', '경기', 2, '2012-12-07 12:00:00'),
       (22, '서정문', 39, '남성', '서울', 5, '2012-10-05 10:00:00');

# 3번
SELECT *
FROM registered_member
ORDER BY name;

# 4번
SELECT name
FROM registered_member
WHERE age >= 30
ORDER BY name;

# 5번
SELECT name, datetime
FROM registered_member
ORDER BY datetime DESC
LIMIT 1;

# 6번
SELECT *
FROM registered_member
ORDER BY grade DESC, datetime;

# 7번
SELECT grade
FROM registered_member
ORDER BY grade
LIMIT 1;
SELECT MIN(grade)
FROM registered_member;
# MIN을 통한 해결이 가능 -> 필드가 하나뿐이기 때문에 집약이 가능

# 8번
SELECT COUNT(*)
FROM registered_member;

# 9번
SELECT COUNT(tmp.grade)
FROM (SELECT DISTINCT grade
      FROM registered_member) AS tmp;
SELECT COUNT(DISTINCT grade)
FROM registered_member;
# COUNT에 DISTINCT 예약어를 넣어서 해결 가능

# 10번
SELECT grade, COUNT(grade)
FROM registered_member
GROUP BY grade
ORDER BY grade;

# 11번
SELECT grade, COUNT(grade)
FROM registered_member
GROUP BY grade
HAVING COUNT(grade) >= 2
ORDER BY grade;

# 12번
SELECT *
FROM registered_member
WHERE datetime BETWEEN '2012-07-01' AND '2012-09-30'
ORDER BY datetime;

# 13번
SELECT MONTH(datetime), COUNT(*)
FROM registered_member
WHERE datetime BETWEEN '2012-07-01' AND '2012-09-30'
GROUP BY MONTH(datetime)
ORDER BY MONTH(datetime);
# ORDER BY의 기준은 SELECT 의해 선택된 칼럼 중 하나여야 함

# 14번
SELECT MONTH(datetime), COUNT(*)
FROM registered_member
WHERE datetime BETWEEN '2012-01-01' AND '2012-08-31'
GROUP BY MONTH(datetime)
ORDER BY MONTH(datetime); # 틀린 풀이

SET @month = 0;
SELECT (@month := @month + 1)                                                   AS month,
       (SELECT COUNT(id) FROM registered_member WHERE MONTH(datetime) = @month) AS count
FROM registered_member
WHERE @month < 8;

# 15번
SELECT id
FROM registered_member
WHERE address IS NULL
ORDER BY id;

# 16번
SELECT id
FROM registered_member
WHERE address IS NOT NULL
ORDER BY id;

# 17번
SELECT name, IF(address IS NULL, '지역 정보 없음', address) AS address, grade # 3항 문항 형식의 IF 문
FROM registered_member
ORDER BY name;

# 18번
SELECT name, address, gender, datetime
FROM registered_member
WHERE address = '경기'
ORDER BY name;

# 19번
SELECT name, IF(age < 30, "young", "old") AS age
FROM registered_member
ORDER BY name;

SELECT name,
       (
           CASE
               WHEN age < 30 THEN 'young'
               ELSE 'old'
               END
           ) AS age
FROM registered_member
ORDER BY name;

# 20번
SELECT r.id, r.name
FROM registered_member AS r,
     retired_member AS tmp
WHERE r.id = tmp.id
  AND r.datetime > tmp.datetime
ORDER BY r.name;

# 21번
SELECT rt.id, rt.name
FROM retired_member AS rt
WHERE rt.name NOT IN (SELECT name FROM registered_member)
ORDER BY rt.name;

SELECT rt.id, rt.name
FROM retired_member AS rt
         LEFT JOIN registered_member AS rg ON rt.id = rg.id
WHERE rg.id IS NULL
ORDER BY rt.id;

# 22번
SELECT rg.name, rg.age, rg.datetime
FROM registered_member AS rg
         LEFT JOIN retired_member AS rt ON rg.id = rt.id
WHERE rt.id IS NULL
ORDER BY rg.datetime
LIMIT 2;

# 23번
SELECT rt.name, rt.datetime, rt.grade
FROM registered_member AS rg,
     retired_member AS rt
where rg.id = rt.id
  AND rg.grade > rt.grade
ORDER BY rt.name;

# 24번
SELECT gender, AVG(age), AVG(grade)
FROM registered_member
GROUP BY gender
ORDER BY AVG(grade);

# 25번
SELECT name, grade, age, datetime
FROM registered_member AS rg
WHERE rg.name LIKE '_동빈%'
   OR rg.name LIKE '_길동%'
   OR rg.name LIKE '_민정%'
   OR rg.name LIKE '_성민%'
ORDER BY datetime;

# 26번
SELECT name, grade, age, datetime
FROM registered_member
WHERE name = '홍길동'
   OR name = '이순신'
   OR name = '김성민'
ORDER BY datetime;

SELECT name, grade, age, datetime
FROM registered_member
WHERE name IN ('홍길동', '이순신', '김성민')
ORDER BY datetime;

# 27번
SELECT name, grade, age, datetime
FROM retired_member
WHERE name LIKE '%민%'
  AND gender = '남성'
ORDER BY datetime;

# 28번
SELECT tmp.name, tmp.grade
FROM (SELECT rg.name, rg.grade, (rt.datetime - rg.datetime) AS datetime
      FROM registered_member AS rg
               LEFT JOIN retired_member AS rt ON rg.id = rt.id
      WHERE rt.datetime IS NOT NULL
      ORDER by datetime, rg.name) AS tmp
ORDER BY name
LIMIT 3;

SELECT rg.name, rg.grade
FROM registered_member AS rg
         LEFT JOIN retired_member AS rt ON rg.id = rt.id
ORDER BY (rt.datetime - rg.datetime) DESC,
         name ASC
LIMIT 3;

# 29번
SELECT name, DATE(datetime)
FROM registered_member
WHERE gender = "남성"
ORDER BY datetime;