import re

passport = '''
2000
'''
byr_regex = re.compile(r'\d[1920-2002]')
matches = byr_regex.finditer(passport)
for match in matches:
    print(match)