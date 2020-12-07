import re

with open('input.txt', 'r') as fh:
    passwords = fh.readlines()

valid_pw_count = 0
for line in passwords:
    line_re = re.findall(r"\w+", line)
    min, max, letter, pw = int(line_re[0]), int(line_re[1]), line_re[2], line_re[3]
    frequency = pw.count(letter)
    if min <= frequency <= max:
        valid_pw_count += 1
    
print(f"{valid_pw_count} of {len(passwords)} passwords are valid.")

#TODO: Add p1 and p2 as argvs, make framework