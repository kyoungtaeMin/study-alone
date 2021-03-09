----- 정규식 -----------------------------------------------

SELECT * FROM NOTICE
    WHERE REGEXP_LIKE (TITLE, '01[016-9]-/d{3,4}-/d{4}');
-- 전화번호 검색
    
SELECT * FROM NOTICE
    WHERE TITLE LIKE '\D\w*@\D\w*.(org|net|com)';
-- EMAIL 검색
-- Ragular Expression Library 에서 정규식 조회,작성,테스트
-----------------------------------------------------------
SELECT * FROM NOTICE WHERE ROWNUM BETWEEN 1 AND 5;

SELECT NOTICE.* FROM NOTICE;

SELECT ROWNUM, NOTICE.* FROM NOTICE;

SELECT * FROM  (SELECT ROWNUM NUM, NOTICE.* FROM NOTICE)
WHERE NUM BETWEEN 2 AND 3;

INSERT INTO MEMBER(ID, PWD, NAME, GENDER, BIRTHDAY, PHONE, EMAIL, AGE) 
    VALUES('min', '000', '민경태', '남성', '1991-01-14', 
            '010-9876-5432', 'min7@study.com', 31);

INSERT INTO MEMBER(ID, PWD, NAME, AGE) 
    VALUES('kim', '111', '김두한', 29);

INSERT INTO MEMBER(ID, PWD, NAME, AGE) 
    VALUES('yoo', '123', '유재석', 29);

INSERT INTO MEMBER(ID, PWD, NAME, AGE) 
    VALUES('king', '222', '킹세종', 29);

INSERT INTO MEMBER(ID, PWD, NAME, AGE) 
    VALUES('yong', '333', '김용만', 29);
    
UPDATE MEMBER SET NAME = '뉴렉', AGE = 35
    WHERE ID = 'newlec';

UPDATE MEMBER SET NAME = '강호동', AGE = 35
    WHERE ID = 'kang';
    
UPDATE MEMBER SET AGE = 25
    WHERE ID = 'dragon';

UPDATE MEMBER SET AGE = 40
    WHERE ID = 'yoo';

UPDATE MEMBER SET AGE = 100
    WHERE ID = 'king';
    
----- 문자열 함수 -----------------------------------------------

SELECT DISTINCT AGE FROM MEMBER; 
-- 중복된 값 제거하기(하나의 column에만 적용가능)

SELECT NAME FROM MEMBER;
SELECT SUBSTR(NAME, 2) FROM MEMBER; -- 2번째 문자부터 자른다.
SELECT SUBSTRB(NAME, 3) FROM MEMBER; --BYTE로 자른다.

SELECT NAME, SUBSTR(BIRTHDAY, 6, 2) MONTH FROM MEMBER;
-- 1991-07-14, 6번째 문자부터 2개, MONTH라는 새로운 컬럼으로.

SELECT * FROM MEMBER WHERE PHONE = '011%';
SELECT * FROM MEMBER WHERE SUBSTR(BIRTHDAY, 6, 2) = '07' OR
                            SUBSTR(BIRTHDAY, 6, 2) = '08' OR
                            SUBSTR(BIRTHDAY, 6, 2) = '09';
SELECT * FROM MEMBER WHERE SUBSTR(BIRTHDAY, 6, 2) IN ('07', '08', '09');
SELECT * FROM MEMBER WHERE SUBSTR(BIRTHDAY, 6, 2) NOT IN ('07', '08', '09');

SELECT * FROM MEMBER 
WHERE PHONE IS NULL AND SUBSTR(BIRTHDAY, 6, 2) IN ('02', '03', '09');

SELECT CONCAT('홍', '길동') FROM DUAL; -- 문자열 덧셈
SELECT 3 || '4' FROM DUAL;

SELECT TRIM('  HELLO  ') FROM DUAL; -- 문자열 트림 함수

SELECT LOWER('nEWlec') FROM DUAL; -- 모든 문자를 소문자로 변경
SELECT UPPER('nEWlec') FROM DUAL; -- 모든 문자를 대문자로 변경

SELECT UPPER(ID) FROM MEMBER WHERE ID='king';
SELECT * FROM MEMBER WHERE UPPER(ID)='kim';

SELECT REPLACE('WHERE YOU ARE', 'YOU', 'WE') FROM DUAL;
-- WHERE YOU ARE -> WHERE WE ARE

SELECT TRANSLATE('WHERE WE ARE', 'WE', 'YOU') FROM DUAL;
-- WHERE YOU ARE -> YHORO YO ARO 각각의 문자 순서에 맞게 바뀜

SELECT REPLACE(NAME, ' ', ''), GENDER FROM MEMBER;

SELECT LPAD('HELLO', 10, '0') FROM DUAL; 
-- HELLO 를 왼쪽에 0을 채워 10개의 문자로 정렬해라(한글은 X2의 길이를 사용)
SELECT RPAD('이순신', 8, '님') FROM DUAL;
-- [오른쪽] 길이 : 이순신 = 6, 이순신님 = 8

SELECT INITCAP('the important thing is ....') FROM DUAL;
-- 단어마다 첫 글자를 대문자로 바꿔준다
-- 단어 중간에 한글이 들어가면 한글의 다음에 오는 문자까지 대문자로 바뀜

