import logging
logging.basicConfig(level=logging.INFO,format="%(message)s")
from datetime import datetime
import os
import math
import random
import re
import sys
def time_delta():
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    t = int(input())
    for t_itr in range(t):
        t1 = input()
        t2 = input()
        format_ = '%a %d %b %Y %H:%M:%S %z'
        t1 = datetime.strptime(t1, format_)
        t2 = datetime.strptime(t2, format_)
        delta_seconds = abs((t1 - t2).total_seconds())
        fptr.write(str(int(delta_seconds)) + '\n')
    fptr.close()
