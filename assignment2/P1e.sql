SELECT count(*)
FROM (
	SELECT x.docid, sum(x.count)
	FROM frequency x
	GROUP BY x.docid
	HAVING sum(x.count)>300
) x;
