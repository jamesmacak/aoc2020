from sys import argv
import re

script, part, input_file = argv

with open(input_file, 'r') as fh:
    passwords = fh.readlines()

def p1():
    valid_pw_count = 0
    for line in passwords:
        line_re = re.findall(r"\w+", line)
        min, max, letter, pw = int(line_re[0]), int(line_re[1]), line_re[2], line_re[3]
        frequency = pw.count(letter)
        if min <= frequency <= max:
            valid_pw_count += 1
    
    print(f"{valid_pw_count} of {len(passwords)} passwords are valid.")

def p2():
    valid_pw_count = 0
    for line in passwords:
        line_re = re.findall(r"\w+", line)
        pos1, pos2, letter, pw = int(line_re[0]), int(line_re[1]), line_re[2], line_re[3]
        if (letter == pw[pos1 - 1]) ^ (letter == pw[pos2 - 1]):
            valid_pw_count += 1
    
    print(f"{valid_pw_count} of {len(passwords)} passwords are valid.")

if __name__ == "__main__":
    if part == 'p1':
        p1()
    if part == 'p2':
        p2()

#TODO: Implement DRY