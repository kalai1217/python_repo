import logging
logging.basicConfig(level=logging.INFO,format="%(message)s")
def string_formatted():
    # your code goes here
    n = int(input())
    spacing=len("{0:b}".format(n))
    for i in range(1,n+1):
        logging.info("{0:{s}d} {0:{s}o} {0:{s}X} {0:{s}b}".format(i,s=spacing))

