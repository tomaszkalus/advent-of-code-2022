import pprint
import re

# Processing input
with open('input.txt') as file:
    raw_input = file.read().rstrip()

# Splitting the crates layout from the instructions
crates_list = raw_input.split('\n\n')[0].split('\n')
moves_list = raw_input.split('\n\n')[1].split('\n')

# Determining the dimensions of the crates layout
crates_xlen = int(crates_list[-1].strip()[-1])
crates_ylen = len(crates_list) - 1

# Parsing data to the matrix form
crates_matrix = []
for i in range(crates_ylen):
    row = []
    for j in range(crates_xlen):
        try:
            row.append(crates_list[i][(j * 4) + 1 ])
        except IndexError:
            break
    crates_matrix.append(row)

# Parsing data to the map form
crates = {}
for i in range(crates_ylen + 1):
    crates[i+1] = []
    for j in range(crates_xlen -1, -1, -1):
        try:
            if(crates_matrix[j][i]) != ' ':
                crates[i+1].append(crates_matrix[j][i])
        except IndexError:
            continue

print("Input before moving the crates:")
pprint.pprint(crates)

# Executing all the instructions
for line in moves_list:
    result = re.search("move ([0-9]*) from ([0-9]*) to ([0-9]*)", line)
    move = [int(x) for x in result.groups()]
    for i in range(move[0], 0, -1):
        crates[move[2]].append(crates[move[1]].pop(len(crates[move[1]]) - i))    

print("\nInput after moving the crates:")
pprint.pprint(crates)

# Printing the output
output = ''.join([x[-1] for x in crates.values()])
print(f"\nThe answer is: {output}")