SELECT sum(A.value*B.value)
FROM
(SELECT *
FROM A
WHERE A.row_num=2) A
JOIN
(SELECT *
FROM B
WHERE B.col_num=3) B
ON A.col_num=B.row_num
;