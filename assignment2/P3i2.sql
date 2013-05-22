SELECT x.docid, sum(x.count) as value
FROM
(
SELECT *
FROM frequency
WHERE frequency.term='washington'
UNION
SELECT *
FROM frequency
WHERE frequency.term='taxes'
UNION
SELECT *
FROM frequency
WHERE frequency.term='treasury'
) x
GROUP BY x.docid
ORDER BY value
;