SELECT INSTR('ALL WE NEED TO IS JUST TO...', 'TO') FROM DUAL;
-- 문자열 내에서 TO가 어디에 위치해 있는지 출력(첫번째 TO의 위치만 나옴)
SELECT INSTR('ALL WE NEED TO IS JUST TO...', 'TO', 15) FROM DUAL;
-- 15번째 뒤에 있는 TO를 찾아라
SELECT INSTR('ALL WE NEED TO IS JUST TO...', 'TO', 1, 2) FROM DUAL;
-- 처음부터 찾기 시작해서 두번째로 나오는 TO의 위치를 찾아라
SELECT INSTR(PHONE, '-', 1, 2) FROM MEMBER;
SELECT INSTR(PHONE, '-', 1, 2) - INSTR(PHONE, '-') - 1 FROM MEMBER;
SELECT SUBSTR(PHONE, 5, INSTR(PHONE, '-', 1, 2) - INSTR(PHONE, '-') - 1) 
FROM MEMBER;

SELECT LENGTH('WHERE YOU ARE') FROM DUAL;
-- 문자의 길이
SELECT PHONE, LENGTH(REPLACE(PHONE, '-', '')) FROM MEMBER;

SELECT ASCII('A') FROM DUAL;
-- 코드 값을 반환하는 함수

SELECT CHR(65) FROM DUAL;
-- 코드 값으로 문자를 반환하는 함수

----- 숫자 함수 -----------------------------------------------

SELECT ABS(35), ABS(-35) FROM DUAL;
-- 절대값을 구하는 함수

SELECT SIGN(35), SIGN(-35), SIGN(0) FROM DUAL;
-- 양수/음수를 알려주는 함수(양수 : 1, 음수 : -1, 0 : 0)

SELECT ROUND(34.4567), ROUND(34.5567) FROM DUAL;
-- 숫자를 반올림 하는 함수
SELECT ROUND(10.3456, 2), ROUND(10.3456, 3) FROM DUAL;
-- 뒤에 오는 인자는 소수점자리수

SELECT TRUNC(17/5), MOD(17, 5) FROM DUAL;
-- TRUNC는 몫, MOD는 나머지를 구하는 함수

SELECT POWER(5, 3), SQRT(25) FROM DUAL;
-- POWER는 제곱, SQRT는 제곱근을 구하는 함수

----- 날짜 함수 -----------------------------------------------

SELECT SYSDATE, CURRENT_DATE, SYSTIMESTAMP, CURRENT_TIMESTAMP
    FROM DUAL;
-- Oracle 서버의 시간대를 사용할때는 : SYSDATE, Session의 시간대를 사용할때는 CURRENT

ALTER SESSION SET NLS_DATE_FORMAT = 'YYYY-MM-DD HH24:MI:SS';
-- 날짜와 시간의 표시형식을 바꾸는 함수
SELECT SYSDATE, CURRENT_DATE FROM DUAL;

ALTER SESSION SET TIME_ZONE = '09:00'
-- 표준 시간대를 바꿀 수 있는 함수(한국은 그리니치 천문대를 기준으로 9시간 OVER)

SELECT EXTRACT(YEAR FROM SYSDATE) FROM DUAL;
SELECT EXTRACT(MONTH FROM SYSDATE) FROM DUAL;
SELECT EXTRACT(DAY FROM SYSDATE) FROM DUAL;
-- 날짜 추출 함수
SELECT * FROM MEMBER 
    WHERE EXTRACT(MONTH FROM REGDATE) IN (2,3,11,12);

SELECT * FROM MEMBER WHERE ADD_MONTHS(SYSDATE, -6) < REGDATE;
-- 날짜를 누적하는 함수

SELECT * FROM MEMBER
    WHERE MONTHS_BETWEEN(SYSDATE, REGDATE) < 6;
-- 날짜의 차이를 알아내는 함수

SELECT NEXT_DAY(SYSDATE, '수요일') FROM DUAL;
SELECT NEXT_DAY(SYSDATE, '수') FROM DUAL;
SELECT NEXT_DAY(SYSDATE, '4') FROM DUAL;
-- 다음에 오는 날짜를 알아내는 함수(일요일부터 토요일 순으로 1 부터 7)

SELECT LAST_DAT(SYSDATE) FROM DUAL;
-- 마지막 날짜를 알아내는 함수
SELECT LAST_DAY(ADD_MONTHS(SYSDATE, 1)) FROM DUAL;
-- 1개월 후의 마지막 날짜는?

SELECT ROUND(SYSDATE, 'CC'), TRUNC(SYSDATE, 'CC') FROM DUAL; --세기
SELECT ROUND(SYSDATE, 'YEAR'), TRUNC(SYSDATE, 'YEAR') FROM DUAL; --연도
SELECT ROUND(SYSDATE, 'Q'), TRUNC(SYSDATE, 'Q') FROM DUAL; --분기
SELECT ROUND(SYSDATE, 'MONTH'), TRUNC(SYSDATE, 'MONTH') FROM DUAL; -- 달
SELECT ROUND(SYSDATE, 'W'), TRUNC(SYSDATE, 'W') FROM DUAL; -- 주
SELECT ROUND(SYSDATE, 'DAY'), TRUNC(SYSDATE, 'DAY') FROM DUAL; -- 날
SELECT ROUND(SYSDATE, 'HH'), TRUNC(SYSDATE, 'HH') FROM DUAL; -- 시간
SELECT ROUND(SYSDATE, 'MI'), TRUNC(SYSDATE, 'MI') FROM DUAL; -- 분
-- 지정한 단위로 날짜를 ROUND는 반올림 TRUNC는 내림



COMMIT;
    
SELECT * FROM MEMBER;

SELECT * FROM NOTICE;
