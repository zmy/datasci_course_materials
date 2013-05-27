__author__ = 'moony'
import MapReduce
import sys


mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line


def mapper(record):
    # key: document identifier
    # value: document contents
    mr.emit_intermediate(record[1], record)


def reducer(key, list_of_values):
    for line_item in list_of_values:
        if line_item[0] == 'line_item':
            for order in list_of_values:
                if order[0] == 'order':
                    mr.emit(order + line_item)


# Do not modify below this line
# =============================
if __name__ == '__main__':
    inputdata = open(sys.argv[1])
    mr.execute(inputdata, mapper, reducer)