from sys import argv
import time

t0 = time.time()
print(t0)

script, part, input_file = argv

with open(input_file, 'r') as fh:
    batch = fh.readlines()

def p1():
    pass

def p2():
    pass

if __name__ == "__main__":
    if part == 'p1':
        p1()
    if part == 'p2':
        p2()

t1 = time.time()
print(t1-t0)