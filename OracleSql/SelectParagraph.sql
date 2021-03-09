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

SELECT * FROM MEMBER;

SELECT * FROM NOTICE;