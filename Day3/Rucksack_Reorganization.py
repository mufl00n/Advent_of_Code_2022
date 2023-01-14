### Day 3 ### Rucksack Reorganization ###
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
points = [] # point assigned to individual alphabet letters in range 1-52 (a-Z)
common_elements = [] # list of elements appearing in both half of input strings
final_dictionary = {} # dictionary of alphabet : common elements
element_score = [] # list of points assigned to found elements

# fullfil "points" list
for n in range(1,53):
    points.append(n)
# print(f'printing list of points: \n {points}')

# fullfil "common_elements" list

def part1(text_file):
    with open(text_file) as fp:
        lines = fp.readlines()
        for index, line in enumerate(lines):
            line1 =slice(0,len(line)//2)
            line2 = slice(len(line)//2, len(line))
            list1 = line[line1]
            list2 = line[line2]
            result = [i for i in list1 if i in list2]
            common_elements.append(result[0])


    # pairs alphabet and common_elements into "final_dictionary"
    for key in alphabet:
        for value in points:
            final_dictionary[key] = value
            points.remove(value)
            break

    # fullfil "element_score" list
    for i in common_elements:
        element_score.append(final_dictionary.get(i))

    #print(sum(element_score))
    print(f'\nresult of Part1 is: {sum(element_score)}')

### PART 2 ###
common_elements_part2 = []
final_dictionary_part2 = {}
score = []
def part2(text_file):
    with open(text_file) as fp:
        lines = fp.readlines()
        for index, line in enumerate(lines):
            if index % 3 ==0:
                for i in lines[index]:
                    if i in lines[index + 1] and i in lines[index + 2] and i != '\n':
                        common_elements_part2.append(i)
                        break

    for key in alphabet:
        for value in points:
            final_dictionary_part2[key] = value
            points.remove(value)
            break

    print(f'printujem finalny slovnik {final_dictionary_part2}')
    print(f'printujem common_elements_part2 {common_elements_part2}')

    for p in common_elements_part2:
        score.append(final_dictionary_part2.get(p))

    print(f'printujem score: {sum(score)}')


part2('rucksacks.txt')