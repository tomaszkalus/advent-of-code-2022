import string

ALPHABET = string.ascii_letters

with open('input.txt', encoding='utf-8') as inp:
    data_raw = inp.read()

# Preparing data
data = [[x[0: int(len(x)/2)], x[int(len(x)/2): len(x)]]
        for x in data_raw.strip().split('\n')]

# Summation of badges priorities
priorities_sum = 0
for sack in data:
    for item in sack[0]:
        if item in sack[1]:
            print(f"{sack[0]} {sack[1]} - {item} ")
            priorities_sum += ALPHABET.index(item) + 1
            break

print(f"The sum of priorities of the items which appear in both compartments of each rucksack is: {priorities_sum}")
