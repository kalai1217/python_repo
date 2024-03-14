import logging
from itertools import combinations
logging.basicConfig(level=logging.INFO,format="%(message)s")
def iterables_and_iterators():
    l = int(input())
    s = input().split()
    c = int(input())
    length = len(list(combinations(s, c)))
    data = 0
    for i in combinations(s, c):
        if "a" in i:
            data += 1
    logging.info(float("{:.12f}".format(data / length)))
