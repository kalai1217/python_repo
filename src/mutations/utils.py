import logging
logging.basicConfig(level=logging.INFO,format="%(message)s")
def mutate_string():
    string = input()
    position,character = input().split()
    pos=int(position)
    mutant=string[:pos]+character+string[pos+1:]
    logging.info(mutant)
    return mutant
