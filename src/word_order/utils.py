import logging
logging.basicConfig(level=logging.INFO,format="%(message)s")
def word_order():
    n_ish = int(input())
    counter_dict = {}
    words_list = []
    for i in range(n_ish):
        word = input()
        words_list.append(word)
        if word in counter_dict:
            counter_dict[word] += 1
        else:
            counter_dict[word] = 1
    logging.info(len(counter_dict))
    logging.info(' '.join([str(counter_dict[word]) for word in counter_dict]))