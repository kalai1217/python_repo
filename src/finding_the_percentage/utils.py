import logging
def finding_the_percentage():
    logging.basicConfig(level=logging.INFO, format='%(message)s')
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    avg=sum(student_marks[query_name])/len(student_marks[name])
    logging.info(avg)