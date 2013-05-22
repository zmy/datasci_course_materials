SELECT sum(A.count*B.count)
FROM
(SELECT *
FROM frequency
WHERE frequency.docid="10080_txt_crude") A
JOIN
(SELECT *
FROM frequency
WHERE frequency.docid="17035_txt_earn") B
ON A.term=B.term
;