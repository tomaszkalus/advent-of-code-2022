with open('input.txt') as f:
    raw_data = f.read()

pairs = [[x.split(',')[0], x.split(',')[1]] for x in raw_data.strip().split('\n')]

counter = 0
for pair in pairs:
    x1_s = int(pair[0].split('-')[0])
    x1_e = int(pair[0].split('-')[1])
    x2_s = int(pair[1].split('-')[0])
    x2_e = int(pair[1].split('-')[1])

    if (x1_s <= x2_s and x1_e >= x2_e) or (x2_s <= x1_s and x2_e >= x1_e):
        counter += 1

print(f"Number of assignments pairs where one range fully contain the other: {counter}")
