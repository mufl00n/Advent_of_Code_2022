#--------------------------------SOLUTION 1:-----------------------------#

# from openpyxl import load_workbook
#
# wb = load_workbook('elves.xlsx')
# ws1 = wb['calories']
#
#
# def elf_di_tutti_elves(sheet):
#     sub_total = 0
#     total = []
#     top_numbers = 0
#     scrooges = []
#     for rowNumber in range(1, sheet.max_row + 1):
#         if sheet.cell(row=rowNumber, column=1).value != None:
#             sub_total += sheet.cell(row=rowNumber, column=1).value
#
#         else:
#             total.append(sub_total)
#             sub_total = 0
#             continue
#     while top_numbers <3:
#         top_numbers += 1
#         scrooges.append(max(total))
#         total.remove(max(total))
#     print(sum(scrooges))
#
# elf_di_tutti_elves(ws1)

#--------------------------------SOLUTION 2:-----------------------------#

with open("elves.txt") as fp:
    lines = fp.readlines()
    calories_list = []
    calories_total = 0
    for line in lines:
        if line.strip() == '':
            calories_list.append(calories_total)
            calories_total = 0
        else:
            calories_total += int(line.strip())
    calories_list.append(calories_total)

print(max(calories_list))
calories_list.sort(reverse=True)
print(sum(calories_list[:3]))







