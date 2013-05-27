__author__ = 'moony'
import MapReduce
import sys


mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line


def mapper(record):
    # key: document identifier
    # value: document contents
    matrix = record[0]
    i = record[1]
    j = record[2]
    value = record[3]
    if matrix == 'a':
        for k in range(0, 5):
            mr.emit_intermediate((i, k), (j, value))
    else:
        for k in range(0, 5):
            mr.emit_intermediate((k, j), (i, value))


def reducer(key, list_of_values):
    i = key[0]
    j = key[1]
    sum = 0
    value = {}
    for (k, v) in list_of_values:
        if k in value:
            sum += value[k] * v
        else:
            value[k] = v
    mr.emit((i, j, sum))


# Do not modify below this line
# =============================
if __name__ == '__main__':
    inputdata = open(sys.argv[1])
    mr.execute(inputdata, mapper, reducer)