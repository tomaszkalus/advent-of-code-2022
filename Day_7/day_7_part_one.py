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
    if not root.parent:
        print(root.name, f"({root.size})")
    if not root.children:
        return
    for child in root.children.values():
        print('\t' * (lvl + 1), child.name, f"({child.size})")
        print_tree(child, lvl + 1)


stack = deque()


def traverse(node):
    ''' Traverse through the directory tree via post-order traversal and add them to stack'''
    if not node.parent:
        stack.append(node)
    if not node.children:
        return
    for child in node.children.values():
        stack.append(child)
        traverse(child)


traverse(root)

# Adding the file of all child directories to all the parent directories
sum_100k = 0
while stack:
    node = stack.pop()
    if node.parent:
        node.parent.size += node.size
        if node.size <= 100000:
            sum_100k += node.size

print_tree(root, 0)
print("The sum of all the directories whose size is at most 100 000:", sum_100k)
