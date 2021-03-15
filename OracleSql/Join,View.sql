---------- JOIN -------------------------------------------
UPDATE NOTICE SET WRITER_ID = 'joo' WHERE ID = 7;
COMMIT;

-- INNER JOIN --
SELECT * FROM MEMBER INNER JOIN NOTICE ON MEMBER.ID = NOTICE.WRITER_ID;
-- 표준 조인 문장

-- OUTER JOIN --
SELECT * FROM NOTICE N LEFT OUTER JOIN MEMBER M ON N.WRITER_ID = M.ID;
SELECT * FROM NOTICE N RIGHT OUTER JOIN MEMBER M ON N.WRITER_ID = M.ID;
SELECT * FROM NOTICE N FULL OUTER JOIN MEMBER M ON N.WRITER_ID = M.ID;

-- SELF JOIN --
-- 데이터가 서로 포함 관계를 가지는 경우
SELECT M.*, B.NAME BOSS_NAME FROM MEMBER M
LEFT OUTER JOIN MEMBER B ON B.ID = M.BOSS_ID;
-- 참조하고 싶은 데이터가 같은 데이블 내에 있는 경우 사용
-- 테이블명을 그냥 둘 다 쓰면 에러가 나기 때문에 별칭을 줘서 사용
-- JOIN 하는 경우에는 항상 주인공이 누구인지를 찾아라!

---------- ORACLE JOIN -------------------------------------------
SELECT N.*, M.NAME WRITER_NAME
FROM NOTICE N JOIN MEMBER M ON M.ID = N.WRITER_ID;

SELECT N.*, M.NAME WRITER_NAME
FROM NOTICE N, MEMBER M WHERE M.ID = N.WRITER_ID; -- INNER


SELECT N.*, M.NAME WRITER_NAME
FROM NOTICE N LEFT OUTER JOIN MEMBER M ON M.ID = N.WRITER_ID;

SELECT N.*, M.NAME WRITER_NAME
FROM NOTICE N, MEMBER M WHERE M.ID(+) = N.WRITER_ID; -- OUTER


SELECT N.*, M.NAME WRITER_NAME
FROM NOTICE N, MEMBER M WHERE M.ID(+) = N.WRITER_ID(+); -- FULL은 에러


SELECT N.*, M.NAME WRITER_NAME
FROM NOTICE N CROSS JOIN MEMBER M; 

SELECT N.*, M.NAME WRITER_NAME
FROM NOTICE N, MEMBER M; -- CROSS 곱하기로 그냥 만듦

---------- UNION -------------------------------------------
-- 관련이 없더라도 합치고 싶을 때 UNION을 사용한다.
-- 컬럼이 늘어나는 것이 아니고 레코드를 합치는 작업이다.
SELECT ID, NAME FROM MEMBER
    UNION
SELECT WRITER_ID, TITLE FROM NOTICE;
-- UNION은 값이 겹치는 레코드는 삭제한다.
-- 삭제 되는 것 없이 모든 데이터를 합치고 싶을 때는 UNION ALL을 쓰면 된다

SELECT ID, NAME FROM MEMBER
    MINUS
SELECT WRITER_ID, TITLE FROM NOTICE;
-- 주인공인 테이블에서 뒤의 테이블과 공통되는 분모를 빼서 출력한다.

SELECT ID, NAME FROM MEMBER
    INTERSECT
SELECT WRITER_ID, TITLE FROM NOTICE;
-- 공통 분모만 남긴다.

SELECT ID, NAME FROM MEMBER WHERE ID LIKE '%i%'
    UNION
SELECT ID, NAME FROM MEMBER WHERE ID LIKE '%o%';
-- 하나의 테이블로도 가능!!!

---------- CREATE VIEW -------------------------------------------
-- 데이터는 쪼개져서 저장이 되어 있다가 우리가 필요에 의해서 JOIN하여 합쳐서 사용할 수 있다
-- 하지만 매 작업마다 데이터를 합치는 작업을 하면 귀찮잖아?
-- 그래서 데이터를 합치는 작업을 마친 테이블의 쿼리문을 미리 만들어 놓은 것이 VIEW 되겠다.
-- 저장은 원래 처럼 쪼개져서 되고, 복잡한 서브쿼리를 읽지 않아도 
-- 지정해 놓은 VIEW 이름 하나로 불러올 수 있으니 얼마나 좋냐

CREATE VIEW NOTICE_VIEW AS
SELECT N.ID, N.TITLE, N.WRITER_ID, M.NAME WRITER_NAME, COUNT(C.ID) COMMENT_CNT
FROM MEMBER M
RIGHT OUTER JOIN NOTICE N ON M.ID = N.WRITER_ID
LEFT OUTER JOIN "COMMENT" C ON N.ID = C.NOTICE_ID
GROUP BY N.ID, N.TITLE, N.WRITER_ID, M.NAME;
COMMIT;

SELECT * FROM NOTICE_VIEW;

---------- DATE DICTIONARY -------------------------------------------
-- 데이터의 정보가 저장되어 있는 공간(ex. 사용자 정보, 권한, 테이블 정보, 제약조건 등..)
-- 딕셔너리 안의 테이블은 직접 사용할 수 없다. 다만 뷰 형태로 제공 하고 있다.

SELECT * FROM DICT;

SELECT * FROM USER_TABLES;
SELECT * FROM USER_TAB_COLUMNS;
SELECT * FROM USER_TAB_COLUMNS WHERE TABLE_NAME = 'MEMBER';
-- 요즘은 굳이 딕셔너리를 뒤지는 일은 별로 없단다




























