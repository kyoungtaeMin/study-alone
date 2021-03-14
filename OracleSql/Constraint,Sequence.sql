----- Constraint ---------------------------------------
----- Domain Constraint ---------------------------------------
-- column 단위의 유효한 값에 범위를 잡아주는 것이 도메인 제약 조건이다.
-- NOT NULL : 사용자가 값을 반드시 입력해야 하는 데이터에 사용
-- DEFAULT : 값을 반드시 입력해야 하지만 입력하지 않는 경우에 알아서 값을 가지게 할때 사용
--CHECK : 도메인 범위를 잘 체크하도록 사용
---------- NOT NULL, DEFAULT Constraint ------------------------
INSERT INTO notice (
    id,
    title,
    writer_id
) VALUES (
    13,
    '13번째 게시글',
    'ma'
);
SELECT * FROM NOTICE ORDER BY ID DESC;

---------- CHECK Constraint ------------------------------------
-- 값의 범위나 값의 형식이 맞지 않으면 입력이 되지 않도록 제약을 건다.
-- 테이블을 생성할 때 적용 방법
-- CREATE TABLE TEST
-- (
--     ID VARCHAR2(50) NULL,
--     PHONE VARCHAR2(200) CHECK(PHONE LIKE '010-%-____') NOT NULL,
--     EMAIL VARCHAR2(500) NULL
-- );
-- 테이블을 생성 한 후에 적용 방법
-- ALTER TANLE TEST ADD CONSTRAINT CK_TEST_PHONE 
-- CHECK(PHONE LIKE '010-%-____');
INSERT INTO MEMBER(ID,PWD, NAME, PHONE, GENDER) 
VALUES ('minjoo', '4040', '김민주', '010-4561-7854', '여성');
COMMIT;

-- CHECK 제약조건을 좀 더 정밀하게 잡아주기 위해서 정규식을 사용한다.
ALTER TABLE MEMBER
DROP CONSTRAINT MEMBER_PHONE_CHK1;

SELECT * FROM user_constraints
WHERE TABLE_NAME = 'MEMBER';

ALTER TABLE MEMBER
ADD CONSTRAINT MEMBER_PHONE_CHK1 
CHECK(REGEXP_LIKE(PHONE, '^01[01]-\d{3,4}-\d{4}$'));

----- ENTITY Constraint ---------------------------------------
-- PRIMARY KEY 와 UNIQUE : 중복된 레코드가 없도록 제한한다.
-- PRIMARY KEY : 식별키가 되는 컬럼에 사용. NULL도 안되고 중복도 안된다.
-- UNIQUE : NULL은 허용하나 중복은 안된다.

---------- PRIMARY KEY, UNIQUE 적용 ----------------------------
-- 테이블 생성시 사용
-- CREATE TABLE TEST
-- (
--     ID NUMBER,
--     TITLE VARCHAR2(300) NOT NULL,
--     WRITER_ID VARCHAR2(50) NOT NULL,

--     CONSTRAINT TEST_ID_PK PRIMARY KEY(ID),
--     CONSTRAINT TEST_WRITER_ID_UK UNIQUE(WRITER_ID)
-- );

-- 테이블 생성한 후에 적용 할때
-- ALTER TABLE NOTICE
-- ADD CONSTRAINT NOTICE_ID_PK PRIMARY KEY(ID);
-- ALTER TABLE NOTICE
-- ADD CONSTRAINT NOTICE_WRITER_ID_UK UNIQUE(WRITER_ID);

---------- SEQUENCE ------------------------------------
-- 중복이 되면 안되고 계속해서 증가해야한다.
-- 레코드 입력할 때매다 몇번째부터 해야되지? 하면서 확인하려면 귀찮잖아?
-- 그래서 다음 값을 쉽게 얻어낼 수 있으면 편하니까 준비하는 것이 SEQUENCE 되겠다.
INSERT INTO NOTICE(ID, TITLE, WRITER_ID)
VALUES(NOTICE_ID_SEQ.NEXTVAL, '시퀀스 예제', 'minjoo');

INSERT INTO NOTICE(TITLE, WRITER_ID)
VALUES('시퀀스 예제2', 'minjoo');
commit;
SELECT NOTICE_ID_SEQ.NEXTVAL FROM DUAL;
-- 시퀀스 목록에서 시퀀스 생성, 수정
-- 테이블 수정 ID열 에서 시퀀스 연결