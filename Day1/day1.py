with open('input.txt') as fh:
    expense_report = [int(line.rstrip('\n')) for line in fh]

# PART 1
target = 2020
for i, cur in enumerate(expense_report[:-1]):
    comp = target - cur
    if comp in expense_report[i+1:]:
        print("Solution Found: {} and {}".format(cur, comp))
        sol = cur * comp
        print("Product: {}".format(sol))

# PART 2
target = 2020
for i in range(0, len(expense_report) - 2):
    for j in range(i + 1, len(expense_report) - 1):
        for k in range(j + 1, len(expense_report)):
            
            if expense_report[i] + expense_report[j] + expense_report[k] == target:
                print("Solution Found: {}, {}, and {}".format(expense_report[i], expense_report[j], expense_report[k]))
                sol2 = expense_report[i] * expense_report[j] * expense_report[k]
                print("Product: {}".format(sol2))
