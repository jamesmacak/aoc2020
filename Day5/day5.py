import re

with open('input.txt') as fh:
    seats = fh.readlines()
    seats = [seat.strip() for seat in seats]
rows = [i for i in range(128)]
cols = [j for j in range(8)]
# print(rows, cols, sep='\n')
def run_search(char_one, char_two, seq_len):
    '''Provide two chars and length of sequence.
    Returns list rows_matches.
    '''
    rows_matches = []
    for seat in seats:
        # print(seat)
        # regex = re.compile(r'[F|B]{7}')
        regex = re.compile(r'['+char_one+'|'+char_two+']{'+str(seq_len)+'}')
        matches = regex.finditer(seat)
        for match in matches:
            # print(match)
            rows_matches.append(match)
    return rows_matches

fb_matches = run_search('F', 'B', 7)
lr_matches = run_search('L', 'R', 3)
# print(help(run_search))
# for match in fb_matches:
#     print(match)