# TEST
#    [D]
# [N] [C]
# [Z] [M] [P]
#  1   2   3

column_1 = ['Z','N']
column_2 = ['M','C','D']
column_3 = ['P']

#         [F] [Q]         [Q]
# [B]     [Q] [V] [D]     [S]
# [S] [P] [T] [R] [M]     [D]
# [J] [V] [W] [M] [F]     [J]     [J]
# [Z] [G] [S] [W] [N] [D] [R]     [T]
# [V] [M] [B] [G] [S] [C] [T] [V] [S]
# [D] [S] [L] [J] [L] [G] [G] [F] [R]
# [G] [Z] [C] [H] [C] [R] [H] [P] [D]
#  1   2   3   4   5   6   7   8   9
#
# column_1 = ['G','D','V','Z','J','S','B']
# column_2 = ['Z','S','M','G','V','P']
# column_3 = ['C','L','B','S','W','T','Q','F']
# column_4 = ['H','J','G','W','M','R','V','Q']
# column_5 = ['C','L','S','N','F','M','D']
# column_6 = ['R','G','C','D']
# column_7 = ['H','G','T','R','T','R','J','D','S','Q']
# column_8 = ['P','F','V']
# column_9 = ['D','R','S','T','J']


def move_boxes(loops,from_destination, to_destination):
    loop_iter = 0
    temp_var = "column_" + str(from_destination)
    temp_var2 = eval(temp_var)[-1]
    from_column = "column_" + str(from_destination)
    to_column = "column_" + str(to_destination)
    while loop_iter != loops:
        exec(f"{to_column}.append(temp_var2)")
        exec(f"{from_column}.remove(temp_var2)")
        loop_iter+=1
    print(column_1)
    print(column_2)
    print(column_3)
# def parse_lines():
#     print

def skuska():
    counter = 0
    number_how_many = input('kolko: ')
    number_from = input('odkial: ')
    number_to = input('kam: ')
    temp_var = "column_"+str(number_from)

    from_column = "column_"+str(number_from)
    to_column = "column_" + str(number_to)

    if number_how_many == str(1):
        print(f'zacinam robit toto')
        temp_var2 = eval(temp_var)[-1]
        exec(f"{to_column}.append(temp_var2)")
        exec(f"{from_column}.remove(temp_var2)")
        print(column_1)
        print(column_2)
    else:
        while str(counter) < str(number_how_many):
            print(f'idem komplikovanejsie')
            temp_var2 = eval(temp_var)[-1]
            exec(f"{to_column}.append(temp_var2)")
            exec(f"{from_column}.remove(temp_var2)")
            counter+=1

with open('test.txt') as f:
    lines = f.readlines()
    lines = [x.strip().split() for x in lines]
    for line in lines:
        how_many = line[1]
        take_box = line[3]
        pull_box = line[5]
        loop_iter = 0
        from_column = "column_" + str(take_box)
        to_column = "column_" + str(pull_box)
        temp_var = eval(from_column)[-1]
        while loop_iter != how_many:
            exec(f"{to_column}.append(temp_var)")
            exec(f"{from_column}.remove(temp_var)")
            loop_iter+=1
    print(column_1[-1])
    print(column_2[-1])
    print(column_3[-1])

    print(column_4[-1])
    print(column_5[-1])
    print(column_6[-1])
    print(column_7[-1])
    print(column_8[-1])
    print(column_9[-1])



        # from_column = "column_" + str(take_box)
        # to_column = "column_" + str(pull_box)
        # while loop_iter != how_many:
        #     exec(f"{pull_box}.append(temp_var2)")
        #     exec(f"{take_box}.remove(temp_var2)")
        #     loop_iter+=1






skuska()


