-- 코드를 입력하세요
SELECT B.USER_ID, NICKNAME, CONCAT(CITY, ' ', STREET_ADDRESS1, ' ', STREET_ADDRESS2) AS '전체주소',
       CONCAT(SUBSTRING(TLNO,1,3),'-', SUBSTRING(TLNO,4,4),'-',SUBSTRING(TLNO,8,4)) AS '전화번호'
FROM USED_GOODS_BOARD AS A JOIN USED_GOODS_USER AS B ON A.WRITER_ID = B.USER_ID
GROUP BY B.USER_ID
HAVING COUNT(*) >= 3
ORDER BY B.USER_ID DESC