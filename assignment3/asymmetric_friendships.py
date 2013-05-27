__author__ = 'moony'
import MapReduce
import sys


mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line


def mapper(record):
    # key: document identifier
    # value: document contents
    mr.emit_intermediate(record[0], record[1])
    mr.emit_intermediate(record[1], record[0])


def reducer(key, list_of_values):
    count = {}
    for name in list_of_values:
        count[name] = count.get(name, 0) + 1
    for name in list_of_values:
        if count[name] == 1:
            mr.emit((key, name))


# Do not modify below this line
# =============================
if __name__ == '__main__':
    inputdata = open(sys.argv[1])
    mr.execute(inputdata, mapper, reducer)