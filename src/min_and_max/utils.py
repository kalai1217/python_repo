import logging
logging.basicConfig(level=logging.INFO,format="%(message)s")
import numpy
def min_and_max():
    N, M = map(int, input().split())
    storage = numpy.array([input().split() for _ in range(N)], int)
    logging.info(numpy.max(numpy.min(storage, axis=1), axis=0))
