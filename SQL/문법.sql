# 데이터베이스 생성
CREATE DATABASE `my_database` CHARACTER SET utf8 COLLATE utf8_general_ci;

# 데이터베이스 조회
SHOW DATABASES;

# 데이터베이스 접근
USE my_database;

# 데이터베이스 삭제
DROP DATABASE `my_database`;


# 데이터베이스 내부 테이블 확인
SHOW TABLES;

# 코드 컨벤션
# 예약어 대분자
# 단어는 축약하지 않음
# 능동태 사용
# 테이블과 열에는 소문자 사용, 단수형, 스네키으 케이스
# 라인별 띄어쓰기는 일관성있게 사용
# ;을 사용하여 문장 종료

# 행 = 레코드 = 튜플
# 열 = 필드 = 열

# 테이블 생성
CREATE TABLE `student`
(
    student_id         INT PRIMARY KEY,
    student_name       VARCHAR(20) NOT NULL,
    student_birth_date DATE        NOT NULL
);
# -> 소괄호
# NOT NULL : NULL 값 비허용, 중복 허용
# UNIQUE : NULL 값 허용, 중복 비허용
# PRIMARY KEY : NULL 값 비허용, 중복 비허용, 테이블 당 하나
# DEFAULT : 해당 칼럼의 기본 값을 설정

# 테이블의 구조를 확인
DESC student;

# 외래키는 하나의 테이블이 다른 테이블을 참조할 떄 사용
CREATE TABLE registration
(
    student_id INT,
    lecture_id INT,
    data       DATETIME,
    #            registration의 칼럼      student테이블의 student_id 참조
    FOREIGN KEY (student_id) REFERENCES student (student_id),
    FOREIGN KEY (lecture_id) REFERENCES lecture (lecture_id)
);

# 만약 테이블이 존재하면 삭제
DROP TABLE IF EXISTS student;

# 실습 테이블
CREATE TABLE course
(
    course_id   INT PRIMARY KEY,
    course_name VARCHAR(50) NOT NULL,
    course_cost INT         NOT NULL,
    course_date DATETIME
);

# INSERT 명령어, 테이블 칼럼 순서대로 입력
INSERT INTO course
    VALUES (1, '데이터베이스', 4000000, '2012-05-05 00:00:00');

INSERT INTO course (course_id, course_name, course_cost) # 칼럼을 명시적으로 입력 가능
    VALUES (2, '인공지능', 4000000);

# 여러 개의 값을 한 번에 INSERT
INSERT INTO course (course_id, course_name, course_cost)
    VALUES
        (3, '컴퓨터개론', 150000),
        (4, '알고리즘', 4000000),
        (5, '자료구조', 2750000);

# DELETE 명령어, WHERE 절에 따라 제거
DELETE FROM course WHERE course_id = 1;
DELETE FROM course WHERE course_name = '데이터베이스'; # 데이터베이스가 이름인 행 모두 삭제
DELETE FROM course; # 테이블에 존재하는 모든 데이터 삭제
TRUNCATE course; # 테이블에 모든 데이터 삭제 DELETE에 비해 빠르지만 복구 불가

# UPDATE 테이블에서 업데이트
UPDATE course
    SET course_cost = 100000
    WHERE course_name = '데이터베이스';

# SELECT
# 실습 테이블
DROP TABLE IF EXISTS course;
CREATE TABLE course(
    course_id INT PRIMARY KEY,
    course_name VARCHAR(50) NOT NULL,
    course_cost INT NOT NULL,
    course_date DATE
);
DESC course;

INSERT INTO course
    VALUES
        (1, 'Programing', 30000, '2015-09-07'),
        (2, 'MySQL', 40000, '2015-09-10'),
        (3, 'Oracle 11g', 35000, '2015-09-09'),
        (4, 'Physics', 20000, '2015-09-10'),
        (5, 'Education', 30000, '2015-09-09'),
        (6, 'Economics', 40000, '2015-09-10');

SELECT * FROM course WHERE course_cost = 40000 OR course_cost = 35000;
SELECT * FROM course WHERE course_name = 'Programing';

# AS를 통해서 별칭 부여, 테이블에 부여도 가능
SELECT course_name AS name, course_cost AS cost FROM course;
SELECT c.course_name AS name, c.course_cost AS cost FROM course AS c WHERE c.course_cost = 30000;
SELECT c.course_name AS name, c.course_cost * 1.1 AS cost FROM course AS c WHERE c.course_cost = 30000; # 결과에 사칙연산 간으
# ORDER BY 를 통한 정렬(기본은 오름차순)
SELECT * FROM course ORDER BY course_cost DESC; #ASC
SELECT * FROM course ORDER BY course_cost DESC, course_name ASC; # 두 개의 기준
# GROUP BY 명령어 -> 집계함수를 사용하지 않으면 전체가 노출이 안됨
SELECT course_cost, COUNT(course_id) FROM course GROUP BY course_cost;
# JOIN 명령어
# INNER JOIN A와 B에 동일한 키가 있는 테이블
# LEFT JOIN A테이블을 모두 조회하면서 B에 동일한 키가 있는 레코드와 매칭
# FULL OUTER JOIN 테이블 A와 B의 모든 레코드를 조회하되, 동일한 키가 있는 레코드는 매칭
# 실습
CREATE TABLE student(
    student_id INT PRIMARY KEY,
    name VARCHAR(20) NOT NULL,
    age INT NOT NULL
);

INSERT INTO student
    VALUES
        (1, '홍길동', 20),
        (2, '김철수', 22),
        (3, '이순신', 25),
        (4, '나동빈', 30),
        (5, '장영실', 29),
        (6, '장국역', 22);

CREATE TABLE belonging(
    student_id INT NOT NULL,
    department_name VARCHAR(20) NOT NULL
);

INSERT INTO belonging
    VALUES
        (1, '컴퓨터공학과'),
        (2, '전자공학과'),
        (3, '식품영양학과'),
        (4, '간호학과'),
        (4, '기계공학과'),
        (7, '산업디자인과');

# 교차 조인: 두 테이블에 대하여 카테시안 곱을 수행하여 반환
# 반환되는 레코드 수 = 테이블 A의 레코드 수 * 테이블 B의 레코드 수
SELECT * FROM student, belonging;
# INNER JOIN: 테이블 A와 테이블 B에 동일한 키가 있는 레코드에 대해서만 조회
# 암묵적 표현
SELECT * FROM student, belonging WHERE student.student_id = belonging.student_id;
# 명시적 표현
SELECT * FROM student INNER JOIN belonging ON student.student_id = belonging.student_id;

# 레프트 조인: 테이블 A의 코든 레코드를 조회하되, 테이블 B에 동일한 키의 레코드와 매칭
SELECT * FROM student LEFT JOIN belonging ON student.student_id = belonging.student_id;

# 완전 외부 조인: 테이블 A와 B의 코든 레코드를 조회하되, 동일한 키가 있는 레코드는 매칭
# MySQL 에서는 완전 외부 조인을 위한 명시적인 SQL 문법은 지원하지 않음 -> UNION 명령어를 사용하여 실행
SELECT *
FROM student
LEFT JOIN belonging ON belonging.student_id = student.student_id
UNION
SELECT *
FROM student
RIGHT JOIN belonging ON belonging.student_id = student.student_id;

# 연산자와 자료형