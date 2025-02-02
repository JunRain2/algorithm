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
        (7, '김성민', 37, '남성', '경기');

INSERT INTO company
    VALUES
        (1, '천국테크', 'IT', '서울'),
        (2, '내일은개발왕', 'IT', '경기'),
        (3, '서울방송', '방송', '서울'),
        (4, 'K디자인', '디자인', '인천'),
        (5, '빛나리', '디자인', '서울');

INSERT INTO affiliation
    VALUES
        (1, 1, 1, 3000, '2012-05-09'),
        (2, 1, 1, 3000, '2012-05-09'),
        (3, 1, 1, 3000, '2012-05-09'),
        (4, 2, 1, 3000, '2012-05-09'),
        (5, 2, 1, 3000, '2012-05-09'),
        (6, 3, 1, 3000, '2012-05-09'),
        (7, 4, 1, 3000, '2012-05-09'),
        (8, 4, 1, 3000, '2012-05-09'),
        (9, 5, 1, 3000, '2012-05-09');

# 문제 3
SELECT e.name AS name, e.address AS address
    FROM employee AS e, affiliation AS a, company AS c
    WHERE e.employee_id = a.employee_id AND a.company_id = c.company_id AND c.name = '천국테크'
    ORDER BY e.name ASC;