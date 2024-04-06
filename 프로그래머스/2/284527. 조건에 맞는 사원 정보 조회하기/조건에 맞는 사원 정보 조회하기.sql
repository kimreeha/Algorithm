-- 코드를 작성해주세요
SELECT B.SCORE, A.EMP_NO, A.EMP_NAME, A.POSITION, A.EMAIL
FROM HR_EMPLOYEES AS A JOIN (SELECT EMP_NO, SUM(SCORE) AS SCORE 
                             FROM HR_GRADE 
                             WHERE YEAR = 2022 
                             GROUP BY EMP_NO) AS B USING(EMP_NO)
ORDER BY B.SCORE DESC LIMIT 1
                             
