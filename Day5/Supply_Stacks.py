# TEST
#    [D]
# [N] [C]
# [Z] [M] [P]
#  1   2   3

with open('test.txt') as f:
    lines = f.readlines()
    lines = [x.strip().split() for x in lines]
    for line in lines:
        print(line[0][1])