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

A = "Rock"
B = "Paper"
C = "Scissors"

X = "Rock"
Y = "Paper"
Z = "Scissors"
#
# loss = 0
# draw = 3
# win = 6
#
# Rock = 1
# Paper = 2
# Scissors = 3
#
# points = 0
#
# with open("RPS.txt") as fp:
#     lines = fp.readlines()
#
# def part2():
#     points = 0
#     for line in lines:
#         if line.strip()[:1] == 'A' and (line.strip()[-1:]) == 'X':
#             print(line.strip())
#             points += loss + Scissors
#             print(f'{loss} + {Scissors}')
#             print(points)
#             print('')
#         elif line.strip()[:1] == 'A' and (line.strip()[-1:]) == 'Y':
#             print(line.strip())
#             points += draw + Rock
#             print(f'{draw} + {Rock}')
#             print(points)
#             print('')
#         elif line.strip()[:1] == 'A' and (line.strip()[-1:]) == 'Z':
#             print(line.strip())
#             points += win + Paper
#             print(f'{win} + {Paper}')
#             print(points)
#             print('')
#         if line.strip()[:1] == 'B' and (line.strip()[-1:]) == 'X':
#             print(line.strip())
#             points += loss + Rock
#             print(f'{loss} + {Rock}')
#             print(points)
#             print('')
#         elif line.strip()[:1] == 'B' and (line.strip()[-1:]) == 'Y':
#             print(line.strip())
#             points += draw + Paper
#             print(f'{draw} + {Paper}')
#             print(points)
#             print('')
#         elif line.strip()[:1] == 'B' and (line.strip()[-1:]) == 'Z':
#             print(line.strip())
#             points += win + Scissors
#             print(f'{win} + {Scissors}')
#             print(points)
#             print('')
#         if line.strip()[:1] == 'C' and (line.strip()[-1:]) == 'X':
#             print(line.strip())
#             points += loss + Paper
#             print(f'{loss} + {Paper}')
#             print(points)
#             print('')
#         elif line.strip()[:1] == 'C' and (line.strip()[-1:]) == 'Y':
#             print(line.strip())
#             points += draw + Scissors
#             print(f'{draw} + {Scissors}')
#             print(points)
#             print('')
#         elif line.strip()[:1] == 'C' and (line.strip()[-1:]) == 'Z':
#             print(line.strip())
#             points += win + Rock
#             print(f'{win} + {Rock}')
#             print(points)
#             print('')
#     print(f'Result is:{points}')
#
# def part1():
#     points = 0
#     for line in lines:
#         if line.strip()[:1] == 'A':
#             if (line.strip()[-1:]) == 'X':
#                 print(line.strip())
#                 points += draw + Rock
#                 print(f'{draw} + {Rock}')
#                 print(points)
#                 print('')
#
#
#             elif (line.strip()[-1:]) == 'Y':
#                 print(line.strip())
#                 points += win + Paper
#                 print(f'{win} + {Paper}')
#                 print(points)
#                 print('')
#
#
#             elif (line.strip()[-1:]) == 'Z':
#                 print(line.strip())
#                 points += loss + Scissors
#                 print(f'{loss} + {Scissors}')
#                 print(points)
#                 print('')
#
#
#         elif line.strip()[:1] == 'B':
#             if (line.strip()[-1:]) == 'X':
#                 print(line.strip())
#                 points += loss + Rock
#                 print(f'{loss} + {Rock}')
#                 print(points)
#                 print('')
#
#             elif (line.strip()[-1:]) == 'Y':
#                 print(line.strip())
#                 points += draw + Paper
#                 print(f'{draw} + {Paper}')
#                 print(points)
#                 print('')
#
#             elif (line.strip()[-1:]) == 'Z':
#                 print(line.strip())
#                 points += win + Scissors
#                 print(f'{win} + {Scissors}')
#                 print(points)
#                 print('')
#
#         elif line.strip()[:1] == 'C':
#             if (line.strip()[-1:]) == 'X':
#                 print(line.strip())
#                 points += win + Rock
#                 print(f'{win} + {Rock}')
#                 print(points)
#                 print('')
#
#             elif (line.strip()[-1:]) == 'Y':
#                 print(line.strip())
#                 points += loss + Paper
#                 print(f'{loss} + {Paper}')
#                 print(points)
#                 print('')
#
#             elif (line.strip()[-1:]) == 'Z':
#                 print(line.strip())
#                 points += draw + Scissors
#                 print(f'{draw} + {Scissors}')
#                 print(points)
#                 print('')
#
#     print(f'Result is:{points}')
#
# part1()
# part2()
###=======================================================================================###

# ###### Janciho riesenie #######
values = {
    'X': 1,
    'Y': 2,
    'Z': 3,
}

draw_values = {
    'A': 1,
    'B': 2,
    'C': 3,
}

loose_values = {
    'A': 3,
    'B': 1,
    'C': 2,
}

win_values = {
    'A': 2,
    'B': 3,
    'C': 1,
}
def calculate_winnings(player1: str, player2: str) ->int:
    if (player1 == 'A' and player2 == 'X') \
        or (player1 == 'B' and player2 == 'Y') \
        or (player1 == 'C' and player2 == 'Z'):
        return 3 + values[player2]

    if (player1 == 'A' and player2 == 'Y') \
        or (player1 == 'B' and player2 == 'Z') \
        or (player1 == 'C' and player2 == 'X'):
        return 6 + values[player2]

def calculate_shape(player1: str, player2: str) ->int:
    if player2 == 'X':   # loose
        return loose_values[player1]

    if player2 == 'Y':   # draw
        return 3 + draw_values[player1]

    if player2 == 'Z':   # win
        return 6 + win_values[player1]


part_one = 0
part_two = 0
with open("RPS.txt") as fp:
    lines = fp.readlines()
    for line in lines:
        opponent, me = line.strip().split(' ')
        part_one += calculate_winnings(opponent, me)
        part_two += calculate_shape(opponent, me)

print(part_one)
print(part_two)



