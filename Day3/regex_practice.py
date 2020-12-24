import time, re

t0 = time.time()
print(f'{t0}\n')

# slopes = ['1,1', '3,1', '5,1', '7,1', '1,2']
# x_regex = re.compile(r"[\d+]")
# y_regex = re.compile(r",[\d+]")

# for s in slopes:
#     if x_regex.search(s):
#         print("Found X" + str(x_regex.search(s)))
#     if y_regex.search(s):
#         print("Found Y" + str(y_regex.search(s)))
#     else:
#         print("Did not find X or Y. Something went wrong.")

# for i in range(len(slopes)):
#     kw = ','
#     X, kw, Y = slopes[i].partition(kw)
#     print(f'\nX: {X}')
#     print(f'Y: {Y}')


sentence = '''
321-555-4321
123.555.1234
'''

pattern = re.compile(r'\d\d\d[-.]\d\d\d[-.]\d\d\d\d')
matches = pattern.finditer(sentence)
for match in matches:
    print(match)

t1 = time.time()
total_time = t1-t0
print(f'\n{total_time}')