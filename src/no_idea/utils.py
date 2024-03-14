import logging
logging.basicConfig(level=logging.INFO,format="%(message)s")
def no_idea():
    happiness = 0
    n, m = map(int, input().strip().split(' '))
    elements_arr = list(map(int, input().strip().split(' ')))
    A = set(map(int, input().strip().split(' ')))
    B = set(map(int, input().strip().split(' ')))
    for i in elements_arr:
        if i in A:
            happiness += 1
        elif i in B:
            happiness -= 1
    logging.info(happiness)