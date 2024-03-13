import logging
def runnerup_score():
    logging.basicConfig(level=logging.INFO,format="%(message)s")
    n = int(input())
    arr = list(map(int, input().split()))
    sorted_array = sorted(arr)
    n = len(sorted_array)
    largest = sorted_array[0]
    for i in range(n):
        if (sorted_array[i] > largest):
            largest = sorted_array[i]
    second_largest = 0
    for i in range(n - 2, -1, -1):
        if (sorted_array[i] != largest):
            second_largest = sorted_array[i]
            break
    logging.info(second_largest)
    return second_largest
