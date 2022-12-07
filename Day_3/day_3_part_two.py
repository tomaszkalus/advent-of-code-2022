import string

ALPHABET = string.ascii_letters

with open('input.txt', encoding='utf-8') as inp:
    data_raw = inp.read()

# Preparing data
data = [x for x in data_raw.strip().split('\n')]
groups = []
group = []
for i, line in enumerate(data):
    group.append(line)
    if (i + 1) % 3 == 0:
        groups.append(group)
        group = []

priorities_sum = 0

# Summation of badges priorities
for group in groups:
    for item in group[0]:
        if item in group[1] and item in group[2]:
            priorities_sum += ALPHABET.index(item) + 1
            break

print(f"The sum of priorities of the badges of each elf group is: {priorities_sum}")