import logging
logging.basicConfig(level=logging.INFO,format="%(message)s")
def merge_the_tools():
    string, k = input(), int(input())
    m=0
    l=[]
    for i in range(len(string)//k):
        l.append(string[m:m+k])
        m+=k
    #print(l)
    for i in l:
        # print(list(i))
        # print(dict.fromkeys(list(i)))
        # print(dict.fromkeys(list(i), 1))
        # print(list(dict.fromkeys(list(i), 1)))
        logging.info("".join(list(dict.fromkeys(list(i)))))
