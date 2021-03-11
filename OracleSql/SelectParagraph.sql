----- SELECT PARAGRAPH ----------------------------------------

---------- ORDER BY -------------------------------------------

SELECT * FROM MEMBER ORDER BY AGE DESC;
-- 나이를 내림차순으로 정렬(dfault는 ASC)

SELECT * FROM MEMBER WHERE NAME LIKE '박%' ORDER BY AGE ASC;
-- 박씨 성을 가진 회원들을 나이의 오름차순으로 정렬하라

SELECT * FROM NOTICE ORDER BY HIT DESC, REGDATE DESC;
-- NOTICE를 조회수 와 등록일 모두 내림차순으로 정렬하라

---------- 집계 함수 -------------------------------------------
SELECT COUNT(TITLE) FROM NOTICE;
-- TITLE의 개수를 알려준다. (NULL값인 행은 세지 않는다)

SELECT WRITER_ID, COUNT(TITLE) COUNT FROM NOTICE GROUP BY WRITER_ID;

SELECT WRITER_ID, COUNT(TITLE) COUNT 
FROM NOTICE 
--WHERE
GROUP BY WRITER_ID
ORDER BY COUNT DESC;

-- 실행순서 : FROM > CONNECT BY > WHERE > GROUP BY 
--              > HAVING > SELECT > ORDER BY
-- SELECT절에서 ALIAS한 별칭은 HAVING절 부터는 사용할 수 없다.

SELECT SUM(HIT) FROM NOTICE; -- 합계
SELECT AVG(HIT) FROM NOTICE; -- 평균
SELECT MIN(HIT) FROM NOTICE; -- 최소값
SELECT MAX(HIT) FROM NOTICE; -- 최대값

---------- HAVING 절 -------------------------------------------
SELECT WRITER_ID, COUNT(N.ID) FROM NOTICE N
WHERE COUNT(N.ID) < 2
GROUP BY WRITER_ID; --에러
-- WHERE절 에서는 집계함수를 사용할 수 없다. 이런 경우는 HAVING절로 변경하여 사용한다.
SELECT WRITER_ID, COUNT(N.ID) FROM NOTICE N
GROUP BY WRITER_ID
HAVING COUNT(N.ID) < 2; -- 정상적으로 분석값 반환

---------- ROW_NUMBER(), RANK(), PARTITION ---------------------------------
SELECT ROW_NUMBER() OVER (ORDER BY HIT), ID, TITLE, WRITER_ID, REGDATE, HIT
FROM NOTICE;
--WHERE 절 쯤에서 만들어 지기 때문에 ORDER BY에 적용되지 않는다.
--GROUP BY
--HAVING
--ORDER BY HIT;
-- ROWNUM을 함수화 시켜놓은 ROW_NUMBER() OVER를 사용하여 정렬 시킬 수 있다.

SELECT RANK() OVER (ORDER BY HIT), ID, TITLE, WRITER_ID, REGDATE, HIT
FROM NOTICE;
-- 정렬된 상태로 등수를 매기는 함수
SELECT DENSE_RANK() OVER (ORDER BY HIT), ID, TITLE, WRITER_ID, REGDATE, HIT
FROM NOTICE;
-- 공동 순위에 다음에 오는 등수를 건너 뛰지 않고 바로 다음 등수로 매기는 함수

SELECT ROW_NUMBER() OVER (PARTITION BY WRITER_ID ORDER BY HIT DESC),
ID, TITLE, WRITER_ID, REGDATE, HIT
FROM NOTICE;
-- 지정한 컬럼을 기준으로 그룹을 만들어 그 안에서 등수를 매기는 함수

---------- SUB QEURY -------------------------------------------
SELECT * FROM NOTICE WHERE ROWNUM BETWEEN 1 AND 10;

SELECT * FROM NOTICE 
ORDER BY REGDATE DESC
WHERE ROWNUM BETWEEN 1 AND 10; -- ERORR 그럼 어떻게해?

SELECT * FROM (SELECT * FROM NOTICE ORDER BY REGDATE DESC) 
WHERE ROWNUM BETWEEN 1 AND 10;
-- 원하는 결과를 끌어내기 위해 식의 순서를 바꿔야 할 때 사용 할 수 있다.
-- 평생 쓸꺼같으니까 연습 많이 하자....

SELECT * FROM MEMBER WHERE AGE >= 30;

SELECT * FROM MEMBER 
WHERE AGE >= (SELECT AVG(AGE) FROM MEMBER);
-- 먼저 평균나이를 구해야 하니까 구하고 나서 다음 조건 진행

---------- JOIN -------------------------------------------

SELECT * FROM MEMBER;

SELECT * FROM NOTICE;