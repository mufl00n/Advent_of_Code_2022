### Day 2 ### RockPaperScisors ###

# fist column:
# A - Rock
# B - Paper
# C - Scissors

# second column:
# X - Rock
# Y - Paper
# Z - Scissors

# shape point:
# 1 for Rock
# 2 for Paper
# 3 for Scissors

# outcome points:
# 0 if you lost
# 3 if the round was a draw
# 6 if you won

# opponent_dict = {
#     "A" : "Rock",
#     "B" : "Paper",
#     "C" : "Scissors",
# }
A = "Rock"
B = "Paper"
C = "Scissors"

X = "Rock"
Y = "Paper"
Z = "Scissors"

# my_dict = {
#     "X" : "Rock",
#     "Y" : "Paper",
#     "Z" : "Scissors"
# }

loss = 0
draw = 3
win = 6

Rock = 1
Paper = 2
Scissors = 3


points = 0

with open("RPS_test.txt") as fp:
    lines = fp.readlines()

# for line in lines:
#     if line.strip()[:1] == 'B':
#         if (line.strip()[-1:]) == 'Z':
#             points += win + Paper
#             continue
#
#
#     else:
#         print('nie je tam B')

for line in lines:
    if line.strip()[:1] == 'B':
        if (line.strip()[-1:]) == 'Z':
            print(line.strip())
            points += win + Scissors
            print(f'{win} + {Scissors}')
            print(points)
            print('')

        elif (line.strip()[-1:]) == 'X':
            print(line.strip())
            points += loss + Rock
            print(f'{loss} + {Rock}')
            print(points)
            print('')

