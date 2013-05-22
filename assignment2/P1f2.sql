SELECT t.docid
FROM
(SELECT *
FROM frequency
WHERE frequency.term="transactions") t
JOIN
(SELECT *
FROM frequency
WHERE frequency.term="world") w
ON t.docid=w.docid
;
