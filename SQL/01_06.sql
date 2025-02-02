# 1번
CREATE TABLE employee
(
    employee_id INT PRIMARY KEY,
    name        VARCHAR(30)  NOT NULL,
    age         INT          NOT NULL,
    gender      VARCHAR(30)  NOT NULL,
    address     VARCHAR(100) NOT NULL
);

CREATE TABLE company
(
    company_id INT PRIMARY KEY,
    name       VARCHAR(30)  NOT NULL,
    category   VARCHAR(30)  NOT NULL,
    address    VARCHAR(100) NOT NULL
);

CREATE TABLE affiliation
(
    affiliation_id INT PRIMARY KEY,
    employee_id    INT  NOT NULL,
    company_id     INT  NOT NULL,
    pay            INT  NOT NULL,
    entry_date     DATE NOT NULL,
    FOREIGN KEY (employee_id) REFERENCES employee(employee_id), # REFERENCES 복수형
    FOREIGN KEY (company_id) REFERENCES company(company_id)
);

# 2번
INSERT INTO employee
    VALUES
        (1, '나동빈', 27, '남성', '경기'),
        (2, '홍길동', 20, '남성', '경기'),
        (3, '김영희', 32, '여성', '서울'),
        (4, '이순신', 24, '남성', '서울'),
        (5, '임꺽정', 45, '남성', '인천'),
        (6, '임민정', 33, '여성', '인천'),
        (7, '김성민', 37, '남성', '경기'),
        (8, '박지은', 33, '여성', '서울'),
        (9, '이선희', 32, '여성', '경기');

INSERT INTO company
    VALUES
        (1, '천국테크', 'IT', '서울'),
        (2, '내일은개발왕', 'IT', '경기'),
        (3, '서울방송', '방송', '서울'),
        (4, 'K디자인', '디자인', '인천'),
        (5, '빛나리', '디자인', '서울');

INSERT INTO affiliation
    VALUES
        (1,  1, 1,3000, '2012-05-09'),
        (2,  2, 1,5000, '2012-05-21'),
        (3,  3, 1,4500, '2012-08-11'),
        (4,  4, 2,6500, '2012-05-14'),
        (5,  5, 2,7000, '2012-04-23'),
        (6,  6, 3,4000, '2012-09-15'),
        (7,  7, 4,3500, '2012-05-06'),
        (8,  8, 4,5500, '2012-08-08'),
        (9,  9, 5,4500, '2012-08-07');

# 문제 3
SELECT DISTINCT e.name AS name, e.address AS address
    FROM employee AS e, company AS c, affiliation as a
    WHERE e.employee_id = a.employee_id
        AND c.company_id = a.company_id
        AND c.name = '천국테크'
    ORDER BY e.name;

# 문제 4
SELECT e.name, c.name, c.address, e.address
    FROM employee AS e, company AS c, affiliation AS a
    WHERE e.employee_id = a.employee_id
        AND c.company_id = a.company_id
        AND NOT e.address = c.address # !=를 활용해도 됨
    ORDER BY e.name;

# 문제 5
SELECT c.name, COUNT(e.employee_id), AVG(a.pay)
    FROM company AS c, affiliation  AS a, employee AS e
    WHERE c.company_id = a.company_id
        AND e.employee_id = a.employee_id
    GROUP BY c.name
    ORDER BY c.name;

# 문제 6
SELECT e.name, c.company_id, a.pay
    FROM employee AS e, company AS c, affiliation AS a
    WHERE e.employee_id = a.employee_id
        AND a.company_id = c.company_id
    GROUP BY c.company_id
        HAVING AVG(a.pay) < a.pay
    ORDER BY e.name;