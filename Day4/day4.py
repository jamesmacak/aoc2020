from sys import argv
import re

script, part, input_file = argv

with open(input_file, 'r') as fh:
    batch = fh.readlines()
    batch = [line.strip() for line in batch]

def p1():
    regex = re.compile(r'(byr|iyr|eyr|hgt|hcl|ecl|pid|cid):(#?\w+)')
    passports = []
    passport = {}
    for line in batch:
        matches = regex.finditer(line)
        if line == '':
            passports.append(passport)
            passport = {}
        else:
            for match in matches:
                passport[match.group(1)] = match.group(2)
    
    passports.append(passport) # account for the last passport in batch
    valid_passport_count = 0
    for passport in passports:
        if len(passport) == 8 or (len(passport) == 7 and passport.get('cid') == None):
            valid_passport_count += 1
    print(valid_passport_count)
    return(passports)


def p2():
    passports = p1()
    for passport in passports:
        print(passport)
    
    byr_regex = re.compile(r'') # no regex, int() then check
    iyr_regex = re.compile(r'')
    eyr_regex = re.compile(r'')
    hgt_regex = re.compile(r'')
    hcl_regex = re.compile(r'')
    ecl_regex = re.compile(r'')
    pid_regex = re.compile(r'')
    cid_regex = re.compile(r'')


if __name__ == "__main__":
    if part == 'p1':
        p1()
    if part == 'p2':
        p2()