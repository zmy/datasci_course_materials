import MapReduce
import json
import sys


# Map function
# mr - MapReduce object
# data - json object formatted as a string
def mapper(mr, data):
    data = json.loads(data+'}', encoding='latin-1')
    for (doc_id, txt) in data:
        for key in txt:
            value = doc_id
            # output (key, value) pair (only for mapper)
            mr.emit_intermediate(key, value)


# Reduce function
# mr - MapReduce object
# key - key generated from map phse, associated to list_of_values
# list_of_values - values generated from map phase, associated to key
def reducer(mr, key, list_of_values):
    # output item (only for reducer)
    mr.emit({key: list_of_values})


def main():
    # Assumes first argument is a file of json objects formatted as strings, 
    #one per line.
    MapReduce.execute(open(sys.argv[1]), mapper, reducer)


if __name__ == '__main__':
    main()
