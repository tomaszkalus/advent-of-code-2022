from collections import deque


class Node:
    ''' Declaration of a Node class, which represents a directory of the file tree'''

    def __init__(self, name) -> None:
        self.name = name
        self.parent = None
        self.children = {}
        self.size = 0


# Opening the file, removing the last whitespace characters and splitting it into lines
with open('input.txt', encoding='UTF-8') as f:
    raw_input = f.read().rstrip().split('\n')

root = Node('/')
cd = root

# Parsing the input and converting it into the tree data structure
for l in raw_input:
    if l.startswith('$ cd'):
        name = l.split()[2]
        if name == '/':
            directory = root

        elif name == '..':
            cd = cd.parent

        else:
            directory = cd.children[name]
            cd = directory

    elif l.startswith('dir'):
        name = l.split()[1]
        directory = Node(name)
        cd.children[name] = directory
        directory.parent = cd

    elif l.split()[0].isnumeric():
        size = l.split()[0]
        filename = l.split()[1]
        cd.size += int(size)


def print_tree(root, lvl):
    ''' Helper method for printing the tree'''
    if not root.children:
        return
    for child in root.children.values():
        print('\t' * lvl, child.name, f"({child.size})")
        print_tree(child, lvl + 1)


stack = deque()


def traverse(node):
    if not node.parent:
        stack.append(node)
    if not node.children:
        return
    for child in node.children.values():
        stack.append(child)
        traverse(child)


traverse(root)

while stack:
    node = stack.pop()
    if node.parent:
        node.parent.size += node.size

SPACE = 70000000
FREE_SPACE_NEEDED = 30000000
CURRENT_FREE_SPACE = SPACE - root.size
SPACE_TO_FREE = FREE_SPACE_NEEDED - CURRENT_FREE_SPACE
print("Current free space is:", CURRENT_FREE_SPACE)
print("You need", SPACE_TO_FREE, "more space")
dirs_to_delete = set()


def find_dirs_to_delete(root):
    ''' Function for finding the appropriate directories for removing and adding them
    to the set'''
    if root.size >= SPACE_TO_FREE:
        dirs_to_delete.add(root)
    if not root.children:
        return
    for child in root.children.values():
        find_dirs_to_delete(child)


find_dirs_to_delete(root)

# Finding the directory suitable for deleting with minimum size
min_size = min(dirs_to_delete, key=lambda x: x.size).size

print("The size of the smallest directory which would free up the space:", min_size)
