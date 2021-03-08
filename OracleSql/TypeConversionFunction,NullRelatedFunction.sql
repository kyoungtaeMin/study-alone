----- 형식 변환 함수 ----------------------------------------

SELECT TO_CHAR(12345678, '$99,999,999,999.99') FROM DUAL;
-- 숫자 길이보다 더 큰 길이를 가지고 있어야 한다
--9 : 숫자, 0 : 빈자리를 채우는 문자, $는 앞에 표시
-- (천 단위 구분자 표시는  ,로 한다. 소수점 표시는 .으로 한다.
SELECT TO_CHAR(123) || 'HELLO' FROM DUAL;

SELECT TO_CHAR(12345678, '99999999') FROM DUAL;
SELECT TO_CHAR(1234567, '09,999,999,999') FROM DUAL;
-- 자릿수가 모자랄 때에는 남은 자리 수 만큼 앞에 공백으로 채워진다.
-- 공백이 싫을 때는 0을 입력해주면 0으로 채워진다.

SELECT TRIM(TO_CHAR(1234567.45, '9,999,999,999.99')) || '원' FROM DUAL;
-- 공백을 없애는 함수 TRIM을 중복 사용하여 공백을 없앨 수 있다.

SELECT TO_CHAR(SYSDATE, 'YYYY-MM-DD HH24:MI:SS') FROM DUAL;
-- 날짜형식를 문자형식로 변환

SELECT TO_DATE('2021-03-07 16:13:22', 'YYYY-MM-DD HH24:MI-SS') FROM DUAL;
-- 문자형식을 날짜형식으로 변환

SELECT TO_TIMESTAMP('2021-03-07 16:13:22', 'YYYY-MM-DD HH24:MI-SS') FROM DUAL;
-- 문자형식을 숫자형식으로 변환

SELECT TO_NUMBER('2021') FROM DUAL;
-- 문자형식을 숫자형식으로 변환
SELECT TO_NUMBER('6') + 4 FROM DUAL;

----- NULL 관련 함수 ----------------------------------------

SELECT NVL(AGE, 0) FROM MEMBER;
-- 반환 값이 NULL일 경우에 대체 값을 제공하는 함수(NULL, 대체값)

SELECT TRUNC(NVL(AGE, 0)/10)*10 FROM MEMBER;
-- MEMBER의 AGE의 NULLL값을 0으로 대체하고 10으로 나눠 소수점을 날리고 10을 곱해라

SELECT NVL2(AGE, TRUNC(AGE/10)*10, 0) FROM MEMBER;
-- NVL은 모든 행에서 연산이 이루어 지지만 NVL2는 NULL이 아닐 때만 연산 가능
-- 결과는 똑같이 보이지만 연산이 이루어지는 횟수가 다름

SELECT NULLIF(AGE, 35) FROM MEMBER;
-- 35를 NULL 값으로 반환해라. 지정한 값을 NULL로 변환

----- 기타 함수 ----------------------------------------

SELECT DECODE(GENDER, '남성', 1, 2) FROM MEMBER;
-- GENDER에서 '남성'이면 1로 반환하고 그렇지 않으면 2로 반환해라

SELECT DECODE(SUBSTR(PHONE, 1, 3),
            '011', 'SK',
            '016', 'KT', '기타') FROM MEMBER;
-- PHONE에서 1번째부터 3문자를 잘라라. 
-- 그리고 거기서 '011'은 'SK'로 '016'은 'KT'로 변환하고 나머지는 '기타'로 변환해라
-- DECODE(기준값, 비교값, 출력값, 비교값, 출력값, 기본값)


SELECT AGE FROM MEMBER;