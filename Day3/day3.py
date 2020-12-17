from sys import argv
import numpy as np

script, part, input_file = argv

with open(input_file, 'r') as fh:
    geology = fh.readlines()

def move(x, y, X, Y, horizon, geology): # X right, Y down
    x = (x + X) % (len(horizon) - 1)
    # print(f"About to move, length of geology: {str(len(geology))}")
    if y + Y <= len(geology):
        y = y + Y
    else:
        y = y

    return x, y

def p1():
    #TODO
    # Convert 'working' into an endless map (as needed) going right 'geology'
    #  geology -> endless (x + 3) % 'hoz length
    # Consider 2D array
    # Define 'move' function (right 3, down 1)
    # Count number of trees
    # print(geology)

    slopes = int(input("Enter number of slopes: "))
    total_hit = 1
    for i in range(slopes):
        X = int(input("\nSet X step: "))
        Y = int(input("Set Y step: "))
        trees = 0
        x, y = 0, 0 # Is 'y' needed?
        for row in geology:
            horizon = list(geology[y]) # think objects
            if horizon[x] == '#':
             trees += 1
            x, y = move(x, y, X, Y, horizon, geology)
        # print(horizon)

        print(f"I hit {trees} trees.")
        total_hit = total_hit * trees
    print(f"I hit a total of {total_hit} trees.")


def p2():
    # trees = 1
    # slopes = int(input("How many slopes: "))

    # for slope in range(slopes):
    #     trees_hit = 0
    #     X = int(input("\nSet X step: "))
    #     Y = int(input("Set Y step: "))
    #     x, y = 0, 0
    #     for y in range(y, len(geology) - 1, Y):
    #         horizon = list(geology[y]) # think objects
    #         print(f"x {x}, y {y}")
    #         if horizon[x] == '#':
    #             trees_hit += 1
                
    #         x, y = move(x, y, X, Y, horizon)
    #         # print(horizon)
    #     trees = trees * trees_hit
    #     print(f"{trees_hit} trees_hit, {trees} trees")

    # trees = 0
    # x, y = 0, 0
    # mountain = np.zeros([31, 323], str)
    # for i, row in enumerate(geology):
    #     horizon = list(row)
    #     for j, col in enumerate(horizon):
    #         mountain[i, j - 1] = col
    # print(mountain)

    # print(f"I hit {trees} trees over {slopes} slopes.")
    pass

if __name__ == "__main__":
    if part == 'p1':
        p1()
    if part == 'p2':
        p2()