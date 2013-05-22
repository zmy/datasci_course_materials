SELECT count(*)
FROM (
SELECT x.docid
FROM frequency x
WHERE x.term="transactions"
INTERSECT
SELECT y.docid
FROM frequency y
WHERE y.term="world"
) z;
