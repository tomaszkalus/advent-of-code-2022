import pprint

with open("input.txt", encoding="utf-8") as f:
    raw_input = f.read().rstrip()

tree_matrix = [[int(col) for col in row] for row in raw_input.split('\n')]
n = len(tree_matrix)
max_score = 1

for i in range(1, len(tree_matrix) - 1):
    row = tree_matrix[i]
    for j in range(1, len(row) - 1):
        col = row[j]
        
        vertical = [x[j] for x in tree_matrix]
        left = reversed(row[:j])
        right = row[j + 1:]
        up = reversed(vertical[:i])
        down = vertical[i + 1:]

        score = 1
        for direction in [left, right, up, down]:
            points = 0
            for t in direction:
                points += 1
                if t >= col:
                    break
            score *= points

        if score > max_score:
            max_score = score

print("The highest scenic score possible for any tree is:", max_score)
