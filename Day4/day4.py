from sys import argv

script, part, input_file = argv

with open(input_file, 'r') as fh:
    # batch = fh.readlines()
    # print(batch)
    req_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid']
    batch = []
    pass_count = 0
    for line in fh:
        if line.strip() == '':
            pass
            pass_count += 1
            print("NEXT PASSPORT")
        else:
            pass
            batch.append(line)
            print(line)
    print(pass_count)
    

def p1():
    pass
        
def p2():
    pass

if __name__ == "__main__":
    if part == 'p1':
        p1()
    if part == 'p2':
        p2()



# with open(input_file, 'r') as fh:
#     batch = [] # passport as elem of batch
#     passport = {}
#     for line in fh:
#         if line.stip() == '': # '\n'
#             print(line)
#             pass
#         else: # some lines have multiple k,v sep by '\s'
#             for param in line.split(' '):
#                 # print(param)
#                 k, v = param.split(':')
#                 passport[k] = v.strip()
#     batch.append(passport)