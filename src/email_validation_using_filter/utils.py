import logging
logging.basicConfig(level=logging.INFO,format="%(message)s")
import re
def fun(s):
    # return True if s is a valid email, else return False
       # defining the patterns
    pattern = re.compile("^[\\w-]+@[0-9a-zA-Z]+\\.[a-z]{1,3}$")
    return pattern.match(s)
def filter_mail(emails):
    return list(filter(fun, emails))

def email_validation_using_filter():
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())
    filtered_emails = filter_mail(emails)
    filtered_emails.sort()
    logging.info(filtered_emails)
