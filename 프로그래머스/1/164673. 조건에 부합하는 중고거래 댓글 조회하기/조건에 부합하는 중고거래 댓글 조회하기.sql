-- 코드를 입력하세요
SELECT A.TITLE, A.BOARD_ID, B.REPLY_ID, B.WRITER_ID, B.CONTENTS, DATE_FORMAT(B.CREATED_DATE, '%Y-%m-%d') AS CREATED_DATE
FROM USED_GOODS_BOARD AS A, USED_GOODS_REPLY AS B
WHERE A.BOARD_ID = B.BOARD_ID 
AND (YEAR(A.CREATED_DATE) = 2022 AND MONTH(A.CREATED_DATE) = 10)
ORDER BY B.CREATED_DATE, A.TITLE