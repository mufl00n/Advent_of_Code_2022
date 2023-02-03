import sys

# PART 1
def range_contains(a_start, a_end, b_start, b_end):
    ratadlo = 0
    for line in lines:
        first, second = line.split(",")
        a_start, a_end = first.split("-")
        b_start, b_end = second.split("-")
        if int(b_start) <= int(a_start) and int(a_end) <= int(b_end) or int(b_start) >= int(a_start) and int(a_end) >= int(b_end):
            ratadlo += 1
    return ratadlo

# PART 2
def overlapin(setA,setB):
    counter = 0
    for line in lines:
        first, second = line.split(",")
        a_start, a_end = first.split("-")
        b_start, b_end = second.split("-")
        range1 = range(int(a_start), int(a_end) + 1)
        range2 = range(int(b_start), int(b_end) + 1)
        set1 = set(range1)
        set2 = set(range2)
        if set1 & set2 or set2 & set1:
            counter +=1
    return counter



# PREPARATION
with open('shiftplan.txt') as f:
    lines = f.readlines()

for line in lines:
    first, second = line.split(",")
    a_start, a_end = first.split("-")
    b_start, b_end = second.split("-")
    range1 = range(int(a_start),int(a_end)+1)
    range2 = range(int(b_start),int(b_end)+1)
    set1 = set(range1)
    set2 = set(range2)
    # range_contains(a_start,a_end,b_start,b_end)
    overlapin(set1,set2)


# PRINT RESULTS
ratadlo_value = range_contains(a_start,a_end,b_start,b_end)
print(f'result of part1: {ratadlo_value}')

counter_value = overlapin(set1,set2)
print(f'result of part2: {counter_value}')
