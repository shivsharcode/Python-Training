
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


# In-order (left, Root, right)
def print_inorder(node):
    if node:
        print_inorder(node.left)
        print(node.value, end=' ')
        print_inorder(node.right)

# Pre-Order (Root, Left, Right)
def print_preorder(node):
    if node:
        print(node.value, end=' ')
        print_preorder(node.left)
        print_preorder(node.right)


# Post-order (Left, Right, Root)
def print_postorder(node):
    if node:
        print_postorder(node.left)
        print_postorder(node.right)
        print(node.value, end='  ')


# bfs (print level by level)
from collections import deque

def print_level_order(root):
    if not root:
        return

    queue = deque([root])
    while queue:
        node = queue.popleft()
        print(node.value, end=' ')

        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)


# Pretty print
# if you want to see a structured or indented version of the tree, here's a recursive way
def pretty_print_tree(node, level=0, prefix="Root: "):
    if node is not None:
        print("  "*level + prefix + str(node.value))
        pretty_print_tree(node.left, level+1, prefix = "L--- ")
        pretty_print_tree(node.right, level+1, prefix = "R---")

# Example : Creating nodes manually
# 1 2 3 4 5
root = Node(1)
root.left = Node(2)
root.right = Node(3)

# Adding more nodes
root.left.left = Node(4)
root.right.right = Node(5)

print(print_inorder(root))
print(print_preorder(root))
print(print_postorder(root))

print("Root = ", root.value)
print(print_level_order(root))
print(pretty_print_tree(root))

