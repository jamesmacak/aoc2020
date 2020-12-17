from sys import argv

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