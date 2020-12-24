from sys import argv

script, part, input_file = argv

with open(input_file, 'r') as fh:
    geography = fh.readlines()
    geography = [line.strip() for line in geography]

def load_slopes(part):
    if part == '1':
        slopes = [(3,1)]
    if part == '2':
        slopes = [(1,1), (3,1), (5,1), (7,1), (1,2)]
    return slopes

def send_it(slopes):
    total = 1
    for slope in slopes:
        trees = 0
        y, x = 0, 0
        while (y + slope[1]) < len(geography):
            y += slope[1]
            x += slope[0]
            
            point = geography[y][x % len(geography[y])]
            if point == '#':
                trees += 1
        total *= trees
    return(total)

def p1():
    slopes = load_slopes('1')
    print(send_it(slopes))

def p2():
    slopes = load_slopes('2')
    print(send_it(slopes))

if __name__ == "__main__":
    if part == 'p1':
        p1()
    if part == 'p2':
        p2()