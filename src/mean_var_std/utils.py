import numpy as np
import logging
logging.basicConfig(level=logging.INFO,format="%(message)s")
def mean_var_std():
    n, _ = map(int, input().split())
    x = np.array([input().split() for _ in range(n)], int)
    logging.info(np.mean(x, axis=1))
    logging.info(np.var(x, axis=0))
    logging.info(np.mean(round(np.std(x), 11)))
