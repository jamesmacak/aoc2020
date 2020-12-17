from sys import argv

script, part, input_file = argv

with open(input_file, 'r') as fh:
    batch = {}
    for line in fh:
        if line == '\n':
            break
        else:
            k, v = line.split(':')
            batch[k] = v.strip()
        

def p1():
    print(batch)

def p2():
    pass

if __name__ == "__main__":
    if part == 'p1':
        p1()
    if part == 'p2':
        p2()