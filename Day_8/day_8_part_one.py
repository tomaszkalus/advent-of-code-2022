import pprint

with open("input.txt", encoding="utf-8") as f:
    raw_input = f.read().rstrip()

tree_matrix = [[int(col) for col in row] for row in raw_input.split('\n')]
n = len(tree_matrix)
visible_trees = 0

for i, row in enumerate(tree_matrix):
    if i == 0 or i == n - 1:
        visible_trees += n
    else:
        for j, col in enumerate(row):
            if j == 0 or j == n - 1:
                visible_trees += 1
            else:
                vertical = [x[j] for x in tree_matrix]
                left = max(row[:j])
                right = max(row[j + 1:])
                up = max(vertical[:i])
                down = max(vertical[i + 1:])

                if (col > min([left, right, up, down])):
                    visible_trees += 1

print("There are", visible_trees, "visible trees from outside the grid.")
