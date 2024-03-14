import numpy
import logging
logging.basicConfig(level=logging.INFO,format="%(message)s")
def linear_algebra():
    N = int(input())
    A = numpy.array([input().split() for _ in range(N)], float)
    logging.info(round(numpy.linalg.det(A), 2))
