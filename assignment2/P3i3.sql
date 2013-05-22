
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
;