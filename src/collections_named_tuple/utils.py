from collections import namedtuple
import logging
logging.basicConfig(level=logging.INFO,format="%(message)s")
def collections_named_tuple():
    input_ = int(input())
    my_fields = input().split()
    total_marks = 0
    for _ in range(input_):
        students = namedtuple('my_student', my_fields)
        MARKS, CLASS, NAME, ID = input().split()
        my_student = students(MARKS, CLASS, NAME, ID)
        total_marks += int(my_student.MARKS)
    logging.info((total_marks / input_))

